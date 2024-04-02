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

background_image_path = "input.png"
overlay_image_path = "mask.png"
output_image_path = "result.png"
overlay_images(background_image_path, overlay_image_path, output_image_path)
