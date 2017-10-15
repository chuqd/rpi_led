import lirc
sockid = lirc.init("myprogram", "/home/pi/.lircrc")

print(lirc.nextcode())
lirc.deinit()
