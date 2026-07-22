import pkgutil

print("Installed Packages")
print("="*25)

count=0
for package in pkgutil.iter_modules():
    print(package.name)
    count+=1

print("="*25)
print("Installed Packages: ",count)

