# SCT_CS_2

**Introduction**

This Python script offers a basic image encryption tool that employs pixel manipulation techniques. 
It supports operations like swapping pixel values and applying fundamental mathematical operations to individual pixels. 
While this approach provides a rudimentary level of encryption, it's essential to note that for highly sensitive data, more sophisticated encryption algorithms are recommended.


**Usage:**

*1 Install Requirements:*

Ensure you have Python 3.x installed.

Install cv2 from OpenCV

Install the required libraries using pip:

    pip install opencv-python numpy

*2 Download Python file:*



*3 Prepare Images:*

Place your images in a directory.

*4 Run the Script:*

Modify the image_path variable in the script to point to your desired image.

Choose the desired encryption operation ('swap', 'add', 'subtract', 'multiply', or 'divide') and set the 'swap_interval' if applicable.

Run the script:

    python pixel_manipulation.py

**Output:**

The script will create two new image files:

encrypted_image.jpg: The encrypted image.

decrypted_image.jpg: The decrypted image (if decryption is implemented).

**Functionality**

The script operates in the following manner:

Image Loading: The script loads the specified image file using OpenCV.

Pixel Manipulation: It iterates through each pixel in the image and applies the chosen encryption operation. This could involve swapping pixels, adding a constant value, subtracting a constant value, multiplying by a constant, or dividing by a constant.

Encrypted Image Creation: The modified pixel values are used to create a new, encrypted image.

Decryption (Optional): If a decryption operation is implemented, it reverses the encryption process to recover the original image.


**Key Features:**

Simple Encryption: Provides a straightforward method for encrypting images.

Customizable Operations: Allows you to select different encryption operations based on your requirements.

Flexibility: Can be adapted to incorporate additional encryption techniques.
