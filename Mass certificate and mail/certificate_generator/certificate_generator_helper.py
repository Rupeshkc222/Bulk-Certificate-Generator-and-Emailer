import os
from PIL import Image, ImageDraw, ImageFont

def generate_certificate(candidate_name, template_path, output_directory):
    if candidate_name:
        # Create the output directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)

        template = Image.open(template_path)
        draw = ImageDraw.Draw(template)

        # Set the font and size for the candidate's name
        font = ImageFont.truetype("arial.ttf", 48)  # Update the font file and size as needed

        # Calculate the position to place the candidate's name
        text_width, text_height = draw.textsize(candidate_name, font=font)
        x = (template.width - text_width) // 2  # Center horizontally
        y = (template.height - text_height) // 2  # Center vertically

        # Draw the candidate's name on the template
        draw.text((x, y), candidate_name, fill="black", font=font)

        # Save the certificate as a file
        output_path = os.path.join(output_directory, f"{candidate_name}_certificate.png")
        template.save(output_path)
        print(f"Certificate generated for {candidate_name}")
    else:
        print("Empty candidate name encountered. Skipping certificate generation.")
