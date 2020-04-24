from game import RockPaperScissors


N_ITER = 1000
if __name__ == '__main__':

    rpc = RockPaperScissors()

    for _ in range(N_ITER):

        rpc.step()
        # print("winner is ", rpc.winner_id)
    print("player1_score is ", rpc.agent1.get_score())
    print("player2_score is ", rpc.agent2.get_score())
