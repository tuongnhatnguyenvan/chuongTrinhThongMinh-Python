while True:
    def duAn():                                   # màn hình
        print("|"+"-"*70+"|")
        print("|"+"*"*70+"|")
        print("|"+"*"*21+"Chương Trình Học Thông Minh"+"*"*22+"|")
        print("|"+"*"*70+"|")
        print("|"+"-"*70+"|")
        print(" "*72)
        print("|"+"-"*70+"|")
        print("|"+"="*34+"MENU"+"="*32+"|")
        print("|"+"-"*70+'|')
        print(" "*72)
        print("|"+"-"*70+'|')
        print("|"+"  "+"Xin vui lòng chọn:"+" "*50+"|")
        print("|"+"  "+"1. Xem lịch"+" "*57+"|")
        print("|"+"  "+"2. Tính lương"+" "*55+"|")
        print("|"+"  "+"3. Xem lương được sắp xếp"+' '*43+"|")
        print("|"+"  "+"4. Xem thông tin nhân viên"+" "*42+"|")
        print("|"+"  "+"5. Tính điểm của học sinh"+" "*43+"|")
        print("|"+'  '+"6. Thoát chương trình"+" "*47+"|")
        print("|"+"-"*70+'|')
    duAn()
    a = int(input('Chọn Menu: '))
    def troLaiHayTiepTuc(str):
        if str=="n":
            return False
        else:
            return True                
    if a ==1:
        while True:
            def demNgay(number):                # câu 1
                if 0<number<=12:
                    thang=[1,2,3,4,5,6,7,8,9,10,11,12]
                    ngay=[31,[28,29],31,30,31,30,31,31,30,31,30,31]
                    for i in range(len(thang)):
                        if number==2:
                            nam=int(input("nhap nam: "))
                            if nam%400==0 or nam%4==0 and nam%100!=0:
                                b=ngay[1][1]
                                return b
                            else:
                                b=ngay[1][0]   
                                return b 
                        if number==thang[i]:
                            b=ngay[i]
                            return b
            while True:
                try:
                    thang=int(input("Nhập tháng: "))
                    if thang>0 and thang<12:
                        break
                    else: print("Không có tháng",thang,"vui lòng nhập tháng từ 1 đến 12")
                except: print("Nhập lại đi bạn")
            c=demNgay(thang)
            print("Có",c,"ngày trong tháng",thang)
            hoi=str(input("Có muốn xem tiếp hay trở lại(y/n):"))
            if troLaiHayTiepTuc(hoi)==False:break            
    if a==2:
        while True:
            def tinhLuong(gio,luongGio):      # câu 2
                if gio>40:
                    d=gio-40
                    luongThem=d*1.5*luongGio
                    luongTong=40*luongGio+luongThem
                else:
                    luongTong=luongGio*gio
                return luongTong
            while True:
                try:
                    gio=float(input("Nhập giờ làm:"))
                    if gio>0:
                        luongGio=float(input("Nhập lương theo giờ:"))
                        if luongGio>0:break
                        else:print("nó không thể âm,hãy nhập lại")
                    else:print("nó không thể âm,hãy nhập lại")
                except ValueError:print("Dữ liệu sai vui lòng nhap lại ")
            tong=tinhLuong(gio,luongGio)
            print("Tiền lương tổng cộng là:",tong)
            hoi=str(input("Có muốn xem tiếp hay trở lại(y/n):"))
            if troLaiHayTiepTuc(hoi)==False:break  
    if a==3:
        while True:
            def thuTuTangDan(number):      # câu 3
                dsTen=[]
                dsTienLuong=[]
                z=[]
                for n in range(number):
                    s=str(str(input("Nhập tên nhân viên "+str(n+1)+":")))
                    l=int((input("Nhập lương của nhân viên "+str(n+1)+":")))
                    dsTen.append(s)
                    dsTienLuong.append(l)
                for i in range(0,number-1):
                    for j in range(i+1,number):
                        if dsTienLuong[i]>dsTienLuong[j]:
                            a=dsTienLuong[i]
                            dsTienLuong[i]=dsTienLuong[j]
                            dsTienLuong[j]=a
                            b=dsTen[i]
                            dsTen[i]=dsTen[j]
                            dsTen[j]=b
                for a in range(len(dsTen)):
                    y=""
                    y=str(dsTen[a])+":"+str(dsTienLuong[a])
                    z.append(y)
                print("Danh sách nhân viên sau khi sắp xếp theo lương là:",z)
            l=int(input("Nhập số lượng nhân viên cần sắp xếp lương:"))
            thuTuTangDan(l)
            hoi=str(input("Có muốn xem tiếp hay trở lại(y/n):"))
            if troLaiHayTiepTuc(hoi)==False:break
    if a==4:
        while True:
            def capitalLetterFirst(text):     # câu 4
                doiLai=" "+text+" "
                caChuoi=""
                for k in range(len(doiLai)):
                    if doiLai[k-1]==" ":
                        inH=doiLai[k].upper()
                        caChuoi=caChuoi+inH
                    else:
                        caChuoi=caChuoi+doiLai[k]
                caMang=[]
                bienGan=""
                ho_tenLot=""
                for i in range(len(caChuoi)):
                    if caChuoi[i]!=" ":
                            bienGan=bienGan+str(caChuoi[i])
                    else:
                            caMang.append(bienGan)
                            bienGan=""
                for i in caMang:
                    if i!=caMang[len(caMang)-1]:
                        ho_tenLot=ho_tenLot+" "+str(i)
                    else:
                        ten=str(caMang[len(caMang)-1])
                print("Họ và tên lót của nhân viên là:",ho_tenLot,"\n"+"Tên của nhân viên là:",ten,"\n"+"Họ và tên đầy đủ của nhân viên là:",caChuoi)
            f=str(input("Nhập họ và tên nhân viên:"))
            capitalLetterFirst(f)
            hoi=str(input("Có muốn xem tiếp hay trở lại(y/n):"))
            if troLaiHayTiepTuc(hoi)==False:break
    if a==5:
        while True:
            def diemTrungBinh(number):      # Câu 5
                heSo=[1,1.5,2,2.5,3]
                tongDiemNhanHeSo=0
                tongHeSo=0
                for i in range (number):
                    while True:
                        d=float(input("Điểm môn học "+str(i+1)+":"))
                        e=float(input("Hệ số của môn học (Hệ số thuộc (1 1,5 2 2,5 hoặc 3)) "+str(i+1)+":"))
                        if 0<d<10 and e in heSo:
                            break
                        else:
                            print("Gia tri nhap sai,vui long nhap lai")
                    tongDiemNhanHeSo=tongDiemNhanHeSo+(d*e)
                    tongHeSo=tongHeSo+e
                    dtb=tongDiemNhanHeSo/tongHeSo
                print("Số môn học:",number,"\n"+"Tổng hệ số là:",tongHeSo,"\n"+"Điểm trung bình của",number,"môn học là:",dtb)
            x=int(input("Nhap so mon hoc can tinh:"))
            diemTrungBinh(x)
            hoi=str(input("Có muốn xem tiếp hay trở lại(y/n):"))
            if troLaiHayTiepTuc(hoi)==False:break
    if a==6:
        y=input("Bạn muốn tiếp tục(y/n)")
        if y=="n":break