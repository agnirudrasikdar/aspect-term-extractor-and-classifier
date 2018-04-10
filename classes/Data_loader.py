import pandas as pd

from classes.Sentence_iterator import iterate_sentence


def load_data(path, nlp):
    features_df = {
        "id": [],
        "text": [],
        "all_aspects": [],
        "token": [],
        "label": []
    }

    for sentence_tokens, sentence_id, sentence_text, aspect_info, labels in iterate_sentence(path, nlp):
        for n, t in enumerate(sentence_tokens):
            features_df["id"].append(sentence_id)
            features_df["text"].append(sentence_text)
            features_df["all_aspects"].append([a[-1] for a in aspect_info])
            features_df["token"].append(t)
            features_df["label"].append(labels[n])

    return pd.DataFrame(features_df)[["id", "token", "label", "all_aspects", "text"]]



