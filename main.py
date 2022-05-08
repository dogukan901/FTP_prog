#DOĞUKAN OKÇU 181180761 BİLGİSAYAR AĞLARI FTP ÖDEV
# Import Module
import ftplib

#connection parameters
ftpHost = 'localhost'
ftpPort = 21
ftpUname = 'abcd'
ftpPass = '1234'



ftp = ftplib.FTP(timeout = 30)

ftp.connect(ftpHost,ftpPort)

ftp.login(ftpUname,ftpPass)

# fnames = ftp.nlst()

# print(fnames)

ftp.cwd("folder1/abcd")

targetFilename = "dogukansfiletodownload.txt"

# ftp.rename(targetFilename, "AdıDegistirildi.txt")

ftp.delete("AdıDegistirildi.txt")

"""
localFilePath = 'bm402upload.txt'

with open(localFilePath, 'rb') as file:
    retCode = ftp.storbinary("STOR bm402upload.txt",file, blocksize=1024*1024) """

""" targetFilename = "dogukansfiletodownload.txt"
localFilePath = targetFilename

with open(localFilePath,'wb') as file:
    retCode = ftp.retrbinary(f"RETR {targetFilename}", file.write) """

ftp.quit()

""" if retCode.startswith("226"):
    print("download basarili!")
else:
    print("download basarisiz...") """

""" if retCode.startswith("226"):
    print("upload basarili!")
else:
    print("upload basarisiz...") """

print("execution complete")
print("DOĞUKAN OKÇU 181180761 BİLGİSAYAR AĞLARI FTP ÖDEV")
