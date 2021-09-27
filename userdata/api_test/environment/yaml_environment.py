import yaml
from environment import base_environment


class YamlEnvironment(base_environment.BaseEnvironment):

    def read(self):
        with open(self.filename, 'r') as stream:
            return yaml.safe_load(stream)

    def write(self):
        with open(self.filename, 'w') as stream:
            yaml.dump(self.environment, stream)
