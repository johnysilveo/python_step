class ConsolManager:
    _instance = None

    def __init__(self):
        if ConsolManager._instance is not None:
            raise Exception("Only one insatnce of class")
        else:
            ConsolManager._instance = self

    @staticmethod
    def get_instance():
        if ConsolManager._instance is None:
            ConsolManager()
        return ConsolManager._instance

    def log(self,msg):
        print(f'log entry: {msg}')

log_manager = ConsolManager.get_instance()
log_manager.log('Singleton pattern is returned')

