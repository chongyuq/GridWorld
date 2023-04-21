from utils.builtin import *


class RLLearning:
    def __init__(self, agent, epsilon, threshold, alpha, gamma):
        self.agent = agent
        self.epsilon = epsilon
        self.threshold = threshold
        self.alpha = alpha
        self.gamma = gamma
        # self.original_state = copy.deepcopy(self.agent.states)
        self._reset()

    def _reset(self):
        # self.agent.states = copy.deepcopy(self.original_state)
        for s in self.agent.states:
            for a in s.actions:
                a.value = 0
                a.policy = 0.25
        self.tot_a = len(self.agent.states[0].actions)
        return

    def update_policy(self, s_index: int):
        s = self.agent.states[s_index]
        v_max = max(s.q_value)
        old_policy = s.policy
        n = len(s.actions)
        p_unnorm = []
        for q in s.q_value:
            if q >= (v_max - self.threshold):
                p_unnorm.append(1)
            else:
                p_unnorm.append(0)
        norm = sum(p_unnorm)
        for i, a in enumerate(s.actions):
            a.policy = (1 - self.epsilon) * p_unnorm[i] / norm + self.epsilon / n
        if old_policy == s.policy:
            s.stable_policy = True
        return

    def update_sr_value_policy(self):
        reward_index = self.agent.reward_state.index
        reward = np.zeros(self.agent.n_s)
        reward[reward_index] = 1
        sr_value = reward @ self.agent.world.successor_matrix
        for s in self.agent.states:
            s.value = sr_value[s.index]
            for a in self.agent.states[0].actions:  # assume actions in one state can be taken in all states
                i = s.x + a.x
                j = s.y + a.y
                if (i, j) not in self.agent.world.state_indices:
                    continue
                neighbour_index = self.agent.world.state_indices[(i, j)]
                # based on how the indices have been designed 0 is opposite of 2, 1 is opposite of 3
                self.agent.states[neighbour_index].actions[(a.index + 2) % 4].value = sr_value[s.index]
        for s in self.agent.states:
            self.update_policy(s.index)

    def qlearn_update(self, s_index: int, a_index: int, s1_index: int):
        s, a, s1 = self.agent.states[s_index], self.agent.states[s_index].actions[a_index], self.agent.states[s1_index]
        if s1.terminal:
            return
        a1_index = np.argmax(s1.q_value)
        a1 = s1.actions[a1_index]
        a.value = (1 - self.alpha) * a.value + self.alpha * (s1.reward + self.gamma * a1.value)
        self.update_policy(s_index)
        return

    def learn(self, episodes, exploring_start=False, reset=True):
        if reset:
            self._reset()
        for i in range(episodes):
            if exploring_start:
                self.agent.state = random.choice(self.agent.available_states)
            else:
                self.agent.state = self.agent.initial_state
            old_state = self.agent.state
            action = random.choices(range(self.tot_a), self.agent.state.policy)[0]
            while True:
                self.agent.step(action)
                new_state = self.agent.state
                self.qlearn_update(old_state.index, action, new_state.index)
                action = random.choices(range(self.tot_a), self.agent.state.policy)[0]
                old_state = new_state
                if self.agent.state.terminal:
                    break


