from utils.builtin import *
from core.agent import Agent


def highlight_cell(x, y, ax=None, **kwargs):
    rect = plt.Rectangle((x - .5, y - .52), 1, 1, **kwargs)
    if ax is None:
        ax = plt.gca()
    ax.add_patch(rect)
    return rect


def plot_agent(agent: Agent, stretch=1, ax=None):
    if ax is None:
        ax, fig = plt.gca(), plt.gcf()
    array = np.zeros((agent.ny, agent.nx))
    if agent.state is not None:
        highlight_cell(agent.state.x, agent.state.y, ax=ax, linewidth=3, color='red', fill=None)
    for s in agent.states:
        # array[s.y, s.x] = eval('s.'+attr_name)
        if s.terminal:
            highlight_cell(s.x, s.y, ax=ax, linewidth=3, color='blue', fill=None)
        if s.blocked:
            highlight_cell(s.x, s.y, ax=ax, linewidth=5, color='black', fill=None)
        for a in s.actions:
            ax.arrow(s.x, s.y, a.x * a.policy * stretch, a.y * a.policy * stretch,
                     head_width=0.1, length_includes_head=True, linestyle='--', fill=None)
    a = ax.imshow(array, cmap='coolwarm')
    ax.set_xticks([i for i in range(agent.nx)])
    ax.set_yticks([i for i in range(agent.ny)])
    ax.invert_yaxis()
    fig.colorbar(a)
    return a
