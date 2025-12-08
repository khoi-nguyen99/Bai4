print("Sinh vien: Dinh viet khoi Nguyen")
print("Ma so SV  :  245752021610082")
print("################################")
chuoi_nhap = input("Nhap cac tu tieng Anh (cach nhau boi dau cach): ")
ds_tu = chuoi_nhap.split()

ds_tu.sort()

print(", ".join(ds_tu))
