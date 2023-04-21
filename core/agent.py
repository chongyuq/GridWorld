from utils.builtin import *
from core.worldbuilder import WorldBuilder
from core.state import State


@dataclass
class Agent:
    world: WorldBuilder
    state: Optional[State] = None
    reward_state: Optional[State] = None

    def __post_init__(self):
        self._world_reset()

    def _world_reset(self):
        self.states, self.blocks = self.world.states, self.world.blocks_to_add
        self.initial_state = [s for s in self.states if s.initial]
        self.nx = max([s.x for s in self.states]) + 1
        self.ny = max([s.y for s in self.states]) + 1
        self.state_indices = {(s.x, s.y): s.index for s in self.world.states}
        self.n_s = len(self.states)

    @property
    def blocked_states(self):
        return [s.blocked for s in self.states]

    @property
    def world_state(self):
        return [int(bool(s.blocked)) for s in self.states]

    @property
    def available_states(self):
        return [s for s in self.states if not s.blocked]

    def remove_reward(self):
        for s in self.states:
            s.reward, s.terminal = -1, False
        self.reward_state = None
        return

    def set_reward_state(self, state_xy: tuple):
        index = self.state_indices[state_xy]
        state = self.states[index]
        self.remove_reward()
        state.reward, state.terminal = 1, True # self.world_state[index]
        self.reward_state = state
        return

    def set_state(self, state_xy: tuple):
        index = self.state_indices[state_xy]
        self.state = self.states[index]
        return

    def random_reward_generate(self):
        reward_state = random.choice(self.available_states)
        self.set_reward_state((reward_state.x, reward_state.y))
        return

    def step(self, action: int):  # action is an index
        if self.state.actions[action].blocked or self.state.terminal:
            return
        x = int(self.state.x + self.state.actions[action].x)
        y = int(self.state.y + self.state.actions[action].y)
        if (x, y) not in self.state_indices:
            self.state.actions[action].blocked = True
            return
        index = self.state_indices[(x, y)]
        if self.states[index].blocked:
            self.state.actions[action].blocked = True  # changing self.state should change the values in self.states
            return
        self.state = self.states[index]
        return self.state

    def yield_policy(self):
        for s in self.states:
            yield s.policy

    def yield_value(self):
        for s in self.available_states:
            yield s.value

