monitor usage
-------------

+ depends on `python/2.7.13_sci_01`.
+ `monitor_usage.sh` calculates disk usages (in GB) for `/projects` and `/scratch` per user, and outputs `hitlist.csv`.
+ `plot_hitlist.py` plots `hitlist.csv`.
+ calculating disk usage is quite slow, and should be done sparingly. Also, it is best done as root.
