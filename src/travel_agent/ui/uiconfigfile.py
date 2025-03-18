import configparser
import os

class UIConfig:
    def __init__(self, config_path="uiconfigurable.ini"):
        self.config_path = config_path
        self.config = configparser.ConfigParser()
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_path):
            self.config.read(self.config_path)
        else:
            raise FileNotFoundError(f"Config file '{self.config_path}' not found.")

    def get(self, section, key, fallback=None):
        return self.config.get(section, key, fallback=fallback)

    def get_boolean(self, section, key, fallback=False):
        return self.config.getboolean(section, key, fallback=fallback)

    def get_int(self, section, key, fallback=0):
        return self.config.getint(section, key, fallback=fallback)

    def get_float(self, section, key, fallback=0.0):
        return self.config.getfloat(section, key, fallback=fallback)

# Example usage
if __name__ == "__main__":
    ui_config = UIConfig()
    app_title = ui_config.get("General", "app_title", "AI Travel Agent")
    max_flight_results = ui_config.get_int("Flights", "max_flight_results", 5)

    print(f"App Title: {app_title}")
    print(f"Max Flight Results: {max_flight_results}")