import gym
import cityflow


class cityEnv(gym.Env):
    def __init__(self):
        self.eng = cityflow.Engine(config_file="config.json", thread_num=1)

    def step(self,action):
        reward = 0
        done = False
        self.eng.next_step()
        return self.get_obs(), reward, done, {}

    def get_obs(self):
        return 0
        
    def reset(self):
        return self.get_obs()