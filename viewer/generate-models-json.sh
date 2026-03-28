#!/bin/bash
# generate-models-json.sh
# Reads spacecraft.json and generates a clean models.json for the 3D viewer
# Run this whenever you update spacecraft.json or add new models

set -e  # Exit on error

INPUT_JSON="spacecraft.json"
OUTPUT_JSON="viewer/models.json"

echo "🔄 Generating models.json from $INPUT_JSON ..."

# Check if input file exists
if [ ! -f "$INPUT_JSON" ]; then
  echo "❌ Error: $INPUT_JSON not found in the current directory."
  exit 1
fi

# Start building the JSON
cat > "$OUTPUT_JSON" << EOF
{
  "models": [
EOF

first=true

# Process each spacecraft entry
jq -r '.Spacecraft[] | "\(.Name)|\(.GLTF)"' "$INPUT_JSON" | while IFS='|' read -r name gltf_url; do
  if [ -z "$name" ] || [ -z "$gltf_url" ]; then
    continue
  fi

  # Extract filename from the URL (e.g. "ace.gltf")
  filename=$(basename "$gltf_url")

  # Use the "Name" field as both folder name and display name
  folder="$name"

  if [ "$first" = false ]; then
    echo "    ," >> "$OUTPUT_JSON"
  fi
  first=false

  cat >> "$OUTPUT_JSON" << EOF
    {
      "name": "$name",
      "folder": "$folder",
      "filename": "$filename"
    }
EOF

done

# Close the JSON array and object
cat >> "$OUTPUT_JSON" << EOF
  ]
}
EOF

# Validate the generated JSON
if jq empty "$OUTPUT_JSON" >/dev/null 2>&1; then
  count=$(jq '.models | length' "$OUTPUT_JSON")
  echo "✅ Success! Generated $OUTPUT_JSON with $count spacecraft models."
  echo "   You can now run: ./viewer/index.html"
else
  echo "❌ Error: Generated JSON is invalid."
  exit 1
fi