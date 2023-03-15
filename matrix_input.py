import numpy as np 
import torch
import torch.nn as nn





colors = 10
img_size = 12
max_img_size = 20
batch_size = 8
max_examples = 3


z = np.random.randint(0, colors, size=(batch_size, max_examples*2, max_img_size, max_img_size))

#print(z.shape)
#print(z)

def pad_input(input, max_size = 30):
    padded_input = np.zeros((max_size, max_size), dtype=np.int8)
    r, c = input.shape
    padded_input[:r,:c] = input 
    return padded_input

#x = pad_input(z, max_size=20)
#print(x.shape)
#print(x)
x = torch.tensor(z, dtype=torch.long)
print(x.shape)


batch = torch.flatten(x, -2, -1)

print(batch.shape)


input_T = batch.shape[-1]
emb_dim = 128

token_embedding_table = nn.Embedding(input_T, emb_dim)

# add learned positional embedding

xEmb = token_embedding_table(batch)
print("batch embedded:", xEmb.shape)


print("examples concatenated:")
z = torch.flatten(xEmb, 1, 2)
print(z.shape)


# how to handle this input in ARCFormer
'''
going to be passing in a batch
of stacks of examples (IO pairs)
and one input-only 'prompt'

so thats BATCH_SIZE * MAX_EXAMPLES * IMAGE_DIM_1 * IMAGE_DIM_2 * 1

basically want to get the whole stack of images down to a single sequences

what would it look like for one image?
maybe each pixel gets embedded (but it should be based on its neighbors...)

I dont want to treat the examples in the stack as channels of an image
will lose the meaning
the pairing between IO/IO/IO 



'''