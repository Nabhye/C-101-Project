import os
import shutil
import dropbox.files
import WriteMode
# import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))

def main():
    access_token = 'sl.A_vVhE22t7zvpFJPsfVm_E1E1p7tiex7mgZUVMzTUS2WOuXyKpYoRWO6jYmvCisEghPIzrb1F7jGBTppo3hv3AySLc5A_zswkSlaGVrJ6-zZ4l6PAGOfSG4Qoa2qJkWGEZVAH8M'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer: "))
    file_to = str(input("Enter the full path to upload to dropbox: "))

    transferData.upload_file(file_from, file_to)
    print("file has been moved")

main()