#!/usr/bin/env python3
'''
Created on 20190807
Update on 20190808
@author: Eduardo Pagotto
'''

import dbus
import common

if __name__ == '__main__':

    bus = dbus.SessionBus()
    try:
        deviceStatus = bus.get_object(common.ECHO_BUS_NAME, common.ECHO_OBJECT_PATH)
    except dbus.DBusException as e:

        if e._dbus_error_name == 'org.freedesktop.DBus.Error.ServiceUnknown':
            print('Servico Desconhecido')
        elif e._dbus_error_name == 'org.freedesktop.DBus.Error.NameHasNoOwner':
            print('Sem nome vinculado')
        else:
            print('client: No one can hear me!!')
    else:

        print('Valor enable 1: {0}'.format(str(deviceStatus.getEnable())))
        deviceStatus.setEnable(True)
        print('Valor enable 2: {0}'.format(str(deviceStatus.getEnable())))

        print('Valor msg 1: {0}'.format(str(deviceStatus.getMessage())))
        deviceStatus.setMessage('online')
        print('Valor msg 2: {0}'.format(str(deviceStatus.getMessage())))

        # # Encerra servidor
        # deviceStatus.quit()