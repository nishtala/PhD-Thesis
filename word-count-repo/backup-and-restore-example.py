#!/usr/bin/env python
import os
import sys
import fnmatch
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

TOKEN = 'sUHruvPbqFoAAAAAAANESYG5t1XkQLg9hiYKSTaTZf3AdPj04bVHmcNWAvZSSS9i'

folder = '/home/nishtala/Dropbox/UPC/PhD-Thesis/'
globstring = '*.tex'
saveto = '/home/nishtala/Dropbox/UPC/dropbox-thesis-directive/logs/'

# Look at all of the available revisions on Dropbox, and return the oldest one
def select_revision(filename, dbx):
    # Get the revisions for a file (and sort by the datetime object, "server_modified")
    #print("Finding available revisions on Dropbox...")
    revisions = sorted(dbx.files_list_revisions(filename, limit=100).entries, key=lambda entry: entry.server_modified)
    output_folder = saveto
    for revision in revisions:
        revision_id = revision.rev
        mod_time    =  str(revision.client_modified).replace(" ", "_").replace(":", "").replace("+", "").replace(',', '')

        if not os.path.exists(output_folder):
            os.mkdir(output_folder)

        folder = os.path.join(output_folder, os.path.splitext(os.path.basename(filename))[0])

        if not os.path.exists(folder):
            os.mkdir(folder)

        out_filename = os.path.join(folder, '%s.tex' % (mod_time))

        if not os.path.exists(out_filename):
            dbx.files_download_to_file(out_filename, filename, revision.rev) #as f:

def recursive_file_search(path, pattern):
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches


def download_history_for_files(folder, globstring, dbx, recursive=True):
    if recursive:
        files = recursive_file_search(folder, globstring)
    else:
        files = glob(folder + globstring)

    for dropboxpath in files:
        dropbox_location = '/home/nishtala/Dropbox/'
        #print (dropboxpath)
        dbpath = os.path.relpath(dropboxpath, dropbox_location).replace("\\", "/")
        dbpath = '/' + dbpath
        select_revision(dbpath, dbx)


def main():
    # Check for an access token
    if (len(TOKEN) == 0):
        sys.exit("ERROR: Looks like you didn't add your access token. Open up backup-and-restore-example.py in a text editor and paste in your token in line 14.")

    # Create an instance of a Dropbox class, which can make requests to the API.
    print("Creating a Dropbox object...")
    dbx = dropbox.Dropbox(TOKEN)

    # Check that the access token is valid
    try:
        dbx.users_get_current_account()
    except AuthError as err:
        sys.exit("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")
    download_history_for_files(folder, globstring, dbx)



if __name__ == '__main__':
    main()
