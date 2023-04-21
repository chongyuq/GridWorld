from utils.builtin import *
from core.worldbuilder import WorldBuilder
from core.agent import Agent
from policyfuncs.RL import RLLearning


def SR_policies(agent: Agent, world_state: list, world_idx: int):
    """

    :param agent:
    :param world_state:
    :param world_idx:
    :return:
    """
    policies = []
    RL_learner = RLLearning(agent=agent, epsilon=0, threshold=0, alpha=1e-5, gamma=0.995)
    for i, j in enumerate(world_state):
        if j == 0:
            reward_tuple = (i // 15, i % 15)
            agent.set_reward_state(reward_tuple)
            RL_learner.update_sr_value_policy()
            policy = list(np.array(list(agent.yield_policy())).argmax(axis=-1))
            policies.append([world_idx, i, policy])
    return policies
