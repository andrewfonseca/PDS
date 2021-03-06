#!/usr/bin/python3.5
import numpy as np
import matplotlib.pyplot as plt
import math


def main():
    item_01()
    item_02()
    item_03()
    item_04()
    item_05()
    item_06()


def item_01():
    interval = [0, 32]

    n = np.arange(interval[0], interval[1] + 1, 1)
    x = np.cos(2 * np.pi * n / 16.)

    plt.figure(facecolor='w', figsize=(7, 7))

    plt.stem(n, x, 'k', linewidth=1.5)
    plt.axis([interval[0], interval[1], -1.1, 1.1])

    plt.grid()

    plt.title('Lab1-4.1' + '\n' + r'$x[n]=\cos \left[2\pi\frac{n}{16}\right]$', fontsize=18)

    plt.savefig("lab1_4.1.png", bbox_inches='tight', transparent=False)
    plt.show()
    plt.close('all')


def item_02():
    interval = [-50, 50]

    n = np.arange(interval[0], interval[1] + 1, 1)
    x = (10 / np.pi * n) * np.sin(np.pi * n / 10.)
    x[0] = 1

    plt.figure(facecolor='w', figsize=(7, 7))

    plt.stem(n, x, 'k', linewidth=1.5)
    plt.axis([interval[0], interval[1], -120, 150])

    plt.grid()

    plt.title('Lab1-4.2' + '\n' + r'$x[n]=\frac{10}{\pi n}\sin \left[\frac{\pi n}{10}\right], x[0]=1$', fontsize=18)

    plt.savefig("lab1_4.2.png", bbox_inches='tight', transparent=False)
    plt.show()
    plt.close('all')


def item_03():
    interval = [-15, 15]

    n = np.arange(interval[0], interval[1] + 1, 1)
    x = np.exp(-1 * np.abs(n / 3)) * np.cos(2 * np.pi * n / 2)

    plt.figure(facecolor='w', figsize=(7, 7))

    plt.stem(n, x, 'k', linewidth=1.5)
    plt.axis([interval[0], interval[1], -0.9, 1.3])

    plt.grid()

    plt.title('Lab1-4.3' + '\n' + r'$x[n]=e^{- \left |\frac{n}{3} \right |}\cos\left[2\pi\frac{n}{2} \right ]$', fontsize=20)

    plt.savefig("lab1_4.3.png", bbox_inches='tight', transparent=False)
    plt.show()
    plt.close('all')


def item_04():
    interval = [-50, 50]

    n = np.arange(interval[0], interval[1] + 1, 1)
    x = np.exp(-1 * np.abs(n / 10)) * np.sin(2 * np.pi * n / 20)

    plt.figure(facecolor='w', figsize=(7, 7))

    plt.stem(n, x, 'k', linewidth=1.5)
    plt.axis([interval[0], interval[1], -0.8, 0.8])

    plt.grid()

    plt.title('Lab1-4.4' + '\n' + r'$x[n]=e^{- \left |\frac{n}{10} \right |}\sin\left[2\pi\frac{n}{20} \right ]$', fontsize=20)

    plt.savefig("lab1_4.4.png", bbox_inches='tight', transparent=False)
    plt.show()
    plt.close('all')


def item_05():
    interval = [0, 200]

    n = np.arange(interval[0], interval[1] + 1, 1)
    x = (1 / 2) * (1 + np.cos(2 * np.pi * n / 100)) * np.cos(np.pi * n)

    plt.figure(facecolor='w', figsize=(7, 7))

    plt.stem(n, x, 'k', linewidth=1.5)
    plt.axis([interval[0], interval[1], -1.5, 1.5])

    plt.grid()

    plt.title('Lab1-4.5' + '\n' + r'$x[n]=\frac{1}{2}\left(1+\cos \left[2\pi\frac{n}{100}\right]\right)\cos (\pi n)$', fontsize=18)

    plt.savefig("lab1_4.5.png", bbox_inches='tight', transparent=False)
    plt.show()

    plt.close('all')


def item_06():
    interval = [-40, 40]

    n = np.arange(interval[0], interval[1] + 1, 1)
    x = np.cos((2 * np.pi / 20) * (50 + 10 * np.cos(2 * np.pi * n / 20)))

    plt.figure(facecolor='w', figsize=(7, 7))

    plt.stem(n, x, 'k', linewidth=1.5)
    plt.axis([interval[0], interval[1], -1.5, 1.5])

    plt.grid()

    plt.title('Lab1-4.6' + '\n' + r'$x[n]=\cos \left[\frac{2\pi}{20}\left(50+10\cos\left[\frac{2\pi n}{20}\right]\right)\right]$', fontsize=18)

    plt.savefig("lab1_4.6.png", bbox_inches='tight', transparent=False)
    plt.show()

    plt.close('all')


if __name__ == '__main__':
    main()
