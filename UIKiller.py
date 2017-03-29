import os,sys,re
dict={}
basedir=sys.argv[1]

sizearray=['mdpi','hdpi','xhdpi','xxhdpi','xxxhdpi']
dirlist=os.listdir(basedir)
filelist = []
def lowertranslate(filedirpath,filename):
    if filename.islower():
        pass
    else:
        os.rename(os.path.join(filedirpath, filename), os.path.join(filedirpath, filename.lower()))
        print("小写了"+filename)
def removeInvisiable(fileddirpath,filename):
    if filename.startswith('.'):
        fileorpath=os.path.join(fileddirpath,filename)
        if os.path.isdir(fileorpath):
            os.removedirs(fileorpath)
        else:
            os.remove(fileorpath)
        print("删了"+filename)
def replacemidline(fileddirpath,filename):
        oldname=filename;
        newname=filename.replace('-','_')
        if oldname!=newname:
            print("横线匹配了" + filename)
            os.rename(os.path.join(fileddirpath, filename), os.path.join(filedirpath, newname))


def dorename(num):
    strwhole=filelist[num]
    type="drawable"
    oldname=""
    extend=''
    print("待命名文件"+strwhole)
    newname=input("请输入新名字")
    newname=newname.lower().replace('-','_')
    strarray=re.split('/|\\|.|-',strwhole)
    if strarray[0].endswith("mipmap"):
        type="mipmap"
    if len(strarray)<=2:
        oldname=strarray[1]
        strtemp=os.path.join(basedir,type)
        os.rename(os.path.join(strtemp,oldname),os.path.join(strtemp,newname))
    else:
        oldname = strarray[2]
        strtemp=os.path.join(basedir,type+'-'+strarray[1])
        os.rename(os.path.join(strtemp,oldname),os.path.join(strtemp,newname))
        extend=strarray[1]
    for sizeextend in sizearray:
        if sizeextend==extend:
            continue
        pathsearch=os.path.join(basedir,type+"-"+sizeextend)
        if(len(strarray)>2):
            filesearch=os.path.join(pathsearch,oldname)
        else:
            filesearch=os.path.join(pathsearch,oldname)
        if os.path.isfile(filesearch):
            os.rename(filesearch,os.path.join(pathsearch,newname))
    print(strarray)

def listtorename():
    index=0
    for singledir in dict.keys():
        for filedetail in dict[singledir]:
            strshow=str(index)+'.'+os.path.join(singledir,filedetail)
            filelist.append(strshow)
            print(strshow)
            index=index+1
    strnum=input("请输入待命名的序号")
    num=int(strnum)
    if num in range(len(filelist)):
        dorename(num)
    else:
        print("请输入合法数值")

for singledir in dirlist:
    if singledir.startswith('mipmap')|singledir.startswith('drawable'):
        filedirpath=os.path.join(basedir,singledir)
        for filename in os.listdir(filedirpath):
            removeInvisiable(filedirpath,filename)
        for filename in os.listdir(filedirpath):
            lowertranslate(filedirpath, filename)
            replacemidline(filedirpath, filename)
        dict[singledir]=os.listdir(filedirpath)
listtorename()