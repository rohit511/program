punction='''!()-[]{}:;''"|%$#@<>&?*~`_'''
x="hellowe %5@ it %$ is me"
no_punct=""
for char in  x:
    if char not in punction:
        no_punct=no_punct+char
print(no_punct)
