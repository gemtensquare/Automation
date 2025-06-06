# import os
# from PIL import Image, ImageDraw, ImageFont

# # Load the image
# image = Image.open("mee1.jpg").convert("RGB")

# # Resize if needed
# image = image.resize((800, 450))  # standard 16:9 ratio for news

# # Create drawing context
# draw = ImageDraw.Draw(image)

# # Load a font (make sure you have a TTF font file, or use a system path)
# try:
#     font_headline = ImageFont.truetype("arialbd.ttf", 40)  # bold headline
#     font_banner = ImageFont.truetype("arialbd.ttf", 30)
# except IOError:
#     font_headline = ImageFont.load_default()
#     font_banner = ImageFont.load_default()

# # Add a red banner at bottom
# banner_height = 70
# draw.rectangle(
#     [(0, image.height - banner_height), (image.width, image.height)],
#     fill="red"
# )

# # Add white text on banner (e.g., "BREAKING NEWS")
# draw.text((10, image.height - banner_height + 15), "BREAKING NEWS", font=font_banner, fill="white")

# # Add headline at top
# headline_text = "Unexpected Weather Hits the City!"
# draw.text((20, 20), headline_text, font=font_headline, fill="white")

# # Optionally, add a translucent black rectangle behind headline
# draw.rectangle(
#     [(0, 0), (image.width, 80)],
#     fill=(0, 0, 0, 128)
# )
# draw.text((20, 20), headline_text, font=font_headline, fill="white")

# # Show final image
# image.show()

# # Save if needed
# # image.save("enhanced_news_template.jpg")



from PIL import Image, ImageDraw, ImageFont


def helper_image(image):
    image = image.resize((800, 450))  # 16:9 ratio

    draw = ImageDraw.Draw(image)

    # Load fonts
    try:
        font_headline = ImageFont.truetype("arialbd.ttf", 40)
        font_subheadline = ImageFont.truetype("arialbd.ttf", 25)
        font_small = ImageFont.truetype("arial.ttf", 20)
    except:
        font_headline = ImageFont.load_default()
        font_subheadline = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # === TOP Banner (BREAKING NEWS) ===
    draw.rectangle([(0, 0), (image.width, 60)], fill="red")
    draw.text((10, 10), "BREAKING NEWS", font=font_headline, fill="white")

    # === Main Headline ===
    draw.rectangle([(0, 70), (image.width, 140)], fill=(0, 0, 0, 180))
    draw.text((20, 80), "Unexpected Weather Hits the City!", font=font_headline, fill="white")

    # === Subheadline ===
    draw.text((20, 150), "Heavy rain floods major roads this morning.", font=font_subheadline, fill="white")

    # === Reporter Info and Location ===
    draw.text((20, 190), "Reported by: Md. Sishir Rahman Siam", font=font_small, fill="white")
    draw.text((20, 220), "Dhaka - 8:30 AM", font=font_small, fill="white")

    # === Bottom Ticker ===
    ticker_height = 50
    draw.rectangle([(0, image.height - ticker_height), (image.width, image.height)], fill="black")
    draw.text((10, image.height - ticker_height + 15), "Stay tuned for more updates...", font=font_small, fill="yellow")

    # Show and Save
    return image
    # image.save("news_template_full.jpg")

# # Load and resize image
# image = Image.open("mee2.jpg").convert("RGB")
# image = helper_image(image)

# # Show image
# image.show()