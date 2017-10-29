from django.shortcuts import render, HttpResponse
import pymysql
class Transact:
    def __init__(self,name, email, Phone, balance=500):
        self.name = name
        self.email = email
        self.Phone= Phone
        self.balance=balance
    def home(request):
	    return render(request,'home.html')
    def show_page(request):
	    return render(request,'viewpage.html')
    def register(self, request):
        name = request.POST['name']
        email = request.POST['email']
        Phone = request.POST['Phone']
        mydb=pymysql.connect('localhost','root','root','bank')
        cur=mydb.cursor()
        query = "insert into details values(NULL, '%s','%s', '%s', %d);"%(name, email, Phone, self.balance)
        print(query)
        cur.execute(query)
        mydb.commit()
        mydb.close()
        return render(request,'viewpage.html')
    def transaction(request):
        return render(request,'transactions.html')
    def deposit(request):
        deposit = request.POST['deposit']
        self.balance=self.balance+int(deposit)
        return render(request,'compute.html')  




