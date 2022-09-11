import re
gygygy = input("What file do you want to open?")
pythoncode = []
elifarray = []
elifvariable = []
elifinsert = []
elifinsert2 = []

def codeindent(line):
  spaces = 0
  for i in pythoncode[line]:
    if i == ' ':
      spaces = spaces + 1
    else:
      break
  return(spaces)

def endinsert(line,endstatement):
  currentline = line + 1
  spaces = codeindent(line)
  startspaces = spaces
  while codeindent(currentline) > spaces or ('else' in pythoncode[currentline] or 'elif' in pythoncode[currentline]) and codeindent(currentline) == spaces:
    currentline = currentline + 1
    if len(pythoncode) == currentline:
      break
  z = (" "*startspaces+endstatement)
  pythoncode.insert(currentline,z)



PythonFile = open(gygygy)
for line in PythonFile:
   line = line.strip('\n')
   pythoncode.append(line)


def eliffind(codelength):
  for i in range(0,codelength):
    string = []
    if 'elif' in pythoncode[i]:
      elifarray.append(i)
  return(elifarray)

def elifinsertfind(codelength1):
  for i in range(0,codelength1):
    for j in range(elifarray[i],0,-1):
      print(elifarray[i])
      print('j',j)
      if 'IF' in pythoncode[j] and 'elif' not in pythoncode[j] and 'ENDIF' not in pythoncode[j]:
        elifinsert.append(j)
        break
  return(elifinsert)

def elifinsert2find(codelength1):
  for i in range(0,codelength1):
    for j in range(elifarray[i],len(pythoncode)):
      if 'ELSE' in pythoncode[j]:
        elifinsert2.append(j)
        break
  return(elifinsert2)

def removespaces(line,variable):
  string = ''
  stringarray = [char for char in variable]
  for i in range(0,len(stringarray)):
    if stringarray[i] == ' ':
      stringarray[i] = ''
    else:
      break
  print(stringarray)
  for i in range(0,len(stringarray)):
    string = string+stringarray[i]
  return(string)
      

for i in range(0,len(pythoncode)):
  if '_' in pythoncode[i]:
    pythoncode[i] = pythoncode[i].replace('_','')
  if '%' in pythoncode[i]:
    pythoncode[i] = pythoncode[i].replace('%',' MOD ')
  if '!=' in pythoncode[i]:
    pythoncode[i] = pythoncode[i].replace('!=','<>')

for i in range(0,len(pythoncode)):
  if '=' in pythoncode[i]:
    if '==' in pythoncode[i]:
      pythoncode[i] = pythoncode[i].replace('==','=')
    elif ' = ' in pythoncode[i]:
      pythoncode[i] = pythoncode[i].replace(' = ','<-')

i = 0
while i < len(pythoncode):
  if 'if' in pythoncode[i] and 'elif' not in pythoncode[i] and i not in elifinsert:
    pythoncode[i] = pythoncode[i].replace('if','IF')
    pythoncode[i] = pythoncode[i].replace(':','')
    endinsert(i,"ENDIF")
    ifspaces = codeindent(i)
    z = (" "*(ifspaces+1)+"THEN")
    pythoncode.insert(i+1,z)
  if 'else' in pythoncode[i] and i not in elifinsert2:
    pythoncode[i] = pythoncode[i].replace('else:','ELSE')
  i = i + 1

for i in range(0,len(pythoncode)):
  if ' int(' in pythoncode[i] and 'integer' not in pythoncode[i]:
    pythoncode[i] = pythoncode[i].replace('int','STRING_TO_NUM')
  if ' str(' in pythoncode[i] and 'string' not in pythoncode[i]:
    pythoncode[i] = pythoncode[i].replace('str','NUM_TO_STRING')

