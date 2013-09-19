# -*- coding: utf8 -*-
import ftplib
import os
import zipfile

def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))

def sendftp(spath, sfilename):
    sfilename = sfilename +".zip"
    spath = spath +""+ sfilename
    session = ftplib.FTP('192.168.137.140','test','test')  
    myfile = open(spath,'rb')
    session.storbinary('STOR '+sfilename, myfile)
    print sfilename +" to send."
    myfile.close()                                          
    session.quit()                                        

if __name__ == '__main__':
    path="D:\\"
    dirname ="file"
    zip = zipfile.ZipFile(path+""+dirname+".zip", 'w')
    zipdir(path+""+dirname, zip)
    zip.close()
    sendftp(path, dirname)
