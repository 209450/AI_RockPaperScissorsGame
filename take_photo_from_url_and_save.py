import argparse
import keyboard
from pathlib import Path
import requests


def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_dir', dest='output_dir', action='store', required=True,
                        help='output directory')
    parser.add_argument('--ulr', dest='url', action='store', required=True,
                        help='photo url')
    parser.add_argument('--start_index', dest='start_index', action='store', default=1,
                        help='start index of photo')

    return parser.parse_args()


photo_index = 1
output_file_extension = '.jpg'


def caputure_photo_and_save(url, output_dir):
    global photo_index

    respone_content = requests.get(url, stream=True).content
    image_name = output_dir / str(photo_index)
    image_path = image_name.with_suffix(output_file_extension)

    with open(image_path, 'wb') as file:
        file.write(respone_content)
    photo_index += 1

    print(f"taken {photo_index}")


if __name__ == "__main__":
    args = parse_input()

    url = args.url
    photo_index = int(args.start_index)
    output_dir = Path(args.output_dir)
    assert output_dir.is_dir, "Path is not a directory"

    keyboard.add_hotkey("space", caputure_photo_and_save, args=(url, output_dir))
    keyboard.wait('esc')
