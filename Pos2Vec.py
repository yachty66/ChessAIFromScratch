'''
1. 773–600–400–200–100.

need to get data for feeding into autoencoder

need to figure out how to implement autoencoder

1. Try to implement auto encoder till the point where i need data for them. before check what DBN's are 

run everything from here since this will help me to understand the functionality of python better 

i do not really understand the architecture. should I train an autoencoder and than using the result of the autoencoder somehow

try to create the 773-600-773 autoencoder
'''
import torch
import matplotlib.pyplot as plt

class AutoEncoder773(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
        self.encoder = torch.nn.Sequential(
            torch.nn(773),
            torch.nn.ReLU(),
            torch.nn(600),
            torch.nn.ReLU(),
            torch.nn(400),
            torch.nn.ReLU(),
            torch.nn(200),
            torch.nn.ReLU(),
            torch.nn(100),
        )

        self.decoder = torch.nn.Sequential(
            torch.nn(100),
            torch.nn.ReLU(),
            torch.nn(200),
            torch.nn.ReLU(),
            torch.nn(400),
            torch.nn.ReLU(),
            torch.nn(600),
            torch.nn.ReLU(),
            torch.nn(773)
        )