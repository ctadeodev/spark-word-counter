import re

from PyPDF2 import PdfReader
from pyspark.sql import SparkSession


def read_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text


def parse_words(text):
    text = re.sub(r'\W+', ' ', text)
    return text.lower().split()


def count_words(pdf_path):
    spark = SparkSession.builder \
        .appName("PDF Word Count") \
        .master("spark://localhost:7077") \
        .getOrCreate()

    text = read_pdf(pdf_path)
    words = parse_words(text)
    print(f'Total input word count: {len(words)}')

    words_rdd = spark.sparkContext.parallelize(words)
    # Map each word to (word, 1), reduce by key to get word counts, and collect results
    word_counts = words_rdd.map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b) \
        .collect()

    print(f'Total output word count: {sum([x[1] for x in word_counts])}')
    word_counts = sorted(word_counts, key=lambda x: x[1], reverse=True)
    n = 10
    print(f'Top {n} words:')
    for idx, (word, count) in enumerate(word_counts[:n]):
        print(f" {idx + 1}: {word}: {count}")

    spark.stop()


if __name__ == '__main__':
    count_words('zen-of-python.pdf')
