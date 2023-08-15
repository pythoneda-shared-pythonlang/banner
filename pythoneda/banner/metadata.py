#!/usr/bin/env python3
"""
pythoneda/banner/metadata.py

This file defines the Metadata class.

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
import sys
from typing import List

class Metadata:
    """
    Defines common metadata.

    Class name: Metadata

    Responsibilities:
        - Holds PythonEDA project metadata.

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
    ) -> List[str]:
        """
        Initializes the instance.
        :param org: The organization name (in github terms).
        :type org: str
        :param repo: The repository name.
        :type repo: str
        :param tag: The tag.
        :type tag: str
        :param space: The space type ('D' for Decision, 'A' for Artifact, 'R' for Runtime, 'T' for Tenant).
        :type space: str
        :param archRole: The architecture role ('B' for Bounded Context, 'E' for Event, 'S' for Shared Kernel, 'R' for Realm).
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
        super().__init__()
        self._org = org
        self._repo = repo
        self._tag = tag
        self._space = space
        self._arch_role = archRole
        self._layer = layer
        self._python_version = pythonVersion
        self._nixpkgs_release = nixpkgsRelease
        self._dep_count = self.__class__.count_dependencies()
        self._pythoneda_dep_count = self.__class__.count_pythoneda_dependencies()

    @property
    def org(self) -> str:
        """
        Retrieves the organization name (in github terms).
        :return: Such name.
        :rtype: str
        """
        return self._org

    @property
    def repo(self) -> str:
        """
        Retrieves the repository name.
        :return: Such name.
        :rtype: str
        """
        return self._repo

    @property
    def tag(self) -> str:
        """
        Retrieves the tag.
        :return: Such tag.
        :rtype: str
        """
        return self._tag

    @property
    def space(self) -> str:
        """
        Retrieves the space type ('D' for Decision, 'A' for Artifact, 'R' for Runtime, 'T' for Tenant).
        :return: Such information.
        :rtype: str
        """
        return self._space

    @property
    def arch_role(self) -> str:
        """
        Retrieves the architecture role ('B' for Bounded Context, 'E' for Event, 'S' for Shared Kernel, 'R' for Realm).
        :return: Such information.
        :rtype: str
        """
        return self._arch_role

    @property
    def layer(self) -> str:
        """
        Retrieves the hexagonal layer ('D' for Domain, 'I' for Infrastructure, 'A' for Application).
        :return: Such information.
        :rtype: str
        """
        return self._layer

    @property
    def python_version(self) -> str:
        """
        Retrieves the Python version.
        :return: Such version.
        :rtype: str
        """
        return self._python_version

    @property
    def nixpkgs_release(self) -> str:
        """
        Retrieves the Nixpkgs release.
        :return: Such information.
        :rtype: str
        """
        return self._nixpkgs_release

    @property
    def dep_count(self) -> int:
        """
        Retrieves the number of dependencies.
        :return: Such information.
        :rtype: int
        """
        return self._dep_count

    @property
    def pythoneda_dep_count(self) -> int:
        """
        Retrieves the number of PythonEDA dependencies.
        :return: Such information.
        :rtype: int
        """
        return self._pythoneda_dep_count

    @classmethod
    def count_dependencies(cls) -> int:
        """
        Counts the number of entries in sys.path
        :return: Such count.
        :rtype: int
        """
        return len(sys.path)

    @classmethod
    def count_pythoneda_dependencies(cls) -> int:
        """
        Counts the number of PythonEDA entries in sys.path
        :return: Such count.
        :rtype: int
        """
        return sum(1 for path in sys.path if "pythoneda" in path)

    @classmethod
    def parse_cli(cls, description: str):
        """
        Parses command-line arguments.
        :param description: The description of the feature.
        :type description: str
        """
        import argparse

        parser = argparse.ArgumentParser(description=description)
        parser.add_argument(
            "-o", "--organization", required=True, help="The github organization"
        )
        parser.add_argument(
            "-r", "--repository", required=True, help="The name of the git repository"
        )
        parser.add_argument(
            "-t", "--tag", required=True, help="The tag of the git repository"
        )
        parser.add_argument(
            "-s",
            "--space",
            choices=["D", "A", "R", "T"], # decision, artifact, runtime, tenant
            required=True,
            help="The Pescio space of the project",
        )
        parser.add_argument(
            "-a",
            "--arch-role",
            choices=["B", "E", "S", "R"], # bounded context, event, shared kernel, realm
            required=True,
            help="The architecture role of the project",
        )
        parser.add_argument(
            "-l",
            "--layer",
            choices=["D", "I", "A"], # domain, infrastructure, application
            required=True,
            help="The layer of the project",
        )
        parser.add_argument(
            "-p", "--python-version", required=True, help="The Python version"
        )
        parser.add_argument(
            "-n", "--nixpkgs-release", required=True, help="The Nixpkgs release"
        )
        args, unknown_args = parser.parse_known_args()

        return cls(
            args.organization,
            args.repository,
            args.tag,
            args.space,
            args.arch_role,
            args.layer,
            args.python_version,
            args.nixpkgs_release,
        )
