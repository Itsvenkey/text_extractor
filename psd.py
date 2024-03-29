

from psd_tools import PSDImage


#name of the psd file present in the directory psd
name = 'diwali'

# Open a PSD file
psd = PSDImage.open(r'psd/'+name+'.psd')

# Get the number of layers
num_layers = len(psd._layers)

layers = psd._layers
# this loop is just to create a space between the warning and the actual output
for i in range(10):
    print('')

# Output the number of layers
print("Number of layers:", num_layers,end='\n\n')


#this gives the resolutions of each layer
for i in range(num_layers):
    print(f'layer {i+1} has: width= {layers[i].size[0]}, height={layers[i].size[1]}',end='\n\n')

#this is to print the text from each layer
for _layers in psd:
    if _layers.kind=='type':
        print(_layers.text)






    
