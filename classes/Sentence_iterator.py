import xmltodict

from classes.Bio_labeller import get_bio


def iterate_sentence(path, nlp):
    with open(path) as f:
        dataset_parsed = xmltodict.parse(f.read(), strip_whitespace=False)

    for sentence in dataset_parsed["sentences"]["sentence"]:
        sentence_id = sentence["@id"]
        sentence_text = sentence["text"]

        aspect_info = []
        all_terms = sentence.get("aspectTerms", {}).get("aspectTerm", [])
        if type(all_terms) is not list:
            all_terms = [all_terms]
        for aspect_term in all_terms:
            # Extracting relevant terms for the analysis
            term = aspect_term["@term"]
            index_loc_from = int(aspect_term["@from"])
            index_loc_to = int(aspect_term["@to"])
            aspect_info.append((index_loc_from, index_loc_to, term))

        # nlp tokenizes the sentence into tokens
        sentence_tokens = list(nlp(sentence_text))
        labels = get_bio(sentence_tokens, aspect_info)

        yield sentence_tokens, sentence_id, sentence_text, aspect_info, labels
