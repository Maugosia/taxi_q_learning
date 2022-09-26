import gym
import numpy as np
import agent
from q_learning import q_learning_algorithm_get_train_data
import matplotlib.pyplot as plt


def experiment_1(input_list):
    print("hello agent TAXI~!!!")

    # ---------------------INITIALIZE ENVIROMENT
    env = gym.make("Taxi-v3")
    datas = []
    datas_smooth = []
    for p in input_list:
        # ----------------------INITIALIZE AGENT
        learning_rate = 0.5
        discount = p
        epsilon = 0.9
        q_table_0 = np.zeros([env.observation_space.n, env.action_space.n])

        agent_taxi = agent.Agent(learning_rate, discount, epsilon, q_table_0)

        # -------------------------REINFORCEMENT LEARNING
        number_episodes = 2000
        learned_agent, data = q_learning_algorithm_get_train_data(env, agent_taxi, number_episodes)
        data_smooth = smooth(data)
        datas.append(data)
        datas_smooth.append(data_smooth)

    colors = ["red", "blue", "orange", "violet", "green", "yellow", "k", "magenta", "aqua"]

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_xlabel('n dziesiątek epizodów')
    ax1.set_ylabel('średnia nagroda za rozgrywkę')
    ax1.set_title('Proces uczenia dla różnych wartości  parametru gamma')

    color_id = 0
    for y_data in datas:
        ax1.plot(y_data, color=colors[color_id], lw=2, label=str(input_list[color_id]))
        color_id = color_id + 1
    plt.legend()
    plt.show()

    # plt.clf()

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_xlabel('n setek epizodów')
    ax1.set_ylabel('średnia nagroda za rozgrywkę')
    ax1.set_title('Proces uczenia dla różnych wartości  parametru gamma')

    color_id = 0
    for y_data in datas_smooth:
        ax1.plot(y_data, color=colors[color_id], lw=2, label=str(input_list[color_id]))
        color_id = color_id + 1
    plt.legend()
    plt.show()

    # ----------------------END ENVIRONMENT
    env.close()


def smooth(data_in):
    data_out = []
    for i in range(0, int(len(data_in)/10)):
        data_out.append(np.mean(np.array(data_in[i*10:(i+1)*10])))

    return data_out


if __name__ == "__main__":
    params = [0.1, 0.3, 0.5, 0.7, 0.9]
    experiment_1(params)
