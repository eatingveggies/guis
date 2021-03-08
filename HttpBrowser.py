import requests 

#r = requests.get('https://redpandazine.com/2016/01/28/red-panda-pet') # make a request
# This creates a response objects

#print (r) # Will tell us the response type
#print(help(r)) # Shows us how we can interact with this
#print(r.text)


#####################################################
# Download an image 
r1 = requests.get('http://www.storytrender.com/wp-content/uploads/2019/04/28_CATERS_Pug_has_rolls_003-968x1024.jpg')

FILENAME = 'Pugs.gif'
with open(FILENAME,'wb') as f:
    f.write(r1.content)