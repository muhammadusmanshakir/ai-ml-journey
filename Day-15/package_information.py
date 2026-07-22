import importlib.util
package=input("Enter package name: ")

if importlib.util.find_spec(package):
    print(f"{package} is installed")
else:
    print(f"{package} is not installed")

