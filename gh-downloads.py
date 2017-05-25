#!/usr/bin/python
# -*- coding: utf-8 -*-

############################################################################
#   Copyright (C) 2014 Evgeniy Alekseev                                    #
#                                                                          #
#   This program is free software: you can redistribute it and/or          #
#   modify it under the terms of the GNU General Public License as         #
#   published by the Free Software Foundation, either version 3 of the     #
#   License, or (at your option) any later version.                        #
#                                                                          #
#   This program is distributed in the hope that it will be useful,        #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#   GNU General Public License for more details.                           #
#                                                                          #
#   You should have received a copy of the GNU General Public License      #
#   along with this program. If not, see http://www.gnu.org/licenses/      #
############################################################################


import argparse
import json
import requests


def getCountByRepo(owner, repo):
    """
    get info from latest release
    """
    requestUrl = "https://api.github.com/repos/{}/{}/releases".format(
        owner, repo)
    response = requests.get(requestUrl).json()
    return response[0]["tag_name"], dict((ass["name"], ass["download_count"])
                                         for ass in response[0]["assets"])


def getCountById(owner, repo, asset):
    """
    get info by id
    """
    requestUrl = "https://api.github.com/repos/{}/{}/releases/assets/{}".format(
        owner, repo, asset)
    response = requests.get(requestUrl).json()
    return asset, {response["name"]: response["download_count"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get number of downloads for given owner and project")
    parser.add_argument("owner", help="repository owner")
    parser.add_argument("repository", help="repository name")
    parser.add_argument("-q", "--quiet", help="less output",
                        action="store_true")
    parser.add_argument("-i", "--id", help="release ID")
    args = parser.parse_args()

    if args.id:
        tag, count = getCountById(args.owner, args.repository, args.id)
    else:
        tag, count = getCountByRepo(args.owner, args.repository)

    if not args.quiet:
        print("Release tag: {}".format(tag))
    for asset in count:
        print("{}: {}".format(asset, count[asset]))
