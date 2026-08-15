def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("Thank you")
    #finally ensures the execution of a piece of code irrespective of the exception
    
main()