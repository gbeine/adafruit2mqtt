from setuptools import setup

setup(name='adafruit2mqtt',
      version='0.1',
      description='adafruit 2 MQTT bridge',
      url='https://github.com/gbeine/adafruit2mqtt',
      author='Gerrit',
      author_email='mail@gerritbeine.de',
      license='MIT',
      packages=['adafruit2mqtt'],
      requires=[
          'logging',
          'paho.mqtt',
          'pyyaml',
          'Adafruit_DHT',
        ],
      zip_safe=False)
