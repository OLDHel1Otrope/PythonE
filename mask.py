from PIL import Image, ImageFilter

def overlay_images(background_img_path, overlay_img_path, output_img_path):
    background_img = Image.open(background_img_path)
    overlay_img = Image.open(overlay_img_path)
    if background_img.size != overlay_img.size:
        raise ValueError("Images must have the same dimensions")
    overlay_img_gray = overlay_img.convert("L")
    blurred_overlay_img = overlay_img_gray.filter(ImageFilter.GaussianBlur(radius=0))
    mask = Image.eval(overlay_img_gray, lambda pixel: 255 if pixel == 0 else 0)
    background_img.paste(blurred_overlay_img, (0, 0), mask)
    background_img.save(output_img_path)


def extract_areas_using_mask(background_img_path, overlay_img_path, output_img_path):

    background_img = Image.open(background_img_path)
    overlay_img = Image.open(overlay_img_path)
    if background_img.size != overlay_img.size:
        raise ValueError("Images must have the same dimensions")
    overlay_img_gray = overlay_img.convert("L")

    # creating a mask where black areas in the overlay image are transparent
    mask = overlay_img_gray.point(lambda pixel: 0 if pixel < 128 else 255)

    # iterating through each pixel of the overlay image
    width, height = overlay_img.size
    for x in range(width):
        for y in range(height):
            # If the pixel in the overlay image is black, copy the corresponding pixel from the background image
            if mask.getpixel((x, y)) == 0:
                background_pixel = background_img.getpixel((x, y))
                overlay_img.putpixel((x, y), background_pixel)
    overlay_img.save(output_img_path)

def extract_text_from_image(image_path):
    # Open the image
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text
    
background_image_path = "input.png"
overlay_image_path = "mask.png"
output_image_path = "result.png"
output_adv_image_path = "extracted_text.png"
overlay_images(background_image_path, overlay_image_path, output_image_path)
extract_areas_using_mask(background_image_path, overlay_image_path, output_adv_image_path)
