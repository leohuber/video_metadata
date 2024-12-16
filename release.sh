#!/bin/bash

VERSION="1.1.0"

# Check if GitHub CLI is installed
if ! command -v gh &> /dev/null
then
    echo "GitHub CLI could not be found. Please install it to proceed."
    exit 1
fi

# Check if GitHub CLI is authenticated
if ! gh auth status &> /dev/null
then
    echo "GitHub CLI is not authenticated. Please log in to proceed."
    exit 1
fi

# Check for uncommitted changes
if ! git diff-index --quiet HEAD --
then
    echo "There are uncommitted changes in the repository. Please commit or stash them to proceed."
    exit 1
fi

# Check if we are on the main branch
current_branch=$(git branch --show-current)
if [ "$current_branch" != "main" ]; then
    echo "You are not on the main branch. Please switch to the main branch to proceed."
    exit 1
fi

# Remove old versions of release if they exist
rm -Rf dist

# Build the module
uv build

# Create a new release
gh release create v${VERSION} --title "Release v${VERSION}" --generate-notes ./dist/*.gz ./dist/*.whl
