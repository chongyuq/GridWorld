from utils.builtin import *


def adjacency_matrix_calculate(world):
    """

    :param world:
    :return:
    """
    adjacency_matrix = np.zeros((world.tot_states, world.tot_states))
    for s in world.states:
        if not s.blocked:
            for a in s.actions:
                if not a.blocked:
                    x1, y1 = s.x + a.x, s.y + a.y
                    i = world.state_indices[(x1, y1)]
                    adjacency_matrix[s.index, i] = 1
    return adjacency_matrix


def successor_matrix_calculate(adjacency_matrix: np.array, gamma=0.995):
    probs = np.divide(adjacency_matrix.transpose(), adjacency_matrix.sum(axis=1),
                      out=np.zeros_like(adjacency_matrix.transpose()),
                      where=adjacency_matrix.sum(axis=1) != 0)
    successor_matrix = np.linalg.inv(np.eye(probs.shape[0]) - gamma * probs)
    return successor_matrix

