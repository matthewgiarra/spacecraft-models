# spacecraft-models
3D models of spacecraft from [NASA Eyes On The Solar System (EOTSS)](https://eyes.nasa.gov/apps/solar-system)

View & download models using our simple model viewer on [Github Pages](https://matthewgiarra.github.io/spacecraft-models/).

# Overview
Each folder in the `models` directory contains a 3D model for a single spacecraft. Where multiple missions on EOTSS use the same 3D model, only a single copy of the model is provided.

Models are for illustrative purposes and are probably not radiometrically accurate.

## Model formats
Models for each spacecraft are provided in both `.gltf` (Graphics Library Transmission Format) and `.glb` (gLTF binary) formats. `.gltf` files are JSON files that specify geometry and reference resources (e.g. texture maps). `.glb` are binary files that consolidate geometry and textures in a single file (not human-readable).

`spacecraft.json` specifies the download URLs for all the `.gltf` files, which were deduced by inspecting network traffic on the [EOTS webpage](https://eyes.nasa.gov/apps/solar-system). 

The `.gltf` files and associated resources (e.g. .png, .jpg, .webp images) for each spacecraft were downloaded directly from [NASA Eyes On The Solar System (EOTSS)](https://eyes.nasa.gov/apps/solar-system) using the `eots-model-downloader.py` script.

The corresponding `.glb` files were created from the `.gltf` and resource files using the provided shell script `gltf2glb.sh`. Some models' files contained naming discrepancies (between names of resource files referenced in the `.gltf` file and of the resource files themselves) that needed to be fixed manually, so simply running `eots-model-downloader.py` followed by `gltf2glb.sh` might not work flawlessly. **We recommend skipping those scripts altogether and sticking with the model files included in the `models` directory of this repo.**

### Running the viewer locally 
To run the browser-based model viewer locally (offline):

1. Install git-lfs
```bash
sudo apt-get update
sudo apt-get install git-lfs
git lfs install
```
2. Download/clone the repo
```bash
git clone https://github.com/matthewgiarra/spacecraft-models
```
3. Start an HTTP server in the spacecraft-models directory
```bash
cd spacecraft-models
python3 -m http.server 8000
```
3. Navigate a browser to `localhost:8000`

That's it, you should see the viewer in your browser.

### Making changes
The model viewer (`viewer/index.html`) reads `viewer/models.json`, which contains the same information as `spacecraft.json` plus a little extra (like file paths). `viewer/models.json` is generated from `spacecraft.json` using the script `viewer/generate-models-json.py`. **Don't modify `viewer/models.json` by hand.** If you want to make changes (e.g., update the model descriptions), modify `spacecraft.json`, then update `viewer/models.json` by running `python viewer/generate-models-json.py`.
