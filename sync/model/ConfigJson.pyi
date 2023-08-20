from pathlib import Path
from typing import (
    List,
    Dict,
    Any,
    Optional,
    overload,
    Self,
    Union
)

from .JsonIO import JsonIO

T = Dict[str, Any]

class ConfigJson(JsonIO):
    _config: T

    CONFIG_VERSION: int
    TRACK_VERSION: int

    @overload
    def __init__(
        self,
        *,
        name: str,
        base_url: str,
        max_num: int,
        enable_log: bool,
        log_dir: Optional[Path]): ...
    @overload
    def __init__(self, config: T): ...
    @overload
    def __init__(self, *args, **kwargs): ...
    @property
    def name(self) -> str: ...
    @property
    def base_url(self) -> str: ...
    @property
    def max_num(self) -> int: ...
    @property
    def enable_log(self) -> bool: ...
    @property
    def log_dir(self) -> Optional[Path]: ...
    @property
    def config_version(self) -> int: ...
    @property
    def track_version(self) -> int: ...
    def _set_property(self, key: str): ...
    def _set_properties(self): ...
    def write(self: Union[Self, Dict], file: Path): ...
    @classmethod
    def default(cls) -> ConfigJson: ...
    @classmethod
    def filename(cls) -> str: ...
    @classmethod
    def expected_fields(cls) -> List[str]: ...