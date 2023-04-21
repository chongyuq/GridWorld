from utils.builtin import *


@dataclass
class Action:
    x: int
    y: int
    index: Optional[int] = None
    blocked: bool = False
    representation: Optional = None
    policy: Optional = 0.25
    value: Optional = 0