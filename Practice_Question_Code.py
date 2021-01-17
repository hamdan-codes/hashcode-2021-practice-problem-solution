
# coding: utf-8

# ## Google Hashcode 2021, Practice Problem
# ###       Even More Pizza
# 
# #### By <a href="https://chaudharyhamdan.me/">Chaudhary Hamdan </a>

# In[1]:


# Import of libraries
import os
import random


# In[2]:


# Reading file names in the Input directory 
files = os.listdir('Input_Files/')
l = len(files)

# Cleaning file names
for i in range(l):
    files[i] = files[i][:-3]


# In[3]:


# Function to compute and return Answers.
def solve(m,t2,t3,t4,ing,shuff):
    i,score = 0, 0
    
    # Shuffling Data to get optimized result
    random.shuffle(shuff)
    
    tt,ttt,tttt = [],[],[]
    
    # While we have some pizzas left
    while i < m:
        
        # If 2 member team is still left and we have pizza to deliver them
        if i+2 <= m and t2 > 0:
            t2 -= 2 # Updating after delivering it to a team
            tt.append([shuff[i],shuff[i+1]]) # Appending to the answer
            ss = len(set(ing[shuff[i]]+ing[shuff[i+1]])) # Unique Ingredients delivered
            i += 2 # 2 pizzas Delivered.
        
        elif i+3 <= m and t3 > 0:
            t3 -= 3
            ttt.append([shuff[i],shuff[i+1],shuff[i+2]])
            ss = len(set(ing[shuff[i]]+ing[shuff[i+1]]+ing[shuff[i+2]]))
            i += 3
        
        elif i+4 <= m and t4 > 0:
            t4 -= 4
            tttt.append([shuff[i],shuff[i+1],shuff[i+2],shuff[i+3]])
            ss = len(set(ing[shuff[i]]+ing[shuff[i+1]]+ing[shuff[i+2]]+ing[shuff[i+3]]))
            i += 4
        
        # If no team is left or we don't have sufficient pizzas, Break loop
        else:
            break
        
        # Score Calculation
        score += ss**2
        
    # Returning the vals computed
    return len(tt),len(ttt),len(tttt),tt,ttt,tttt,score 


# In[4]:



# Loop to iterate through all input files
for i in range(l):
    
    # Opening files
    with open('Input_Files/'+files[i]+'.in', 'r') as f:
        
        # Reading contents
        content = f.readlines()
        ingredients = []
        m, t2, t3, t4 = [int(x) for x in content[0].split()]
        for j in range(1,m+1):
            
            # Ingredients in the pizza
            ingredient = content[j].split()[1:]
            ingredients.append((ingredient))
    
    bestscore = 0
    besttwo,bestthree,bestfour = [],[],[]
    vals = list(range(m))
    
    # Get best score out of 1000 (increase for better answers) iterations.
    for _ in range(1000):
        l2,l3,l4,two,three,four,score = solve(m,2*t2,3*t3,4*t4,ingredients,vals)
        
        # Comparing with the best score till now.
        if score > bestscore:
            bestscore,besttwo,bestthree,bestfour = score,two,three,four

    # Writing the best results to output files in Output Directory.
    with open('Output_Files/'+files[i]+'.out', 'w') as f:
        f.write(str(l2+l3+l4)+'\n')
        
        # Writing in proper format as mentioned in the question
        for ii in range(l2):
            f.write('2 ')
            for j in range(2):
                f.write(str(besttwo[ii][j])+' ')
            f.write('\n')
        for ii in range(l3):
            f.write('3 ')
            for j in range(3):
                f.write(str(bestthree[ii][j])+' ')
            f.write('\n')
        for ii in range(l4):
            f.write('4 ')
            for j in range(4):
                f.write(str(bestfour[ii][j])+' ')
            f.write('\n')
    
    # Printing to Terminal to get the progress.
    print("Done ",files[i],"\nScore :",bestscore)
    
# Printing for 'THE END'.
print("All Done")


# ### Thank You
