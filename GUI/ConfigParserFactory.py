import configparser


class ConfigParserFactory:
    __config_path = "config.ini"

    @classmethod
    def load_config_parser(cls):
        config = configparser.ConfigParser()
        config.read(cls.__config_path)
        return config
