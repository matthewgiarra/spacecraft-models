import json
import os
import argparse

def getModelInfo(spacecraftDictIn):
    modelDictOut = {}
    modelDictOut['ModelName'] = spacecraftDictIn['Name']
    modelDictOut['FolderName'] = spacecraftDictIn['Name']
    modelDictOut['gltfFileName'] = os.path.basename(spacecraftDictIn['GLTF'])
    modelDictOut['glbFileName']  = os.path.basename(spacecraftDictIn['GLTF']).replace(".gltf", ".glb")
    modelDictOut['DisplayName'] = spacecraftDictIn['DisplayName']
    modelDictOut['FullName'] = spacecraftDictIn['FullName']
    modelDictOut['Description'] = spacecraftDictIn['Description']
    modelDictOut['eotssURL'] = spacecraftDictIn['URL']
    
    return modelDictOut

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', type=str, default="spacecraft.json", help="Name of the json-formatted file containing names and URLs of spacecraft models content")
    parser.add_argument('-o', '--outfile', type=str, default=os.path.join('viewer', 'models.json'), help="Path to output file. Default: viewer/models.json")
    args = parser.parse_args()
    infile = args.infile
    outfile = args.outfile

    # Read the input file
    print("Reading %s" % infile)
    with open(infile, 'r') as f:
        data = json.load(f)

    # Populate models list
    models = [getModelInfo(x) for x in data['Spacecraft']]
    modelsDict = {'Models':models}

    # Write the output file
    print("Writing %s" % outfile)
    with open(outfile, 'w') as f:
        json.dump(modelsDict, f)

if __name__ == "__main__":
    main()