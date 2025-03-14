def alpha_beta_search(gameState):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.
    
    You can ignore the special case of calling this function
    from a terminal state.
    """
    alpha = float("-inf")
    beta = float("inf")
    best_score = float("-inf")
    best_move = None
    for a in gameState.actions():
        v = min_value(gameState.result(a), alpha, beta)
        if v > best_score:
            best_score = v
            best_move = a
        alpha = max(alpha, best_score)
    return best_move

# TODO: modify the function signature to accept an alpha and beta parameter
def min_value(gameState, alpha, beta):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if gameState.terminal_test():
        return gameState.utility(0)  # Return utility from perspective of player 0
    
    v = float("inf")
    for a in gameState.actions():
        v = min(v, max_value(gameState.result(a), alpha, beta))
        if v <= alpha:  # Alpha pruning
            return v
        beta = min(beta, v)
    return v

# TODO: modify the function signature to accept an alpha and beta parameter
def max_value(gameState, alpha, beta):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if gameState.terminal_test():
        return gameState.utility(0)  # Return utility from perspective of player 0
    
    v = float("-inf")
    for a in gameState.actions():
        v = max(v, min_value(gameState.result(a), alpha, beta))
        if v >= beta:  # Beta pruning
            return v
        alpha = max(alpha, v)
    return v
