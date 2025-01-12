#ex="He Said, "What's there?""
ex="He Said, \"What's there?\""#Double quotes
print(ex)

ex='He Said, "What\'s there ? " '#Single
print(ex)


double=lambda x: x*2

input="hello"
output=""
for i in input:
    output=output+double(i)
    print(output)

