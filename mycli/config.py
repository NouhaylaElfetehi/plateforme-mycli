import json 

class Config:
    @staticmethod
    def load_config():
        with open('mycli/config.json', 'r') as f:
            return json.load(f)
