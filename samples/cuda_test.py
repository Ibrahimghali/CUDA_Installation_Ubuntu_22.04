from numba import cuda
import numpy as np

# Define a CUDA kernel
@cuda.jit
def hello_from_gpu():
    print("Hello from GPU!")

# Host code to run the kernel
def main():
    # Print initial memory usage
    gpu = cuda.get_current_device()
    print(f"Initial GPU memory used: {cuda.current_context().get_memory_info()[1]} bytes")

    print("Hello from CPU!")
    # Launch the kernel (1 block, 16 threads)
    hello_from_gpu[1, 16]()

    # Synchronize the device to make sure the kernel is done
    cuda.synchronize()

    # Print final memory usage
    print(f"Final GPU memory used: {cuda.current_context().get_memory_info()[1]} bytes")

if __name__ == "__main__":
    main()
