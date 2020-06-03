from DataObjects.ClassLevel import Level


class SystemDescriptor:

    def __init__(self, system_name):
        self.system_name = system_name
        self.levels = []

    def add_level(self, level: Level):
        assert level not in self.levels, "Level was already added"
        self.levels.append(level)
