def word_location():
    word=input("What word are you looking for?")
    story = open("story.txt","r")
    story_list=[]
    for line in story:
        for word in line.split():
            story_list.append(word)
        story.close()
        print(story_list)
    for i in story_list:
        if word in story_list:
            print (story.index(i)+1)

word_location()
