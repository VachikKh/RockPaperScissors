from agent import Agent


class RockPaperScissors:
    def __init__(self):

        self.agent1 = Agent()
        self.agent2 = Agent()
        self.winner_id = "Tie"

    @staticmethod
    def get_winner_id(player1_action, player2_action):
        """
        return winnerid
         if 0 it is draw
         if 1 player 1 wins
         if 2 player 2 wins
         """
        if player1_action == "rock" and player2_action == "rock":
            return 0

        elif player1_action == "rock" and player2_action == "paper":
            return -1

        elif player1_action == "rock" and player2_action == "scissors":
            return 1

        elif player1_action == "paper" and player2_action == "rock":
            return 1

        elif player1_action == "paper" and player2_action == "paper":
            return 0

        elif player1_action == "paper" and player2_action == "scissors":
            return -1

        elif player1_action == "scissors" and player2_action == "rock":
            return -1

        elif player1_action == "scissors" and player2_action == "paper":
            return 1

        elif player1_action == "scissors" and player2_action == "scissors":
            return 0

    def step(self):

        action1 = self.agent1.get_action(policy="random")
        action2 = self.agent2.get_action(policy="random")
        self.winner_id = self.get_winner_id(action1, action2)

        if self.winner_id == 1:
            self.agent1.update_utility(won=True)
            self.agent2.update_utility(won=False)

        elif self.winner_id == -1:
            self.agent2.update_utility(won=True)
            self.agent1.update_utility(won=False)

        else:
            pass
