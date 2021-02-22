
# NOTE(krishan711): waiting for JSON type to be defined in mypy: https://github.com/python/typing/issues/182
# NOTE(krishan711): copied from https://gist.github.com/BMDan/ede923f733dfdf5ed3f6c9634a3e281f
from typing import Any, Dict, List, Mapping, Union
JSON_v = Union[str, int, float, bool, None]
JSON_5 = JSON_v
JSON_4 = Union[JSON_v, List[JSON_5], Mapping[str, JSON_5]]
JSON_3 = Union[JSON_v, List[JSON_4], Mapping[str, JSON_4]]
JSON_2 = Union[JSON_v, List[JSON_3], Mapping[str, JSON_3]]
JSON_1 = Union[JSON_v, List[JSON_2], Mapping[str, JSON_2]]
JSON = Union[JSON_v, List[JSON_1], Mapping[str, JSON_1]]
UnsafeJSON_5 = Union[JSON_v, List[Any], Mapping[str, Any]]  # type: ignore
UnsafeJSON_4 = Union[JSON_v, List[UnsafeJSON_5], Mapping[str, UnsafeJSON_5]]
UnsafeJSON_3 = Union[JSON_v, List[UnsafeJSON_4], Mapping[str, UnsafeJSON_4]]
UnsafeJSON_2 = Union[JSON_v, List[UnsafeJSON_3], Mapping[str, UnsafeJSON_3]]
UnsafeJSON_1 = Union[JSON_v, List[UnsafeJSON_2], Mapping[str, UnsafeJSON_2]]
UnsafeJSON = Union[JSON_v, List[UnsafeJSON_1], Mapping[str, UnsafeJSON_1]]
