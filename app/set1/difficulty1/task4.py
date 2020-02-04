def single_match(balance, weights):
    for weight in weights:
        if balance[0] == weight + balance[1]:
            return weight
        elif balance[1] == weight + balance[0]:
            return weight
    return None


def double_balance(balance, w1, w2):
    if balance[0]           == balance[1] + w1 + w2:
        return True
    elif balance[1]         == balance[0] + w1 + w2:
        return True
    elif balance[0] + w1    == balance[1] + w2:
        return True
    elif balance[0] + w2    == balance[1] + w1:
        return True
    else:
        return False


def double_match(balance, weights):
    for i1 in range(len(weights)):
        remaining = weights.copy()
        w1 = remaining.pop(i1)
        for i2 in range(len(remaining)):
            w2 = remaining[i2]
            if double_balance(balance, w1, w2):
                solution = [w1, w2]
                solution.sort()
                return solution
    return None


def balancing(balance:list, weights:list):
    # Initial tests
    if len(balance) != 2:
        return None
    if len(weights) < 1:
        return None
    
    # Initial prints.
    print('Input :', balance, '\t', weights)
    solution = None

    # Check if single value match.
    x = single_match(balance, weights)

    # If not single, maybe double?
    if x is None and len(weights) > 1:
        x = double_match(balance, weights)

    # Final prints and return.
    if x is None:
        solution = 'Ikke mulig!'
    else:
        solution = x
    print(solution)
    return solution
