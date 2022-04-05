# Translating from Papers Algorithm to python code.
# But this is still in general

import random

def deep_q_learning(num_episodes: int, max_replay_mem: int, epsilon: float, num_actions: int, warmpups_steps: int):
    # ReplayMemory(max_replay_mem) # Initialize Replay Memory dengan kapasitas max_replay_mem
    # eval_net, target_net = model_init() # Initialize random Model with input (state) and output (actions)
    for i in range(num_episodes):
        game_end = False
        while not game_end:
            state = None # Game.getState()
            actions = None
            if random.random() > epsilon:
                actions = random.randint(0, num_actions - 1)
            else:
                actions = None # model.predict(state)
            # rewards, next_state = Game.exectue(actions)
            # ReplayMemory.store(state, actions, rewards, next_state)
            # Calculate yj
            
            # now yj is a "true" data and X is state Y is actions
            
            # eval model fit on [X, Y] targeting yj with losses using MSE