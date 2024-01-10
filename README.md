# DeepRacer Custom Track

This repository contains custom tracks for AWS DeepRacer. It's purpose is to be an extension to the default tracks in the [DeepRacer Simapp](https://github.com/aws-deepracer-community/deepracer-simapp), which contains the tracks that are also available in the AWS DeepRacer Console. See the [Race Data Repository's Track List](https://github.com/aws-deepracer-community/deepracer-race-data/blob/main/raw_data/tracks/README.md) for all details about the official tracks.

Custom tracks can be:
* A mash-up of the official tracks by adding/removing features like buildings, lights etc. - whilst still keeping the original track shape.
* A 'cut-out' of an offical track to reduce the size.
* A completely new track.

Motivation for creating a new track can be:
* Increased variability to reduce risk of overfitting for physical racing.
* Creating a smaller foot-print track to allow for physical racing at home.

## Using the repository

The repository works by adding its files 'on top' of an existing Robomaker/Simapp Docker Image.

To use the repository run the following commands:
1. `scripts/build.sh` to collect the relevant files into the `build/` directory.
1. `docker build . -t awsdeepracercommunity/deepracer-robomaker:5.1.1-ext-cpu-avx2 -f scripts/Dockerfile.localext --build-arg FROM_TAG=5.1.1-cpu-avx2`

In the last command the docker image tag after `-t` is the tag of the new image (as an example, choose your tag). The part after FROM_TAG is the tag of the image that you will add the tracks to. This image should be on your system already, if not Docker will download it.

Once built the image can be used by altering DRfC's `system.env` by using the new tag `5.1.1-ext-cpu-avx2`.