
#control parameter
prt_ctrl = 1;
#parameter
para_len = 30;
para_k = 29;
para_loop = 15;
#input 
w_dat = [];
w_loc = [];
x_dat = [];
for i in range(para_len):
	w_dat.append(0);
	w_loc.append(i);
for i in range(para_len,32):
	w_dat.append(-1);
	w_loc.append(i);
for i in range(32):
	x_dat.append("0");
#Function
def print_w_raw():
	print("%10s is : ["%("index"),end="");
	for i in range(32):
		print("%3d"%(i),end="");
	print("]");
	print("%10s is : ["%("w_dat"),end="");
	for i in range(32):
		print("%3d"%(w_dat[i]),end="");
	print("]");
	print("%10s is : ["%("w_loc"),end="");
	for i in range(32):
		print("%3s"%(hex(w_loc[i])[2:]),end="");
	print("]");
def print_w():
	if(prt_ctrl):
		print_w_raw();	
def sort_select(i,j):
	if(w_dat[i] > w_dat[j]):
		tmp_d = w_dat[i];
		tmp_l = w_loc[i];
		w_dat[i] = w_dat[j];
		w_loc[i] = w_loc[j];
		w_dat[j] = tmp_d;
		w_loc[j] = tmp_l;
def clear_x_dat():
	#x_dat = "";
	for i in range(30):
		x_dat[i]="0";
	for i in range(30,32):
		x_dat[i]="1";
def print_binary(x):
	#use hex format
	tmp="";
	res="";
	for i in range(8):
		tmp="";
		for j in range(4):
			tmp=tmp + x[31-(4*i+j)];
		hex_str=hex(int(tmp,2));
		res=res+hex_str[2:];
	print(res);
print_w();
#Loop
for i in range(para_loop):
	print("------------Loop "+str(i)+" Start---------------");
	if(i == 0 or i == 2 or i == 5 or i == 9 or i == 14):
		for j in range(15):
			sort_select(2*j,2*j+1);
		print_w();
	elif(i == 1):
		for j in range(8):
			#for k in range(2):
			sort_select(4*j,4*j+3);
			sort_select(4*j+1,4*j+2);
		print_w();
	elif(i == 3):
		for j in range(4):
			sort_select(8*j,8*j+7);
			sort_select(8*j+1,8*j+6);
			sort_select(8*j+2,8*j+5);
			sort_select(8*j+3,8*j+4);
		print_w();
	elif(i == 4 or i == 8 or i == 13):
		for j in range(8):
			sort_select(4*j,4*j+2);
			sort_select(4*j+1,4*j+3);
		print_w();
	elif(i == 6):
		for j in range(2):
			sort_select(16*j,16*j+15);
			sort_select(16*j+1,16*j+14);
			sort_select(16*j+2,16*j+13);
			sort_select(16*j+3,16*j+12);
			sort_select(16*j+4,16*j+11);
			sort_select(16*j+5,16*j+10);
			sort_select(16*j+6,16*j+9);
			sort_select(16*j+7,16*j+8);
		print_w();
	elif(i == 7 or i == 12):
		for j in range(4):
			sort_select(8*j,8*j+4);
			sort_select(8*j+1,8*j+5);
			sort_select(8*j+2,8*j+6);
			sort_select(8*j+3,8*j+7);
		print_w();
	elif(i == 10):
		for j in range(16):
			sort_select(j,31-j);
		print_w();
	elif(i == 11):
		for j in range(2):
			for z in range(8):
				sort_select(16*j+z,16*j+z+8);
		print_w();

print("The final w result is :");
print_w_raw();
#generate x
clear_x_dat();
for i in range(para_k):
	x_dat[w_loc[31-i]] = '1';
if prt_ctrl:
	print("x_dat is: ");
	print(x_dat);
	print_binary(x_dat);
