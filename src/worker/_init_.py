import smbus2 as smbus
import time
from datetime import datetime
import mysql.connector as MySQLdb

def __init__(self, db_connector,channel=1):
    """エキスパンダの初期化"""
    self.connector = db_connector
    self.channel = channel
    self.ICADDR = 0x20
    self.REG_IODIR_A = 0x00
    self.REG_IODIR_B = 0x01
    self.REG_GPIO_A = 0x12
    self.REG_GPIO_B = 0x13
    self.REG_OLAT_A = 0x14
    self.REG_OLAT_B = 0x15
    self.bus = smbus.SMBus(self.channel)

    # カーソル取得
    self.cursor = self.connector.cursor()

    # 制御レジスタの初期化
    try:
        self.bus.write_byte_data(address, self.REG_IODIR_A, 0b00000000)
        self.bus.write_byte_data(address, self.REG_IODIR_B, 0b11111111)
        self.bus.write_byte_data(address, self.REG_OLAT_A, 0b00000000)
    except OSError as e:
            print(f"I2C初期化中にエラーが発生しました1: {e}")
    
def close(self):
    """データベース接続を閉じる"""
    self.cursor.close()
    self.connector.close()

if __name__ == "__main__":
    __init__()
