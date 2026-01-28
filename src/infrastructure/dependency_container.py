class DependencyContainer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._dependencies = {}
        return cls._instance

    def set(self, name: str, dependency):
        self._dependencies[name] = dependency

    def get(self, name: str):
        if name not in self._dependencies:
            raise ValueError(f"Dependency '{name}' not found")
        return self._dependencies[name]

    def clear(self):
        self._dependencies.clear()


container = DependencyContainer()
