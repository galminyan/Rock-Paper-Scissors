import random
moves = ['rock', 'paper', 'scissors']
cyMoves = ['rock', 'paper', 'scissors', 'rock', 'paper']


class Player:
    def __init__(self):
        self.i = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.prev1 = my_move
        self.prev2 = their_move


class ReflectPlayer(Player):
    prev1 = random.choice(moves)

    def reflect_move(self):
        return self.prev1


class CyclePlayer(Player):
    def cycle_move(self):
        return cyMoves[self.i]


class HumanPlayer(Player):
    def human_move(self):
        while True:
            play = input('Chose your move! Please enter "rock", "paper",'
                         ' "scissors" (or "q" to quit):')
            if play == "rock":
                return "rock"
            elif play == "paper":
                return "paper"
            elif play == "scissors":
                return "scissors"
            elif play == "q":
                exit()
            else:
                print("\nError: Invalid Entry! Try again.")


class RandomPlayer(Player):
    def comp_move(self):
            return random.choice(moves)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        if WhichGame == 'random':
            move1 = self.p1.comp_move()
        elif WhichGame == 'reflect':
            move1 = self.p1.reflect_move()
        elif WhichGame == 'cycle':
            move1 = self.p1.cycle_move()
        elif WhichGame == 'repeat':
            move1 = self.p1.move()
        else:
            move1 = self.p1.comp_move()
        move2 = self.p2.human_move()

        print(f'TheComputer: {move1}  You: {move2}')

        if move1 == move2:
            print("It's a Tie")
            print(f'Score: TheComputer:{self.score1} - You:{self.score2}')
        elif beats(move1, move2):
            print(f'One point to TheComputer, {move1} wins {move2}')
            self.score1 += 1
            print(f'Score: TheComputer:{self.score1} - You:{self.score2}')
        elif beats(move2, move1):
            print(f'One point to You, {move2} wins {move1}')
            self.score2 += 1
            print(f'Score: TheComputer:{self.score1} - You:{self.score2}')
        else:
            self.play_round()

        self.p1.learn(move2, move1)
        self.p2.learn(move1, move2)
        self.p1.i += 1

    def play_game(self):
        print('Game start!')
        print(f'The computer will play {WhichGame} moves!')

        for round in range(5):
            print(f'\nRound {round+1}:')

            self.play_round()
        print('Game over!')
        self.winner()

    def winner(self):
        if self.score1 > self.score2:
            print('And the winner is >>>>>>> TheComputer!')
        elif self.score2 > self.score1:
            print('And the winner is >>>>>>> You!')
        else:
            print('There is no winner on this game!')


if __name__ == '__main__':
    WhichGame = input('Who would you like to play with? Please enter'
                      ' "random", "repeat", "reflect" or "cycle":')
    if WhichGame == 'random':
        Player = RandomPlayer()
    elif WhichGame == 'reflect':
        Player = ReflectPlayer()
    elif WhichGame == 'cycle':
        Player = CyclePlayer()
    elif WhichGame == 'repeat':
        Player = Player()
    else:
        WhichGame = 'random'
        Player = RandomPlayer()

    game = Game(Player, HumanPlayer())
    game.play_game()
