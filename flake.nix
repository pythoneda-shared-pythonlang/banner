# flake.nix
#
# This file packages pythoneda-shared-pythoneda/banner as a Nix flake.
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
{
  description = "Banner for PythonEDA projects";
  inputs = rec {
    nixos.url = "github:NixOS/nixpkgs/nixos-23.05";
    flake-utils.url = "github:numtide/flake-utils/v1.0.0";
  };
  outputs = inputs:
    with inputs;
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixos { inherit system; };
        pname = "pythoneda-shared-pythoneda-banner";
        pythonpackage = "pythoneda.banner";
        package = builtins.replaceStrings [ "." ] [ "/" ] pythonpackage;
        entrypoint = "banner";
        entrypoint-path = "${package}/${entrypoint}.py";
        description = "Banner for PythonEDA projects";
        license = pkgs.lib.licenses.gpl3;
        homepage = "https://github.com/pythoneda-shared-pythoneda/domain";
        maintainers = [ "rydnr <github@acm-sl.org>" ];
        nixosUrlParts = builtins.split "/" nixos.url;
        nixpkgsRelease =
          builtins.elemAt nixosUrlParts (builtins.length nixosUrlParts - 1);
        shared = import ./nix/shared.nix;
        pythoneda-shared-pythoneda-banner-for = { python, version }:
          let
            pnameWithUnderscores =
              builtins.replaceStrings [ "-" ] [ "_" ] pname;
            package = builtins.replaceStrings [ "." ] [ "/" ] pythonpackage;
            pythonVersionParts = builtins.splitVersion python.version;
            pythonMajorVersion = builtins.head pythonVersionParts;
            pythonMajorMinorVersion =
              "${pythonMajorVersion}.${builtins.elemAt pythonVersionParts 1}";
            wheelName =
              "${pnameWithUnderscores}-${version}-py${pythonMajorVersion}-none-any.whl";
          in python.pkgs.buildPythonPackage rec {
            inherit pname version;
            projectDir = ./.;
            src = ./.;
            pyprojectTemplateFile = ./pyprojecttoml.template;
            pyprojectTemplate = pkgs.substituteAll {
              authors = builtins.concatStringsSep ","
                (map (item: ''"${item}"'') maintainers);
              desc = description;
              inherit homepage pname pythonMajorMinorVersion pythonpackage
                version;
              package = builtins.replaceStrings [ "." ] [ "/" ] pythonpackage;
              src = pyprojectTemplateFile;
            };

            format = "pyproject";

            nativeBuildInputs = with python.pkgs; [ pip pkgs.jq poetry-core ];
            propagatedBuildInputs = with python.pkgs; [ ];

            pythonImportsCheck = [ pythonpackage ];

            unpackPhase = ''
              cp -r ${src} .
              sourceRoot=$(ls | grep -v env-vars)
              chmod +w $sourceRoot
              cp ${pyprojectTemplate} $sourceRoot/pyproject.toml
            '';

            postInstall = ''
              pushd /build/$sourceRoot
              for f in $(find . -name '__init__.py'); do
                if [[ ! -e $out/lib/python${pythonMajorMinorVersion}/site-packages/$f ]]; then
                  cp $f $out/lib/python${pythonMajorMinorVersion}/site-packages/$f;
                fi
              done
              popd
              mkdir $out/dist $out/bin
              cp dist/${wheelName} $out/dist
              jq ".url = \"$out/dist/${wheelName}\"" $out/lib/python${pythonMajorMinorVersion}/site-packages/${pnameWithUnderscores}-${version}.dist-info/direct_url.json > temp.json && mv temp.json $out/lib/python${pythonMajorMinorVersion}/site-packages/${pnameWithUnderscores}-${version}.dist-info/direct_url.json
              chmod +x $out/lib/python${pythonMajorMinorVersion}/site-packages/${entrypoint-path}
              echo '#!/usr/bin/env sh' > $out/bin/${entrypoint}.sh
              echo "export PYTHONPATH=$PYTHONPATH" >> $out/bin/${entrypoint}.sh
              echo "${python}/bin/python $out/lib/python${pythonMajorMinorVersion}/site-packages/${entrypoint-path} \$@" >> $out/bin/${entrypoint}.sh
              chmod +x $out/bin/${entrypoint}.sh
            '';

            meta = with pkgs.lib; {
              inherit description homepage license maintainers;
            };
          };
        pythoneda-shared-pythoneda-banner-0_0_1a2-for = { python }:
          pythoneda-shared-pythoneda-banner-for {
            version = "0.0.1a2";
            inherit python;
          };
      in rec {
        apps = rec {
          default = pythoneda-shared-pythoneda-banner-latest;
          pythoneda-shared-pythoneda-banner-0_0_1a2-python38 = shared.app-for {
            package =
              self.packages.${system}.pythoneda-shared-pythoneda-banner-0_0_1a2-python38;
            inherit entrypoint;
          };
          pythoneda-shared-pythoneda-banner-0_0_1a2-python39 = shared.app-for {
            package =
              self.packages.${system}.pythoneda-shared-pythoneda-banner-0_0_1a2-python39;
            inherit entrypoint;
          };
          pythoneda-shared-pythoneda-banner-0_0_1a2-python310 = shared.app-for {
            package =
              self.packages.${system}.pythoneda-shared-pythoneda-banner-0_0_1a2-python310;
            inherit entrypoint;
          };
          pythoneda-shared-pythoneda-banner-0_0_1a2-python311 = shared.app-for {
            package =
              self.packages.${system}.pythoneda-shared-pythoneda-banner-0_0_1a2-python311;
            inherit entrypoint;
          };
          pythoneda-shared-pythoneda-banner-latest =
            pythoneda-shared-pythoneda-banner-latest-python311;
          pythoneda-shared-pythoneda-banner-latest-python38 =
            pythoneda-shared-pythoneda-banner-0_0_1a2-python38;
          pythoneda-shared-pythoneda-banner-latest-python39 =
            pythoneda-shared-pythoneda-banner-0_0_1a2-python39;
          pythoneda-shared-pythoneda-banner-latest-python310 =
            pythoneda-shared-pythoneda-banner-0_0_1a2-python310;
          pythoneda-shared-pythoneda-banner-latest-python311 =
            pythoneda-shared-pythoneda-banner-0_0_1a2-python311;
        };
        defaultApp = apps.default;
        defaultPackage = packages.default;
        packages = rec {
          default = pythoneda-shared-pythoneda-banner-latest;
          pythoneda-shared-pythoneda-banner-0_0_1a2-python38 =
            pythoneda-shared-pythoneda-banner-0_0_1a2-for {
              python = pkgs.python38;
            };
          pythoneda-shared-pythoneda-banner-0_0_1a2-python39 =
            pythoneda-shared-pythoneda-banner-0_0_1a2-for {
              python = pkgs.python39;
            };
          pythoneda-shared-pythoneda-banner-0_0_1a2-python310 =
            pythoneda-shared-pythoneda-banner-0_0_1a2-for {
              python = pkgs.python310;
            };
          pythoneda-shared-pythoneda-banner-0_0_1a2-python311 =
            pythoneda-shared-pythoneda-banner-0_0_1a2-for {
              python = pkgs.python311;
            };
          pythoneda-shared-pythoneda-banner-latest =
            pythoneda-shared-pythoneda-banner-latest-python311;
          pythoneda-shared-pythoneda-banner-latest-python38 =
            pythoneda-shared-pythoneda-banner-0_0_1a2-python38;
          pythoneda-shared-pythoneda-banner-latest-python39 =
            pythoneda-shared-pythoneda-banner-0_0_1a2-python39;
          pythoneda-shared-pythoneda-banner-latest-python310 =
            pythoneda-shared-pythoneda-banner-0_0_1a2-python310;
          pythoneda-shared-pythoneda-banner-latest-python311 =
            pythoneda-shared-pythoneda-banner-0_0_1a2-python311;
        };
      });
}
