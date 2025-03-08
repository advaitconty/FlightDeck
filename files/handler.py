import pathlib
import files.picture
import files.markdown

def read_file(file):
    print(f"Reading file: {file}")
    extension = pathlib.Path(file).suffix.lower()
    print("Extension:", extension)

    image = [".jpg", ".jpeg", ".png"]
    
    if extension in image:
        files.picture.print_image(file)
    elif extension == ".md":
        files.markdown.print_markdown_fancy(file)

