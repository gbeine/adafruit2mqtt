#!/usr/bin/env python3

from adafruit2mqtt import config
from adafruit2mqtt import daemon

def main():
	cfg = config.Config()
	cfg.read()
	d = daemon.Daemon(cfg)
	d.run()
	
main()

