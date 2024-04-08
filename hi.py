import requests
from bs4 import BeautifulSoup

def find(tag,attribute,name):
     abu=soup.find(f'{tag}',attrs={f'{attribute}': f'{name}'})
     print(abu.get_text())


def findall(tag,attribute,name):
     abu=soup.find_all(f'{tag}',attrs={f'{attribute}': f'{name}'})
     print(abu)
def text(name):
     abu=soup.find_all(string=f'{name}')
     print(f'{abu} quantity: {len(abu)}')

    
        

        
   

    
print('welcome to my webscraper!')
while True:
        url_input=input("Enter your URL:")
        if "https" not in url_input:
            print("invalid Input!")
            continue
        else:
            break
rq=requests.get(url_input)
soup =BeautifulSoup(rq.text,'html.parser')
start_input=input('Do you want to get the first data or the all data(first,all)').strip().lower()
while True:
    if start_input== 'all':
        initial_input=input('Does your search require a tag?(yes or no)')
        if initial_input=='yes':
            tag=input('Enter the tag you are searching for(without < >):').lower().strip()
            sec_input=input('which attribute do you want to find?(class,id,href,text)').lower().strip()
            if sec_input== 'class':
                
                attribute= 'class'

                
            elif sec_input=='id':
            
                attribute='id'
            elif sec_input=='href':
                attribute='href'
                
            elif sec_input=='text':
                attribute='text'
            name=input('enter the name of the id/class/link/text:').strip().lower()
            findall(tag,attribute,name)
            break
        if initial_input== 'no':
            name=input('enter the name of the text:').strip().lower()
            text(name)
            break
             
    elif start_input== 'first':
            
            tag=input('Enter the tag you are searching for(without < >):').lower().strip()
            sec_input=input('which attribute do you want to find?(class,id,href,text)').lower().strip()
            if sec_input== 'class':
                
                attribute= 'class'

                
            elif sec_input=='id':
            
                attribute='id'
            elif sec_input=='href':
                attribute='href'
                
            elif sec_input=='text':
                attribute='text'
            name=input('enter the name of the id/class/link/text:')
            findall(tag,attribute,name)
         
             
    else:
        continue
        
             