#!/usr/bin/env bash

mkdir -p build/meshes build/models build/routes build/worlds build/track_iconography

for a in $(ls -d tracks/*/ | cut -f2 -d\/);
do
    echo "Found track $a." 
    cp tracks/$a/worlds/* build/worlds
    cp tracks/$a/track_iconography/* build/track_iconography
    cp tracks/$a/routes/* build/routes

    mkdir -p build/meshes/$a build/models/$a
    cp -r tracks/$a/meshes/* build/meshes/$a/
    cp -r tracks/$a/models/* build/models/$a/

done