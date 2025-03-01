# Import necessary libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image (Ensure the correct filename and extension)
image_path = r"C:\Users\Bhavy\OneDrive\Desktop\your_image.jpg"  # Replace with actual image name
image = cv2.imread(image_path)

# Check if image is loaded correctly
if image is None:
    print("Error: Image not found. Check the file path.")
    exit()

# Convert BGR image to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the scale factors
scale_factor_1 = 3.0  # Zoom in (increase size)
scale_factor_2 = 1/3.0  # Scale down (decrease size)

# Get original dimensions
height, width = image_rgb.shape[:2]

# Resize the image (Zoomed)
zoomed_image = cv2.resize(image_rgb, 
                          (int(width * scale_factor_1), int(height * scale_factor_1)), 
                          interpolation=cv2.INTER_CUBIC)

# Resize the image (Scaled down)
scaled_image = cv2.resize(image_rgb, 
                          (int(width * scale_factor_2), int(height * scale_factor_2)), 
                          interpolation=cv2.INTER_AREA)

# Create subplots
fig, axs = plt.subplots(1, 3, figsize=(12, 5))

# Display Original Image
axs[0].imshow(image_rgb)
axs[0].set_title(f'Original Image Shape: {image_rgb.shape}')

# Display Zoomed Image
axs[1].imshow(zoomed_image)
axs[1].set_title(f'Zoomed Image Shape: {zoomed_image.shape}')

# Display Scaled Image
axs[2].imshow(scaled_image)
axs[2].set_title(f'Scaled Image Shape: {scaled_image.shape}')

# Remove axis ticks
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

# Show images
plt.tight_layout()
plt.show()
