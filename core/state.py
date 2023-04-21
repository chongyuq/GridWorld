from utils.builtin import *
from core.action import Action


@dataclass
class State:
    x: int
    y: int
    index: int = None
    actions: List[Action] = field(
        default_factory=lambda: [Action(x=1, y=0, index=0),
                                 Action(x=0, y=1, index=1),
                                 Action(x=-1, y=0, index=2),
                                 Action(x=0, y=-1, index=3)])
    blocked: bool = False
    reward: Optional = -1
    observation: Optional = None
    stable_policy: Optional = False
    terminal: Optional = False
    initial: Optional = False
    value: Optional = 0

    @property
    def trapped(self):
        if sum([a.blocked for a in self.actions]) == len(self.actions):
            return True
        return False

    @property
    def policy(self):
        return [a.policy for a in self.actions]

    @property
    def q_value(self):
        return [a.value for a in self.actions]

    # @property
    # def value(self):
    #     return sum([a.value * a.policy for a in self.actions])