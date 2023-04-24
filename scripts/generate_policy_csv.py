from utils.builtin import *
# from envs.envs import *
from envs.BeatrizMazes import *
from policyfuncs.SR import SR_policies
from policyfuncs.QLearn import QLearn_policies
from plot.agent import plot_agent
from core.agent import Agent


def main():
    params = myDict(
        data_path='../../data/policies',
        world='maze_world_6'
    )
    # define world
    # world = eval(f'{params.world}()')[0]
    world = Maze95().make_world()
    world_state = [int(i.blocked) for i in world.states]

    # find policies
    agent = Agent(world=world)
    # policies = SR_policies(agent=agent, world_state=world_state, world_idx=params.world)
    policies = QLearn_policies(agent=agent, world_state=world_state, world_idx=params.world, episodes=2000,
                               distribution=True)

    # plot policies to check
    plot_agent(agent=agent, stretch=0.7)
    plt.show()

    # output csv file
    df_sr = pd.DataFrame(policies, columns=['world_idx', 'reward_idx', 'SR_policies'])
    df_sr.to_csv(f'{params.data_path}/{params.world}_SR_policies.csv')
    return


if __name__ == "__main__":
    main()
