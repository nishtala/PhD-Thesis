from DropboxDownloader import DropboxDownloader

# Initialise the object and give it the folder to store its downloads in
d = DropboxDownloader('/home/nishtala/Dropbox/UPC/dropbox-thesis-directive/logs')

# Download all available previous versions
d.download_history_for_files("/home/nishtala/Dropbox/UPC/PhD-Thesis",  # Folder containing files to download
                             "*.tex",  # 'glob' string specifying files to download
                             "/home/nishtala/Dropbox/")  # Path to your Dropbox folder
