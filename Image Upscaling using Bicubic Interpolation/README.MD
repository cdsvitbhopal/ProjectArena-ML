## Image Upscaling With Bicubic Interpolation

### Introduction:
This project is a quick and dirty from scratch implementation of Image upscaling

Upscaling is the process by which for a given image we increase the size of data, in this case images, by interpolating missing data from data present (Creating new pixels from the current pixels)

There are several methods by which we can interpolate data. The one which I have used in this program is bicubic interpolation which provides us with upscaled images with greater quality but the tradeoff being increased computation costs.

![Bicubic interpolation - Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Comparison_of_1D_and_2D_interpolation.svg/1200px-Comparison_of_1D_and_2D_interpolation.svg.png)
### Usage:
You need to have the following prerequisites to run this program:

 1. OpenCV
 2. Numpy
 3. Python

**Note**: **Make sure both dependencies (OpenCV and Numpy) are installed in the same virtual environment**

You can run this program by cloning this repository and running the `bicubic.py` file as follows:

    python bicubic.py path/to/1080p/image.jpg
the resultant upscaled image will be created in the same directory as  source image.

### How It Works:
[This](https://www.youtube.com/watch?v=poY_nGzEEWM&t=306s) video was instrumental for me to understand what bicubic interpolation was and how it works so I recommend anyone reading this to check it out.

fundamentally, bicubic interpolation takes a 4x4 neighborhood of pixels and fits a curve or function outputting the pixel value (for all color channels - Red, Green and Blue). It takes into consideration 16 pixels' values and fits the curve creating a smoother, non linear curve as opposed to bilinear interpolation, which creates a linear function or a line by taking only 4 points (2x2 neighborhood) with the tradeoff in computational time.

Here is the algorithm of my script:

 1. Importing the image
 2. Splitting image into R, G, B color channels
 3. Creating a new image which is scaled by 2 (1920 x 1080 multiplied by 2 is equal to 3840 x 2160 which is 4k)
 4. Placing known pixels onto new image
 5. Interpolating pixels on the same horizontal line as known pixels
 6. Interpolating pixels on the same vertical line as known pixels
 7. Interpolating rest of the pixels with previously interpolated pixels
 8. Merging the 3 color channels into 1.
 9. Outputting new Images

**Handling edge cases**
Corner and edge pixels do not have a 4x4 neighborhood so I interpolated their values using the nearest neighbor method which involves setting their value to the that of the nearest known pixel but other techniques like clamping, mirroring and wrapping can be used to interpolate their values.

### Improvements:
This was a quick implementation of the bicubic interpolation method for image upscaling so there is definitely massive room for improvements such as generalizing the code to accept different image resolutions as well as different scaling factors, parallelization since operations can definitely be parallelized for efficient creation of upscaled images and general code optimization for increased adherence to the DRY principle.

