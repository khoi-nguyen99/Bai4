print("Sinh vien: Dinh viet khoi Nguyen")
print("Ma so SV  :  245752021610082")
print("################################")
ds = input('Nhap chuoi:').split()
x = ds[0:-1]

ds.append('abc')
  
ds.remove('123')

vi_tri = ds.index('abc')
print("vị trí của chuỗi abc là", vi_tri)
