sbd = input("Nhập số báo danh: ")
khoi = input("Nhập khối: ").strip().upper()
sp = ["A00", "A01", "A02", "B00", "B08", "C00", "C03", "C04", "C14", "C19", "C20", "D01"]
diem = tsTT = rankTT = 0
check = False

if khoi not in sp:
    print("Không tìm thấy khối thi")
    exit()

with open(f"diem_thi_sort/{khoi}.txt") as f:
	tsQG = f.readline().strip()
	for i, line in enumerate(f):
		if line.startswith("45"):
			tsTT += 1
			if check:
				rankTT += 1
		if line[:8] == sbd:
			rankQG = i+1
			diem = line.split()[1].strip()
			check = True

if not diem:
	print("Không tìm thấy điểm thi")
	exit()

print("Thí sinh:", sbd)
print(f"Điểm khối {khoi}: {float(diem):.2f}")
print(f"Xếp hạng tỉnh/thành: {tsTT-rankTT}/{tsTT}")
print(f"Xếp hạng quốc gia: {rankQG}/{tsQG}")
