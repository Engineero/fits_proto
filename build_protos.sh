#!/bin/bash

protoc \
    --cpp_out=. \
    --csharp_out=. \
    --java_out=. \
    --python_out=. \
    fits.proto
