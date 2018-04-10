def word_to_features(token, sent, no_embedding=False):
    loc = token.i
    sent_token_sum = len(sent)

    contain_upper_fn = lambda t: int(len([c for c in t.text if c.isupper()]) != 0)

    # current token feature
    features = {
        "len": len(token.text),
        "pos": token.pos_,
        "like_num": int(token.like_num),
        "is_quote": int(token.is_quote),
        "is_head": int(token.head.text == token.text),
        "is_digit": int(token.is_alpha),
        "is_upper": contain_upper_fn(token),
        "is_punct": int(token.is_punct),
        "is_end": int(loc == sent_token_sum - 1),
        "is_start": int(loc == 0)
    }

    # preceding  token's feature
    if loc > 0:
        prev_token = sent[loc - 1][0]
        features["prev:pos"] = prev_token.pos_
        features["prev:like_num"] = prev_token.like_num
        features["prev:is_quote"] = prev_token.is_quote
        features["prev:is_head"] = int(prev_token.head.text == prev_token.text)
        features["prev:is_upper"] = contain_upper_fn(prev_token)
        features["prev:is_punct"] = prev_token.is_punct

    # succeeding token's feature
    if loc != sent_token_sum - 1:
        next_token = sent[loc + 1][0]
        features["next:pos"] = next_token.pos_
        features["next:like_num"] = next_token.like_num
        features["next:is_quote"] = next_token.is_quote
        features["next:is_head"] = int(next_token.head.text == next_token.text)
        features["next:is_upper"] = contain_upper_fn(next_token)
        features["next:is_punct"] = next_token.is_punct

    if no_embedding:
        features["lemma"] = token.lemma_
    else:
        for n, dim_val in enumerate(token.vector):
            features["vector_dim_{}".format(n)] = dim_val
    return features


def sentence_to_features(sent, no_embedding=False):
    return [word_to_features(token, sent, no_embedding) for token, label in sent]


def sentence_to_labels(sent):
    return [label for token, label in sent]


def sentence_to_tokens(sent):
    return [token for token, label in sent]
