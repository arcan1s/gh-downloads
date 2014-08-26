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


import argparse, json
try:
    import urllib.request
    from io import StringIO
except ImportError:
    import urllib


def getCountByRepo(owner, repo):
    """function to get info from latest release"""
    tag = ""
    count = 0
    requestUrl = "https://api.github.com/repos/" + owner + "/" + repo + "/releases"
    try:
        jsonOutput = [jsonString for jsonString in json.load(urllib.urlopen(requestUrl))]
    except AttributeError:
        io = StringIO(urllib.request.urlopen(requestUrl).read().decode("utf-8"))
        jsonOutput = [jsonString for jsonString in json.load(io)]
    except:
        pass
    try:
        count = jsonOutput[0][u'assets'][0][u'download_count']
        tag = jsonOutput[0][u'tag_name']
    except:
        pass
    return tag, count


def getCountById(owner, repo, id):
    """function to get info by id"""
    tag = ""
    count = 0
    requestUrl = "https://api.github.com/repos/" + owner + "/" + repo + "/releases/assets/" + id
    try:
        jsonOutput = json.load(urllib.urlopen(requestUrl))
    except AttributeError:
        io = StringIO(urllib.request.urlopen(requestUrl).read().decode("utf-8"))
        jsonOutput = json.load(io)
    except:
        pass
    try:
        count = jsonOutput[u'download_count']
        tag = id
    except:
        pass
    return tag, count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Get number of downloads for given owner and project')
    parser.add_argument('-q', '--quiet', dest = 'quiet',
                        help = 'less output', action = 'store_true', default = False)
    parser.add_argument('-i', '--id', dest = 'id',
                        help = 'release ID', action = 'store', default = False)
    parser.add_argument('-o', '--owner', dest = 'owner',
                        help = 'repository owner', action = 'store',
                        default = False, required = True)
    parser.add_argument('-r', '--repository', dest = 'repository',
                        help = 'repository name', action = 'store',
                        default = False, required = True)
    args = parser.parse_args()

    tag = ""
    count = 0
    if (args.id):
        tag, count = getCountById(args.owner, args.repository, args.id)
    else:
        tag, count = getCountByRepo(args.owner, args.repository)

    if (args.quiet):
        print (count)
    else:
        print ("Release tag: " + tag + "\nDownloads: " + str(count))
