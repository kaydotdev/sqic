# Stochastic Quantization for Image Compression

by [Anton Kozyriev](mailto:a.kozyriev@kpi.ua)<sup>1</sup>, [Vladimir Norkin](mailto:v.norkin@kpi.ua)<sup>1,2</sup>

 - Igor Sikorsky Kyiv Polytechnic Institute, National Technical University of Ukraine, Kyiv, 03056, Ukraine
 - V.M.Glushkov Institute of Cybernetics, National Academy of Sciences of Ukraine, Kyiv, 03178, Ukraine

This paper has been submitted for publication in ["Cybernetics and Computer Technologies" (CCTech)](http://cctech.org.ua/).

## Demo

<a href="#"><img src="./results/figures/original_image.png" width="45%" alt="Original image"></a>
<a href="#"><img src="./results/animations/compressed_image.gif" width="45%" alt="Compressed image"></a>

## Abstract

Lossy image compression algorithms play a crucial role in various domains, including graphics, and image processing. 
As image information density increases, so do the resources required for processing and transmission. One of the most 
prominent approaches to address this challenge is color quantization, proposed by Orchard et al. (1991). This technique 
optimally maps each pixel of an image to a color from a limited palette, maintaining image resolution while 
significantly reducing information content. Color quantization can be interpreted as a clustering problem (Krishna et 
al. (1997), Wan (2019)), where image pixels are represented in a three-dimensional space, with each axis corresponding 
to the intensity of an RGB channel.

However, Norkin et al. (2024) demonstrated that scaling traditional algorithms like K-Means can be challenging for 
large data, such as modern images with millions of colors. This paper reframes color quantization as a 
three-dimensional stochastic transportation problem between the set of image pixels and an optimal color palette, 
where the number of colors is a predefined hyperparameter. We employ Stochastic Quantization (SQ) with a seeding 
technique proposed by Arthur et al. (2007) to enhance the scalability of color quantization. This method introduces 
a probabilistic element to the quantization process, potentially improving efficiency and adaptability to diverse 
image characteristics.

To demonstrate the efficiency of our approach, we present experimental results using images from the ImageNet dataset. 
These experiments illustrate the performance of our Stochastic Quantization method in terms of compression quality, 
computational efficiency, and scalability compared to traditional color quantization techniques.

## Keywords

non-convex optimization, stochastic quantization, color quantization, lossy compression

## Data

To evaluate the efficiency of the proposed color quantization approach, a comparative analysis was conducted using 
individual images from the [ImageNet 2012 dataset](https://www.image-net.org/index.php).

Russakovsky, O., Deng, J., Su, H., Krause, J., Satheesh, S., Ma, S., Huang, Z.,  Karpathy, A., Khosla, A., Bernstein, 
M., Berg, A.C., Fei-Fei, L.: ImageNet Large Scale Visual Recognition Challenge. International Journal of Computer 
Vision (IJCV) **115**(3), 211–252 (2015). https://doi.org/10.1007/s11263-015-0816-y

## License

...
