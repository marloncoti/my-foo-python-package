#!/bin/bash

# VERSION=''

# tag="v1.0.0.0"

# preffix=${tag:0:1}

# if [ "${preffix,,}" == "v" ]; then VERSION="${tag:1}"; else VERSION="${tag:0}"; fi

# echo $VERSION


TAG_NAME='v1343.1203'
TAG=''
PREFIX=''
VERSION=''

if [ -z "$TAG_NAME" ]; then TAG="1.0.0"; else TAG=${TAG_NAME}; fi

PREFIX=${TAG:0:1}
if [ "${PREFIX,,}" == "v" ]; then VERSION="${TAG:1}"; else VERSION="${TAG:0}"; fi
echo $VERSION 
