#!/bin/bash

VERSION=''

tag="v1.0.0.0"

preffix=${tag:0:1}

if [ "${preffix,,}" == "v" ]; then VERSION="${tag:1}"; else VERSION="${tag:0}"; fi

echo $VERSION