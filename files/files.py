import pathlib
import image
import markdown

def read_file(file):
    extension = pathlib.Path(file).suffix().lower()

    image = ["jpg", "jpeg", "png"]
    
    if extension in image:
        image.print_image(file)
    elif extension == "md":
        markdown.print_markdown_fancy(file)

