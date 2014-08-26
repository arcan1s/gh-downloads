gh-downloads
============

Information
-----------

Python script which returns a number of downloads by given GitHub project.

Usage
-----

    gh-downloads.py [-h] [-i ID] [-q] -o OWNER -r REPOSITORY

    optional arguments:
    -h, --help            show this help message and exit
    -i ID, --id ID        release ID
    -q, --quiet           less output
    -o OWNER, --owner OWNER
                            repository owner
    -r REPOSITORY, --repository REPOSITORY
                            repository name

If `ID` is not given result of the **latest release** and the **first asset** will be printed.

If `quiet` is not set the output is:

    Release tag: tag_name
    Downloads: count

otherwise it is:

    count
