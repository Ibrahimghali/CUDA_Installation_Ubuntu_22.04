# CUDA Installation Guide for Ubuntu 22.04

This guide walks you through the steps to install NVIDIA's CUDA toolkit on Ubuntu 22.04. CUDA allows you to harness the power of NVIDIA GPUs for computing-intensive tasks like machine learning, simulations, and more.

## Prerequisites
- A machine running Ubuntu 22.04
- A CUDA-compatible NVIDIA GPU

## Steps

### 1. Update Your System
Update and upgrade your system packages:
```bash
sudo apt update && sudo apt upgrade
```

### 2. Install the NVIDIA Driver
Identify and install the recommended NVIDIA driver for your GPU:
```bash
sudo ubuntu-drivers devices
sudo apt install nvidia-driver-<version>  # Replace <version> with your recommended driver
```

Reboot your machine:
```bash
sudo reboot
```
### Verify NVIDIA Driver Installation
To verify that the NVIDIA driver is installed correctly, run the following command:
```bash
nvidia-smi
```

You should see an output similar to the following, which indicates that the driver is installed and the GPU is recognized:

![NVIDIA-SMI Output](/rsrc/image.png)


### 3. Install CUDA Toolkit
1. Download and install the CUDA repository package:
   ```bash
   wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
   sudo dpkg -i cuda-keyring_1.1-1_all.deb
   sudo apt-get update
   sudo apt-get install -y cuda
   ```

### 4. Set Up the Environment
Update your environment variables by adding the following lines to your `.bashrc`:
```bash
export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-12.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```

Reload the `.bashrc` file:
```bash
source ~/.bashrc
```

Reboot your machine:
```bash
sudo reboot
```

### 5. Verify Installation
After installation, check if CUDA was installed correctly:
```bash
nvcc -V
```

## Further Information
For detailed instructions, see the official [NVIDIA CUDA Toolkit Documentation](https://docs.nvidia.com/cuda/).
