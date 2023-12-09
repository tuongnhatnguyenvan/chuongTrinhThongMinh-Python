def menu():
    print(' '*25, '||', '-'*50, '||')
    print(' '*25, '||', '-'*50, '||')
    print(' '*25, '||', '{:^50} ||'.format("Chuong trinh quan ly hoc sinh sinh vien"))
    print(' '*25, '||', '-'*50, '||')
    print(' '*25, '||', '-'*50, '||')
    print()
    print(' '*5, '||', '-'*90, '||')
    print(' '*5, '||', '-'*90, '||')
    print(' '*5, '||', '{:^90} ||'.format("MENU"))
    print(' '*5, '||', '-'*90, '||')
    print(' '*5, '||', '-'*90, '||')
    print()
    print(' '*5, '||', '-'*90, '||')
    print(' '*5, '||', '-'*90, '||')
    print(' '*5, '||', '{:<90} ||'.format("Xin vui long chon:"))
    print(' '*5, '||', '{:<90} ||'.format("1. to chuc du lieu"))
    print(' '*5, '||', '{:<90} ||'.format("2. xuat du lieu"))
    print(' '*5, '||', '{:<90} ||'.format("3. tim kiem"))
    print(' '*5, '||', '{:<90} ||'.format("4. sap xep"))
    print(' '*5, '||', '{:<90} ||'.format("5. Thoat chuong trinh"))
    print(' '*5, '||', ' '*90, '||')
    print(' '*5, '||', ' '*90, '||')
    print(' '*5, '||', ' '*90, '||')
    print(' '*5, '||', '-'*90, '||')
    print(' '*5, '||', '-'*90, '||')
class Nut:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class DSLK:
    def __init__(self):
        self.head = None
        self.end = None
        
    def printDS(self):
        current = self.head
        while current != None:
            current.data.printSV()
            current = current.next
        
    def addEnd(self, data):
        nut = Nut(data)
        
        if self.head != None:
            self.end.next = nut
            self.end = nut
        else:
            self.head = nut
            self.end = nut
    
    def countDS(self):    
        current = self.head
        i = 0
        while current != None:
            i += 1
            current = current.next
        return i
    def bubbleSort2(self):
        i = self.head
        end = None
        while i.next != None:
            j = self.head
            
            while j.next != end:
                if j.data.maso > j.next.data.maso:
                    j.data, j.next.data = j.next.data, j.data

                j = j.next
            end = j
            i = i.next

    
           
    def findMid(self, start, l , end): 
        mid = int(end + (start - end)/2)
        current = l
        before = None
        i = start
        while  i < mid:
            i += 1
            before = current
            current = current.next
        return current, before, i
    
    def searchBinary(self, l, iOfl, r, iOfr, x):
        
        if  l != None and r != None and r.next != l :
            mid, bfMid, i = self.findMid(iOfl, l, iOfr)

            if mid.data.maso == x:
                return i, mid.data
            if x > mid.data.maso:
                return self.searchBinary(mid.next, i + 1, r, iOfr, x)
            else:
                return self.searchBinary(l, iOfl, bfMid, i-1, x )
        else:
            return -1, None

class SinhVien:
    def __init__(self, maso, ten, diem, lop):
        self.maso = maso
        self.ten = ten
        self.diem = diem
        self.lop = lop
    def printSV(self):
        print(f'ma so la: {self.maso}\n'+
              f'Ten la: {self.ten}\n'+
              f'diem la: {self.diem}\n'+
              f'lop la: {self.lop}\n'+
              '-'*50)            
list1 = DSLK()


while True:
    menu()

    

    choosenMenu = int(input("vui long chon mot so tron menu: "))

            
    if choosenMenu == 1:
        n = int(input("ban muon nhap bao nhieu phan tu: "))
        for i in range(n):
            maso = int(input('ma so: '))
            ten = input("tên sinh viên: ")
            diem = float(input("điểm sinh viên: "))
            lop = input("nhập lớp: ")
            sv = SinhVien(maso, ten, diem, lop)
            list1.addEnd(sv)
            print("-"*50)
    elif choosenMenu == 2:
        list1.printDS()
        
    elif choosenMenu == 3:

        print('chỉ hỗ trợ tìm kiếm theo ID: ')
        x = int(input("gia tri ban muon tim: "))
        list1.bubbleSort2()
        
        result, sv = list1.searchBinary(list1.head, 0, list1.end, list1.countDS() - 1, x)
            
        if result == -1:
            print("khong tim thay :((")
        else:
            print(x, "xuat hien tai vi tri", result + 1)        
            sv.printSV()
    elif choosenMenu == 4:

        list1.bubbleSort2()
        list1.printDS()
      
    else:
        break

    checkContinue = input('bạn muốn tiếp tục chuong trinh, y/n: ')
    if checkContinue == 'n':
        break