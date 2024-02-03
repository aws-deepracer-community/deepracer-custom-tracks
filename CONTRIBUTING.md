# Contributing a Track

To contribute a track to the repository there is a few design guidelines to follow regarding the structure of the files and their names.

## Name

Please select a name for your track. The name should not be the same as the original DeepRacer tracks. (See the [Race Data Repository's Track List](https://github.com/aws-deepracer-community/deepracer-race-data/blob/main/raw_data/tracks/README.md) for all details about the official tracks.) Exception is customized original tracks who should be suffixed with `_custom`.

## Required files and structure

Each track will have it's own folder in the `tracks/` folder. The name of the folder is equal to the track name. The track names and folders are case sensitive.

Needed sub-folders are: `meshes/`, `models/`, `routes/`, `track_iconography/`, `worlds/`. `src/` is optional.

### Example
The Amoeba example shows the folder strcture and the files within. Source files are in `src/`, and includes a Jupyter notebook and a Blender file.
```
tracks/Amoeba/
├── meshes
│   ├── Amoeba_collision.dae
│   ├── Amoeba.dae
│   ├── textures
│   │   ├── background.png
│   │   ├── centerLine.png
│   │   ├── field.png
│   │   ├── outerLine.png
│   │   ├── road.png
│   │   ├── startline.png
│   │   └── wall.png
│   └── wall.dae
├── models
│   ├── Amoeba.sdf
│   └── model.config
├── routes
│   └── Amoeba.npy
├── src
│   ├── Amoeba.blend
│   ├── Amoeba_iconography.svg
│   ├── Amoeba_raw.svg
│   ├── Amoeba.svg
│   └── Create_Track_Amoeba.ipynb
├── track_iconography
│   └── Amoeba.png
└── worlds
    └── Amoeba.world
```

### File details

There is a set of files needed. Some have specific file names, others can be chosen by the track designer.

| Directory           | File                    |  Description       |
|---------------------|-------------------------|--------------------|
| worlds              | `<track_name>.world`    | Gazebo world-file. Describes the overall environment, including lights. Can load in one or more models, one of which needs to be called `racetrack` and reference the track model.
| models              | `models.config`         | Model configuration file. It is a plug file pointing to the SDF.
| models              | `<track_name>.sdf`         | SDF file describing the model, it is used to combine multiple objects/meshes into one model.
| meshes              | `*.dae`         | A set of collada files describing one or more objects. The filenames are referenced in the SDF file.
| meshes              | `*.png`,`*.jpg` | A set of textures referenced by the collada files. Sometimes put into an optional `textures/` subdirectory.
| routes              | `<track_name>.npy`      | The waypoint file describing the bounds of the track programmatically.
| track_iconography   | `<track_name>.png`      | The track image. 640x480 pixels, for a track wider than tall the original track image should be scaled to 510px wide, then centered on the 640x480 canvas. Standard color of the track is `#a9a9a9` with opacity of `0.6`.

## Creating a track
The concept of creating a track is a medium complexity task and will involve using a combination of Jupyter notebooks, Inkscape (edit SVG), Blender (create Collada files) and GIMP (adjust iconography).

Have a look in the [Amoeba Notebook](tracks/Amoeba/src/Create_Track_Amoeba.ipynb) for some guidance on how to create the intermediary SVG files and route Numpy programmatically.

### Testing

#### Using Robomaker Development Environment
To test a track one can clone the [DeepRacer Simapp](https://github.com/aws-deepracer-community/deepracer-simapp/) repository which is used to build the Robomaker images.

The [`build-dev-bundle`](https://github.com/aws-deepracer-community/deepracer-simapp/blob/master/build-dev-bundle.sh) script will provide the development environment needed.

* Clone deepracer-simapp, run `build-dev-bundle.sh` in the simapp directory.
* Run `make copyinstall TARGET=<dir-to-simapp>` in the custom tracks directory.
* Define variables:
    * `export DR_WORLD_NAME=<your_track_name>`
    * `export DR_ROBOMAKER_IMAGE=<robomaker_tag>` (example: `5.1.2-cpu-avx2`)
* Run container using `build-dev-bundle.sh -g`; this will open the gazebo UI showing your track (Linux only).

If you want to do it again just repeat the `make copyinstall` and `build-dev-bundle.sh -g`.

#### Using Robomaker Images
To test directly on a Robomaker image run `make image TAG=<base_tag>`, and alter your DRfC `system.env` to use the new image (containing `-ext`). Then see the track using e.g. `dr-start-evaluation`.