import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "mycompressed.zip")   #makes the path: dest/compressed.zip
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            archive.write(filepath)


if __name__ == "__main__":
    make_archive(filepaths=["file1zip.txt", "file2zip.txt"], dest_dir="dest")
    print("Done!")
