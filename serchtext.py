def serch_word(cur_path,keywords,content,ch,exist,dist):
    counter =0

    if ch == "N":  
            for word in keywords:
                if word in content:
                 exist.append(cur_path)
                 a=cur_path.split('\\')
                 value= a[len(a)-1]
                 dist[word].append(value)
                else:
                 counter=counter+1
                 
    elif ch == "Y":
            for word in keywords:
                if word not in content:
                 counter=counter+1

            if counter == 0:
               allkey=""
               exist.append(cur_path)
               a=cur_path.split('\\')
               value=a[len(a)-1]
               for word in keywords:
                  allkey+=" "+word
               dist[allkey].append(value)

            elif counter!=0:
                 print()