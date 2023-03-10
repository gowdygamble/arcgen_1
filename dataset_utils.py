



START_ROW = -1
END_ROW = -2

START_IMAGE = -3
END_IMAGE = -4

#START_PAIR = -5
#END_PAIR
PAIR_LINK = -5

#START_EXAMPLES
#END_EXAMPLES

#START_INFERENCE
#END_INFERENCE


def example_pair_to_tokens(input, output):

    tokens = [START_IMAGE]

    for row in input:
        r = [START_ROW]
        for col in row:
            r.append(col)
        r.append(END_ROW)
        tokens.extend(r)

    tokens.append(END_IMAGE)
    tokens.append(PAIR_LINK)
    tokens.append(START_IMAGE)

    for row in output:
        r = [START_ROW]
        for col in row:
            r.append(col)
        r.append(END_ROW)
        tokens.extend(r)

    tokens.append(END_IMAGE)

    return tokens
