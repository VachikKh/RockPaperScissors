import numpy as np
from game import RockPaperScissors


class Agent:

    def __init__(self):
        self.utility = 0
        self.regrets = {"rock": 0, "paper": 0, "scissors": 0}
        self.possible_actions = ["rock", "paper", "scissors"]

    @staticmethod
    def get_action(policy):

        # TODO CFR
        if policy == "pure":
            action = "rock"
        elif policy == "mixed":
            action = np.random.choice(["rock", "paper"])
        elif policy == "random":
            action = np.random.choice(["rock", "paper", "scissors"])
        else:
            action = np.random.choice(["rock", "paper", "scissors"])
        return action

    def update_utility(self, won):
        self.utility += 2 * int(won) - 1

    def get_score(self):
        return self.utility

    def update_regret(self, action1, action2):
        for best_action in self.possible_actions:
            self.regrets[best_action] += (RockPaperScissors.get_winner_id(action1, best_action)
                                           - RockPaperScissors.get_winner_id(action1, action2))




