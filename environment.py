import gym
import cityflow


class cityEnv(gym.Env):
    def __init__(self):
        self.eng = cityflow.Engine(config_file="config.json", thread_num=1)

    def step(self,action):
        reward = 0
        done = False
        self.eng.set_tl_phase(action)
        self.eng.next_step()
        return self.get_obs(), reward, done, {}

    def get_obs(self):
        return list(self.eng.get_lane_vehicle_count().values())
        
    def reset(self):
        return self.get_obs()