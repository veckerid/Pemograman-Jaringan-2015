# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.
from twisted.internet import reactor, protocol
import socket
import re
import sys
import os


class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""
    
    # Fungsi callback ketika ada pesan masuk
    def dataReceived(self, data):
        try:
            split = re.split(" ", data)
            operation = split[0]
            nama_file = split[1]
            
            
            if(operation =='new'):
                isi_raw = re.split("\'", data)
                isi_file = isi_raw[1]
                self.buatfile(nama_file, isi_file)
                
            elif(operation=='del'):
                self.dell_file(nama_file)
                

            elif(operation=='read'):
                self.readfile(nama_file)

            else:
                hasil = 'operation tidak dikenali'
                self.transport.write(hasil)

        except Exception, e:
            sys.exit(0)


    def buatfile(self,nama_file, isi):
        try:
            file = open(nama_file,'w')   # Trying to create a new file or open one
            file.write(isi)
            file.close()
            hasil= 'OK file berhasil di buat!'
            self.transport.write(hasil)
        except:
            hasil = "File gagal dibuat!"
            self.transport.write(hasil)
            sys.exit(0) # quit Python

    def dell_file(self,nama_file):
        try:
            os.remove(nama_file)
            hasil = "OK file telah terhapus!"
            self.transport.write(hasil)
        except:
            hasil = "file gagal dihapus!"
            self.transport.write(hasil)
            sys.exit(0) # quit Python

    def readfile(self,nama):
        try:
            # file = open('contoh.txt','r+')
            # f= file.readlines()
            # hasil = "".join(f)
            # file.close()
            # self.transport.write(hasil)
            file = open(nama,'r+')
            f= file.readlines()
            hasil = "".join(f)
            file.close()
            self.transport.write(hasil)
        except:
            hasil = "file gagal diload atau file belum ada!"
            self.transport.write(hasil)

def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(6666,factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
    
