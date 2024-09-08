from typing import Union, Tuple, Optional

import numpy as np


def calculate_loss(xi: np.ndarray, y: np.ndarray) -> np.float64:
    """Calculates stochastic Wasserstein (or Kantorovich–Rubinstein) distance between distributions ξ and y:

    F(y) = Σᵢ₌₁ᴵ pᵢ min₁≤k≤K d(ξᵢ, yₖ)ʳ

    Parameters
    ----------
    xi : np.ndarray
        The original distribution ξ with shape (N, D, ...).
    y : np.ndarray
        The quantized distribution y with shape (M, D, ...).

    Returns
    -------
    np.float64
        The calculated stochastic Wasserstein distance between distributions ξ and y.

    Raises
    ------
    ValueError
        If there is a shape mismatch between individual elements in distribution ξ and y.
    """

    if xi.shape[1:] != y.shape[1:]:
        raise ValueError("The dimensions of individual elements in distribution `xi` and `y` must match. Elements in "
                         f"`xi` have shape {xi.shape[1:]}, but y elements have shape {y.shape[1:]}.")

    pairwise_distance = np.linalg.norm(xi[:, np.newaxis] - y, axis=-1)
    min_distance = np.min(pairwise_distance, axis=-1)

    return np.sum(min_distance)


def find_nearest_element(
    y: np.ndarray, target: np.ndarray
) -> Tuple[np.ndarray, np.uint]:
    """Searches for the nearest element in `y` to `target` based on Euclidean distance. This function computes the
    Euclidean distance between each element in `y` and the `target`, then returns the element from `y` that has the
    smallest distance to `target`, along with its index. The shape of an individual element of `y` must match the
    shape of `target`.

    Parameters
    ----------
    y : np.ndarray
        The input tensor containing multiple elements to search from with shape (N, D, ...).

    target : np.ndarray
        The target tensor with shape (D, ...).

    Returns
    -------
    Tuple[np.ndarray, np.uint]
        A tuple containing two elements:

        1. np.ndarray: The nearest element found in `y` to the `target` with shape (D, ...).
        2. np.uint: The index of the nearest element in `y`.

    Raises
    ------
    ValueError
        If there is a shape mismatch between individual elements in `y` and `target`.
    """

    if y.shape[1:] != target.shape:
        raise ValueError("The dimensions of individual elements in `y` and `target` must match. Elements in `y` have "
                         f"shape {y.shape[1:]}, but `target` tensor has shape {target.shape}.")

    distance = np.linalg.norm(target - y, axis=1)
    nearest_index = np.argmin(distance)

    return y[nearest_index, :], nearest_index


