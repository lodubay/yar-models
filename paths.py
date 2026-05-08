"""
Exposes common paths useful for manipulating datasets and generating figures.
"""

from pathlib import Path

# Absolute path to the top level of the repository
root = Path(__file__).resolve().parents[0].absolute()
# root = Path(__file__).resolve().absolute()

# Folder containing multizone model outputs
outputs = root / 'outputs'

# Folder containing plots
plots = root / 'plots'

# Folder containing plotting styles
styles = root / 'styles'