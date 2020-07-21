import rl
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.layers.advanced_activations import LeakyReLU, PReLU, ReLU
from keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import EpsGreedyQPolicy
import environment

env = environment.cityEnv()

model = Sequential()
model.add(Flatten(input_shape=(1,24)))
model.add(Dense(35,activation='linear'))
model.add(LeakyReLU(alpha=.001))
model.add(Dense(8))
model.add(Activation('linear'))

memory = SequentialMemory(limit=50000, window_length=1)
policy = EpsGreedyQPolicy(0.02)
dqn = DQNAgent(model=model, nb_actions=8, memory=memory, nb_steps_warmup=10,
               target_model_update=1e-2, policy=policy)
dqn.compile(Adam(lr=1e-3), metrics=['mae'])
dqn.fit(env, nb_steps=50000, visualize=True, verbose=2)
dqn.test(env, nb_episodes=5, visualize=True)