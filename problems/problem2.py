"""Write a program that takes two integers as input and prints their sum."""


from string import Template


def add(num1, num2):
    print(
        f"Using Literal String Interpolation: Sum of {num1} and {num2} = {num1+num2}")
    print("Using %% formating: Sum of %s and %s = %s" %
          (num1,  num2, num2+num1))
    print("Using str.format() : Sum of {} and {} = {}".format(num1, num2, num1+num2))
    print("Using str.format(): Sum of {n1} and {n2} = {sum}".format(
        n2=num2, n1=num1, sum=num1+num2))

    str = Template(
        "Using String Template class: Sum of $num1 and $num2 = $sum")
    print(str.substitute(num1=num1, num2=num2, sum=num1+num2))


add(3, 5)
