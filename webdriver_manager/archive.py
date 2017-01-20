import os
import tarfile
import zipfile


def extract_zip(zip_file, to_directory):
    archive = zipfile.ZipFile(zip_file)
    archive.extractall(to_directory)
    return archive.namelist()


def extract_tar_file(tar_file, to_dir):
    tar = tarfile.open(tar_file.name, mode="r:gz")
    members = tar.getmembers()
    tar.extractall(to_dir)
    tar.close()
    return members


def unpack(archive):
    to_directory = os.path.dirname(archive.name)
    if archive.name.endswith(".zip"):
        return extract_zip(archive, to_directory)
    else:
        file_list = extract_tar_file(archive, to_directory)
        return [x.name for x in file_list]
