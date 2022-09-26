import numpy as np


class Agent:
    def __init__(self, learning_rate, discount_factor, explore_vs_exploit, q_tab):
        self.alpha = learning_rate
        self.gamma = discount_factor
        self.epsilon = explore_vs_exploit
        self.q_table = q_tab

    def act(self, environment, state):
        random_draw = np.random.uniform(0., 1.)
        if random_draw > self.epsilon:
            action = np.argmax(self.q_table[state])
        else:
            action = environment.action_space.sample()
        next_state, reward, episode_is_finished, info = environment.step(action)

        return action, next_state, reward, episode_is_finished, info

    def act_greedy(self, environment, state):
        action = np.argmax(self.q_table[state])     
        next_state, reward, episode_is_finished, info = environment.step(action)

        return action, next_state, reward, episode_is_finished, info

    def learn(self, state, action, current_state_value, next_best_state_value, reward):
        self.q_table[state, action] = (1 - self.alpha) * current_state_value + \
                                      self.alpha * (reward + (self.gamma * next_best_state_value) - current_state_value)

    def solve_task(self, environment, printing=False):
        state = environment.reset()
        if printing:
            environment.render()
        done = False
        rewards = 0
        while not done:
            action = np.argmax(self.q_table[state])
            state, reward, done, info = environment.step(action)
            rewards += reward
            if printing:
                environment.render()
                print(reward)
                print()
            # time.sleep(0.5)
        return rewards

    def save_agent(self, dir_name, num_episodes):
        file_name = dir_name + "/agent_{}_{}_{}_{}.txt".format(self.epsilon, self.alpha, self.gamma, num_episodes)
        np.savetxt(file_name, self.q_table, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='',
                   comments='# ', encoding=None)

    def load_agent_data(self, dir_name, num_episodes):
        file_name = dir_name + "/agent_{}_{}_{}_{}.txt".format(self.epsilon, self.alpha, self.gamma, num_episodes)
        self.q_table = np.loadtxt(file_name, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None)