i = 0
while i < len(pythoncode):
  if 'print(' in pythoncode[i]:
    pythoncode[i] = pythoncode[i].replace('print','OUTPUT ')
    pythoncode[i] = pythoncode[i].replace('(','')
    pythoncode[i] = pythoncode[i].replace(')','')

  if 'input(' in pythoncode[i]:
    newstring1 = pythoncode[i].split('input(',1)[-1]
    print(newstring1)
    newstring1 = newstring1.replace(')','')
    if len(newstring1) > 0:
      newstring1 = 'OUTPUT '+newstring1
      newstring1 = (' '*codeindent(i)+newstring1)
      pythoncode.insert(i,newstring1)
      i = i + 1
    newstring2 = pythoncode[i].split('<-')[0]
    newstring2 = newstring2.replace(' ','')
    newstring2 = 'INPUT '+newstring2
    newstring2 = (' '*codeindent(i)+newstring2)
    pythoncode.insert(i,newstring2)
    if 'int' in pythoncode[i+1]:
      newstring2 = newstring2.replace('INPUT ','')
      newstring2 = removespaces(i,newstring2)
      newstring3 = newstring2+' <- STRING_TO_NUM('+newstring2+')'
      print('newstring3',newstring3)
      newstring3 = (' '*codeindent(i-1)+newstring3)
      pythoncode.insert(i+1,newstring3)
      i = i + 1
    print('pythoncode',pythoncode[i+1])
    del(pythoncode[i+1])
  i = i + 1

i = 0
while i < len(pythoncode):
  if 'for' in pythoncode[i]:
    pythoncode[i] = pythoncode[i].replace('for','FOR')
    if re.search('[0-9]{1},[0-9]{1,3}',pythoncode[i]):
      pythoncode[i] = pythoncode[i].replace('in range(','<-')
      pythoncode[i] = pythoncode[i].replace(',',' TO ')
      pythoncode[i] = pythoncode[i].replace('):','')
      if re.search(r'TO \d+ TO',pythoncode[i]):
        looparray = pythoncode[i].split()
        looparray[5] = 'STEP'
        forstring = ''
        for j in range(0,len(looparray)):
          forstring = forstring+looparray[j]+' '
        pythoncode[i] = ' '*codeindent(i)+forstring
      endinsert(i,'NEXT')
    elif re.search('[0-9]{1}',pythoncode[i]):
      pythoncode[i] = pythoncode[i].replace('in range(','<- 0 TO')
      pythoncode[i] = pythoncode[i].replace('):','')
      endinsert(i,'NEXT')
  i = i + 1

i = 0
while i < len(pythoncode):
  if 'break' in pythoncode[i]:
    print(pythoncode[i-2])
    pythoncode[i-2] = pythoncode[i-2].replace(':','')
    pythoncode[i-2] = pythoncode[i-2].replace(' ','')
    pythoncode[i-2] = pythoncode[i-2].replace('IF','UNTIL ')
    del(pythoncode[i-1])
    del(pythoncode[i])
    for j in range(i-2,0,-1):
      if 'while True:' in pythoncode[j]:
        print(pythoncode[j])
        print(j)
        pythoncode[j] = pythoncode[j].replace('while True:','REPEAT')
        z = (' '*(codeindent(j))+pythoncode[i-2])
        print(codeindent(j))
        pythoncode[i-2] = z
        break
  i = i + 1

i = 0
while i < len(pythoncode):
  if '  break' in pythoncode[i]:
    del(pythoncode[i])
  i = i + 1

i = 0
while i < len(pythoncode):
  if 'while ' in pythoncode[i]:
    pythoncode[i] = pythoncode[i].replace('while','WHILE')
    pythoncode[i] = pythoncode[i].replace(':',' DO')
    endinsert(i,'ENDWHILE')
  i = i + 1

