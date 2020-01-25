

# author: Kingsley H.Y. Huang
#2020-01-25


# ver. A2:
#   leave small jpg files untouched;
#   establish inbox/outbox
import os,string,   sys  
import urllib,re, socket
from PIL import Image
import zipfile
import subprocess


def dezip(filename, tempFolderName='tempfolder'):
     
    try:
        for root, dirs, files in os.walk(tempFolderName, topdown=False):
            for name in files:
                #print('remove',root,name)
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(tempFolderName)
        print(tempFolderName ,': ground cleared. Extracting...')
    except:
        print(tempFolderName ,': ground cleared weird. Extracting...')

    subprocess.call('copy "' + filename+'" temp.zip',shell=True)
    zip_ori = zipfile.ZipFile('temp.zip', 'r')
    zip_ori.extractall(tempFolderName)
    zip_ori.close()
    subprocess.call('del temp.zip', shell=True)
    print('Extraction completed.')
    return 0

def comp_img(filename):    
    return Image.open(filename)

def walk_img(startdir, minSize=10240):    

    files = os.listdir(startdir)       
    print('starting:',startdir)
    for root, dirs, files in os.walk(startdir):
        print(root, len(files),' elements')
        for file in files:   
            filename=os.path.join(root,file)
            if os.path.isfile(filename)==False:
                    continue   
             
            if len(file)>=4:
                if file[-4:] == '.jpg':
                    #print("jpg found:",filename)
                    #print(os.stat( filename ).st_size)

                    if  os.stat( filename ).st_size > minSize:                            
                        newImg= comp_img(filename)
                        newImg.save(filename, 'JPEG',  quality=20)
                        print('>', end='')
                    else:
                        print('_', end='')
                    
def zipepub(oriname,epubpath,startdir='outbox'):
    newname='de_'+oriname
    myzip=zipfile.ZipFile(os.path.join(epubpath,newname), 'w') 
    for root, dirs, files in os.walk(startdir):
        for file in files:       
            myzip.write(os.path.join(root,file))
    myzip.close()        
    return newname

def job(epubname,epubdir='',newepubdir='outbox',tempFolderName='tempfolder'):
    oldsize=os.stat( os.path.join(epubdir,epubname)).st_size 
    print('/n/n',epubname,'at path ',epubdir,'/n original size:', oldsize)
    dezip(os.path.join(epubdir,epubname))
    startdir = os.path.join(os.curdir, tempFolderName)
    walk_img(startdir)
    
    newname=zipepub(epubname,newepubdir,startdir)
    newsize=os.stat( os.path.join(newepubdir,newname)).st_size
    print('/n new size:',newsize, ' ratio =',oldsize/newsize)
    return 0

if __name__=='__main__':
    #default='temp.epub'
    res=[]
    inbox_path='inbox'
    for root, dirs, files in os.walk(inbox_path, topdown=False):
        for name in files:
            if len(name)>=5:
                if name[-5:]=='.epub':
                     res.append([root, name])
    print(res)
    confirm=input('Do jobs on them?(y/n)')
    if confirm in ['y','Y']:
        for [root,name] in res:
            job(name,root)
             
    

