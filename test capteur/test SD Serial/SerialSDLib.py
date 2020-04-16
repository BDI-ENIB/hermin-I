import machine
import time
import pycom

def SetupOpenLog(uart_sd,resetOpenLogPin):

    pycom.rgbled(0x202000)
    resetOpenLogPin.value(0)
    time.sleep(0.05)
    resetOpenLogPin.value(1)

    while 1:
        if uart_sd.any()>0:
            if str(uart_sd.read(1)) == "<":
                break
    pycom.rgbled(0x000000)
    return

def createFile(uart_sd,fileName):
    uart_sd.write('new ')
    uart_sd.write(fileName)
    uart_sd.write('\r')

    while 1:
        if uart_sd.any()>0:
            if str(uart_sd.read(1)) == "<":
                break

    uart_sd.write('append ')
    uart_sd.write(fileName)
    uart_sd.write('\r')

    while 1:
        if uart_sd.any()>0:
            if str(uart_sd.read(1)) == "<":
                break
    return
