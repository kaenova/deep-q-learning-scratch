# Membuat game yang mengharuskan player menjalankan ke arah tujuan
# [P - - - - T - - - - -]
# Disini P = Player dan T = Tujuan. Pada kasus di atas, player harus bergerak ke kanan
# untuk mendekati tujuan

import random

class Game:
    # Actions
    # 0 = player bergerak ke kiri
    # 1 = player bergerak ke kanan
    num_actions = 2
    
    # State
    # 0 = player position (1 on state space)
    # 1 = target position (2 on state space)
    state = {
        0 : None,
        1 : None
    }
    
    MAX_MOVEMENT = 5
    current_movement = 5
    
    bot_idx = 0
    up_idx = 9
    
    def __init__(self) -> None:
        player = random.randint(self.bot_idx, self.up_idx)
        target = player
        while target == player:
            x = random.randint(- self.MAX_MOVEMENT, self.MAX_MOVEMENT)
            target = (x + player if x + player >= self.bot_idx and x + player <= self.up_idx else player)
        self.state = [player, target]
    
    def print_state(self):
        print(self.get_state())
        
    def get_state(self):
        state = [0 for _ in range(10)]
        state[self.state[0]] = 1 # player assign
        state[self.state[1]] = 2 # target assign
        return state
    
    def execute_action(self, action_num):
        rewards = None
        
        state_before = self.state.copy()
        if action_num == 0:
            if self.state[0] - 1 >= self.bot_idx:
                self.state[0] -= 1
        else:
            if self.state[0] + 1 <= self.up_idx:
                self.state[0] += 1
            
        rewards = self.__calculate_rewards__(self.state, state_before)
        
        self.current_movement -= 1
        
        return self.get_state(), rewards, self.__check_game_end__()
    
    def __calculate_rewards__(self, current_state, previous_state):
        # Calculate the distance between player and target and normalize it
        current = abs(current_state[0] - current_state[1])
        before = abs(previous_state[0] - previous_state[1])
        if current < before:
            return 1
        else:
            return -1
    
    def __check_game_end__(self):
        if self.current_movement == 0:
            return 1
        
        if self.state[0] == self.state[1]:
            return 1
        else:
            return 0
        
class GameInterface:
    
    def __init__(self) -> None:
        self.game = Game()
        
    def play(self):
        game_end = False
        while not game_end:
            self.game.print_state()
            action = self.player_input()
            _, _, game_end = self.game.execute_action(action)
            
            
    def player_input(self):
        pesan = """Aksi
        0 = Ke arah kiri
        1 = Ke arah kanan"""
        print(pesan)
        return int(input("Masukkan aksi: "))
    
    
def main():
    interface = GameInterface()
    interface.play()
    
if __name__ == "__main__":
    main()