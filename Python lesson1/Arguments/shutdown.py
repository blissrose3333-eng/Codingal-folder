def shutdown(password):
    correct_password="opensesame"
    if password==correct_password:
        return "Shutting down.."
    else:
        return "Shutdown aborted,Invalid password."

user_input=input("Enter password to shut down:")
result= shutdown(user_input)
print(result)