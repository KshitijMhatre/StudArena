import random
def digits(num):
	arr=[]
	while num>0:
		arr.append(num%10)
		num//=10
	return arr

def make_num(arr):	
	'''
	strings
	return(int(''.join(map(str,arr))))
	'''
	#no strings attached
	num=0
	arr=arr[::-1]
	for i in range(len(arr)):
		num+=(arr[i]*10**i)
	return num

def ask_n_check(ans,resp,msg):
	if ans==-1:
		print("No such number possible")
		return False
	right = (ans==resp)
	print("correct "if right else msg+str(ans))
	return right

def calc(num,Big,Odd=None):
	global totalqs
	if Odd==None:		
		return make_num(sorted(digits(num),reverse = Big)) #if Biggest then sorted reverse
	else:
		if Odd:
			fil = lambda x:x%2!=0
		else:
			fil = lambda x:x%2==0
		digs=digits(num)
		arr=[0 for _ in digs]
		try:
			if Big:
				arr[-1]=min(filter(fil,digs))
			else:
				arr[-1]=max(filter(fil,digs))				
		except ValueError:
			totalqs-=1
			return -1
		digs.remove(arr[-1])
		arr[:-1]=sorted(digs,reverse =Big)
		return make_num(arr)

def big(num):	
	return calc(num,Big=True)

def bigo(num):
	return calc(num,Big=True,Odd=True)

def bige(num):	
	return calc(num,Big=True,Odd=False)

def small(num):
	return calc(num,Big=False)

def smallo(num):	
	return calc(num,Big=False,Odd=True)

def smalle(num):	
	return calc(num,Big=False,Odd=False)

totalqs=0

def main():
	t=int(input("Enter No. of questions :"))
	global totalqs
	totalqs=t*6
	correct=0
	r=int(input("Enter range of nums(+ve) :"))
	while t>0:
		t-=1
		q=random.randint(0,r)
		print("Let,",q,"be the number")
		ans= int(input("Enter biggest number formed with digits of "+str(q)+" :"))
		correct += ask_n_check(big(q),ans,"Biggest number is :")
		ans= int(input("Enter biggest odd number formed with digits of "+str(q)+" :"))
		correct += ask_n_check(bigo(q),ans,"Biggest odd number is :")
		ans= int(input("Enter biggest even number formed with digits of "+str(q)+" :"))
		correct += ask_n_check(bige(q),ans,"Biggest even number is :")
		ans= int(input("Enter smallest number formed with digits of "+str(q)+" :"))
		correct += ask_n_check(small(q),ans,"Smallest number is :")
		ans= int(input("Enter smallest odd number formed with digits of "+str(q)+" :"))
		correct += ask_n_check(smallo(q),ans,"Smallest odd number is :")
		ans= int(input("Enter smallest even number formed with digits of "+str(q)+" :"))
		correct += ask_n_check(smalle(q),ans,"Smallest even number is :")

	print("You scored ",correct,"accuracy ",correct/totalqs*100)
	

if __name__=='__main__':
	main()
