# Spark PySpark Word Counter

A Dockerized PySpark application for counting word frequencies in a PDF document

In this basic configuration, we will create the following:

1. A word_count.py script that list of words (top 10) that appear in a pdf document and the number of their occurence
2. A 3-node (1 master, 2 worker) spark cluster that runs in Docker

I ran these both on my local machine, but in theory, the driver and cluster can be on separate machines
