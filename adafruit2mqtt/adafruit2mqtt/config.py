import yaml
import logging
import logging.config

class Config:
	"""Class for parsing adafruit2mqtt.yaml."""
	
	def __init__(self):
		"""Initialize Config class."""
		logging.config.fileConfig('logging.conf')
		self._mqtt = {}
		self._adafruit = {}
	
	
	def read(self, file='adafruit2mqtt.yaml'):
		"""Read config."""
		logging.debug("Reading %s", file)
		try:
			with open(file, 'r') as filehandle:
				config = yaml.load(filehandle)
				self._parse_mqtt(config)
				self._parse_adafruit(config)
		except FileNotFoundError as ex:
			logging.error("Error while reading %s: %s", file, ex)


	def _parse_mqtt(self, config):
		"""Parse the mqtt section of adafruit2mqtt.yaml."""
		if "mqtt" in config:
			self._mqtt = config["mqtt"]
		if not "host" in self._mqtt:
				raise ValueError("MQTT host not set")
		if not "port" in self._mqtt:
				raise ValueError("MQTT port not set")
		if not "user" in self._mqtt:
				raise ValueError("MQTT user not set")
		if not "password" in self._mqtt:
				raise ValueError("MQTT password not set")
		if not "topic" in self._mqtt:
				raise ValueError("MQTT topic not set")


	def _parse_adafruit(self, config):
		"""Parse the adafruit section of adafruit2mqtt.yaml."""
		if "adafruit" in config:
			self._adafruit = config["adafruit"]
		if not "sensor" in self._adafruit:
				raise ValueError("adafruit sensor not set")
		if not "gpio" in self._adafruit:
				raise ValueError("adafruit gpio not set")
		if not "topic" in self._adafruit:
				raise ValueError("adafruit topic not set")


	def mqtt(self):
		return self._mqtt

	def adafruit(self):
		return self._adafruit
