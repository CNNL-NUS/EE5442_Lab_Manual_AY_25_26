import os
import gzip
import shutil
import subprocess

raw = './mnist/MNIST/raw'
os.makedirs(raw, exist_ok=True)

files = [
    'train-images-idx3-ubyte.gz',
    'train-labels-idx1-ubyte.gz',
    't10k-images-idx3-ubyte.gz',
    't10k-labels-idx1-ubyte.gz'
]

base_url = 'https://ossci-datasets.s3.amazonaws.com/mnist/'

print("Downloading MNIST files...", flush=True)
for f in files:
    out = os.path.join(raw, f)
    if os.path.exists(out) or os.path.exists(out[:-3]):
        print(f"Already exists, skipping: {f}", flush=True)
        continue
    print(f"Downloading {f}...", flush=True)
    subprocess.run(['wget', '-q', '--show-progress', base_url + f, '-O', out], check=True)

print("Unzipping...", flush=True)
for f in files:
    gz_path  = os.path.join(raw, f)
    out_path = os.path.join(raw, f[:-3])
    if os.path.exists(out_path):
        print(f"Already unzipped, skipping: {f[:-3]}", flush=True)
        continue
    with gzip.open(gz_path, 'rb') as f_in:
        with open(out_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    try:
        os.remove(gz_path)
    except FileNotFoundError:
        pass                         # already gone, no problem
    print(f"Done: {f[:-3]}", flush=True)

print("All files ready. Run cnn.py now.", flush=True)