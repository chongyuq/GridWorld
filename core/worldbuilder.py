from utils.builtin import *
from core.block import Block, ManipulateBlock, CreateBlock
from core.state import State
from functional.successor import *


class WorldBuilder:
    def __init__(self, shape): # , tot_rewards=0, initial=False, reward=False
        self.shape = shape
        self._reset_states()

    def _reset_states(self):
        self.blocks_to_add = []
        self.states = [State(x, y, i) for i, (x, y) in enumerate(product(range(self.shape[0]), range(self.shape[1])))]
        self._block_edges
        self.state_indices = {(s.x, s.y): s.index for s in self.states}
        self.tot_actions = len(self.states[0].actions)
        self.tot_states = len(self.states)
        return

    @property
    def _block_edges(self):
        for s in self.states:
            if s.x == self.shape[0] - 1:
                s.actions[0].blocked = True
            if s.y == self.shape[1] - 1:
                s.actions[1].blocked = True
            if s.x == 0:
                s.actions[2].blocked = True
            if s.y == 0:
                s.actions[3].blocked = True
        return

    def block_state(self, index: int, add=1):
        s = self.states[index]
        self.states[index].blocked += add  # changes self.states too!
        for a in self.states[0].actions:  # assume actions in one state can be taken in all states
            i = s.x + a.x
            j = s.y + a.y
            if (i, j) not in self.state_indices:
                continue
            neighbour_index = self.state_indices[(i, j)]
            # based on how the indices have been designed 0 is opposite of 2, 1 is opposite of 3
            self.states[neighbour_index].actions[(a.index + self.tot_actions // 2) % self.tot_actions].blocked += add
        return

    def add_block(self, block: Block, add=1):
        for x, y in block.blocked_states:
            if (x, y) not in self.state_indices:
                return False
        for x, y in block.blocked_states:
            index = self.state_indices[(x, y)]
            self.block_state(index, add)
        return True

    @property
    def overlap(self):
        for s in self.states:
            if s.blocked > 1:
                return True
        return False

    @property
    def all_states_connected(self):
        not_blocked_indices = [s.index for s in self.states if not s.blocked]
        SR = self.successor_matrix
        SR = SR[not_blocked_indices, :][:, not_blocked_indices]
        if np.all(abs(SR) > 1e-15): # 1e-15
            return True
        return False

    @property
    def adjacency_matrix(self):
        return adjacency_matrix_calculate(self)

    @property
    def successor_matrix(self):
        return successor_matrix_calculate(self.adjacency_matrix)


class RandomWorldBuilder(WorldBuilder):
    def __init__(self, shape, blocks: List[Block], rotation=True):
        super().__init__(shape)
        self.rotation = rotation
        self.blocks = blocks
        self.tot_blocks = len(self.blocks)

    def transform_block(self, b, rotation=0, shift=[0,0]) -> Block: # shift should not be None
        a = ManipulateBlock(self.blocks[b]).rotate_block(rotation)
        return ManipulateBlock(a).shift_block(shift)

    def random_block_transform(self, b):
        if self.rotation:
            rotation = random.randrange(self.tot_actions)
        else:
            rotation = 0
        shift = [random.randrange(self.shape[0] - self.blocks[b].x),\
                 random.randrange(self.shape[1] - self.blocks[b].y)]
        a = self.transform_block(b, rotation=rotation * pi / 2, shift=shift)
        return a

    def random_world_generate(self, border=True):
        self._reset_states()
        if border:
            self.add_block(CreateBlock().build_room(self.shape))
            self.add_block(ManipulateBlock(CreateBlock().build_wall([self.shape[0] - 2, 1])).shift_block([1, self.shape[1] - 1]))
        for b in range(self.tot_blocks):
            block_added = False
            tries = 0
            while not block_added:
                tries += 1
                if tries > 5:
                    return self.random_world_generate()
                new_block = self.random_block_transform(b)
                self.add_block(new_block, add=1)
                if self.overlap or not self.all_states_connected:
                    self.add_block(new_block, add=-1)
                    continue
                block_added = True
                self.blocks_to_add.append(new_block)
        return self.states, self.blocks_to_add


class RandomWorldBuilder2(RandomWorldBuilder):
    def __init__(self, shape, blocks: List[Block], rotation=True):
        super().__init__(shape, blocks, rotation)

    def random_block_transform(self, b):
        if self.rotation:
            rotation = random.uniform(0, 1)
            # rotation = random.randrange(self.tot_actions)
        else:
            rotation = 0
        shift = [
            1 + random.randrange(self.shape[0]-2 - self.blocks[b].x),
            1 + random.randrange(self.shape[1]-2 - self.blocks[b].y)
        ]
        # this is to take into account that you dont want walls to be placed where the border walls are
        a = self.transform_block(b, rotation=rotation * 2 * pi, shift=shift)
        return a

    def random_world_generate(self, border=True):
        self._reset_states()
        if border:
            self.add_block(CreateBlock().build_room(self.shape))
            self.add_block(ManipulateBlock(CreateBlock().build_wall([self.shape[0] - 2, 1])).shift_block([1, self.shape[1] - 1]))
        for b in range(self.tot_blocks):
            block_added = False
            tries = 0
            while not block_added:
                tries += 1
                if tries > 5:
                    return self.random_world_generate()
                new_block = self.random_block_transform(b)
                self.add_block(new_block, add=1)
                if not self.all_states_connected:
                    self.add_block(new_block, add=-1)
                    continue
                block_added = True
                self.blocks_to_add.append(new_block)
        return self.states, self.blocks_to_add