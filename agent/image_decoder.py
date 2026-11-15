import base64
import io
from pathlib import Path
from tkinter import TclError, Tk, filedialog
from langchain.messages import HumanMessage
from PIL import Image, UnidentifiedImageError
from dotenv import load_dotenv

load_dotenv()

def choose_image_file() -> Path:
    """Open a local file picker when no image path is passed on the command line."""
    root = None
    try:
        root = Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        filename = filedialog.askopenfilename(
            title="Choose an image",
            filetypes=[
                ("Images", "*.png *.jpg *.jpeg *.webp"),
                ("All files", "*.*"),
            ],
        )
    except TclError:
        filename = input("Image path: ").strip().strip('"').strip("'")
    finally:
        if root is not None:
            root.destroy()

    if not filename:
        raise SystemExit("No image selected.")

    return Path(filename).expanduser()

def image_to_data_url(image_path: Path) -> str:
    image_path = image_path.expanduser().resolve()

    if not image_path.is_file():
        raise FileNotFoundError(f"Image not found: {image_path}")

    try:
        with Image.open(image_path) as image:
            image.load()  # Fail here with a local, actionable error for corrupt files.
            # Sending a normalized JPEG avoids MIME/codec mismatches with OpenAI-compatible
            # endpoints (for example, HEIC files renamed to .jpg or animated WebP).
            image = image.convert("RGB")
            buffer = io.BytesIO()
            image.save(buffer, format="JPEG", quality=90)
    except (UnidentifiedImageError, OSError) as exc:
        raise ValueError(f"Could not decode image file: {image_path}") from exc

    image_b64 = base64.b64encode(buffer.getvalue()).decode("ascii")
    return f"data:image/jpeg;base64,{image_b64}"

def build_image_message(image_path: Path, prompt:str) -> HumanMessage:
    return HumanMessage(
        content=[
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": image_to_data_url(image_path)}},
        ]
    )
