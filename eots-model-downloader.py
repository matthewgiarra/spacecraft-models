import json
from pathlib import Path
import os
import requests
from urllib.parse import urljoin
import argparse
import pdb

def download_file(url, filepath):
    print(f"  ↓ Downloading: {url}")
    response = requests.get(url, stream=True)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    with open(filepath, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"  ✓ Saved: {filepath}")

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--names', nargs = '+', type=str, default = [], help='Spacecraft name corresponding to the Name field in the config file (e.g. in spacecraft.json)')
    parser.add_argument('-d', '--outdir', type=str, default="models", help="Path to output directory (in which model folders will be saved). Default: models")
    args = parser.parse_args()
    names_list = args.names
    outdir = args.outdir

    # Read the JSON configuration
    with open("spacecraft.json") as f:
        data = json.load(f)

    # List of spacecraft names
    spacecraft_list = data["Spacecraft"]

    # Convert the sat names from the arg list to lower case
    names_list = [x.lower() for x in names_list]

    # Pick out the spacecraft from the spacecraft list.
    # If there were no spacecraft names specified in the arg list (e.g. if satnames = []), then run all entries in the config file.
    if len(names_list) > 0:
        spacecraft_list = [x for x in spacecraft_list if x["Name"].lower() in names_list]
    
    # Download all the GLTF files
    for spacecraft in spacecraft_list:
        spacecraft_name = spacecraft["Name"]
        gltf_url = spacecraft["GLTF"]
        print(f"\n🚀 Processing: {spacecraft_name}")

        # Create satellite folder
        model_folder = Path(outdir).joinpath(Path(spacecraft_name.lower()))
        model_folder.mkdir(parents=True, exist_ok=True)
        gltf_path = model_folder.joinpath(Path(gltf_url).name)

        print("GLTF URL: %s" % gltf_url)
        print("GLTF Path: %s" % gltf_path)

        # Download files
        try:

            # Download the GLTF file
            download_file(gltf_url, gltf_path)

            # Read the glTF file and download all referenced files
            with open(gltf_path) as f:
                gltf = json.load(f)

            # Download .bin files (buffers)
            for buffer in gltf.get("buffers", []):
                uri = buffer.get("uri")
                if uri and not uri.startswith("data:"):
                    file_url = urljoin(gltf_url, uri)
                    file_path = model_folder.joinpath(uri)
                    download_file(file_url, file_path)

            # Download image files (.png, .jpg, etc.)
            for image in gltf.get("images", []):
                uri = image.get("uri")
                if uri and not uri.startswith("data:"):
                    file_url = urljoin(gltf_url, uri)
                    file_path = model_folder.joinpath(uri)
                    download_file(file_url, file_path)
        except:
            print("Problem with %s" % gltf_path)
            with open("errors.txt", "w+") as fid:
                print("%s" % gltf_path, file = fid)

    print("\n✅ Done!")


if __name__ == "__main__":
    main()
