Sync Docker Images between registries
=====================================

Use this script to sync all tags for a given Docker repository from one registry to another.

Right now this script has only been tested using quay.io as source and hub.docker.com as destination.

Any destination is supposed to work. For a source to work it should use the /v2 version of Docker registry API.

# Instructions

- Install requirements: `pip install -r requirements.txt`
- Ensure you have access from your cli to the source and target repositories (login to the corresponding registries if needed).
- Run the script: `./sync.py quay.io/<docker-repo> <target-docker-repo`.

    Example: `./sync.py quay.io/pantheon-public/build-tools-ci pantheonpublic/build-tools-ci`
- Go grab a coffee! It will take some time to complete :)

