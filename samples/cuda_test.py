from numba import cuda
import numpy as np

# Define a CUDA kernel
@cuda.jit
def hello_from_gpu():
    print("Hello from GPU!")

# Host code to run the kernel
def main():
    print("Hello from CPU!")
    # Launch the kernel (1 block, 1 thread)
    hello_from_gpu[1, 1]()

if __name__ == "__main__":
    main()
