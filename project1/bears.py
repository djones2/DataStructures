def bears(n):
    """A True return value means that it is possible to win
    the bear game by starting with n bears. A False return value means
    that it is not possible to win the bear game by starting with n
    bears."""
    # Check if game is won.
    if n == 42:
        return True
    # Check if game is lost.
    if n < 42:
        return False
    # Check if value is divisible by 2
    if n % 2 == 0:
        # If so, return half of the bears.
        if bears(n // 2) == True:
            return True
        # Check if value is divisible by 3 or 4.
    if n % 3 == 0 or n % 4 == 0:
        # Ensure resultant multiplication of last two digits
        # is not 0.
        if n % 10 != 0 and (n % 100) // 10 != 0:
            # Give back product of last two digits and keep playing.
            if bears(n - ((n % 10)*((n % 100) // 10))) == True:
                return True
    # Check if value is divisible by 5.
    if n % 5 == 0:
        # If so, give back 42 bears and keep playing
        if bears(n - 42) == True:
            return True
    return False
