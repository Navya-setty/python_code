#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open(r"C:\Users\Navya Pillarisetty\Downloads\Night_Changes_Lyrics.txt","a") as song:
    song.write("\nEnd of the song")
    song.close()


# In[29]:



try: 
    with open(r"C:\Users\Navya Pillarisetty\Downloads\Night_Changes_Lyrics.txt","r") as song:
        
        for j,i in enumerate(song):
            if j==0:
                i= i.upper()
                print("The name of the song is: ",i)
            if i=="End of the song":
                break
            if i== i.upper():
                print("#"*10,"Well this line refers to the band","#"*10)
                print(i)
            line_number= j
            if j>=2:
                print("The line number is: ",j+1)
                print("The line of the lyrics is: ",i)
                word= i.split(" ")
                cnt= len(word)            
                print("*"*10,"The number of words in each sentence are: ",cnt,"*"*10)
                number_of_characters= 0
                for f in i:
                    number_of_characters+=1
                print("The number of characters in each line are: ",number_of_characters)
                print("-"*80)
                
except Exception as e:
    print(f"File is not available, please give correct file: {e}")
else:
    print("Code is successful")


# In[ ]:




