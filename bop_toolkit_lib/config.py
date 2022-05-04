# Author: Tomas Hodan (hodantom@cmp.felk.cvut.cz)
# Center for Machine Perception, Czech Technical University in Prague
import os
from pathlib import Path
COSYPOSE_DIR = Path(os.environ['COSYPOSE_DIR'])

"""Configuration of the BOP Toolkit."""

######## Basic ########

# Folder with the BOP datasets.
if 'BOP_DATASETS_PATH' in os.environ:
    datasets_path = str(os.environ['BOP_DATASETS_PATH'])
else:
    datasets_path = str(COSYPOSE_DIR / 'local_data/bop_datasets')

if 'BOP_RESULTS_PATH' in os.environ:
    results_path = str(os.environ['BOP_RESULTS_PATH'])
else:
    results_path = str(COSYPOSE_DIR / 'local_data/bop_predictions_csv')

# Folder for the calculated pose errors and performance scores.
if 'BOP_EVAL_PATH' in os.environ:
    eval_path = str(os.environ['BOP_EVAL_PATH'])
else:
    eval_path = str(COSYPOSE_DIR / 'local_data/bop_eval_outputs')

######## Extended ########

# Folder for outputs (e.g. visualizations).
output_path = r'/path/to/output/folder'

# For offscreen C++ rendering: Path to the build folder of bop_renderer (github.com/thodan/bop_renderer).
bop_renderer_path = r'/path/to/bop_renderer/build'

# Executable of the MeshLab server.
meshlab_server_path = r'/path/to/meshlabserver.exe'
