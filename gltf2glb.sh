#!/bin/bash
# convert-to-glb.sh - Create .glb alongside each .gltf (keeps original files untouched)

echo "Starting conversion to .glb (embedded textures)..."

for dir in models/*/ ; do
  if [ -d "$dir" ]; then
    folder=$(basename "$dir")
    gltf_file=$(find "$dir" -maxdepth 1 -name "*.gltf" | head -n 1)

    if [ -n "$gltf_file" ]; then
      glb_file="${dir}${folder}.glb"   # e.g. models/ace/ace.glb

      echo "Converting: $folder → ${folder}.glb"

      gltf-pipeline -i "$gltf_file" -o "$glb_file" --separate false --embed true
    fi
  fi
done

echo "✅ Conversion complete! .glb files are now inside each model folder."