#练习01-17中发生的部分错误

###ex. 05	
<p>line 18 少输入了一个变量 my_weight</p>
> 只照着书本输入，没有复查。

###ex. 08	
“But it didn’t sing.”之后没有加入” , ”
>

###ex. 10	

for语句后没有用” : ”

###ex. 11	
<pre><code>  
$ python ex11.py
python: can't open file 'ex11.py': [Errno 2] No such file or directory
</code></pre>

###ex. 13	
<pre><code>  
$ python ex13.py
Traceback (most recent call last):
File "ex13.py", line 3, in <module>
script, first, second, third = argv
ValueError: need more than 1 value to unpack
</code></pre>

$ python ex13.py A B C D
Traceback (most recent call last):
File "ex13.py", line 3, in <module>
script, first, second, third = argv
ValueError: too many values to unpack
</code></pre>

###ex. 15 
<pre><code>
$ python ex15.py ex15_sample.txt
Traceback (most recent call last):
File "ex15.py", line 5, in <module>
txt = open(filename)
IOError: [Errno 2] No such file or directory: 'ex15_sample.txt'

$ python ex15.py ex15_sample.txt
File "ex15.py", line 1
SyntaxError: Non-ASCII character '\xe5' in file ex15.py on line 1, 
but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
</code></pre>

###ex. 16
<pre><code>
Traceback (most recent call last):
  File "ex16.py", line 35, in <module>
    print target.read(), "removed"

Traceback (most recent call last):
  File "ex16.py", line 35, in <module>
    print target.read(), "removed"
IOError: File not open for reading

Traceback (most recent call last):
  File "ex16.py", line 16, in <module>
    target.truncate()
IOError: [Errno 22] Invalid argument

Traceback (most recent call last):
  File "ex16.py", line 22, in <module>
    line1, line2, line3 = raw_input(prompt*3 % (1, 2, 3))
ValueError: need more than 1 value to unpack

$ python ex16.py test.txt
  File "ex16.py", line 28
    target.write(line1 "\n" line2 "\n" line3)
                          ^
SyntaxError: invalid syntax
$ python ex16.py test.txt
  File "ex16.py", line 28
    target.write(line1 "\n", line2 "\n", line3)
                          ^
SyntaxError: invalid syntax
</code></pre>

###ex. 17
<pre><code>
Traceback (most recent call last):
  File "ex17.py", line 4, in <module>
    script, from_file, to_file = argv
ValueError: need more than 1 value to unpack

Traceback (most recent call last):
  File "ex17.py", line 6, in <module>
    print "Copying from %s to %s" %s (from_file, to_file)
NameError: name 's' is not defined
</code></pre>