def sq(
    X: np.ndarray,
    n_quants: Union[int, np.uint] = 2,
    learning_rate: Union[float, np.float64] = 0.001,
    rank: Union[int, np.uint] = 3,
    max_iter: Union[int, np.uint] = 1,
    random_state: Optional[np.random.RandomState] = None,
) -> Tuple[np.ndarray, np.float64]:
    """Solves a Stochastic Quantization problem by minimizing the transportation objective function

    This function implements an algorithm to find the optimal quantized distribution that minimizes the Wasserstein
    (or Kantorovich–Rubinstein) distance between the input distribution and the quantized distribution:

    min₍y = { y₁, …, yₖ } ∈ Y^K ⊂ ℝ^(nK)₎ F(y₁, …, yₖ)

    The objective function is defined as:

    F(y) = F(y₁, …, yₖ) = Σᵢ₌₁ᴵ pᵢ min₁≤ₖ≤ₖ d(ξᵢ, yₖ)ʳ = 𝔼ᵢ∼ₚ min₁≤ₖ≤ₖ d(ξᵢ, yₖ)ʳ

    The algorithm is defined as a numeric iterative sequence, that updates parameters {yₖ} based on the calculated
    gradient value of a norm between sampled ξᵢ and the nearest element yₖ:

        1. k⁽ᵗ⁾ ∈ S(ξ̃⁽ᵗ⁾,y⁽ᵗ⁾) = argmin₁≤k≤K d(ξ̃⁽ᵗ⁾, yₖ⁽ᵗ⁾), t=0,1,…;
        2. gₖ⁽ᵗ⁾ = { r ‖ ξ̃⁽ᵗ⁾ - yₖ⁽ᵗ⁾ ‖ʳ⁻² (yₖ⁽ᵗ⁾ - ξ̃⁽ᵗ⁾), if k = k⁽ᵗ⁾; 0, if k ≠ k⁽ᵗ⁾;
        3. yₖ⁽ᵗ⁺¹⁾ = πY(yₖ⁽ᵗ⁾ - ρₜgₖ⁽ᵗ⁾), k=1,…,K;

    Parameters
    ----------
    X : np.ndarray
        The input tensor containing training element {ξᵢ}.
    n_quants : int or np.uint
        The number of elements in tensor {yₖ} containing quantized distribution. Must be greater than or equal to 1.
        Defaults to 2.
    learning_rate : float or np.float64
        The learning rate parameter ρ, which determines the convergence speed and stability of the algorithm. Must be
        greater than 0. Defaults to 0.001.
    rank : int or np.uint
        The degree of the norm (rank) r. Must be greater of equal to 3. Defaults to 3.
    max_iter : int or np.uint
        Maximum number of iteration for the algorithm to converge. In a single iteration, the algorithm samples all
        elements from {ξᵢ} uniformly. Must be greater than or equal to 1. Defaults to 1.
    random_state : np.random.RandomState, optional
        Random state for reproducibility. Defaults to None.

    Returns
    -------
    Tuple[np.ndarray, np.uint]
        A tuple containing two elements:

        1. np.ndarray: The optimal values {yₖ*} of quantized distribution.
        2. np.uint: The algorithm inertia value, i.e., the optimal transportation value F(y*).

    Raises
    ------
    ValueError
        If any of the hyperparameters (n_quants, learning_rate, rank, max_iter) do not meet the specified constraints.
    """

    if rank < 3:
        raise ValueError("The degree of the norm (rank) must be greater of equal to 3.")

    if learning_rate <= 0.0:
        raise ValueError("The learning rate must be greater than 0.")

    if n_quants < 1:
        raise ValueError("The number of quants must be greater than or equal to 1.")

    if max_iter < 1:
        raise ValueError("The maximum number of iterations must be greater than or equal to 1.")

    if random_state is None:
        random_state = np.random.RandomState()

    X_len, X_dims = X.shape
    random_indices = random_state.choice(X_len, size=1, replace=False)
    opt_quants = np.expand_dims(X[random_indices.item()], axis=0)

    # Initial quants seeding
    for _ in range(1, n_quants):
        pairwise_distance = np.min(
            np.linalg.norm(X[:, np.newaxis] - opt_quants, axis=-1),
            axis=-1,
        )
        pairwise_probabilities = pairwise_distance / np.sum(pairwise_distance)
        cumulative_probabilities = np.cumsum(pairwise_probabilities)
        next_quant_index = np.searchsorted(
            cumulative_probabilities, random_state.rand()
        )
        opt_quants = np.vstack((opt_quants, X[next_quant_index]))

    # Minimizing the Wasserstein (Kantorovich–Rubinstein) distance between two distributions iteratively
    for i in range(max_iter):
        for ksi_j in np.random.permutation(X):
            y, yi = find_nearest_element(opt_quants, ksi_j)  # Find the nearest center
            grad_y = rank * np.linalg.norm(ksi_j - y, ord=2) ** (rank - 2) * (y - ksi_j)  # Calculate gradient
            opt_quants[yi, :] = y - learning_rate * grad_y  # Update nearest center

    return opt_quants, calculate_loss(X, opt_quants)
