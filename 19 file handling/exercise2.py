with open('exercise_file2.html','r') as rf:
    with open('all_links.txt','a') as wf:
        for line in rf.readlines():
            if "<a href=" in line:
                pos = line.find("<a href=")
                first_quote = line.find('\"',pos)
                second_quote= line.find('\"',first_quote+1)
                url = line[first_quote+1:second_quote]
                wf.write(url + '\n')