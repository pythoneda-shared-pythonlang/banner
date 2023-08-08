#!/usr/bin/env python3
"""
pythoneda/banner/ps1.py

This file defines the PS1 class.

Copyright (C) 2023-today rydnr's pythoneda-shared-pythoneda/banner

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.banner import Metadata
from typing import List

class PS1(Metadata):
    """
    Defines the shell prompt.

    Class name: PS1

    Responsibilities:
        - Provides a custom shell prompt for PythonEDA projects.

    Collaborators:
        - None
    """
    def __init__(self, org:str, repo:str, tag:str, space:str, archRole:str, layer:str, pythonVersion:str, nixpkgsRelease:str):
        """
        Initializes the instance.
        :param org: The organization name (in github terms).
        :type org: str
        :param repo: The repository name.
        :type repo: str
        :param tag: The tag.
        :type tag: str
        :param space: The space type (' ' or '_' for none, 'A' for Artifact, 'R' for Runtime, 'T' for Tenant).
        :type space: str
        :param archRole: The architecture role ('B' for Bounded Context, 'E' for Event, 'S' for Shared, 'R' for Realm).
        :type archRole: str
        :param layer: The layer ('D' for Domain, 'I' for Infrastructure, 'A' for Application).
        :type layer: str
        :param pythonVersion: The Python version.
        :type pythonVersion: str
        :param nixpkgsRelease: The name of the nixpkgs release.
        :type nixpkgsRelease: str
        :return: The banner text.
        :rtype: List[str]
        """
        super().__init__(org, repo, tag, space, archRole, layer, pythonVersion, nixpkgsRelease)

    def print(self) -> str:
        """
        Builds the PS1.
        :return: The PS1.
        :rtype: str
        """
        python_major = self.python_version.split('.')[0]
        print(f"\\033[37m[\\[\033[01;34m\\]{self.org}/{self.repo}\033[01;37m#\033[01;33m{self.tag}\\033[01;37m|\\033[01;36m\\]python{python_major}-{self.python_version}\\]\\033[37m|\\[\\033[00m\\]\\[\\033[01;37m\\]\\W\\033[37m]\\033[31m$\\[\\033[00m\\] ")


if __name__ == "__main__":
    inst = PS1.parse_cli("Provides the PS1 value")
    inst.print()
