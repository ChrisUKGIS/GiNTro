# Program to remove emoticons.

string_with_emoticons = "Oh, hai! Can I haz cheezeberger? :D :D"

emoticons = (":D", ":)", ":/", ":p", ";)")

#for i in range(len(emoticons)):
#    print("Fish tickle")
#    j = 0
#    while j<len(emoticons):
        
#        emoticon_start = string_with_emoticons.find(emoticons[i])
#        print(emoticon_start)
        
        # Find the start index of the current emoticon.
#        if (string_with_emoticons.find(emoticons[i])!= -1):
            
            # Use a slice to copy everything left of the emoticon.
#            substring_left = string_with_emoticons[: emoticon_start - 1]
        
            # Use a slide to copy everything right of the emoticon.
 #           substring_right = string_with_emoticons[emoticon_start + 2:]
    
            # Make a new string without the emoticon in it.
 #           string_with_emoticons = substring_left + substring_right
#        j+=1
            
 
for emoticon in emoticons:
    string_with_emoticons = string_with_emoticons.replace(emoticon, "")

print(string_with_emoticons)