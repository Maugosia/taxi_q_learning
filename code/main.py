import gym
import numpy as np
import agent
from q_learning import q_learning_algorithm


def main():
    # ---------------------INITIALIZE ENVIRONMENT
    env = gym.make("Taxi-v3")

    # ----------------------INITIALIZE AGENT
    learning_rate = 0.5
    discount = 0.9
    epsilon = 0.9
    q_table_0 = np.zeros([env.observation_space.n, env.action_space.n])

    agent_taxi = agent.Agent(learning_rate, discount, epsilon, q_table_0)

    # -------------------------REINFORCEMENT LEARNING
    number_episodes = 100
    learned_agent = q_learning_algorithm(env, agent_taxi, number_episodes)
    learned_agent.save_agent("agents", number_episodes)

    sum_rewards = learned_agent.solve_task(env)

    # ----------------------END ENVIRONMENT
    env.close()
    return sum_rewards


if __name__ == "__main__":
    r_list = []
    for i in range(0, 50):
        out = main()
        r_list.append(out)
        print("rep = {} ".format(i), "out = ", out)

    print("MEAN: ", np.mean(np.array(r_list)))
    print("STD: ", np.std(np.array(r_list)))
