from pathlib import Path

from ..model import ConfigJson


class RepoConfig(ConfigJson):
    def __init__(self, root_folder: Path):...
    def _check_config(self):...
    def _set_log_dir(self, root_folder: Path):...
