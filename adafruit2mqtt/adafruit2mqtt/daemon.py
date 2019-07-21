
import time

from adafruit2mqtt import mqtt
from adafruit2mqtt import adafruit

class Daemon:

	def __init__(self, config):
		self._config = config
		self._init_mqtt()
		self._init_adafruit()

	def run(self):
		while True:
			self._adafruit.update_and_publish(self._mqtt)
			time.sleep(300)

	def _init_mqtt(self):
		self._mqtt = mqtt.Mqtt(self._config.mqtt())
		self._mqtt.connect()

	def _init_adafruit(self):
		self._adafruit = adafruit.adafruit(self._config.adafruit())
