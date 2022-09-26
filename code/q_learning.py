import numpy as np


def q_learning_algorithm(environment, agent, num_episodes):

    for i in range(0, num_episodes):
        # print("##################################################################### -> playing episode: ", i)
        state = environment.reset()
        episode_is_finished = False
# 
        if i % 1000 == 0:
            test_rewards = []
            for j in range(0, 30):
                test_is_finished = False
                sum_rewards = 0
                while not test_is_finished:
                    action, next_state, reward, test_is_finished, info = agent.act_greedy(environment, state)
                    sum_rewards += reward
                    state = next_state
                test_rewards.append(sum_rewards)

        while not episode_is_finished:
            # act
            action, next_state, reward, episode_is_finished, info = agent.act(environment, state)
            # observe
            current = agent.q_table[state, action]
            next_best = np.max(agent.q_table[next_state])
            # learn from experience
            agent.learn(state, action, current, next_best, reward)
            state = next_state

    return agent


def q_learning_algorithm_get_train_data(environment, agent, num_episodes):
    progress = []
    for i in range(0, num_episodes):
        # print("##################################################################### -> playing episode: ", i)
        # state = environment.reset()
        episode_is_finished = False

        if i % 10 == 0:
            test_rewards = []
            for j in range(0, 5):
                state = environment.reset()
                test_is_finished = False
                sum_rewards = 0
                while not test_is_finished:
                    action, next_state, reward, test_is_finished, info = agent.act_greedy(environment, state)
                    sum_rewards += reward
                    state = next_state
                test_rewards.append(sum_rewards)
            print(i, test_rewards, "mean = ", np.mean(np.array(test_rewards)))
            progress.append(np.mean(np.array(test_rewards)))

        state = environment.reset()
        while not episode_is_finished:
            # act
            action, next_state, reward, episode_is_finished, info = agent.act(environment, state)
            # observe
            current = agent.q_table[state, action]
            next_best = np.max(agent.q_table[next_state])
            # learn from experience
            agent.learn(state, action, current, next_best, reward)
            state = next_state

    return agent, progress
