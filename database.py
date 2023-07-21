def write_info(info):
    with open ("data.txt","a",encoding="utf-8") as file:
        file.write(info)
        
def find_info (char):
    with open ("data.txt","r",encoding="utf-8") as file:
        lst_sel=[]
        lst=file.readlines()
        count=0
        for line in lst:
            if char in line:
                count+=1
                lst_sel.append(line)
                print(f"{count}) {line.strip()}")
        return lst_sel
                

def change_data (old_data,new_data):
     with open ("data.txt","r",encoding="utf-8") as file: 
         lst_old=file.readlines()
     with open ("data.txt","w",encoding="utf-8") as file: 
         for line in lst_old:
            if old_data in line:
                file.write(new_data)
            else:
                file.write(line)
                
def view ():
    with open ("data.txt","r",encoding="utf-8") as file:
        print(file.read())
        
def delete_data(old_data):
     with open ("data.txt","r",encoding="utf-8") as file: 
         lst_old=file.readlines()
     with open ("data.txt","w",encoding="utf-8") as file: 
         for line in lst_old:
            if old_data in line:
               continue
            else:
               file.write(line)        