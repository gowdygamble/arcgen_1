
# dont want to use negatives!
# adds an extra character...

# wait, why go back to a string at all...


START_SPECIAL_TOKENS = 10



START_PAIR = START_SPECIAL_TOKENS + 1
END_PAIR = START_SPECIAL_TOKENS + 2

ROW_BREAK = START_SPECIAL_TOKENS + 3
PAIR_LINK = START_SPECIAL_TOKENS + 4




def tokenize_sample(sample):
    # sample is a list of images (arrays)
    # every even element is an input
    # every odd element is an output
    # the last element is an input with no output!

    tokens = []
    for i in range(len(sample)):
        if i % 2 == 0:
            tokens.append(START_PAIR)
            tokens.extend(tokenize_single(sample[i]))
            tokens.append(PAIR_LINK)
        else:
            tokens.extend(tokenize_single(sample[i]))
            #tokens.append(END_PAIR)
    return tokens
    

def tokenize_single(single):
    # single is an array (list of lists) representing one image
    tokens = []
    for row in single:
        tokens.extend(row)
        tokens.append(ROW_BREAK)

    return tokens
    

# def example_pair_to_tokens(input, output):

#     tokens = [START_IMAGE]

#     for row in input:
#         r = [START_ROW]
#         for col in row:
#             r.append(col)
#         r.append(END_ROW)
#         tokens.extend(r)

#     tokens.append(END_IMAGE)
#     tokens.append(PAIR_LINK)
#     tokens.append(START_IMAGE)

#     for row in output:
#         r = [START_ROW]
#         for col in row:
#             r.append(col)
#         r.append(END_ROW)
#         tokens.extend(r)

#     tokens.append(END_IMAGE)

#     return tokens
