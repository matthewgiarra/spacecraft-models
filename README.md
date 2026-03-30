# spacecraft-models
3D models of spacecraft from [NASA Eyes On The Solar System](https://eyes.nasa.gov/apps/solar-system)

View & download models using our simple model viewer on [Github Pages](https://matthewgiarra.github.io/spacecraft-models/).

# Overview
Each folder in the `models` directory contains a 3D model for a single spacecraft. Where multiple missions on EOTSS use the same 3D model, only a single copy of the model is provided. ***TODO: The names of all missions on EOTSS that use a spacecraft model are given by the `missions` field in each `spacecraft` entry in `spacecraft-models.json`.***

Models are for illustrative purposes and are probably not radiometrically accurate.

## Model formats
Models for each spacecraft are provided in both `.gltf` (Graphics Library Transmission Format) and `.glb` (gLTF binary) formats. `.gltf` files are JSON files that specify geometry and reference resources (e.g. texture maps). `.glb` are binary files that consolidate geometry and textures in a single file (not human-readable).

The `.gltf` files and associated resources (e.g. .png, .jpg, .webp images) for each spacecraft were downloaded directly from [NASA Eyes On The Solar System (EOTSS)](https://eyes.nasa.gov/apps/solar-system). 

The corresponding `.glb` files were created from the `.gltf` and resource files using the provided shell script `gltf2glb.sh`. 

`spacecraft.json` specifies the download URLs for the `.gltf` files. The `.gltf` URLs were deduced by inspecting network traffic on the [EOTS webpage](https://eyes.nasa.gov/apps/solar-system). 

`eots-model-downloader.py`: 

1. Downloads each `.gltf` file specified in `spacecraft.json`
2. Reads the `gltf` file to determine the names of its associated resource files and infer their URLs
3. Downloads the resource files.

### Running the viewer locally 
To run the browser-based model viewer locally (offline):

1. Download/clone the repo
```bash
git clone https://github.com/matthewgiarra/spacecraft-models
```
2. Start an HTTP server in the spacecraft-models directory
```bash
cd spacecraft-models
python3 -m http.server 8000
```

3. Navigate a browser to `localhost:8000`

That's it, you should see the viewer in your browser. 
