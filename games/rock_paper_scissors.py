import random
import sys


class RPS:  # Rock Paper Scissors
    def __init__(self):  # constructor
        print("Welcome to Rock Paper Scissor!")
        self.moves: dict = {'rock': '🪨', 'paper': '📃', 'scissors': '✂️'}
        self.valid_moves: list[str] = list(self.moves)  # or self.moves.keys()
        self.count_robot: int = 0
        self.count_user: int = 0


    def play_game(self):
        user_move: str = input('Choose between rock, paper or scissors -> ').lower()
        if user_move == 'exit':
            print('Thanks for playing!')
            sys.exit()

        if user_move not in self.valid_moves:
            print('Invalid move')
            return self.play_game()

        robot_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, robot_move)

    def display_moves(self, user_move, robot_move):
        print('-------')
        print(f'You: {self.moves[user_move]}')
        print(f'Robot: {self.moves[robot_move]}')
        print('-------')
        self.check_moves(user_move, robot_move)
        print('-------')
        print('Score count')
        print(f'Robot has won {self.count_robot} times')
        print(f'You have won {self.count_user} times')
        print('-------')
        self.play_game()

    def check_moves(self, user_move, robot_move):
        if user_move == robot_move:
            print('It\'s a tie!')
        elif user_move == 'scissors' and robot_move == 'paper':
            print('You win! 🥳')
            self.count_user += 1
        elif user_move == 'paper' and robot_move == 'rock':
            print('You win! 🥳')
            self.count_user += 1
        elif user_move == 'rock' and robot_move == 'scissors':
            print('You win! 🥳')
            self.count_user += 1
        else:
            print('You lost 😔')
            self.count_robot += 1




if __name__ == '__main__':
    g = RPS()
    g.play_game()

