def get_bio(tokens, aspect_term_info, verbose=False):
    if len(aspect_term_info) == 0:
        aspect_term_info = [(float("inf"), -1, "None")]
    aspect_term_info = sorted(aspect_term_info)
    labelled_term = []
    aspect_from, aspect_to, aspect_term = aspect_term_info.pop(0)

    for t in tokens:
        t_from = t.idx
        t_to = t_from + len(t.text)

        if t_from == aspect_from:
            current_label = "B"
        elif t_from > aspect_from and t_to <= aspect_to:
            current_label = "I"
        else:
            current_label = "O"
        labelled_term.append(current_label)

        if verbose:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(t_from, t_to, aspect_from, aspect_to, t.text, current_label,
                                                      aspect_term))

        # after finishing the current aspect term, it traverses to the next term
        if t_to >= aspect_to:
            if len(aspect_term_info) == 0:
                aspect_from, aspect_to, aspect_term = (float("inf"), -1, "None")
            else:
                aspect_from, aspect_to, aspect_term = aspect_term_info.pop(0)
    if len(aspect_term_info) != 0:
        raise ValueError("Aspect terms are missing \n\t{} \n\n\t{} \n\n\t".format(aspect_term_info, tokens, labelled_term))
    return labelled_term
