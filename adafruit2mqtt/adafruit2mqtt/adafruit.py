
import Adafruit_DHT

class adafruit:

	def __init__(self, config):
		self._config = config
		self._init_adafruit()


	def update_and_publish(self, mqtt):
		data = self._update()
		for topic, value in data.items():
			mqtt.publish("{}/{}".format(self._config["topic"],topic), value)

	def _init_adafruit(self):
		if not "sensor" in self._config:
			raise ValueError("Missing sensor")
		if not "gpio" in self._config:
			raise ValueError("Missing gpio")
		if not "topic" in self._config:
			raise ValueError("Missing topic")


	def _update(self):
		data = {}
		humidity, temperature = Adafruit_DHT.read_retry(self._config["sensor"], self._config["gpio"])
		data["humidity"] = humidity
		data["temperature"] = temperature
		return data
