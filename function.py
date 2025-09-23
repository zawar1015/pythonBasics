def is_strong(password):
    return(
        len(password)>=8
        and any(ch.isdigit() for ch in password)
        and any(ch.isupper() for ch in password)
        and any(ch.islower() for ch in password)

    )

password=input("enter your Password.")
print("strong password" if is_strong(password) else "weak password")