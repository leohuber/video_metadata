#!/bin/bash

VERSION="1.1.0"

# Update the version in the pyproject.toml file
sed -i '' "s/^version = .*/version = $VERSION/" pyproject.toml

# Update the version in the __version__.py file
sed -i '' "1s/.*/__version__ = \"$VERSION\"/" ./video_metadata/__version__.py