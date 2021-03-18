#!/usr/bin/python3
import os # os module allows us to manipulate our file system
  
# Function to rename multiple files 
def main(): 
    pwd = os.getcwd()
    for count, filename in enumerate(os.listdir(pwd)): 
        dst = "lesson"  + str(count) 
        src = pwd + "/" + filename
        dst = pwd + "/" + dst 

        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  

# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
