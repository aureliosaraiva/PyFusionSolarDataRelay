import os

class PvConf:
    def __init__(self, logger):
        self.logger = logger
        self.logger.debug("Conf class instantiated")
        self.apply_default_settings()
        self.apply_environment_settings()

    def apply_default_settings(self):
        self.logger.debug("Setting default conf values")
        
        # Generic default
        self.debug = True
        self.pvsysname = "huawei"

        # Fusionsolar default
        self.fusionsolar = True
        self.fusionsolarurl = "https://la5.fusionsolar.huawei.com/rest/pvms/web/kiosk/v1/station-kiosk-file?kk="
        self.fusionsolarkkid = "XXX"
        
        # The fusionsolar API only updates portal data each half hour, setting to lower value will produce weird PVOutput graph with horizontal bits in it.
        self.fusionhourcron = "*"
        self.fusionminutecron = "0,30" 

        # Mqtt default
        self.mqtt = True
        self.mqtthost = "localhost"
        self.mqttport = 1883
        self.mqttauth = False
        self.mqttuser = "fusionsolar"
        self.mqttpasswd = "fusionsolar"
        self.mqtttopic = "energy/pyfusionsolar"

    def print(self):
        self.logger.info(f"Current settings:")
        self.logger.info(f"_Generic:")
        self.logger.info(f"debug:   {self.debug}")
        self.logger.info(f"_FusionSolar:")
        self.logger.info(f"enabled: {self.fusionsolar}")
        self.logger.info(f"fusionsolarurl: {self.fusionsolarurl}")
        self.logger.info(f"fusionsolarkkid: {self.fusionsolarkkid}")
        self.logger.info(f"sysname: {self.pvsysname}")
        self.logger.info(f"fusionhourcron: {self.fusionhourcron}")
        self.logger.info(f"fusionminutecron: {self.fusionminutecron}")
        self.logger.info(f"_MQTT")
        self.logger.info(f"Enabled: {self.mqtt}")
        self.logger.info(f"Host: {self.mqtthost}")
        self.logger.info(f"Port: {self.mqttport}")
        self.logger.info(f"Auth: {self.mqttauth}")
        self.logger.info(f"User: {self.mqttuser}")
        self.logger.info(f"Passwd: {self.mqttpasswd}")
        self.logger.info(f"Topic: {self.mqtttopic}")

    def getenv(self, envvar):
        envval = os.getenv(envvar)
        self.logger.debug(f"Pulled '{envvar}={envval}' from the environment")
        return envval

    def apply_environment_settings(self):
        self.logger.info(f"Processing environment variables to running config")
        if os.getenv("pvdebug") != None:
            self.debug = self.getenv("pvdebug") == "True"
        if os.getenv("pvfusionsolar") != None:
            self.fusionsolar = self.getenv("pvfusionsolar") == "True"
        if os.getenv("pvfusionsolarurl") != None:
            self.fusionsolarurl = self.getenv("pvfusionsolarurl")
        if os.getenv("pvfusionsolarkkid") != None:
            self.fusionsolarkkid = self.getenv("pvfusionsolarkkid")
        if os.getenv("pvsysname") != None:
            self.pvsysname = self.getenv("pvsysname")
        if os.getenv("pvfusionhourcron") != None:
            self.fusionhourcron = int(self.getenv("pvfusionhourcron"))
        if os.getenv("pvfusionminutecron") != None:
            self.fusionminutecron = int(self.getenv("pvfusionminutecron"))

        if os.getenv("pvmqtt") != None:
            self.mqtt = self.getenv("pvmqtt") == "True"
        if os.getenv("pvmqtthost") != None:
            self.mqtthost = self.getenv("pvmqtthost")
        if os.getenv("pvmqttport") != None:
            self.mqttport = int(self.getenv("pvmqttport"))
        if os.getenv("pvmqttauth") != None:
            self.mqttauth = self.getenv("pvmqttauth") == "True"
        if os.getenv("pvmqttuser") != None:
            self.mqttuser = self.getenv("pvmqttuser")
        if os.getenv("pvmqttpasswd") != None:
            self.mqttpasswd = self.getenv("pvmqttpasswd")
        if os.getenv("pvmqtttopic") != None:
            self.mqtttopic = self.getenv("pvmqtttopic")

