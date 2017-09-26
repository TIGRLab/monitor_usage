#!/usr/bin/env python
import os, sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')   # Force matplotlib to not use any Xwindows backend
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

f, ax = plt.subplots(figsize=(8, 15))
db = pd.read_csv('hitlist.csv').sort_values("total", ascending=False)
sns.set_color_codes("pastel")
sns.barplot(x="total", y="username", data=db, label="Total", color="b")

# Plot the crashes where alcohol was involved
sns.set_color_codes("muted")
sns.barplot(x="projects", y="username", data=db, label="Projects", color="b")

# Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(ylabel="", xlabel="Filesystem usage (projects + scratch) in GB")
sns.despine(left=True, bottom=True)
sns.plt.savefig('hitlist.pdf')
