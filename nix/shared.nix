# nix/shared.nix
#
# This file provides functions used by PythonEDA's flake.nix files.
#
# Copyright (C) 2023-today rydnr's pythoneda-shared-pythoneda/banner
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
rec {
  shellHook-for = { archRole, layer, nixpkgsRelease, org, package, python
    , pythoneda-shared-pythoneda-domain, pythoneda-shared-pythoneda-banner, repo
    , space }:
    let
      pythonVersionParts = builtins.splitVersion python.version;
      pythonMajorVersion = builtins.head pythonVersionParts;
      pythonMajorMinorVersion =
        "${pythonMajorVersion}.${builtins.elemAt pythonVersionParts 1}";
    in ''
      export _PNAME="${package.pname}";
      export _PVERSION="${package.version}";
      export _PYNAME="${python.name}";
      export _PYVERSION="${pythonMajorMinorVersion}";
      export _NIXPKGSRELEASE="${nixpkgsRelease}";
      export _PYTHONEDA="${pythoneda-shared-pythoneda-domain}";
      export _PYTHONEDABANNER="${pythoneda-shared-pythoneda-banner}";
      export _ORG="${org}";
      export _ARCHROLE="${archRole}";
      export _LAYER="${layer}";
      export _REPO="${repo}";
      export _SPACE="${space}";
      export _TAG="${package.version}";
      export PS1="$($_PYTHONEDABANNER/bin/ps1.sh -o $_ORG -r $_REPO -t $_TAG -s $_SPACE -a $_ARCHROLE -l $_LAYER -p $_PYVERSION -n $_NIXPKGSRELEASE)";
      $_PYTHONEDABANNER/bin/banner.sh -o $_ORG -r $_REPO -t $_TAG -s $_SPACE -a $_ARCHROLE -l $_LAYER -p $_PYVERSION -n $_NIXPKGSRELEASE
      export PYTHONPATH="$(python $_PYTHONEDA/dist/scripts/fix_pythonpath.py)";
    '';
  devShell-for = { archRole, layer, nixpkgsRelease, org, package, pkgs, python
    , pythoneda-shared-pythoneda-domain, pythoneda-shared-pythoneda-banner, repo
    , space }:
    pkgs.mkShell {
      buildInputs = [ package pythoneda-shared-pythoneda-banner ];
      shellHook = shellHook-for {
        inherit archRole layer nixpkgsRelease org package python
          pythoneda-shared-pythoneda-domain pythoneda-shared-pythoneda-banner
          repo space;
      };
    };
  app-for = { package, entrypoint }: {
    type = "app";
    program = "${package}/bin/${entrypoint}.sh";
  };
}
