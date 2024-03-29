import warnings
from psd_tools import PSDImage

name = 'diwali'
# Open a PSD file
psd = PSDImage.open(r'psd/'+name+'.psd')

# Suppress all warnings globally
warnings.filterwarnings("ignore")

# Get the number of layers
num_layers = len(psd._layers)

layers = psd._layers

for i in range(10):
    print('')

for _layers in psd:
    if _layers.kind=='type':
        print(_layers.text)



# Output the number of layers
print("Number of layers:", num_layers)


for i in range(num_layers):
    print(f'layer {i} has:\nwidth= {layers[i].size[0]},  height={layers[i].size[1]}')
    
