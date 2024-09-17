import cv2
import numpy as np

def encrypt_image(image_path, operation, swap_interval=2):
    """Encrypts an image using specified pixel manipulation operations.

    Args:
        image_path: Path to the image file.
        operation: Encryption operation to apply (e.g., 'swap', 'add', 'subtract', 'multiply', 'divide').
        swap_interval: Interval for swapping pixels (only for 'swap' operation).

    Returns:
        The encrypted image.
    """

    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Could not read image at path: {image_path}")
        return None  

    height, width, channels = image.shape

    encrypted_image = np.zeros_like(image)

    height, width, channels = image.shape

    encrypted_image = np.zeros_like(image)

    for i in range(height):
        for j in range(width):
            for k in range(channels):
                pixel_value = image[i, j, k]

                if operation == 'swap':
                    if (j + 1) % swap_interval == 0:
                        encrypted_image[i, j, k] = image[i, j - swap_interval, k]
                    else:
                        encrypted_image[i, j, k] = pixel_value
                elif operation == 'add':
                    encrypted_image[i, j, k] = (pixel_value + 10) % 256
                elif operation == 'subtract':
                    encrypted_image[i, j, k] = (pixel_value - 10) % 256
                elif operation == 'multiply':
                    encrypted_image[i, j, k] = (pixel_value * 2) % 256
                elif operation == 'divide':
                    encrypted_image[i, j, k] = pixel_value // 2
                else:
                    raise ValueError("Invalid operation: " + operation)

    return encrypted_image

def decrypt_image(encrypted_image, operation, swap_interval=2):
    """Decrypts an encrypted image using the same operation and parameters.

    Args:
        encrypted_image: The encrypted image.
        operation: Decryption operation (same as encryption operation).
        swap_interval: Swap interval (same as encryption).

    Returns:
        The decrypted image.
    """


    return encrypted_image

# Example usage:
image_path = r"D:\BMSIT\skillcraft\input.jpg"
operation = "swap"  # Change to "add", "subtract", "multiply", or "divide" as needed
swap_interval = 2
encrypted_image = encrypt_image(image_path, operation, swap_interval)
decrypted_image = decrypt_image(encrypted_image, operation, swap_interval)

cv2.imwrite(r"D:\BMSIT\skillcraft\encrypted_image.jpg", encrypted_image)
cv2.imwrite(r"D:\BMSIT\skillcraft\decrypted_image.jpg", decrypted_image)

'''print("Encrypted image:")
print(encrypted_image)

print("Decrypted image:")
print(decrypted_image)'''