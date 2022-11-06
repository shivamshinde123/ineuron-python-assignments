

def exep_handle():

    try:
        print(5/0)
    
    except Exception as e:
        print(e)
        raise e

exep_handle()