elifarray = eliffind(len(pythoncode))
elifinsert = elifinsertfind(len(elifarray))
elifinsert2 = elifinsert2find(len(elifarray))
for i in range(0,len(elifarray)):
  pythoncode[elifinsert[i]] = pythoncode[elifinsert[i]].replace('IF','CASE OF')
  if ' = ' in pythoncode[elifinsert[i]]:
    caseofvariable = pythoncode[elifinsert[i]].split('=')[0]
    caseofvariable2 = pythoncode[elifinsert[i]].split('= ')[1]
    caseofvariable2 = (' '*(codeindent(elifinsert[i])+1)+caseofvariable2+':')
    pythoncode[elifinsert[i]+2] = pythoncode[elifinsert[i]+2].split()
    for j in range(0,len(pythoncode[elifinsert[i]+2])):
      caseofvariable2 = caseofvariable2+' '+pythoncode[elifinsert[i]+2][j]
    pythoncode[elifinsert[i]] = caseofvariable
    pythoncode[elifinsert[i]+1] = caseofvariable2
  elif '>' in pythoncode[elifinsert[i]]:
    caseofvariable = pythoncode[elifinsert[i]].split('>')[0]
    caseofvariable2 = pythoncode[elifinsert[i]].split('>')[1]
    caseofvariable2 = (' '*(codeindent(elifinsert[i])+1)+'>'+caseofvariable2+':')
    pythoncode[elifinsert[i]+2] = pythoncode[elifinsert[i]+2].split()
    for j in range(0,len(pythoncode[elifinsert[i]+2])):
      caseofvariable2 = caseofvariable2+' '+pythoncode[elifinsert[i]+2][j]
    pythoncode[elifinsert[i]] = caseofvariable
    pythoncode[elifinsert[i]+1] = caseofvariable2
  elif '<' in pythoncode[elifinsert[i]]:
    caseofvariable = pythoncode[elifinsert[i]].split('<')[0]
    caseofvariable2 = pythoncode[elifinsert[i]].split('<')[1]
    caseofvariable2 = (' '*(codeindent(elifinsert[i])+1)+'<'+caseofvariable2+':')
    pythoncode[elifinsert[i]+2] = pythoncode[elifinsert[i]+2].split()
    for j in range(0,len(pythoncode[elifinsert[i]+2])):
      caseofvariable2 = caseofvariable2+' '+pythoncode[elifinsert[i]+2][j]
    pythoncode[elifinsert[i]] = caseofvariable
    pythoncode[elifinsert[i]+1] = caseofvariable2

for i in range(0,len(elifarray)):
  elifvariable = pythoncode[elifarray[i]].replace('elif ','')
  openspaces = codeindent(elifarray[i]+1)
  elifvariable = elifvariable+' '+pythoncode[elifarray[i]+1][openspaces:]
  openspaces1 = codeindent(elifarray[i]-2)
  elifvariable = removespaces(elifarray[i],elifvariable)
  elifvariable = (' '*openspaces1+elifvariable)
  pythoncode[elifarray[i]] = elifvariable
  pythoncode[elifarray[i]+1] = pythoncode[elifarray[i]+1].split()

i = 0
while i < len(pythoncode):
  print(elifarray)
  print(elifinsert)
  print(elifinsert2)
  print(pythoncode[i],i)
  i = i + 1

for i in range(0,len(elifinsert2)):
  print('i',i)
  if elifinsert2[i] == elifinsert2[i-1]:
    i = i
  else:
    elsevariable = pythoncode[elifinsert2[i]].replace('ELSE','OTHERWISE')
    openspaces = codeindent(elifinsert2[i]+1)
    print('elsevariable',elsevariable)
    print(pythoncode[elifinsert2[i]+1][openspaces:])
    elsevariable = elsevariable+' '+pythoncode[elifinsert2[i]+1][openspaces:]
    print(elsevariable)
    openspaces1 = codeindent(elifinsert2[i]-2)
    elsevariable = removespaces(elifinsert2[i],elsevariable)
    print(elsevariable)
    elsevariable = (' '*openspaces1+elsevariable)
    pythoncode[elifinsert2[i]] = elsevariable
    pythoncode[elifinsert2[i]+1] = pythoncode[elifinsert2[i]+1].split()
    pythoncode[elifinsert2[i]+2] = pythoncode[elifinsert2[i]+2].replace('ENDIF','ENDCASE')

while i < len(pythoncode):
  if type(pythoncode[i]).__name__ == 'list':
    del(pythoncode[i])
  i = i + 1

i = 0
while i < len(pythoncode):
  if 'def' in pythoncode[i]:
    if '()' in pythoncode[i]:
      pythoncode[i] = pythoncode[i].replace('def','PROCEDURE')
      pythoncode[i] = pythoncode[i].replace('()','')
      endinsert(i,'ENDPROCEDURE')
    else:
      pythoncode[i] = pythoncode[i].replace('def','FUNCTION')
      endinsert(i,'ENDFUNCTION')
  i = i + 1

i = 0
while i < len(pythoncode):
  if 'return' in pythoncode[i]:
    pythoncode[i] = pythoncode[i].replace('return','RETURN')
  i = i + 1

i = 0
while i < len(pythoncode):
  print(elifarray)
  print(elifinsert)
  print(elifinsert2)
  print(pythoncode[i],i)
  i = i + 1

print(pythoncode)
for i in range(0,len(pythoncode)):
  print(pythoncode[i])
print(elifinsert)

print(looparray)
print(looparray[5])
print(forstring)
