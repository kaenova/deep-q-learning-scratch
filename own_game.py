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
    # 0 = player position
    # 1 = target position
    state = {
        0 : None,
        1 : None
    }
    
    def __init__(self) -> None:
        player = random.randint(0, 5)
        target = player
        while target == player:
            target = random.randint(0,5)
        self.state = [player, target]
    
    def print_state(self):
        print(f"Target Position : {self.state[1]}")
        print(f"Player Position : {self.state[0]}")
    
    def get_state(self):
        # Must be converted to list or np.array to be processed into TF Models
        return [self.state[0], self.state[1]]
    
    def execute_action(self, action_num):
        rewards = None
        
        state_before = self.state
        if action_num == 0:
            self.state[0] -= 1
        else:
            self.state[0] += 1
            
        rewards = self.__calculate_rewards__(self.state, state_before)
        
        return self.get_state(), rewards, self.__check_game_end__()
    
    def __calculate_rewards__(self, current_state, previous_state):
        # Calculate the distance between player and target and normalize it
        delta_current = (current_state[0] - current_state[1]) ** 2
        delta_before = (previous_state[0] - previous_state[1]) ** 2
        
        if delta_current < delta_before:
            return 1
        else:
            return -1
    
    def __check_game_end__(self):
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