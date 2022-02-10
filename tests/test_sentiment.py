import pytest

from sentiment.model import get_sentiment_analysis

SENTENCES = ["I'm good", "I'm not good"]
LABELS = ["POSITIVE", "NEGATIVE"]


@pytest.mark.parametrize("sentence_labels", zip(SENTENCES, LABELS))
def test_get_sentiment_analysis_positive(sentence_labels):
    sentence, expected_label = sentence_labels
    label, score = get_sentiment_analysis(sentence)
    expected_score_above = 0.5
    assert label == expected_label, f"Expected: {expected_label}, got: {label}"
    assert (
        score > expected_score_above
    ), f"Expected: {expected_score_above}, got: {score}"
