class Player:
    """
    A class representing a player with a name and score.

    Attributes:
    - name (str): the name of the player
    - score (int): the current score of the player

    Methods:
    - win_ball(): increments the score of the player by 1
    """

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def win_ball(self):
        """
        Increments the score of the player by 1.
        """
        self.score += 1


score_dict = {
    0: "love",
    1: "fifteen",
    2: "thirty",
    3: "forty"
}


def is_normal(p1_score, p2_score):
    """
    Check if the scores are in a normal state, meaning that at least one player has scored 
    but neither player has reached the conditions for a game or deuce.

    Args:
    - p1_score: An integer representing the score of player 1
    - p2_score: An integer representing the score of player 2

    Returns:
    - A boolean indicating if the scores are in a normal state.
    """
    return (p1_score > 0 or p2_score > 0) and not is_same(p1_score, p2_score)


def is_initial(p1_score, p2_score):
    """
    Check if both scores are zero, meaning that the game has just started.

    Args:
    - p1_score: An integer representing the score of player 1
    - p2_score: An integer representing the score of player 2

    Returns:
    - A boolean indicating if the scores are in the initial state.
    """
    return p1_score == 0 and p2_score == 0


def is_deuce(p1_score, p2_score):
    """
    Check if the scores are in a deuce state, meaning that both players have scored at least 
    three points and their scores are equal.

    Args:
    - p1_score: An integer representing the score of player 1
    - p2_score: An integer representing the score of player 2

    Returns:
    - A boolean indicating if the scores are in a deuce state.
    """
    return p1_score >= 3 and p2_score >= 3 and is_same(p1_score, p2_score)


def is_same(p1_score, p2_score):
    """
    Check if the scores of both players are equal.

    Args:
    - p1_score: An integer representing the score of player 1
    - p2_score: An integer representing the score of player 2

    Returns:
    - A boolean indicating if the scores of both players are the same.
    """
    return p1_score == p2_score


def is_game(p1_score, p2_score):
    """
    Check if the scores are in a game state, meaning that at least one player has scored 
    four or more points and their score difference is at least 2.

    Args:
    - p1_score: An integer representing the score of player 1
    - p2_score: An integer representing the score of player 2

    Returns:
    - A boolean indicating if the scores are in a game state.
    """
    return (p1_score >= 4 or p2_score >= 4) and abs(p1_score - p2_score) > 1


def is_advantage(p1_score, p2_score):
    """
    Check if the scores are in an advantage state, meaning that at least one player has scored 
    four or more points, their score difference is only one, and the game has not yet been won.

    Args:
    - p1_score: An integer representing the score of player 1
    - p2_score: An integer representing the score of player 2

    Returns:
    - A boolean indicating if the scores are in an advantage state.
    """
    return (p1_score > 3 or p2_score > 3) and not is_same(p1_score, p2_score) and not is_game(p1_score, p2_score)



def is_game_point(p1_score, p2_score):
    """
    Check if the scores are in a game point state, meaning that at least one player has scored 
    three points but the game has not yet been won.

    Args:
    - p1_score: An integer representing the score of player 1
    - p2_score: An integer representing the score of player 2

    Returns:
    - A boolean indicating if the scores are in a game point state.
    """
    return (p1_score == 3 or p2_score == 3) and not is_game(p1_score, p2_score)


def game_point(player_1, player_2):
    """
    Determine which player has a game point based on their scores.

    Args:
    - player_1: A Player object representing the first player
    - player_2: A Player object representing the second player

    Returns:
    - A string indicating which player has a game point.
    """
    game_point_player = player_1 if player_1.score > player_2.score else player_2
    return "{} game point".format(game_point_player.name)


def advantage(player_1, player_2):
    """
    Determine which player has an advantage based on their scores.

    Args:
    - player_1: A Player object representing the first player
    - player_2: A Player object representing the second player

    Returns:
    - A string indicating which player has an advantage.
    """
    advantage_player = player_1 if player_1.score > player_2.score else player_2
    return "{} advantage".format(advantage_player.name)


def game(player_1, player_2):
    """
    Determine which player has won the game based on their scores.

    Args:
    - player_1: A Player object representing the first player
    - player_2: A Player object representing the second player

    Returns:
    - A string indicating which player has won the game.
    """
    winner = player_1 if player_1.score > player_2.score else player_2
    return "{} game".format(winner.name)


def normal_score(p1_score, p2_score):
    """
    Convert the scores to a string representation in a normal state.

    Args:
    - p1_score: An integer representing the score of player 1
    - p2_score: An integer representing the score of player 2

    Returns:
    - A string indicating the score of both players in a normal state.
    """
    return "{}-{}".format(score_dict.get(p1_score), score_dict.get(p2_score))



def same_score(p1_score, p2_score):
    """
    Given two player scores, returns a string representation of the score if they have the same score.
    If both scores are 0, returns "all-love".
    Otherwise, returns the score with the suffix "-all".

    Args:
    p1_score (int): The score of player 1
    p2_score (int): The score of player 2

    Returns:
    str: A string representation of the score if the scores are the same
    """
    if is_initial(p1_score, p2_score):
        return "all-love"
    return "{}-all".format(score_dict.get(p1_score))


def announce_score(player_1, player_2):
    """
    Given two Player objects, returns a string representation of the current game score.
    Checks for different states of the game (deuce, advantage, game point, game, normal score).
    
    Args:
    player_1 (Player): A Player object representing player 1
    player_2 (Player): A Player object representing player 2

    Returns:
    str: A string representation of the current game score
    """
    p1_score = player_1.score
    p2_score = player_2.score

    if is_deuce(p1_score, p2_score):
        return "Deuce"
    elif is_advantage(p1_score, p2_score):
        return advantage(player_1, player_2)
    elif is_game_point(p1_score, p2_score):
        return "{}\n{}".format(normal_score(p1_score, p2_score), game_point(player_1, player_2))
    elif is_game(p1_score, p2_score):
        return game(player_1, player_2)
    elif is_normal(p1_score, p2_score):
        return normal_score(p1_score, p2_score)
    else:
        return same_score(p1_score, p2_score)
