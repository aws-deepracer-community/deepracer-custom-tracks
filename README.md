# DeepRacer Custom Track

This repository contains custom tracks for AWS DeepRacer. It's purpose is to be an extension to the default tracks in the [DeepRacer Simapp](https://github.com/aws-deepracer-community/deepracer-simapp), which contains the tracks that are also available in the AWS DeepRacer Console. See the [Race Data Repository's Track List](https://github.com/aws-deepracer-community/deepracer-race-data/blob/main/raw_data/tracks/README.md) for all details about the official tracks.

Tracks can be:
* A remix of the official tracks by adding/removing features like buildings, lights etc. - whilst still keeping the original track shape.
* A 'cut-out' of an offical track to reduce the size.
* A completely new track.

Motivation for creating a new track can be:
* Increased variability to reduce risk of overfitting for physical racing.
* Creating a smaller foot-print track to allow for physical racing at home.

## Using the repository

The repository works by adding its files 'on top' of an existing Robomaker/Simapp Docker Image.

To use the repository run the following commands:
1. `make build` to collect the relevant files into the `build/` directory.
1. `make image TAG=<your_robomaker_tag>` to extend the `awsdeepracercommunity/deepracer-robomaker:<your_robomaker_tag>` image. 

Once built the image can be used by altering DRfC's `system.env` by using the new tag `<your_robomaker_tag>-ext`.

## Other commands

Two other commands are available:

* `make copy-src TARGET=<your_robomaker_path>` - this will copy the files into the *source* of Robomaker, i.e from `build/` to `$TARGET/bundle`.
* `make copy-install TARGET=<your_robomaker_path>` - this will copy the files into the *built* bundle in Robomaker, i.e from `build/` to `$TARGET/install/deepracer_simulation_environment/share/deepracer_simulation_environment/`.
