#!/usr/bin/python
from argparse import ArgumentParser
import sys

VERSION = '0.1 UNSTABLE'

def print_logo():
    print("   _____  ____   _____         ")
    print("  / ____|/ __ \ / ____|  /\    ")
    print(" | (___ | |  | | (___   /  \   ")
    print("  \___ \| |  | |\___ \ / /\ \  ")
    print("  ____) | |__| |____) / ____ \ ")
    print(" |_____/ \____/|_____/_/    \_\\")
    print(" SharePoint Online Security Auditor\n", VERSION, "\n")

def main():
    parser = ArgumentParser()
    parser.add_argument("-tenant", dest="url", help="Provide a a known tenant within the SharePoint Online ecosystem. Ex: https://test.sharepoint.com")
    parser.add_argument("-username", dest="url", help="Provide a username for the tenant. Ex: reception@test.com")
    parser.add_argument("-password", dest="id", help="Provide a password for the tenant. Ex: hunter1.")
    parser.add_argument("--quiet", dest="quiet",  action="store_true", help="Supress banner and headers to limit to comma dilimeted results only.")
    parser.add_argument("--listsites", dest="listsites",  action="store_true", help="List all sites in the provided tenant that the credentials have access to.")
    parser.add_argument("--listdepth", dest="listdepth",  help="List the depth of subsites that should be listed. Significant performance decrease and increased noise and scanning times should be expected")
    parser.add_argument("--listusers", dest="listusers",  help="List all users and their properties from the user information list.")
    parser.add_argument("--peopleenum", dest="peopleenum",  help="Attempt to identify users by enumerating the people service.")
    arguments = parser.parse_args()

    if len(sys.argv) == 1:
        print_logo()

        parser.error("No arguments given.  Please specify a tenant (url or id) as well as a known username and password from the tenant.")
        sys.exit()

    if arguments.quiet is not True:
        print_logo()

if __name__ == "__main__":
    main()