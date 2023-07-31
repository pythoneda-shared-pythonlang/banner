# PythonEDA Banner

ASCII banner for PythonEDA projects.

## Usage

``` sh
nix run https://github.com/pythoneda-shared-pythoneda/banner#default -- \
  -o [ORGANIZATION] \
  -r [REPOSITORY] \
  -t [TAG] \
  -s [SPACE] \
  -a [ARCHITECTURE_ROLE] \
  -l [LAYER] \
  -p [PYTHON_VERSION] \
  -n [NIXPKGS_RELEASE] 
```

Where:
 * -o ORGANIZATION: The github organization.
 * -r REPOSITORY: The repository.
 * -t TAG: The tag.
 * -s SPACE: The space. '_' for None; A for Artifact; R for Runtime; T for Tenant.
 * -a ARCHITECTURE_ROLE: The architecture role of the project. 'B' for Bounded Context; 'E' for Event; 'S' for Shared Kernels; 'R' for Realms.
 * -l LAYER: The type of hexagonal layer. 'D' for Domain; 'I' for Infrastructure; 'A' for Application.
 * -p PYTHON_VERSION: The Python version.
 * -n NIXPKGS_RELEASE: The nixpkgs release.
