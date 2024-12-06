from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import ComplaintsForm
from .forms import UserRegistrationForm, DepositWithdrawForm,BillPaymentForm,TransferForm
from .models import Account, Transaction
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

 
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Account.objects.create(user=user)
            return render(request, 'registration_success.html', {'account_number': user.account.account_number})
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def registration_success(request):
    return render(request,'registration_success.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account')
    return render(request, 'login.html')

def account_view(request):
    account = request.user.account
    transactions = Transaction.objects.filter(account=account)
    return render(request, 'account.html', {'account': account, 'transactions': transactions, })

def logout(request):
    auth_logout(request)
    return redirect('home')  


def deposit(request):
    if request.method == 'POST':
        form = DepositWithdrawForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            account = request.user.account
            account.balance += amount
            account.save()
            Transaction.objects.create(account=account, amount=amount, transaction_type='deposit')
            return redirect('account')
    else:
        form = DepositWithdrawForm()
    return render(request, 'deposit.html', {'form': form})

def withdraw(request):
    if request.method == 'POST':
        form = DepositWithdrawForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            account = request.user.account
            if account.balance >= amount:
                account.balance -= amount
                account.save()
                Transaction.objects.create(account=account, amount=amount, transaction_type='withdraw')
                return redirect('account')
    else:
        form = DepositWithdrawForm()
    return render(request, 'withdraw.html', {'form': form})


def Home(request):
    return render(request,"home.html")


def Cantact_User(request):
    if request.method == 'POST':
        form = ComplaintsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('succuess')
    else:
        form = ComplaintsForm()
    return render(request,"cantact.html",{'form':form})

def succuess(request):
    return render(request,"succuess.html")

BILL_PAYMENT_OPTIONS = [
    ('electricity', 'Electricity Bill'),
    ('Water', ' Water Bill'),
    ('House', 'House Bill'),
    ('Loan', 'Loan Bill'),
    ('Gas', 'Gas Bill'),
    ('DTH', 'DTH Recharge Bill'),
]

@login_required
def bill_payment(request):
    if request.method == 'POST':
        form = BillPaymentForm(request.POST)
        if form.is_valid():
            bill_type = form.cleaned_data['bill_type']
            amount = form.cleaned_data['amount']
            account = request.user.account
            
            if account.balance >= amount:
                account.balance -= amount
                account.save()
                Transaction.objects.create(account=account, amount=amount, transaction_type='bill_payment')
                
                # Integrate with payment gateway here
                payment_response = process_payment(bill_type, amount)
                
                if payment_response['status'] == 'success':
                    return redirect('payment_success')
                else:
                    return render(request, 'payment_failed.html', {'error': payment_response['message']})
            else:
                return render(request, 'bill_payment.html', {'form': form, 'error': 'Insufficient balance.'})
    else:
        form = BillPaymentForm()
    return render(request, 'bill_payment.html', {'form': form})

def process_payment(bill_type, amount):
    # Simulate payment processing
    # Replace with actual payment gateway integration
    return {'status': 'success', 'message': 'Payment processed successfully.'}

def payment_success(request):
    return render(request, 'payment_success.html')

def payment_failed(request):
    return render(request, 'payment_failed.html')

def transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            recipient_account_number = form.cleaned_data['recipient_account_number']
            account = request.user.account
            try:
                recipient_account = Account.objects.get(account_number=recipient_account_number)
                if account.balance >= amount:
                    account.balance -= amount
                    recipient_account.balance += amount
                    account.save()
                    recipient_account.save()
                    Transaction.objects.create(account=account, amount=amount, transaction_type='transfer')
                    Transaction.objects.create(account=recipient_account, amount=amount, transaction_type='transfer')
                    return redirect('account')
            except Account.DoesNotExist:
                form.add_error('recipient_account_number', 'Account does not exist.')
    else:
        form = TransferForm()
    return render(request, 'transfer.html', {'form': form})

@login_required
def edit_account(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = UserRegistrationForm(instance=request.user)
    return render(request, 'edit_account.html', {'form': form})


            
          
                
            