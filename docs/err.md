## CUDA Toolkit Error

```
Traceback (most recent call last):
  File "/home/qtn/Documents/GitHub/2d-gaussian-splatting/.venv/lib/python3.8/site-packages/torch/__init__.py", line 168, in _load_global_deps
    ctypes.CDLL(lib_path, mode=ctypes.RTLD_GLOBAL)
  File "/home/qtn/.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/ctypes/__init__.py", line 373, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: libcufft.so.10: cannot open shared object file: No such file or directory

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "train.py", line 13, in <module>
    import torch
  File "/home/qtn/Documents/GitHub/2d-gaussian-splatting/.venv/lib/python3.8/site-packages/torch/__init__.py", line 228, in <module>
    _load_global_deps()
  File "/home/qtn/Documents/GitHub/2d-gaussian-splatting/.venv/lib/python3.8/site-packages/torch/__init__.py", line 189, in _load_global_deps
    _preload_cuda_deps(lib_folder, lib_name)
  File "/home/qtn/Documents/GitHub/2d-gaussian-splatting/.venv/lib/python3.8/site-packages/torch/__init__.py", line 154, in _preload_cuda_deps
    raise ValueError(f"{lib_name} not found in the system path {sys.path}")
ValueError: libcublas.so.*[0-9] not found in the system path ['/home/qtn/Documents/GitHub/2d-gaussian-splatting', '/home/qtn/.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python38.zip', '/home/qtn/.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8', '/home/qtn/.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/lib-dynload', '/home/qtn/Documents/GitHub/2d-gaussian-splatting/.venv/lib/python3.8/site-packages', '__editable__.2d_gaussian_splatting-0.1.0.finder.__path_hook__']
Traceback (most recent call last):
  File "/home/qtn/Documents/GitHub/2d-gaussian-splatting/.venv/lib/python3.8/site-packages/torch/__init__.py", line 168, in _load_global_deps
    ctypes.CDLL(lib_path, mode=ctypes.RTLD_GLOBAL)
  File "/home/qtn/.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/ctypes/__init__.py", line 373, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: libcufft.so.10: cannot open shared object file: No such file or directory

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "render.py", line 12, in <module>
    import torch
  File "/home/qtn/Documents/GitHub/2d-gaussian-splatting/.venv/lib/python3.8/site-packages/torch/__init__.py", line 228, in <module>
    _load_global_deps()
  File "/home/qtn/Documents/GitHub/2d-gaussian-splatting/.venv/lib/python3.8/site-packages/torch/__init__.py", line 189, in _load_global_deps
    _preload_cuda_deps(lib_folder, lib_name)
  File "/home/qtn/Documents/GitHub/2d-gaussian-splatting/.venv/lib/python3.8/site-packages/torch/__init__.py", line 154, in _preload_cuda_deps
    raise ValueError(f"{lib_name} not found in the system path {sys.path}")
ValueError: libcublas.so.*[0-9] not found in the system path ['/home/qtn/Documents/GitHub/2d-gaussian-splatting', '/home/qtn/.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python38.zip', '/home/qtn/.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8', '/home/qtn/.local/share/uv/python/cpython-3.8.20-linux-x86_64-gnu/lib/python3.8/lib-dynload', '/home/qtn/Documents/GitHub/2d-gaussian-splatting/.venv/lib/python3.8/site-packages', '__editable__.2d_gaussian_splatting-0.1.0.finder.__path_hook__']
```

### Solution 1
1. Download the CUDA toolkit from [NVIDIA](https://developer.nvidia.com/cuda-downloads).
2. Install the CUDA toolkit to ~/local/cuda.
3. Add the following lines to your `~/.bashrc` file:
   ```bash
   export PATH=~/local/cuda/bin:$PATH
   export LD_LIBRARY_PATH=~/local/cuda/lib64:$LD_LIBRARY_PATH
   ```
4. Source the `~/.bashrc` file:
   ```bash
    source ~/.bashrc
    ``` 

eh didn't work

### Solution 2

install via pip (already added to pyproject.toml)
```bash
# Add site-packages to LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$VIRTUAL_ENV/lib/python3.8/site-packages/nvidia/cufft/lib:$LD_LIBRARY_PATH
```

got this error:
```
  × No solution found when resolving dependencies:
  ╰─▶ Because there is no version of nvidia-cuda-nvrtc-cu11{platform_machine == 'x86_64' and platform_system
      == 'Linux'}==11.7.99 and torch==2.0.0 depends on nvidia-cuda-nvrtc-cu11{platform_machine == 'x86_64'
      and platform_system == 'Linux'}==11.7.99, we can conclude that torch==2.0.0 cannot be used.
      And because torch was not found in the package registry and you require torch, we can conclude that
      your requirements are unsatisfiable.
```

it seems like i need

```
nvidia-cublas-cu12 nvidia-cudnn-cu12 nvidia-cufft-cu12 nvidia-curand-cu12 nvidia-cusolver-cu12 nvidia-cusparse-cu12
```

### Solution 3

- actually those nvidia-* packages are installed with torch
- i just need to `uv pip insstall torch` then `uv pip install -e . --no-build-isolation`