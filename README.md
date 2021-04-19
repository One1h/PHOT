# PHOT
[1] Aiger D ,  Talbot H . The Phase Only Transform for unsupervised surface defect detection.  2013.

"We present a simple, fast, and effective method to detect defects on textured surfaces. Our method is unsupervised and contains no learning stage or information on the texture being inspected. The new method is based on the Phase Only Transform (PHOT) which correspond to the Discrete Fourier Transform (DFT), normalized by the magnitude. The PHOT removes any regularities, at arbitrary scales, from the image while preserving only irregular patterns considered to represent defects. The localization is obtained by the inverse transform followed by adaptive thresholding using a simple standard statistical method. The main computational requirement is thus to apply the DFT on the input image. The new method is also easy to implement in a few lines of code. Despite its simplicity, the methods is shown to be effective and generic as tested on various inputs, requiring only one parameter for sensitivity. We provide theoretical justification based on a simple model and show results on various kinds of patterns. We also discuss some limitations."

## difference
Original paper used Mahalanobis distance to judge the area of defect, I just judge each pixel.

## Original paper result
![Original paper result](https://github.com/One1h/PHOT/blob/main/original.PNG)
