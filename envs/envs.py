from utils.builtin import *
from core.worldbuilder import *
from core.block import *


def create_border(wx, wy):
    blocks = []
    blocks.append(ManipulateBlock(CreateBlock().build_room([wx, wy])).shift_block([0, 0]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([wx-2, 1])).shift_block([1, wy-1]))
    return blocks


def random_world(border=True, seed=None):
    wx, wy = 15, 15
    if seed is not None:
        random.seed(seed)
    n_s = wx * wy
    blocks = []
    blocks.append(CreateBlock().build_wall([1, 5]))
    blocks.append(CreateBlock().build_corner([5, 5]))
    blocks.append(CreateBlock().build_corner([5, 5]))
    world = RandomWorldBuilder([wx, wy], blocks=blocks)
    world.random_world_generate(border=border)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def random_world_2(border=True, seed=None):
    wx, wy = 15, 15
    if seed is not None:
        random.seed(seed)
    n_s = wx * wy
    blocks_to_chose = [CreateBlock().build_wall([1, 1]), CreateBlock().build_wall([1, 2]),
                       CreateBlock().build_wall([1, 3]), CreateBlock().build_wall([1, 4]),
                       CreateBlock().build_wall([1, 5]), CreateBlock().build_wall([1, 6]),
                       CreateBlock().build_wall([1, 7]), CreateBlock().build_wall([1, 8]),
                       CreateBlock().build_corner([2, 3]), CreateBlock().build_corner([2, 4]),
                       CreateBlock().build_corner([2, 5]), CreateBlock().build_corner([2, 6]),
                       CreateBlock().build_corner([2, 7]), CreateBlock().build_corner([2, 8]),
                       CreateBlock().build_corner([3, 3]), CreateBlock().build_corner([3, 4]),
                       CreateBlock().build_corner([3, 4]), CreateBlock().build_corner([3, 5]),
                       CreateBlock().build_corner([3, 6]), CreateBlock().build_corner([3, 7]),
                       CreateBlock().build_corner([4, 4]), CreateBlock().build_corner([4, 5]),
                       CreateBlock().build_corner([4, 6]), CreateBlock().build_corner([5, 5])]
    tot_blocks = random.randint(1, 10)
    blocks = random.choices(blocks_to_chose, weights=None, k=tot_blocks)
    world = RandomWorldBuilder([wx, wy], blocks=blocks)
    world.random_world_generate(border=border)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def random_world_4(border=True, seed=None):
    wx, wy = 15, 15
    if seed is not None:
        random.seed(seed)
    n_s = wx * wy
    blocks_to_chose = [
                           CreateBlock().build_wall([1, 5]), CreateBlock().build_wall([1, 6]),
                           CreateBlock().build_wall([1, 7]), CreateBlock().build_wall([1, 8]),
                           CreateBlock().build_wall([5, 1]), CreateBlock().build_wall([6, 1]),
                           CreateBlock().build_wall([7, 1]), CreateBlock().build_wall([8, 1]),
                       ]
    blocks = random.choices(blocks_to_chose, weights=None, k=2)
    world = RandomWorldBuilder2([wx, wy], blocks=blocks)
    world.random_world_generate(border=border)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def random_world_3(border=True, seed=None):
    wx, wy = random.randint(15, 30), random.randint(15, 30)
    if seed is not None:
        random.seed(seed)
    n_s = wx * wy
    tot_blocks = random.randint(3, 20)
    blocks = []
    for i in tot_blocks:
        b = random.choice([0,1])
        if b == 0:
            blocks.append(CreateBlock().build_wall([random.randint(1, 3), random.randint(1, 10)]))
        if b == 0:
            blocks.append(CreateBlock().build_wall([random.randint(1, 3), random.randint(1, 10)]))
    world = RandomWorldBuilder([wx, wy], blocks=blocks)
    world.random_world_generate(border=border)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def tiago_world():
    wx, wy = 7, 7
    n_s = wx * wy
    blocks = []
    blocks.append(ManipulateBlock(CreateBlock().build_wall([5, 1])).shift_block([1, 3]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def hallway_world():
    wx, wy = 11, 11
    n_s = wx * wy
    blocks = []
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([0, 5]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([2, 5]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([5, 0]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 5])).shift_block([5, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 3])).shift_block([5, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([6, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([9, 4]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def hallway_world2():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx,wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([1, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([6, 1])).shift_block([4, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([11, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 3])).shift_block([7, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([7, 5]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 3])).shift_block([6, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([6, 12]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def hallway_world2_r():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx,wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([12, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([6, 1])).shift_block([5, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([1, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 3])).shift_block([7, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([7, 5]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 3])).shift_block([8, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([8, 12]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def hallway_world2_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx,wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([7, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 6])).shift_block([7, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 3])).shift_block([7, 11]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([1, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([5, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([8, 6]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([12, 6]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def hallway_world2_v_r():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx,wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([7, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 6])).shift_block([7, 5]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 3])).shift_block([7, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([1, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([5, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([8, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([12, 8]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def hallway_world_symmetric():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx,wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([1, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([7, 1])).shift_block([4, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([12, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([7, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 7])).shift_block([7, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([7, 12]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def maze_world_1():
    wx, wy = 5, 5
    n_s = wx * wy
    blocks = []
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([1, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 3])).shift_block([3, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([0, 3]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def maze_world_2():
    wx, wy = 9, 9
    n_s = wx * wy
    blocks = []
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([1, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([3, 0]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([5, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([5, 0]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([1, 5]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([5, 5]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([5, 1])).shift_block([1, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([5, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 3])).shift_block([7, 6]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([8, 1])).shift_block([0, 3]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def maze_world_3():
    wx, wy = 9, 9
    n_s = wx * wy
    blocks = []
    blocks.append(ManipulateBlock(CreateBlock().build_room([9, 9])).shift_block([0, 0]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([7, 1])).shift_block([1, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([2, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([3, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([5, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([5, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([2, 6]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([5, 6]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([6, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([6, 1])).shift_block([1, 4]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def maze_world_4():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = []
    blocks.append(ManipulateBlock(CreateBlock().build_room([15, 15])).shift_block([0, 0]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([13, 1])).shift_block([1, 14]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([4, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([6, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([10, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([2, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([6, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([12, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([8, 1])).shift_block([1, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 5])).shift_block([10, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_corner([1, 3])).shift_block([12, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_corner([1, 1])).shift_block([13, 6]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([2, 6]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([6, 6]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([5, 1])).shift_block([2, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 4])).shift_block([8, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([12, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([6, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([8, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([4, 1])).shift_block([1, 10]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([6, 10]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([4, 1])).shift_block([10, 10]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([10, 11]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([2, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([6, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([8, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([10, 12]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def corner_room():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_corner([8, 8])).shift_block([4, 4]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def corner_room_r():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    corner = ManipulateBlock(CreateBlock().build_corner([8, 8])).rotate_block(np.pi)
    # note has been changed since basic_model_9 8/11/2022
    # world stored in worlds_new_2.csv and policies in sr_policies_new_2.csv
    blocks.append(ManipulateBlock(corner).shift_block([3, 3]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def corner_room_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    corner = ManipulateBlock(CreateBlock().build_corner([8, 8])).rotate_block(np.pi/2)
    # note has been changed since basic_model_9 8/11/2022
    blocks.append(ManipulateBlock(corner).shift_block([3,4]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def corner_room_r_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    corner = ManipulateBlock(CreateBlock().build_corner([8, 8])).rotate_block(3 * np.pi/2)
    # note has been changed since basic_model_9 8/11/2022
    blocks.append(ManipulateBlock(corner).shift_block([4, 3]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def wall_room():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([9, 2])).shift_block([3, 7]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def wall_room_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 9])).shift_block([7, 3]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def wall_room2():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([9, 1])).shift_block([3, 7]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def wall_room2_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 9])).shift_block([7, 3]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def linear_room():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([11, 1])).shift_block([1, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([11, 1])).shift_block([3, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([11, 1])).shift_block([1, 10]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def linear_room_r():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([11, 1])).shift_block([3, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([11, 1])).shift_block([1, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([11, 1])).shift_block([3, 10]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def linear_room_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 11])).shift_block([4, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 11])).shift_block([7, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 11])).shift_block([10, 1]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def linear_room_r_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 11])).shift_block([4, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 11])).shift_block([7, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 11])).shift_block([10, 3]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def line_room():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([9, 1])).shift_block([3, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([9, 1])).shift_block([3, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([9, 1])).shift_block([3, 10]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def line_room_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 9])).shift_block([4, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 9])).shift_block([7, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 9])).shift_block([10, 3]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def room_room():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_room([9, 9])).shift_block([3, 3]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def room_room_r():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    room = ManipulateBlock(CreateBlock().build_room([9, 9])).rotate_block(np.pi)
    blocks.append(ManipulateBlock(room).shift_block([3, 3]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def room_room_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    room = ManipulateBlock(CreateBlock().build_room([9, 9])).rotate_block(np.pi/2)
    blocks.append(ManipulateBlock(room).shift_block([3, 3]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def room_room_r_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    room = ManipulateBlock(CreateBlock().build_room([9, 9])).rotate_block(3*np.pi/2)
    blocks.append(ManipulateBlock(room).shift_block([3, 3]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def room_room2():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_room([9, 9])).shift_block([3, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_room([3, 1])).shift_block([4, 11]))
    blocks.append(ManipulateBlock(CreateBlock().build_room([3, 1])).shift_block([8, 11]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def room_room2_r():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    room = ManipulateBlock(CreateBlock().build_room([9, 9])).rotate_block(np.pi)
    blocks.append(ManipulateBlock(room).shift_block([3, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_room([3, 1])).shift_block([4, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_room([3, 1])).shift_block([8, 3]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def room_room2_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    room = ManipulateBlock(CreateBlock().build_room([9, 9])).rotate_block(np.pi/2)
    blocks.append(ManipulateBlock(room).shift_block([3, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_room([1, 3])).shift_block([3, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_room([1, 3])).shift_block([3, 8]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def room_room2_r_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    room = ManipulateBlock(CreateBlock().build_room([9, 9])).rotate_block(3*np.pi/2)
    blocks.append(ManipulateBlock(room).shift_block([3, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_room([1, 3])).shift_block([11, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_room([1, 3])).shift_block([11, 8]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def snake_room():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([9, 1])).shift_block([3, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([3, 5]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([9, 1])).shift_block([3, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([11, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([9, 1])).shift_block([3, 10]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def snake_room_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 9])).shift_block([4, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([5, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 9])).shift_block([7, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([8, 11]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 9])).shift_block([10, 3]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def t_maze():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([5, 10])).shift_block([1, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([5, 10])).shift_block([9, 4]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def t_maze_r():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([5, 10])).shift_block([1, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([5, 10])).shift_block([9, 1]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def t_maze_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([10, 5])).shift_block([4, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([10, 5])).shift_block([4, 9]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def t_maze_r_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([10, 5])).shift_block([1, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([10, 5])).shift_block([1, 9]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def cross_room():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([9, 1])).shift_block([3, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 4])).shift_block([7, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 4])).shift_block([7, 8]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def obstacle_room():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([10, 1])).shift_block([1, 7]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def obstacle_room_r():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([10, 1])).shift_block([4, 7]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def obstacle_room_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 10])).shift_block([7, 1]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def obstacle_room_r_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 10])).shift_block([7, 4]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def pretend_corner_room():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 6])).shift_block([4, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([6, 1])).shift_block([6, 10]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def pretend_corner_room_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([6, 1])).shift_block([3, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 6])).shift_block([10, 6]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def i_maze():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([5, 7])).shift_block([1, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([5, 7])).shift_block([9, 4]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def i_maze_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([7, 5])).shift_block([4, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([7, 5])).shift_block([4, 9]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def maze_world_5():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([2, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([6, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([8, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([10, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([4, 1])).shift_block([1, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([6, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 4])).shift_block([8, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([12, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([10, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([6, 1])).shift_block([1, 6]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 4])).shift_block([10, 6]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([12, 6]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([2, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([6, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([12, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([2, 10]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([5, 1])).shift_block([6, 10]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([12, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([2, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([6, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([10, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([12, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([6, 13]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def maze_world_6():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([2, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([6, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([8, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([10, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([4, 1])).shift_block([1, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([6, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 4])).shift_block([8, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([12, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([10, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([6, 1])).shift_block([1, 6]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 4])).shift_block([10, 6]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([12, 6]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([2, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([6, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([12, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([2, 10]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([5, 1])).shift_block([6, 10]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([12, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([2, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([6, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([10, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([12, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([6, 13]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([9, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([4, 13]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def maze_world_7():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([2, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([6, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([8, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([10, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([4, 1])).shift_block([1, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([6, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 4])).shift_block([8, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([12, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([10, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([6, 1])).shift_block([1, 6]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 4])).shift_block([10, 6]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([12, 6]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([2, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([6, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([12, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([2, 10]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([5, 1])).shift_block([6, 10]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([12, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([2, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([6, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([10, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([12, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([6, 13]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([8, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 1])).shift_block([4, 13]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def corridor_room():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 3])).shift_block([5, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 3])).shift_block([9, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 5])).shift_block([5, 5]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 5])).shift_block([9, 5]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 3])).shift_block([5, 11]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 3])).shift_block([9, 11]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([4, 1])).shift_block([1, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([4, 1])).shift_block([10, 7]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def corridor_room_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([1, 5]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([1, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([5, 1])).shift_block([5, 5]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([5, 1])).shift_block([5, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([11, 5]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 1])).shift_block([11, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 4])).shift_block([7, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 4])).shift_block([7, 10]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def spiral_room():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([12, 1])).shift_block([1, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 10])).shift_block([12, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([10, 1])).shift_block([2, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 8])).shift_block([2, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([8, 1])).shift_block([3, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 6])).shift_block([10, 5]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([6, 1])).shift_block([4, 10]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 4])).shift_block([4, 6]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([4, 1])).shift_block([5, 6]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def spiral_room_r():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 12])).shift_block([12, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([10, 1])).shift_block([2, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 10])).shift_block([2, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([8, 1])).shift_block([3, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 8])).shift_block([10, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([6, 1])).shift_block([4, 10]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 6])).shift_block([4, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([4, 1])).shift_block([5, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 4])).shift_block([8, 5]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def spiral_room_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([12, 1])).shift_block([2, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 10])).shift_block([2, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([10, 1])).shift_block([3, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 8])).shift_block([12, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([8, 1])).shift_block([4, 10]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 6])).shift_block([4, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([6, 1])).shift_block([5, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 4])).shift_block([10, 5]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([4, 1])).shift_block([6, 8]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def spiral_room_v_r():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 12])).shift_block([2, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([10, 1])).shift_block([3, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 10])).shift_block([12, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([8, 1])).shift_block([4, 12]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 8])).shift_block([4, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([6, 1])).shift_block([5, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 6])).shift_block([10, 5]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([4, 1])).shift_block([6, 10]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 4])).shift_block([6, 6]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def complex_t_maze():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([4, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([9, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([4, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([9, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([1, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([3, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 3])).shift_block([4, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([6, 3])).shift_block([8, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([9, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 4])).shift_block([11, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 3])).shift_block([11, 11]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([1, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([3, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 6])).shift_block([8, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([7, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([4, 3])).shift_block([7, 11]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def complex_t_maze():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([4, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([9, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([4, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([9, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([1, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([3, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 3])).shift_block([4, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([6, 3])).shift_block([8, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([9, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 4])).shift_block([11, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 3])).shift_block([11, 11]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([1, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([3, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 6])).shift_block([4, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([7, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([4, 3])).shift_block([7, 11]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def complex_t_maze_r():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([13, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([13, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([11, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([11, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([9, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([9, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 3])).shift_block([8, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 6])).shift_block([8, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([7, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([4, 3])).shift_block([4, 11]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 3])).shift_block([1, 11]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([4, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([4, 3]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([6, 3])).shift_block([1, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([4, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 4])).shift_block([1, 7]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def complex_t_maze_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([9, 13]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([4, 13]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([9, 11]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([4, 11]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([13, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([11, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 3])).shift_block([8, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([6, 3])).shift_block([1, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([4, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 4])).shift_block([1, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 3])).shift_block([1, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([13, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([11, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 6])).shift_block([8, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([7, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([4, 3])).shift_block([4, 1]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def complex_t_maze_v_r():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([1, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([1, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([3, 9]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([3, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([4, 13]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([4, 11]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 3])).shift_block([4, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 6])).shift_block([4, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 2])).shift_block([7, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([4, 3])).shift_block([7, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 3])).shift_block([11, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([9, 13]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([9, 11]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([6, 3])).shift_block([8, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([2, 1])).shift_block([9, 7]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([3, 4])).shift_block([11, 4]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def hairpin_room():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([12, 1])).shift_block([1, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([12, 1])).shift_block([1, 6]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([12, 1])).shift_block([1, 10]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([12, 1])).shift_block([2, 4]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([12, 1])).shift_block([2, 8]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([12, 1])).shift_block([2, 12]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def hairpin_room_v():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 12])).shift_block([2, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 12])).shift_block([6, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 12])).shift_block([10, 1]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 12])).shift_block([4, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 12])).shift_block([8, 2]))
    blocks.append(ManipulateBlock(CreateBlock().build_wall([1, 12])).shift_block([12, 2]))
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o


def nothing_room():
    wx, wy = 15, 15
    n_s = wx * wy
    blocks = create_border(wx, wy)
    world = WorldBuilder([wx, wy])
    for b in blocks:
        world.add_block(b)
    n_o = 4 * wx * wy - 2 * wx - 2 * wy + 1
    return world, wx, wy, n_s, n_o