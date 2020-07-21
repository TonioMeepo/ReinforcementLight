import gym
import cityflow


class cityEnv(gym.Env):
    def __init__(self):
        self.steps = 0
        self.action_space=gym.spaces.Discrete(8)
        self.eng = cityflow.Engine(config_file="config.json", thread_num=1)

    def step(self,action):
        self.steps += 1
        done = self.steps == 3000 
        self.eng.set_tl_phase("intersection_1_1",action)
        self.eng.next_step()
        reward = -self.eng.get_vehicle_count()
        return self.get_obs(), reward, done, {}

    def get_obs(self):
        return list(self.eng.get_lane_vehicle_count().values())
        
    def reset(self):
        self.eng = cityflow.Engine(config_file="config.json", thread_num=1)
        self.steps = 0
        return self.get_obs()