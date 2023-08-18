#!/usr/bin/env python3
"""
pythoneda/banner/banner.py

This file defines the Banner class.

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

class Banner(Metadata):
    """
    Prints the PythonEDA banner in ASCII art.

    Class name: Banner

    Responsibilities:
        - Print the PythonEDA banner in ASCII art.

    Collaborators:
        - None
    """

    def __init__(
        self,
        org: str,
        repo: str,
        tag: str,
        space: str,
        archRole: str,
        layer: str,
        pythonVersion: str,
        nixpkgsRelease: str,
        depCount: int,
        pythonedaDepCount: int
    ):
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
        :param depCount: The number of dependencies.
        :type depCount: int
        :param pythonedaDepCount: The number of PythonEDA dependencies.
        :type pythonedaDepCount: int
        """
        super().__init__(org, repo, tag, space, archRole, layer, pythonVersion, nixpkgsRelease, depCount, pythonedaDepCount)

    def center(self, txt:str, space:int) -> tuple:
        """
        Provides a tuple with the number of spaces before and after, so given text gets centered according to the number of characters provided.
        :param txt: The text to print centered.
        :type txt: str
        :param space: The room (in number of characters) available.
        :type space: int
        :return: The tuple with the number of spaces to print before and after the text.
        :rtype: tuple
        """
        remaining = space - len(txt)
        first_half = int(remaining / 2)
        second_half = int(remaining / 2)
        if remaining/2 == int(remaining/2):
            second_half = first_half - 1
        return first_half, second_half

    def build(self) -> List[str]:
        """
        Builds the project banner.
        :return: The banner text.
        :rtype: List[str]
        """
        line1_first_half, line1_second_half = self.center(self.org, 40)
        line2_first_half, line2_second_half = self.center(self.repo, 40)
        result = []
        result.append( " \033[32m             _   _                          \033[35m_\033[0m")
        result.append(f" \033[32m\033[37mGPLv3       \033[32m| | | |                     \033[35m{self._pythoneda_dep_count:>3}\033[35m| |\033[36m{self._dep_count}\033[0m")
        result.append( " \033[32m _ __  _   _| |_| |__   ___  _ __   \033[34m___  \033[35m__| | \033[36m__ _ \033[32mhttps://pythoneda.github.io\033[0m\033[0m")
        result.append(f" \033[32m| '_ \| | | | __| '_ \ / _ \| '_ \ \033[34m/ _ \\\033[35m/ _` |\033[36m/ _` |\033[33mhttps://github.com/{self.org}/{self.repo}/tree/{self.tag}\033[0m")
        result.append(f" \033[32m| |_) | |_| | |_| | | | (_) | | | |\033[34m  __/\033[35m (_| |\033[36m (_| |\033[34mhttps://github.com/{self.org}\033[0m")
        result.append(f" \033[32m| .__/ \__, |\__|_| |_|\___/|_| |_|\033[34m\___|\033[35m\__,_|\033[36m\__,_|\033[35mhttps://github.com/nixos/nixpkgs/tree/{self.nixpkgs_release}\033[0m")
        result.append(f" \033[32m| |     __/ |{' '*line1_first_half}\033[34m{self.org.upper()}{' '*line1_second_half}\033[36mhttps://docs.python.org/{self.python_version}\033[0m")
        result.append(f" \033[32m|_|\033[37m{self.space}\033[31m{self.arch_role}\033[36m{self.layer}\033[32m |___/ {' '*line2_first_half}\033[33m{self.repo.upper()}{' '*line2_second_half}\033[37mhttps://patreon.com/rydnr\033[0m")
        result.append("")
        result.append(f" Thank you for using \033[31m{self.org}/{self.repo} {self.tag}\033[0m, \033[32mpython\033[34me\033[35md\033[36ma\033[0m in general, and for your appreciation of free software.")
        result.append("")
        return result

    def print(self):
        """
        Prints the project banner.
        """
        print('\n'.join(self.build()))

if __name__ == "__main__":
    inst = Banner.parse_cli("Prints the PythonEDA banner")
    inst.print()
