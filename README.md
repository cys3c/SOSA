# SOSA
SharePoint Online Security Auditor (SOSA). A tool designed for quick mapping of SharePoint Online sites and discovery of information of interest to SharePoint Administrators and professional Penetration Testers


## Status

[![Build Status](https://travis-ci.org/codingo/SOSA.svg?branch=master)](https://travis-ci.org/codingo/SOSA)

##Usage

**Install Dependencies:**
```
pip install -r requirements.txt
```
**Run:** 
```
python sosa.py 
```
**usage:** sosa.py [-h] [-tenant URL] [-username URL] [-password ID] [--quiet]
               [--listsites] [--listdepth LISTDEPTH] [--listusers LISTUSERS]
               [--peopleenum PEOPLEENUM]

**optional arguments:**

  -h, --help            show this help message and exit
  
  -tenant URL           Provide a a known tenant within the SharePoint Online
  
                        ecosystem. Ex: https://test.sharepoint.com
  -username URL         Provide a username for the tenant. Ex:
                        reception@test.com
                        
  -password ID          Provide a password for the tenant. Ex: hunter1.
  
  --quiet               Supress banner and headers to limit to comma dilimeted
                        results only.
                        
  --listsites           List all sites in the provided tenant that the
                        credentials have access to.
                        
  --listdepth LISTDEPTH
                        List the depth of subsites that should be listed.
                        Significant performance decrease and increased noise
                        and scanning times should be expected
                        
  --listusers LISTUSERS
                        List all users and their properties from the user
                        information list.
                        
  --peopleenum PEOPLEENUM
                        Attempt to identify users by enumerating the people
                        service.
                        
