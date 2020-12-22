from Maix import GPIO
from fpioa_manager import fm, board_info



fm.register(8,fm.fpioa.GPIOHS11)

en=GPIO(GPIO.GPIOHS11,GPIO.OUT)

en.value(1)
