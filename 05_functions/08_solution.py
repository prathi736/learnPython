def print_kwargs(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} : {value}")


print_kwargs(name="superman", power="fly")
print_kwargs(name="batman")
print_kwargs(name="spiderman", power="web", enemy="venom")