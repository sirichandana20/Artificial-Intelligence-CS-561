def argmin(seq, fn):
    best = seq[0]; best_score = fn(best)
    for x in seq:
        x_score = fn(x)
        if x_score < best_score:
            best, best_score = x, x_score
    return best

def argmax(seq, fn):
    return argmin(seq, lambda x: -fn(x))

movement = [(1,0), (0, -1), (-1, 0), (0, 1)]

def right(shift):
    return movement[movement.index(shift)-1]

def left(shift):
    return movement[(movement.index(shift)+1) % len(movement)]

def if_(test, result, alternative):
    if test:
        if callable(result): return result()
        return result
    else:
        if callable(alternative): return alternative()
        return alternative

def vector_add(a, b):
    return tuple(map(operator.add, a, b))

def value_iteration(mdp):
    U1 = dict([(s, 0) for s in mdp.states])
    R, T = mdp.R, mdp.T
    while True:
        U = U1.copy()
        delta = 0
        for s in mdp.states:
            U1[s] = R(s) + gamma * max([sum([p * U[s1] for (p, s1) in T(s, a)])
                                        for a in mdp.actions(s)])
            delta = max(delta, abs(U1[s] - U[s]))
        if delta < np.float64(epsilon * (1 - gamma) / gamma):
             return U

def policy(mdp, U):
    pi = {}
    for s in mdp.states:
        pi[s] = argmax(mdp.actions(s), lambda a:utility(a, s, U, mdp))
    return pi

def utility(a, s, U, mdp):
    return sum([p * U[s1] for (p, s1) in mdp.T(s, a)])

def update(x, **entries):
    if isinstance(x, dict):
        x.update(entries)
    else:
        x.__dict__.update(entries)
    return x


class MDP:

    def __init__(self, init, actlist, terminals, gamma=.9):
        update(self, init=init, actlist=actlist, terminals=terminals,
               gamma=gamma, states=set(), reward={})

    def R(self, state):
        return self.reward[state]

    def T(state, action):
        abstract

    def actions(self, state):
        if state in self.terminals:
            return [None]
        else:
            return self.actlist

class GridMDP(MDP):
    def __init__(self, grid, terminals, init=(0, 0), gamma=.9):
        MDP.__init__(self, init, actlist=movement,
                     terminals=terminals, gamma=gamma)
        update(self, grid=grid, rows=len(grid), cols=len(grid[0]))
        for x in range(self.cols):
            for y in range(self.rows):
                self.reward[x, y] = grid[y][x]
                if grid[y][x] is not None:
                    self.states.add((x, y))

    def T(self, state, action):
        if action == None:
            return [(0.0, state)]
        else:
            return [(0.7, self.go(state, action)),
                    (0.1, self.go(state, right(action))),
                    (0.1, self.go(state, left(action))),
                    (0.1, self.go(state, left(left(action))))]

    def go(self, state, direction):
        state1 = vector_add(state, direction)
        return if_(state1 in self.states, state1, state)



import numpy as np
import operator
import math

if __name__ == '__main__':
    inp = open("input.txt", "r")
    out = open('output.txt', 'w')

    global gamma
    gamma = 0.9
    global epsilon
    epsilon = 0.1

    size = int(inp.readline())
    cars = int(inp.readline())
    ob = int(inp.readline())

    obs = [[] for i in range(ob)]

    for i in range(ob):
        m, n = inp.readline().split(',')
        a = int(m)
        b = int(n)
        obs[i].append(a)
        obs[i].append(b)

    start = [[] for i in range(cars)]

    for i in range(cars):
        m, n = inp.readline().split(',')
        a = int(m)
        b = int(n)
        start[i].append(int(a))
        start[i].append(int(b))

    finish = [[] for i in range(cars)]
    for i in range(cars):
        m, n = inp.readline().split(',')
        a = int(m)
        b = int(n)
        finish[i].append(a)
        finish[i].append(b)

    inp.close()
    mat = []
    for i in range(cars):
        mat.append(np.full(shape=(size, size), fill_value=(-1)))

    for i in range(ob):
        for j in range(cars):
            mat[j][obs[i][1]][obs[i][0]] = -101

    for i in range(cars):
        mat[i][finish[i][1]][finish[i][0]] = 99

    for j in range(cars):
        final = (finish[j][0], finish[j][1])
        g = GridMDP(mat[j], terminals=[final])
        U = value_iteration(g)
        pi = policy(g, U)

        points = [0 for i in range(10)]
        for i in range(10):
            pos = list(start[j])
            np.random.seed(i)
            swerve = np.random.random_sample(1000000)
            # print(swerve)
            k = 0
            while ((pos[0] != final[0]) or (pos[1] != final[1])):
                move = pi[pos[0], pos[1]]
                if (np.float64(swerve[k]) > 0.7):
                    if (np.float64(swerve[k]) > 0.8):
                        if (np.float64(swerve[k]) > 0.9):
                            move = right(right(move))
                        else:
                            move = right(move)
                    else:
                        move = left(move)

                pos1 = pos[0] + move[0]; pos2 = pos[1] + move[1]
                if pos1 >= 0 and pos2 >= 0:
                    if pos1 < size and pos2 < size:
                        pos = (pos1,pos2)
                rew = g.R((pos[0], pos[1]))

                points[i] += rew
                k += 1

        average = int(math.floor(np.float64(sum(points) / len(points))))
        #out.write(str(average))
        #out.write('\n')
        print(average)
        print('\n')
