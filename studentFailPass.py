passMarks=float(input("Enter Student scored marks:"))


def pass_fail(passMarks):
    if passMarks>50:
        print(f"Student is pass and scored marks is {passMarks}.")
    else:
        print(f"Student is failed and scored marks is {passMarks} .")

pass_fail(passMarks)