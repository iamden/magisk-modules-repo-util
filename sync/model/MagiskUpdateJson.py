import re
from pathlib import Path

from .AttrDict import AttrDict
from .JsonIO import JsonIO
from ..utils import HttpUtils, StrUtils


class MagiskUpdateJson(AttrDict):
    @property
    def version_display(self):
        return StrUtils.get_version_display(self.version, self.versionCode)

    @property
    def zipfile_name(self):
        filename = self.version_display.replace(" ", "_")
        filename = re.sub(r"[^a-zA-Z0-9\-._]", "", filename)
        return f"{filename}.zip"

    @classmethod
    def load(cls, path):
        if isinstance(path, str):
            obj = HttpUtils.load_json(path)
        elif isinstance(path, Path):
            obj = JsonIO.load(path)
        else:
            raise ValueError(f"unsupported type {type(path).__name__}")

        return MagiskUpdateJson(obj)
