import Dropbox
class transferData:
    def _init_(self, access_token):
        self.access_token = access_token


    def upload_file(self, file_from, file_to):
            dbx = dropbox.Dropbox(self.access_token)
            for root, dirs, filews in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbpx_patj = os.path.join(file_to, relatice_path)
            with open(local_path, 'rb') as f:
            dbx.upload_file(f.read(). dropbox_path, mode=WriteMode('overwrite'))
        
    def main()
        access_token = XkFJdoWNt2kAAAAAAAAAAcQcLSaniswCyUgyjpUUQp6TxDFXtOhKuXYzH_8THH91
        transferdata = transferData(access_token)
        file_from = input("")
        file_to = input("")

        transferdata.upload_file(file_from, file_to)
        print("file has been moved")



main()        
