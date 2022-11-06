
def func():

    subjects=["Americans","Indians"]
    verbs=["play","watch"]
    objects=["Baseball","Cricket"]

    try:
        for i in subjects:
            for j in verbs:
                for k in objects:
                    print(f"{i} {j} {k}.")
    
    except Exception as e:
        print(e)
        raise e


func()
