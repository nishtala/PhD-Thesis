from glob import glob
import fnmatch
import os
import dropbox
#from dropbox.client import DropboxOAuth2FlowNoRedirect, DropboxClient
#from dropbox import rest as dbrest


class DropboxDownloader:
    def __init__(self, output_folder):
        self.output_folder = output_folder
        self.c = None

        self.connect_to_dropbox()

    def connect_to_dropbox(self):

        self.c = dropbox.Dropbox('sUHruvPbqFoAAAAAAANESYG5t1XkQLg9hiYKSTaTZf3AdPj04bVHmcNWAvZSSS9i')

    def _recursive_file_search(self, path, pattern):
        """
        Searches recursively for files.

        :param path: Path to search
        :param pattern: Glob-style pattern (eg. *.tex)
        :return:
        """
        matches = []
        for root, dirnames, filenames in os.walk(path):
            for filename in fnmatch.filter(filenames, pattern):
                matches.append(os.path.join(root, filename))

        return matches

    def download_revisions(self, filename, output_folder=None):
        """
        Download all available revisions of the given filename (must be relative to the Dropbox root),
        storing them in output_folder.

        :param filename: Relative path to file inside the Dropbox folder
        :param output_folder: Folder to download to - defaults to None, meaning it uses the class attribute
        output_folder
        """
        print self.c.files_list_revisions
        revs = sorted(self.c.files_list_revisions(filename, limit=10000).entries,
                       key=lambda entry: entry.server_modified)
        print revs
        #revs = self.c.files_list_revisions(filename)
        #revs = self.c.revisions(filename)

        for rev in revs:
            print(rev)
            revision_id = rev.rev
            mod_time = rev['client_mtime'].replace(" ", "_").replace(":", "").replace("+", "").replace(',', '')


            if output_folder is None:
                output_folder = self.output_folder

            if not os.path.exists(output_folder):
                os.mkdir(output_folder)

            folder = os.path.join(output_folder, os.path.splitext(os.path.basename(filename))[0])

            if not os.path.exists(folder):
                os.mkdir(folder)

            out_filename = os.path.join(folder, '%s.tex' % (mod_time))

            if not os.path.exists(out_filename):
                outfile = open(out_filename, 'wb')
                with self.c.get_file(filename, rev=revision_id) as f:
                    outfile.write(f.read())

                outfile.close()
            else:
                print("Already done, skipping")

    def download_history_for_files(self, folder, globstring, dropbox_location, recursive=True):
        """
        Download all available revisions for a given set of files.

        :param folder: The full path to the Dropbox folder which contains the files you're interested in
        :param globstring: The globstring (eg. *.txt) to use to select files
        :param dropbox_location: The full path to the root of your Dropbox folder
        :param recursive: Whether to search recursively (default) or not
        """
        if recursive:
            files = self._recursive_file_search(folder, globstring)
        else:
            files = glob(folder + globstring)

        #print(files)
        for f in files:
            #print(f)
            dropboxpath = os.path.relpath(f, dropbox_location).replace("\\", "/")
            dropboxpath = '/' + (dropboxpath)
            self.download_revisions(dropboxpath)
