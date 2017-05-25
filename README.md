gh-downloads
============

Information
-----------

Python script which returns a number of downloads by given GitHub project.

Usage
-----

```
gh-downloads.py [-h] [-q] [-i ID] owner repository

Get number of downloads for given owner and project

positional arguments:
  owner           repository owner
  repository      repository name

optional arguments:
  -h, --help      show this help message and exit
  -q, --quiet     less output
  -i ID, --id ID  release ID
```

If `ID` is not given result of the **latest release** will be printed.

If `quiet` is not set the output is:

    Release tag: tag_name
    Downloads: count

otherwise it is:

    count
