import eventlet

from st2reactor.sensor.base import Sensor


class HelloSensor(Sensor):
    def __init__(self, sensor_service, config):
        super(HelloSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._stop = False
        # self.hourDuration = 60 * 60 # in seconds`
        self.hourDuration = 60 # in seconds`

    def setup(self):
        pass

    def run(self):
        while not self._stop:

            print(f"value of api_key is {config['api_key']}" ) 

            self._logger.debug("HelloSensor dispatching trigger...")

            count = self.sensor_service.get_value("learnst2.count") or 0
            payload = {"greetings": "Yo, StackStorm!", "api_key": config['api_key'], "location": "Seattle", "count": int(count) + 1}

            self.sensor_service.dispatch(trigger="learnst2.hello_sensor_trigger", payload=payload)

            self.sensor_service.set_value("learnst2.count", payload["count"])
            eventlet.sleep(self.hourDuration)

    def cleanup(self):
        self._stop = True

    # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass
