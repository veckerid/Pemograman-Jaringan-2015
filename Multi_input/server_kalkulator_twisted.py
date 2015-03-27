# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.
from twisted.internet import reactor, protocol
import re, sys


class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""
    
    # Fungsi callback ketika ada pesan masuk
    def dataReceived(self, data):
        split = re.split("_", data)
        angka1 = split[1]
        operation = split[0]
        angka2 = split[2]
        if(operation =='*'):
            hasil = int(angka1)*int(angka2)
            self.transport.write(str(hasil))
        elif(operation=='/'):
            hasil = int(angka1)/int(angka2)
            self.transport.write(str(hasil))
        elif(operation=='+'):
            hasil = int(angka1)+int(angka2)
            self.transport.write(str(hasil))
        elif(operation=='-'):
            hasil = int(angka1)-int(angka2)
            self.transport.write(str(hasil))
        else:
            hasil = 'operation tidak dikenal'
            self.transport.write(str(hasil))


def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(6666,factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
