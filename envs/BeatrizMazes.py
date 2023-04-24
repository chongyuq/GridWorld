from utils.builtin import *
from core.worldbuilder import *
from core.block import *
from envs.envs import create_border
from itertools import product


class Maze48:
    def __init__(self):
        self.world = None
        self.wx, self.wy = 15, 15
        self.n_s = self.wx * self.wy
        self.blocks = create_border(self.wx, self.wy)

        # blocks that will always be in place
        self.block_pos = list(product(range(2, 14, 2), range(2, 14, 2)))
        links = [[1, 4], [1, 6], [3, 2], [3, 4], [3, 8], [3, 10], [3, 12], [4, 13], [5, 2], [5, 6], [5, 10], [6, 3],
                 [6, 9], [6, 13], [7, 4], [7, 8], [7, 12], [8, 1], [8, 7], [9, 6], [9, 10], [10, 3], [10, 9],
                 [10, 11], [11, 2], [12, 9], [13, 4], [13, 6], [13, 8], [13, 12]]
        self.block_pos.extend(links)

    def make_world(self):
        blocks_to_add = list(map(lambda i: ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block(list(i)),
                             self.block_pos))
        self.blocks.extend(blocks_to_add)
        self.world = WorldBuilder([self.wx, self.wy])
        for b in self.blocks:
            self.world.add_block(b)
        return self.world


class Maze49(Maze48):
    def __init__(self):
        super().__init__()
        self.block_pos.append([10, 13])


class Maze50(Maze49):
    def __init__(self):
        super().__init__()
        self.block_pos.append([9, 4])


class Maze51(Maze50):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([10, 11])


class Maze52(Maze51):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([7, 4])


class Maze53(Maze52):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([5, 10])


class Maze54(Maze53):
    def __init__(self):
        super().__init__()
        self.block_pos.append([6, 1])


class Maze55(Maze54):
    def __init__(self):
        super().__init__()
        self.block_pos.append([10, 7])


class Maze56(Maze55):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([5, 2])


class Maze57(Maze56):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([9, 6])


class Maze58(Maze57):
    def __init__(self):
        super().__init__()
        self.block_pos.append([7, 10])


class Maze59(Maze58):
    def __init__(self):
        super().__init__()
        self.block_pos.append([6, 5])


class Maze60(Maze59):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([6, 9])


class Maze61(Maze60):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([6, 3])


class Maze62(Maze61):
    def __init__(self):
        super().__init__()
        self.block_pos.append([3, 6])


class Maze63(Maze62):
    """ note this is the same as maze_world_6 from envs, all walls are single units so they can be removed"""
    def __init__(self):
        super().__init__()
        self.block_pos.append([8, 5])


class Maze64(Maze63):
    def __init__(self):
        super().__init__()
        self.block_pos.append([5, 10])


class Maze65(Maze64):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([9, 4])


class Maze66(Maze65):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([1, 6])


class Maze67(Maze66):
    def __init__(self):
        super().__init__()
        self.block_pos.append([7, 4])


class Maze68(Maze67):
    def __init__(self):
        super().__init__()
        self.block_pos.append([11, 4])


class Maze69(Maze68):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([9, 10])


class Maze70(Maze69):
    def __init__(self):
        super().__init__()
        self.block_pos.append([1, 10])


class Maze71(Maze70):
    def __init__(self):
        super().__init__()
        self.block_pos.append([10, 11])


class Maze72(Maze71):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([3, 10])


class Maze73(Maze72):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([10, 9])


class Maze74(Maze73):
    def __init__(self):
        super().__init__()
        self.block_pos.append([4, 3])


class Maze75(Maze74):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([10, 3])


class Maze76(Maze75):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([1, 4])


class Maze77(Maze76):
    def __init__(self):
        super().__init__()
        self.block_pos.append([9, 2])


class Maze78(Maze77):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([5, 6])


class Maze79(Maze78):
    def __init__(self):
        super().__init__()
        self.block_pos.append([10, 5])


class Maze80(Maze79):
    def __init__(self):
        super().__init__()
        self.block_pos.append([5, 8])


class Maze81(Maze80):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([11, 4])


class Maze82(Maze81):
    def __init__(self):
        super().__init__()
        self.block_pos.append([3, 10])


class Maze83(Maze82):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([8, 7])


class Maze84(Maze83):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([1, 10])


class Maze85(Maze84):
    def __init__(self):
        super().__init__()
        self.block_pos.append([8, 9])


class Maze86(Maze85):
    def __init__(self):
        super().__init__()
        self.block_pos.append([1, 4])


class Maze87(Maze86):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([7, 8])


class Maze88(Maze87):
    def __init__(self):
        super().__init__()
        self.block_pos.append([1, 8])


class Maze89(Maze88):
    def __init__(self):
        super().__init__()
        self.block_pos.append([9, 8])


class Maze90(Maze89):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([5, 10])


class Maze91(Maze90):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([10, 7])


class Maze92(Maze91):
    def __init__(self):
        super().__init__()
        self.block_pos.append([5, 6])


class Maze93(Maze92):
    def __init__(self):
        super().__init__()
        self.block_pos.append([9, 6])


class Maze94(Maze93):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([3, 8])


class Maze95(Maze94):
    def __init__(self):
        super().__init__()
        self.block_pos.remove([7, 4])



# class Maze63:
#     def __init__(self):
#         """ note this is the same as maze_world_6 from envs, all walls are single units so they can be removed"""
#         self.world = None
#         self.wx, self.wy = 15, 15
#         self.n_s = self.wx * self.wy
#         self.blocks = create_border(self.wx, self.wy)
#
#         # blocks that will always be in place
#         self.block_pos = list(product(range(2, 14, 2), range(2, 14, 2)))
#         links = [[1, 4], [1, 6], [3, 2], [3, 4], [3, 6], [3, 8], [3, 10], [3, 12], [4, 13], [5, 6], [6, 1],
#                  [6, 5], [6, 13], [7, 8], [7, 10], [7, 12], [8, 1], [8, 5], [8, 7], [9, 4], [9, 10], [10, 3], [10, 7],
#                  [10, 9], [10, 13], [11, 2], [12, 9], [13, 4], [13, 6], [13, 8], [13, 12]]
#         self.block_pos.extend(links)
#
#     def make_world(self):
#         blocks_to_add = list(map(lambda i: ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block(list(i)),
#                              self.block_pos))
#         self.blocks.extend(blocks_to_add)
#         self.world = WorldBuilder([self.wx, self.wy])
#         for b in self.blocks:
#             self.world.add_block(b)
#         return self.world