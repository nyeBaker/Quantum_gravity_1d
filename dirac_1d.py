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

#set path
import os

path = os.getcwd()

path_2d = os.path.join(path, '2D')
path_3d = os.path.join(path, '3D')

def chdir(path):
    if not os.path.isdir(path):
        os.mkdir(path)
    os.chdir(path)

def plot_u_v(zz, count):
    plt.figure(figsize=(10,8))
    plt.plot(x, u[zz,:].real, 'r', label=r'$\psi_1$ R')
    plt.plot(x, u[zz,:].imag, 'r--', label=r'$\psi_1$ I')
    plt.plot(x, v[zz,:].real, 'k', label=r'$\psi_4$ R')
    plt.plot(x, v[zz,:].imag, 'k--', label=r'$\psi_4$ I')
    plt.title('1D Dirac Equation $t=${}, $\sigma=${}'.format(round(t[zz], 4), sigma))
    plt.ylabel(r'$\psi$')
    plt.xlabel(r'$x$')
    plt.grid(alpha=0.618)
    plt.ylim(-ymax,ymax)
    plt.legend()
    plt.savefig('G{:03d}'.format(count)+'.png')
    plt.close()

def plot_p_j(jj, count):
    plt.figure(figsize=(10,8))
    plt.plot(x, j[jj,:], 'b', label='Current')
    plt.plot(x, p[jj,:], 'r', label='Probability Denisty')
    #plt.plot(x, j[jj,:].imag, 'b', label='Current I')
    plt.title('1D Dirac Equation $t=${}, $\sigma=${}'.format(round(t[jj], 4), sigma))
    plt.ylabel(r'Amplitude')
    plt.xlabel(r'$x$')
    plt.grid(alpha=0.618)
    plt.legend()
    plt.ylim(-ymax,ymax)
    plt.savefig('H{:03d}'.format(count)+'.png')
    plt.close()

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


def init(x, sigma):
    u = np.exp(-(sigma*x)**2/2)
    return u

def P(psi1, psi2):
    return np.conj(psi1)*psi1+np.conj(psi2)*psi2

def J(psi1, psi2):
    return np.conj(psi1)*psi2+np.conj(psi2)*psi1

def build_x(x_min, x_max, dx):
    return np.round(np.arange(x_min, x_max + dx, dx), 8)

def build_t(t_min, t_max, dt):
    dt = round(dt, 8)
    return np.round(np.arange(t_min, t_max + dt, dt), 8)

def m(x):
    return 2*tanh(0.5*x)
    

def LF(t, x, init):
    u = np.zeros(shape=(len(t),len(x)), dtype=np.complex128)
    v = np.zeros(shape=(len(t),len(x)), dtype=np.complex128)
    for tt in tqdm(range(len(t))):
        if tt == 0:
            z = init(x)
            u[tt, :] = z
            v[tt, :] = np.zeros_like(z)
        elif tt == 1:
            u[tt,:] = u[0, :]
            v[tt,:] = v[0, :]
        else:
            for xx in range(len(x)):
                if xx == 0 or xx == len(x) - 1:
                    u[tt, xx] = 0
                    v[tt, xx] = 0
                else:
                    if VAR_MASS:
                        u[tt, xx] = u[tt-2, xx] - l*(v[tt-1, xx+1]-v[tt-1, xx-1])-1j*dt*u[tt-1, xx]*m(xx)
                        v[tt, xx] = v[tt-2, xx] - l*(u[tt-1, xx+1]-u[tt-1, xx-1])+1j*dt*v[tt-1, xx]*m(xx)
                    else:
                        u[tt, xx] = u[tt-2, xx] - l*(v[tt-1, xx+1]-v[tt-1, xx-1])-1j*dt*u[tt-1, xx]
                        v[tt, xx] = v[tt-2, xx] - l*(u[tt-1, xx+1]-u[tt-1, xx-1])+1j*dt*v[tt-1, xx]
    return u, v

PLOT_WF = False
VAR_MASS = False

t_min, t_max = 0, 100
x_min, x_max = -50, 50
sigma = 0.2
h, l = 0.1, 0.1
dx, dt = h, np.round(h*l, 8)

x = build_x(x_min, x_max, dx)
t = build_t(t_min, t_max, dt)
print("M: {0}, N:{1}".format(len(x), len(t)))
time.sleep(1)
 
u, v = LF(t, x, lambda x: init(x,sigma))

if PLOT_WF:
    chdir(path_2d)
    count = 0
    ymax = 1

    for zz in tqdm(range(0, len(u[:,0]), 50)):
        plot_u_v(zz, count)
        count += 1

    plot_u_v(-1, count)
else:
    p = P(u, v)
    j = J(u, v)

    chdir(path_2d)
    ymax = 1
    count = 0
    for jj in tqdm(range(0, len(j[:,0]), 50)):
        plot_p_j(jj, count)
        count += 1

    plot_p_j(-1, count)

gen_gif(path_2d, 'Dirac_2D.gif')