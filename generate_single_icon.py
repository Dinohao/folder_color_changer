import sys
from PIL import Image, ImageDraw, ImageFilter

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def apply_color(base_png_path, hex_color, output_png_path):
    try:
        # Open the base image
        base_image = Image.open(base_png_path).convert("RGBA")
    except FileNotFoundError:
        print(f"Error: Base PNG file not found at {base_png_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error opening base PNG: {e}")
        sys.exit(1)

    # Get the RGB and Alpha channels
    r, g, b, a = base_image.split()

    # Create a new image with the desired color
    rgb_color = hex_to_rgb(hex_color)
    colored_rgb = Image.new("RGB", base_image.size, rgb_color)

    # Merge the new RGB with the original alpha channel
    colored_image = Image.merge("RGBA", (colored_rgb.getchannel('R'), 
                                        colored_rgb.getchannel('G'), 
                                        colored_rgb.getchannel('B'), 
                                        a))

    # Create a shadow effect
    shadow_color_rgba = (0, 0, 0, 100) # Black with some transparency
    shadow_offset = (int(base_image.width * 0.03), int(base_image.height * 0.03)) # Slightly larger offset
    shadow_blur_radius = 8 # Increased blur

    # Create a solid black image with the same alpha as the base image
    shadow_base = Image.new("RGBA", base_image.size, shadow_color_rgba)
    shadow_base.putalpha(a) # Apply the original alpha channel

    # Create a new image for the shadow, offset it, and blur
    shadow = Image.new("RGBA", base_image.size, (0, 0, 0, 0))
    shadow.paste(shadow_base, shadow_offset, shadow_base) # Paste with alpha mask
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=shadow_blur_radius))

    # Composite all layers
    # Start with a transparent background
    final_image = Image.new("RGBA", base_image.size, (0, 0, 0, 0))
    final_image = Image.alpha_composite(final_image, shadow)
    final_image = Image.alpha_composite(final_image, colored_image)

    # Save the result
    try:
        final_image.save(output_png_path)
    except Exception as e:
        print(f"Error saving PNG: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 generate_single_icon.py <base_png_path> <hex_color> <output_png_path>")
        sys.exit(1)

    base_png_path = sys.argv[1]
    hex_color = sys.argv[2]
    output_png_path = sys.argv[3]

    try:
        from PIL import Image, ImageDraw, ImageFilter
    except ImportError:
        print("Pillow library not found. Please install it using: pip install Pillow")
        sys.exit(1)

    apply_color(base_png_path, hex_color, output_png_path)