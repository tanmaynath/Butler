import os
from pathlib import Path
import shutil

DIRECTORIES = {
    "Web Pages": [".html5", ".html", ".htm", ".xhtml"],
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "Docs": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  ".pptx",".pdf"],
    "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "Text": [".txt", ".in", ".out"],
    "Python": [".py"],
    "XML": [".xml"],
    "DMG": [".dmg"],
    "Shell": [".sh"]
}

FILE_FORMATS = {}
for directory, file_formats in DIRECTORIES.items():
    for formats in file_formats:
        FILE_FORMATS[formats] = directory

DOWNLOADS_DIRECTORY = "/Users/tanmaynath/Downloads/"


def cleanup():

    for download in os.scandir(DOWNLOADS_DIRECTORY):
        if download.is_dir():
            continue
        file_path = Path(download.name)
        file_format = file_path.suffix.lower()
        file_path = DOWNLOADS_DIRECTORY + str(file_path)

        if file_format in FILE_FORMATS:
            directory_path = DOWNLOADS_DIRECTORY + str((Path(FILE_FORMATS[file_format])))
            try:
                os.makedirs(directory_path, exist_ok=True)
            except OSError as err:
                print("OS error: {0}".format())
            shutil.move(file_path, directory_path)

    other_folder = DOWNLOADS_DIRECTORY + "Others"
    try:
        os.mkdir(other_folder)
    except OSError as err:
        print("Could not create directory: {0}", err)

    for download in os.scandir(DOWNLOADS_DIRECTORY):
        try:
            if download.is_dir():
                continue
            else:
                other_file_path = DOWNLOADS_DIRECTORY + str(Path(download.name))
                shutil.move(other_file_path,other_folder)
        except OSError as err:
            print("OS Error: {0}".format(err))


if __name__ == "__main__":
    cleanup()

