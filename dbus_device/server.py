#!/usr/bin/env python3

import sys
import gi.repository.GLib
import dbus
import dbus.service
import dbus.mainloop.glib

import common

class DeviceStatus(dbus.service.Object):
    def __init__(self):
        self.__status = 2
        self.__msg = 'offline'
        self.__enable = False

        self.bus = dbus.SessionBus()

        try:
            name = dbus.service.BusName(common.ECHO_BUS_NAME, bus=self.bus, do_not_queue=True)
        except dbus.NameExistsException:
            sys.exit('Server is already running.')
        else:
            print('Server is not running yet. Putting on listening ears.')

        super().__init__(name, common.ECHO_OBJECT_PATH)

    @dbus.service.method(common.GET_ENABLE_INTERFACE, in_signature='', out_signature='b')
    def getEnable(self):
        return self.__enable    

    @dbus.service.method(common.SET_ENABLE_INTERFACE, in_signature='b', out_signature='')
    def setEnable(self, value):
        self.__enable = value

    @dbus.service.method(common.GET_MESSAGE_INTERFACE, in_signature='', out_signature='s')
    def getMessage(self):
        return self.__msg    

    @dbus.service.method(common.SET_MESSAGE_INTERFACE, in_signature='s', out_signature='')
    def setMessage(self, value):
        self.__msg= value

    @dbus.service.method(common.QUIT_INTERFACE, in_signature='', out_signature='')
    def quit(self):
        # this should be a separate object, but I'm
        # showing how one object can have multiple interfaces
        self.mainloop.quit()

if __name__ == '__main__':

    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    loop = gi.repository.GLib.MainLoop()

    scanner = DeviceStatus()
    scanner.mainloop = loop
    
    loop.run()