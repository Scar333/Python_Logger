from datetime import datetime
import logging
import os


class CustomLogger:

    def __init__(self, path_to_folder: str = None) -> None:
        self.name_folder = 'Log'
        if path_to_folder:
            self.path_to_folder = os.path.join(path_to_folder, self.name_folder)
            self._check_folder_for_log_file()
            self.file_path = os.path.join(self.path_to_folder, f'{datetime.now().strftime("%Y.%m.%d")}.log')
        else:
            self.path_to_folder = os.path.join(os.getcwd(), self.name_folder)
            self._check_folder_for_log_file()
            self.file_path = os.path.join(self.path_to_folder, f'{datetime.now().strftime("%Y.%m.%d")}.log')

        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.DEBUG)

        self.file_formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - [%(filename)s] - %(funcName)s: (%(lineno)d) - %(message)s')
        self.console_formatter = logging.Formatter('[%(asctime)s] - %(message)s')

        self.file_handler = logging.FileHandler(self.file_path, encoding='UTF-8')
        self.file_handler.setLevel(logging.DEBUG)
        self.file_handler.setFormatter(self.file_formatter)

        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(logging.DEBUG)
        self.console_handler.setFormatter(self.console_formatter)

        self.log.addHandler(self.file_handler)
        self.log.addHandler(self.console_handler)

    def _check_folder_for_log_file(self) -> None:
        if not os.path.exists(self.path_to_folder):
            os.mkdir(self.path_to_folder)

    def start_initialization(self):
        return self.log


log = CustomLogger().start_initialization()
