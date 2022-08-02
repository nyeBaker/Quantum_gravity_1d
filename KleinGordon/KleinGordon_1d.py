from cmath import tanh
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('default')
import warnings
warnings.filterwarnings("ignore")
import imageio
import os
from tqdm import tqdm
import time

path = os.getcwd()
path_2d = os.path.join(path, '2D')

def chdir(path):
    if not os.path.isdir(path):
        os.mkdir(path)
    os.chdir(path)

def plot_p_j(jj, count):
    plt.figure(figsize=(10,8))
    plt.plot(x, p[jj,:], 'r', label='Probability Denisty')
    plt.title('1D Dirac Equation $t=${}, $\sigma=${}'.format(round(t[jj], 4), sigma))
    plt.ylabel(r'Amplitude')
    plt.xlabel(r'$x$')
    plt.grid(alpha=0.618)
    plt.legend()
    plt.ylim(0,ymax*1.1)
    plt.savefig('H{:03d}'.format(count)+'.png')
    plt.close()

def init(x, sigma):
    u = np.exp(-(sigma*x)**2/2)
    return u

def build_x(x_min, x_max, dx):
    return np.round(np.arange(x_min, x_max + dx, dx), 8)

def build_t(t_min, t_max, dt):
    dt = round(dt, 8)
    return np.round(np.arange(t_min, t_max + dt, dt), 8)

def P(psi1):
    return np.conj(psi1)*psi1

def gen_gif(path, gif_file):
    print("Creating {:s}...".format(gif_file))
    os.chdir(path)
    image_folder = os.fsencode(path)

    filenames = []
    for file in os.listdir(image_folder):
        filename = os.fsdecode(file)
        if filename.endswith(('.png')): #, '.png', '.gif', '.jpg'
            filenames.append(filename)

    filenames.sort()  # this iteration technique has no built in order, so sort the frames

    images = list(map(imageio.imread, filenames))

    # modify the frame duration as needed
    imageio.mimsave(gif_file, images, duration=0.07)  
    print("Done")

def m(x):
    return 5*tanh(0.02*x)


def LF(t,x,init):
    u = np.zeros(shape=(len(t),len(x)), dtype=np.complex128)

    for tt in tqdm(range(len(t))):
        if tt == 0:
            z = init(x)
            u[tt, :] = z
        elif tt == 1:
            u[tt,:] = u[0, :]
        else:
            for xx in range(len(x)):
                if xx == 0 or xx == len(x) - 1:
                    u[tt, xx] = 0 # Boundary conditions
                else:
                    if VAR_MASS:
                        u[tt, xx] = u[tt-2, xx] - l*(u[tt-1, xx+1]-u[tt-1, xx-1])-1j*dt*u[tt-1, xx]*m(xx)
                    else:
                        u[tt, xx] = u[tt-2, xx] - l*(u[tt-1, xx+1]-u[tt-1, xx-1])-1j*dt*u[tt-1, xx]
    return u

VAR_MASS = True
t_min, t_max = 0, 100
x_min, x_max = -50, 50
sigma = 0.2
h, l = 0.1, 0.1
dx, dt = h, np.round(h*l, 8)

x = build_x(x_min, x_max, dx)
t = build_t(t_min, t_max, dt)
print("M: {0}, N:{1}".format(len(x), len(t)))
time.sleep(1)

u = LF(t, x, lambda x: init(x,sigma))

p = P(u)

chdir(path_2d)
ymax = 1
count = 0
for jj in tqdm(range(0, len(p[:,0]), 50)):
    plot_p_j(jj, count)
    count += 1

plot_p_j(-1, count)

gen_gif(path_2d, 'Dirac_2D.gif')