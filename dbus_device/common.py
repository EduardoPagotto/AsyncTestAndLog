'''
Created on 20190807
Update on 20190808
@author: Eduardo Pagotto
'''

# well-known name for our program
ECHO_BUS_NAME = 'com.testez1.api_20190807.DeviceStatus'

GET_ENABLE_INTERFACE = ECHO_BUS_NAME + '.getEnableInterface'
SET_ENABLE_INTERFACE = ECHO_BUS_NAME + '.setEnableInterface'
GET_MESSAGE_INTERFACE = ECHO_BUS_NAME + '.getMessageInterface'
SET_MESSAGE_INTERFACE = ECHO_BUS_NAME + '.setMessageInterface'

QUIT_INTERFACE = ECHO_BUS_NAME + '.quitInterface'

# paths to some objects in our program
ECHO_OBJECT_PATH = '/DeviceStatusServerObject'
