import sys
from pathlib import Path

from agent.models import model
from agent.image_decoder import (
    choose_image_file,
    build_image_message
)

path = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else choose_image_file()

message = build_image_message(
    path,
    "Describe the image and identify all visible ingredients."
)

try:
    response = model.invoke([message])
    print(response.content)

except Exception as e:
    print("Exception:", repr(e))

    if hasattr(e, "body"):
        print("API response body:", e.body)
