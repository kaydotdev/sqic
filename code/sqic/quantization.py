from typing import Tuple, Optional

import numpy as np


def calculate_loss(x: np.ndarray, y: np.ndarray) -> np.float64:
    pairwise_distance = np.linalg.norm(x[:, np.newaxis] - y, axis=-1)
    min_distance = np.min(pairwise_distance, axis=-1)

    return np.sum(min_distance)


def find_nearest_element(
    x: np.ndarray, target: np.ndarray
) -> Tuple[np.ndarray, np.signedinteger]:
    distance = np.linalg.norm(target - x, axis=1)
    nearest_index = np.argmin(distance)

    return x[nearest_index, :], nearest_index


def sq(
    X: np.ndarray,
    n_clusters: int = 2,
    max_iter: int = 10,
    learning_rate: np.float64 = 0.001,
    rank: np.unsignedinteger = 3,
    tol: Optional[np.float64] = None,
    random_state: Optional[np.random.RandomState] = None,
) -> Tuple[np.ndarray, np.float64]:
    if random_state is None:
        random_state = np.random.RandomState()

    X_len, X_dims = X.shape
    random_indices = random_state.choice(X_len, size=1, replace=False)
    opt_quants = np.expand_dims(X[random_indices.item()], axis=0)

    # Initialization of quants position
    for _ in range(1, n_clusters):
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

    loss_iter = [calculate_loss(X, opt_quants)]

    #
    for i in range(max_iter):
        for ksi_j in np.random.permutation(X):
            # Find the nearest center
            y, yi = find_nearest_element(opt_quants, ksi_j)

            # Calculate gradient
            grad_y = rank * np.linalg.norm(ksi_j - y, ord=2) ** (rank - 2) * (y - ksi_j)

            # Update nearest center
            opt_quants[yi, :] = y - learning_rate * grad_y

        current_loss = calculate_loss(X, opt_quants)

        if tol is not None and loss_iter[-1] - current_loss < tol:
            break

    return opt_quants, loss_iter[-1]
