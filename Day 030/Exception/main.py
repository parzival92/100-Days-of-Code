#File not found

try:
    file = open("file.txt")
    a_dict = {"key":"value"}
    print(a_dict["errorkey"])
except FileNotFoundError:
    file = open("file.txt","w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} doesn't exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")

