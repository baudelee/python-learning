#first dump function
import json

name_emb = {'a':'111', 'b':'222', 'c':'3333'}
eml_filename = ('/home/baudel/pythondata/eml.json')
"""dumps function will transfer string type to dict"""
jsObj = json.dumps(name_emb)

with open(eml_filename, "w") as f:
    f.write(jsObj)
    f.close()

print(jsObj)
print(type(jsObj))

name_eml = {"1":"aaa", "2":"bbb","3":"ccc"}
"""dump function will transfer dict type to string and also write content to json file"""
json.dump(name_eml, open(eml_filename, "w"))


"""pool Class
   
"""
import time
from multiprocessing import Pool

def  run(fn):
    time.sleep(1)
    return fn*fn

#if __name__ == "__main__":
    testFL = [1,2,3,4,5,6]
    print 'fn execute process:'
    s = time.time()
    for fn in testFL:
        run(fn)

    e1 = time.time()
    print "execute time:", int (e1 - s)

    print 'concurrent:'
    pool = Pool(5)
    rl = pool.map(run, testFL)
    pool.close()
    pool.join()
    e2 = time.time()
    print "execute time:", int(e2 - e1)
    print rl

""" Airspeed library
Doc link https://wizardforcel.gitbooks.io/velocity-doc/content/43.html
"""
import airspeed

temp = airspeed.Template("""
Old people:
#foreach ($person in $people)
 #if($person.age > 70)
  $person.name
  #end
#end

Third person is $people[2].name
""")

people = [{'name':'Baude', 'age':1000},{'name':'Bob','age':99},{'name':'Bill','age':89}]

print temp.merge(locals())
