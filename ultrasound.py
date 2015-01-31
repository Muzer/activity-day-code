from sr import *

class USRuggeduino(Ruggeduino):
    def distance(self):
        with self.lock:
            resp = self.command("d")
        return int(resp)
