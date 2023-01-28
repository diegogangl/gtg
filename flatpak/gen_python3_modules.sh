#!/usr/bin/bash

set -e

OUTPUT_FILE="python3-requirements.yaml"

# Using flatpak-pip-generator from
# https://github.com/flatpak/flatpak-builder-tools
flatpak-pip-generator \
    --runtime=org.gnome.Sdk//43 \
    --requirements-file requirements.txt \
    --yaml \
    --output "${OUTPUT_FILE%.yaml}"

# Patch the lxml module because it is already in the runtime.
# See: https://gitlab.gnome.org/GNOME/gnome-build-meta/-/issues/380
echo "Patching ${OUTPUT_FILE} for lxml"
sed -i 's@\("lxml.*" --no-build-isolation\)@\1 --ignore-installed@' "${OUTPUT_FILE}"
