import os

class FS:

    def __init__(self):
        self._file_manager = {}

    def list_files(self, path):
        try:
            return os.listdir(path)
        except Exception as e:
            print('ERROR!!! ', e)
            return None

    def open_file(self, path):
        try:
            if path not in self._filem_anager:
                _file = open(path, 'r')
                self._filem_anager[path] = _file
            return True
        except Exception as e:
            print('ERROR!!! ', e)
            return False

    def close_file(self, path):
        try:
            if path in self._filem_anager:
                self._filem_anager[path].close()
                del self._filem_anager[path]
            return True
        except Exception as e:
            print('ERROR!!! ', e)
            return False

    def read_file(self, path):
        try:
            if self.open_file(path):
                if path in self._filem_anager:
                    data = self._filem_anager[path].read()
                self.close_file(path)
            return data
        except Exception as e:
            print('ERROR!!! ', e)
            return None