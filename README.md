# Spark PySpark Word Counter

A Dockerized PySpark application for counting word frequencies in a PDF document

In this basic configuration, we will create the following:

1. A word_count.py script that counts numbers 1–1000 but in a parallelized operation (the Driver/client).
2. A 2-node (1 master, 1 worker) spark cluster that runs in Docker

I ran these both on my local machine, but in theory, the driver and cluster can be on separate machines
