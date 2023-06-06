import argparse
import os
import magic
import shutil
import tqdm

from PIL import Image
from pathlib import Path

image_types = {
    "image/tiff",
    "image/tif",
    "image/jpg",
    "image/jpeg",
    "image/png",
    "image/webp"
}

def check_is_image(filepath: str) -> bool:

    if magic.from_file(filepath, mime=True) not in image_types:
        return False
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "--source_dir",
        type=str,
        default=None,
        required=True,
        help="Source directory to process."
    )
    
    parser.add_argument(
        "--destination_dir",
        type=str,
        default=None,
        required=True,
        help="Destination directory to write into."
    )
    
    parser.add_argument(
        "--output_format",
        type=str,
        default="jpeg",
        required=False,
        help="Destination directory to write into."
    )

    parser.add_argument(
        "--compression_lvl",
        type=int,
        default=90,
        required=False,
        help="JPEG compression level to use."
    )

    parser.add_argument(
        "--dry_run",
        action="store_true",
        default=False,
        help="Wheter to just print actions. Not execute any action."
    )
    
    args = parser.parse_args()

    print("=" * 80)
    print(f"[*] source_dir:        {args.source_dir}")
    print(f"[*] destination_dir:   {args.destination_dir}")
    print(f"[*] output_format:     {args.output_format}")
    print(f"[*] compression_lvl:   {args.compression_lvl}")
    print(f"[*] dry_run:           {args.dry_run}")
    print("=" * 80 + "\n")
    
    source_images = [
        p.resolve() 
        for p in Path(args.source_dir).glob("**/*") 
        if check_is_image(p)
    ]
    
    print(f"Total to process: {len(source_images)}")
    
    if os.path.isdir(args.destination_dir):
        print(f"[INFO] Deleting destination folder: `{args.destination_dir}`")
        if not args.dry_run:
            shutil.rmtree(args.destination_dir)
    
    if not args.dry_run:
        os.makedirs(args.destination_dir)
    
    for source_file in tqdm.tqdm(source_images):
        try:
            # print(source_file.name)
            im = Image.open(source_file)
            
            im.thumbnail(im.size)
            
            if not args.dry_run:
                im.save(
                    f"{args.destination_dir}/{source_file.stem}.{args.output_format.lower()}", 
                    format=args.output_format.upper(), 
                    quality=args.compression_lvl
                )
        except Exception as e:
            print(f"[ERROR] {e}")