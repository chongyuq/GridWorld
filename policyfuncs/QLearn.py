from utils.builtin import *
from core.agent import Agent
from policyfuncs.RL import RLLearning


def QLearn_policies(agent: Agent, world_idx, world_state, episodes=1000, exploring_start=True, reset=True,
                    distribution=False):
    """

    :param agent:
    :param world_idx:
    :param world_state:
    :param episodes:
    :param exploring_start:
    :param reset:
    :param distribution:
    :return:
    """
    policies = []
    RL_learner = RLLearning(agent=agent, epsilon=0.1, threshold=0.2, alpha=0.5, gamma=0.999)
    for i, j in enumerate(world_state):
        if j == 0:
            reward_tuple = (i // 15, i % 15)
            agent.set_reward_state(reward_tuple)
            RL_learner.learn(episodes=episodes, exploring_start=exploring_start, reset=reset)
            if distribution:
                policy = list(agent.yield_policy())
            else:
                policy = list(np.array(list(agent.yield_policy())).argmax(axis=-1))
            policies.append([world_idx, i, policy])
    return policies
