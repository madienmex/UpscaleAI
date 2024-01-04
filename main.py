import cv2  

def upscale_image(input_path, output_path, scale_factor=2.0, interpolation=cv2.INTER_CUBIC):
    # Read the original image
    image = cv2.imread(input_path)
    if image is None:
        print("Error: Unable to load image.")
        return

    # Calculate the new dimensions
    new_width = int(image.shape[1] * scale_factor)
    new_height = int(image.shape[0] * scale_factor)
    new_dimensions = (new_width, new_height)

    # Resize the image
    upscaled_image = cv2.resize(image, new_dimensions, interpolation=interpolation)

    # Save the upscaled image
    cv2.imwrite(output_path, upscaled_image)

    print(f"Image upscaled and saved as {output_path}")

# Example usage
upscale_image("img/vangogh.png", "img/upscaled_vangoghx4.png", scale_factor=4.0)
