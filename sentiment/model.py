from typing import Tuple
from transformers import pipeline


def get_sentiment_analysis(sentence: str) -> Tuple[str, float]:
    """Returns the sentiment analysis of a given sentence.

    Args:
        sentence (str): desired sentence to have an analysis

    Returns:
        str: Label of the analysis
        float: Score of the analysis
    """
    classifier = pipeline("sentiment-analysis")
    dict_answer = classifier(sentence)[0]

    return dict_answer["label"], dict_answer["score"]
