# check_permissions.py
import os

def check_permissions(path):
    if os.path.exists(path):
        print(f"Path exists: {path}")
        if os.access(path, os.R_OK):
            print("Read permission: Yes")
        else:
            print("Read permission: No")

        if os.access(path, os.W_OK):
            print("Write permission: Yes")
        else:
            print("Write permission: No")

        if os.access(path, os.X_OK):
            print("Execute permission: Yes")
        else:
            print("Execute permission: No")
    else:
        print(f"Path does not exist: {path}")

if __name__ == "__main__":
    path_to_check = 'artifact'
    check_permissions(path_to_check)
