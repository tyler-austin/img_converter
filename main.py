import sys
from pathlib import Path

from img_converter import heic_2_png

fn_map = {
    'heic': {
        'png': heic_2_png
    },
    'heif': {
        'png': heic_2_png
    },
    'png': {
        'heic': None
    }
}


def assert_fn(condition: bool, msg: str):
    try:
        assert condition
    except AssertionError:
        print(msg)
        sys.exit(1)


def main(fmt: str, path: str):
    # Parse input path
    path = Path(path)

    # Verify input file exists
    assert_fn(path.exists(), f"File not found: {path}")

    # Verify input file format is supported
    input_fmt = path.suffix.split('.')[-1].lower()
    assert_fn(input_fmt in fn_map, f"Input file format not supported: {input_fmt}")
    assert_fn(fmt in fn_map[input_fmt], f"Output format not supported: {fmt}")

    # Get conversion function
    convert_fn = fn_map[input_fmt][fmt]
    assert_fn(callable(convert_fn), f"Conversion from {input_fmt.upper()} to {fmt.upper()} not supported")

    input_filename = path.stem + path.suffix
    print(f'Converting {input_filename} to {fmt.upper()}')

    # Convert image
    try:
        output_path = convert_fn(path)
        print(f"Converted image saved to:\n{output_path}")
    except Exception as e:
        print(f"Error converting file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main(*sys.argv[1:])
