from utils.builtin import *


@dataclass
class Block:
    x: int
    y: int
    blocked_states: np.array
    category: Optional = None
    rotation: Optional = None
    shift: Optional = None # let this be equal to the location of the block
    features: Optional = None

    @property
    def key_states(self):
        min_x, min_y, max_x, max_y = min(self.blocked_states[:, 0]), min(self.blocked_states[:, 1]), max(
            self.blocked_states[:, 0]), max(self.blocked_states[:, 1]),
        s = set([(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)])
        s = [list(a) for a in s]
        k = np.array([i for i in self.blocked_states.tolist() if i in s])
        return k


class ManipulateBlock:
    def __init__(self, block: Block):
        self.block = copy.copy(block)
        self.original_block = block.blocked_states  # shape: tot_states x 2
        self.manipulated_block = block.blocked_states  # same as the block to start with and then gets changed

    def reset(self):
        self.manipulated_block = self.original_block
        return

    def rotate_block(self, angle):  # always rotate first, in gridworld, angle can only be pi/2, pi, 3pi/2
        rotation_matrix = np.array([[cos(angle), -sin(angle)], [sin(angle), cos(angle)]])
        blocked_states = np.transpose(rotation_matrix @ np.transpose(self.original_block))
        shift = np.array([min(blocked_states[:, 0]), min(blocked_states[:, 1])])
        self.manipulated_block = np.rint(blocked_states - shift).astype(int)  # converting to integer

        self.block.blocked_states, self.block.rotation = self.manipulated_block, angle
        return self.block

    def shift_block(self, shift: np.array) -> Block:  # shift.shape: 2
        blocked_states = self.manipulated_block + shift
        self.manipulated_block = np.rint(blocked_states).astype(int)

        self.block.blocked_states, self.block.shift = self.manipulated_block, shift
        return self.block


class CreateBlock:
    def __init__(self):
        self._block = set()  # set of tuples
        self.category = None

    @property
    def reset(self):
        self._block = set()

    def build_wall(self, shape, offset=[0, 0], category_label=False):
        wall = list(product(range(offset[0], offset[0] + shape[0]), range(offset[1], offset[1] + shape[1])))
        self._block = self._block.union(wall)
        if category_label:
            self.category = 'wall'
        return self.block

    def build_corner(self, shape, category_label=False):  # always return as an L. Can be manipulated
        self.build_wall([1, shape[1]])
        self.build_wall([shape[0], 1])
        if category_label:
            self.category = 'corner'
        return self.block

    def build_room(self, shape, category_label=True):  # always return with the gap at the top. It's a 3 walled thing
        self.build_corner(shape)
        self.build_wall([1, shape[1]], offset=[shape[0] - 1, 0])
        if category_label:
            self.category = 'room'
        return self.block

    @property
    def block(self):
        if self._block:
            blocked_states = np.array(sorted(self._block))
            x, y = max(blocked_states[:, 0]) + 1, max(blocked_states[:, 1]) + 1
            return Block(x, y, blocked_states, self.category)
        return None