from string import Template
name = 'Abdul Waseem'
temp = 'Not very sure though.'


# print Abdul Waseem is a good boy.


print(f"{name} is a good boy.${temp}")


print("%s is a good boy %s" % (name, name))


str = Template("$my_name is a good boy. $second_sentence")

print(str.substitute(my_name=name, second_sentence=temp))
