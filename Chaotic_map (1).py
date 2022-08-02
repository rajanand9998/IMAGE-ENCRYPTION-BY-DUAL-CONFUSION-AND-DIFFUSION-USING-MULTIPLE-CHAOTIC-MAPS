import numpy as np

def logistic_key(x, r, size):
    key = []
    for i in range(size):   
        x = r*x*(1-x)   # The logistic equation
        key.append(int((x*pow(10, 16))%256))    # Converting the generated number between 0 to 255
    return key

def tent_key(init,p,steps):
    xs = np.arange(steps)
    ys = np.zeros((steps))
    ys[0] = init
    key = []
    key.append(16)
    for i in range(1,steps):
        y = ys[i-1]
        if (y < 0.5 and y >=0.0):
            ys[i] = p*y
        elif (y >=0.5):
            ys[i] = p*(1-y)
        key.append(int((ys[i]*pow(10, 5))%256))    # Converting the generated number between 0 to 255
    return key

def lorenz_key(xinit, yinit, zinit, num_steps):
    dt = 0.01
    # Initializing 3 empty lists
    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)
    # Initializing initial values
    xs[0], ys[0], zs[0] = (xinit, yinit, zinit)
    # Initializing constants
    s = 10
    r = 28
    b = 2.667
    # System of equations
    for i in range(num_steps):
        xs[i + 1] = xs[i] + (s * (ys[i] - xs[i]) * dt)
        ys[i + 1] = ys[i] + ((xs[i] * (r - zs[i]) - ys[i]) * dt)
        zs[i + 1] = zs[i] + ((xs[i] * ys[i] - b * zs[i]) * dt)
    return xs, ys, zs