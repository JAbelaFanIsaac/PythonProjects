from matplotlib.pyplot import ylabel, plot, show, xlabel, title


def Regular():
    x = [2, 4, 6, 8, 10, 12]
    y = [2, 2, 2, 2, 2, 2]
    plot(x, y, 'b')
    xlabel('Inputs')
    ylabel('Steps')
    title('Constant Complexity')
    show()

def Linear():
    x = [2, 4, 6, 8, 10, 12]
    y = [2, 3, 4, 5, 6, 7]
    plot(x, y, 'b')
    xlabel('Inputs')
    ylabel('Steps')
    title('Linear Complexity')
    show()

def Log():
    x = [2, 4, 6, 8, 10, 12]
    y = [0.30, 0.60, 0.78, 0.90, 1, 1.08]
    plot(x, y, 'b')
    xlabel('Inputs')
    ylabel('Steps')
    title('Log Complexity')
    show()

def Quadratic():
    x = [2, 4, 6, 8, 10, 12]
    y = [4, 16, 36, 64, 100, 144]
    plot(x, y, 'b')
    xlabel('Inputs')
    ylabel('Steps')
    title('Quadratic Complexity')
    show()

def Exponential():
    x = [2, 4, 6, 8, 10, 12]
    y = [4, 16, 64, 256, 1024, 4096]
    plot(x, y, 'b')
    xlabel('Inputs')
    ylabel('Steps')
    title('Exponential Complexity')
    show()

def Factorial():
    x = [2, 4, 6, 8, 10, 12]
    y = [2, 24, 720, 40320, 3628800, 479001600]
    plot(x, y, 'b')
    xlabel('Inputs')
    ylabel('Steps')
    title('Factorial Complexity')
    show()
