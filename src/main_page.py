import streamlit as st

st.set_page_config(layout="wide")

import numpy as np
import genome_browser as gb
from matplotlib import pyplot as plt

n = 105  # Length of random genomic interval.

g = gb.GenomeDiagram()

# Plot a density of random data, interpolated and filled.
track1 = gb.Graph("Random Density")
track1.new_graph(
    x=np.arange(n), y=np.abs(np.random.randn(n)), fmt="interpolate", fill=True
)

g.add_track(track1)

# Plot 9 random interval features (random start, length, orientation, and color).
track = gb.Feature("Random Intervals", height_ratio=0.4)
for _ in range(9):
    # Feature must follow iterable as (position, width, strand, color)
    track.add_feature(
        [
            np.random.randint(0, n - 15),
            np.random.randint(0, 20),
            np.random.choice(["+", "-", "none"]),
            np.random.choice(["#E74C3C", "#3498DB", "0.2"]),
        ]
    )

g.add_track(track)

# Annotate the figure with interval specific metadata. Will always appear in lower-right
g.annotation = "{}:{:,}-{:,}".format("chr3", 20000, 812383)

fig, axes = g.draw()

st.pyplot(fig)
