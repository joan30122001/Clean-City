from django.shortcuts import render, redirect, HttpResponse, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import EmergencyCollection, Profile, CompanyProfile, IllegalDeposit, Payment
from .forms import RegisterForm, CompanyRegisterForm, EmergencyCollectionForm, UserForm, CompanyUserForm, ProfileForm, CompanyProfileForm, IllegalDepositForm
from django.views.generic import TemplateView, CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
import mimetypes
from django.views import View
from django.contrib.auth.decorators import login_required




def home(request):
    return render(request, 'city/home.html')



@login_required(login_url='/')
def dashboard(request):
    # collections = EmergencyCollection.objects.all() 
    collections = EmergencyCollection.objects.filter(user=request.user) 
    # all_emaregency = EmergencyCollection.objects.all().count()
    all_emaregency = EmergencyCollection.objects.filter(user=request.user).count()

    latest_payment = Payment.objects.filter(user=request.user, paid=True).order_by('-id').first()
    if latest_payment:
        price = latest_payment.price
    else:
        price = "00 XAF"

    return render(request, 'city/dashboard.html', {'collections': collections, 'all_emaregency': all_emaregency, 'price':price})



# import matplotlib.pyplot as plt
# import io
# from django.http import HttpResponse
# from .models import EmergencyCollection
# from collections import Counter
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# def pie_chart(request):
#     # Query the EmergencyCollection and count occurrences by town_street
#     collections = EmergencyCollection.objects.all()
#     location_counts = Counter(collection.town_street for collection in collections)

#     # Data preparation
#     labels = list(location_counts.keys())
#     sizes = list(location_counts.values())
#     colors = plt.cm.Paired(range(len(labels)))  # Get a range of colors

#     # Pie chart creation
#     fig, ax = plt.subplots()
#     ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
#     ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#     # Save the plot as a PNG in memory.
#     buf = io.BytesIO()
#     plt.savefig(buf, format='png')
#     plt.close(fig)
#     response = HttpResponse(buf.getvalue(), content_type='image/png')
#     buf.close()
#     return response

def get_data():
    # Example: Counting entries per day
    data = EmergencyCollection.objects.annotate(date=Trunc('created_at', 'day', output_field=DateField())).values('date').annotate(count=Count('id')).order_by('date')
    dates = [x['date'] for x in data]
    counts = [x['count'] for x in data]
    return dates, counts


import matplotlib.pyplot as plt
from io import BytesIO
from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from django.db.models import Count, DateField
from django.db.models.functions import Trunc


def line_chart(request):
    dates, counts = get_data()

    # Create a new figure and an axes to plot on
    fig, ax = plt.subplots(figsize=(10, 6))  # You can adjust the size here
    ax.plot(dates, counts, label='Number of EmergencyCollections', marker='o', linestyle='-')

    # Customizing the plot
    ax.set_title('EmergencyCollection Counts Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Count')
    ax.grid(True)
    ax.legend()

    # Save the plot to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=100)
    plt.close(fig)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    buf.close()
    return response



@login_required(login_url='/company-login/')
def company_dashboard(request):
    # collection = EmergencyCollection.objects.all() 
    user_location = request.user.profiles.location
    collection = EmergencyCollection.objects.filter(town_street__startswith=user_location)

    all_collection = EmergencyCollection.objects.filter(town_street__startswith=user_location).count()

    deposit = IllegalDeposit.objects.filter(town_street__startswith=user_location)

    all_deposit = IllegalDeposit.objects.filter(town_street__startswith=user_location).count()

    users_location = request.user.profile.town_street
    users_with_payments = User.objects.filter(
        profile__town_street__startswith=user_location,
        payments__paid=True
    ).count()
    return render(request, 'city/company-dashboard.html', {'collection': collection, 'deposit': deposit, 'all_deposit':all_deposit, 'all_collection': all_collection, 'users_with_payments': users_with_payments
    # 'pie_chart_url': 'pie-chart/'
    })



def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'user/register.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password'],
                )

                # user.phone_number = form.cleaned_data['phone_number']
                # user.town_street = form.cleaned_data['town_street']
                # user.street_detail = form.cleaned_data['street_detail']
                # user.frequency = form.cleaned_data['frequency']
                # user.save()

                user_profile = Profile(
                    user=user,
                    phone_number=form.cleaned_data.get('phone_number', ''),
                    town_street=form.cleaned_data['town_street'],
                    street_detail=form.cleaned_data['street_detail'],
                    frequency=form.cleaned_data['frequency']
                )
                user_profile.save()
               
                # Login the user
                login(request, user)
               
                # redirect to accounts page:
                return redirect('dashboard')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})



def company_register(request):
    # if this is a POST request we need to process the form data
    template = 'user/company-register.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        forms = CompanyRegisterForm(request.POST)
        # check whether it's valid:
        if forms.is_valid():
            if User.objects.filter(username=forms.cleaned_data['username']).exists():
                return render(request, template, {
                    'forms': forms,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=forms.cleaned_data['email']).exists():
                return render(request, template, {
                    'forms': forms,
                    'error_message': 'Email already exists.'
                })
            elif forms.cleaned_data['password'] != forms.cleaned_data['password_repeat']:
                return render(request, template, {
                    'forms': forms,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    forms.cleaned_data['username'],
                    forms.cleaned_data['email'],
                    forms.cleaned_data['password'],
                )

                # user.phone_number = forms.cleaned_data['phone_number']
                # user.town_street = forms.cleaned_data['town_street']
                # user.street_detail = forms.cleaned_data['street_detail']
                # user.frequency = forms.cleaned_data['frequency']
                # user.save()

                user_profile = CompanyProfile(
                    user=user,
                    phone_number=forms.cleaned_data.get('phone_number', ''),
                    company_name=forms.cleaned_data['company_name'],
                    location=forms.cleaned_data['location']
                )
                user_profile.save()
               
                # Login the user
                login(request, user)
               
                # redirect to accounts page:
                return redirect('company_dashboard')

   # No post data availabe, let's just show the page.
    else:
        forms = CompanyRegisterForm()

    return render(request, template, {'forms': forms})



def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            # return render(request, 'company/home.html')
            return redirect('dashboard')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'user/login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'user/login.html')



def company_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            # return render(request, 'company/home.html')
            return redirect('company_dashboard')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'user/company-login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'user/company-login.html')



def user_logout(request):
    logout(request)
    return redirect('user_login')



def company_logout(request):
    logout(request)
    return redirect('company_login')



# class ProfileView(LoginRequiredMixin, TemplateView):
#     template_name = 'registration/profile.html'



class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'user/profile.html'

    def post(self, request):
        Profile.objects.get_or_create(user=request.user)
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)



class CompanyProfileUpdateView(LoginRequiredMixin, TemplateView):
    users_form = CompanyUserForm
    profiles_form = CompanyProfileForm
    template_name = 'user/company-profile.html'

    def post(self, request):
        CompanyProfile.objects.get_or_create(user=request.user)
        post_data = request.POST or None
        file_data = request.FILES or None

        users_form = CompanyUserForm(post_data, instance=request.user)
        profiles_form = CompanyProfileForm(post_data, file_data, instance=request.user.profiles)

        if users_form.is_valid() and profiles_form.is_valid():
            users_form.save()
            profiles_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('company_profile'))

        context = self.get_context_data(
                                        users_form=users_form,
                                        profiles_form=profiles_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)



def create_emergency_collection(request):
    if request.method == 'POST':
        form = EmergencyCollectionForm(request.POST, request.FILES)
        if form.is_valid():
            emergency_collection = form.save(commit=False)
            emergency_collection.user = request.user
            emergency_collection.save()
            send_emergency_collection_email(emergency_collection)
            return redirect('dashboard')  # Redirect to a success page
    else:
        form = EmergencyCollectionForm()
    return render(request, 'city/emergency.html', {'form': form})



def send_emergency_collection_email(emergency_collection):
    subject = 'New Emergency Collection Created'
    message = f"""
    A new Emergency Collection has been created.

    Username: {emergency_collection.user.username}
    Description: {emergency_collection.description}
    Image: {emergency_collection.image}
    Town Street: {emergency_collection.town_street}
    Created At: {emergency_collection.created_at}
    Street Detail: {emergency_collection.street_detail}
    """
    # Attach image if it exists
    email = EmailMessage(
        subject,
        message,
        'digital.studios587@gmail.com',
        ['xaviemiello@gmail.com'],  # Replace with admin email
    )
    # if emergency_collection.image:
    #     email.attach(emergency_collection.image.name, emergency_collection.image.read(), emergency_collection.image.content_type)
    # email.send()

    if emergency_collection.image:
        file_path = emergency_collection.image.path
        content_type, _ = mimetypes.guess_type(file_path)
        if content_type:
            with open(file_path, 'rb') as f:
                email.attach(emergency_collection.image.name, f.read(), content_type)
        else:
            print("Could not determine the file's content type")

    email.send()



class EmergencyCollectionEditView(LoginRequiredMixin, View):
    def get(self, request, pk):
        emergency_collection = get_object_or_404(EmergencyCollection, pk=pk)
        return render(request, 'city/edit-emergency.html', {'emergency_collection': emergency_collection})

    def post(self, request, pk):
        emergency_collection = get_object_or_404(EmergencyCollection, pk=pk)
        emergency_collection.description = request.POST.get('description')
        emergency_collection.town_street = request.POST.get('town_street')
        emergency_collection.street_detail = request.POST.get('street_detail')
        emergency_collection.price = request.POST.get('price')
        emergency_collection.paid = 'paid' in request.POST
        image_file = request.FILES.get('image')
        if image_file:
            emergency_collection.image = image_file

        emergency_collection.save()
        return redirect('company_dashboard') 



def create_illegal_deposit(request):
    if request.method == 'POST':
        form = IllegalDepositForm(request.POST, request.FILES)
        if form.is_valid():
            illegal_deposit = form.save(commit=False)
            illegal_deposit.user = request.user
            illegal_deposit.save()
            send_illegal_deposit_email(illegal_deposit)
            return redirect('dashboard')  # Redirect to a success page
    else:
        form = IllegalDepositForm()
    return render(request, 'city/illegal-deposit.html', {'form': form})



def send_illegal_deposit_email(illegal_deposit):
    subject = 'New Emergency Collection Created'
    message = f"""
    A new Illegal Deposit has been created.

    Description: {illegal_deposit.description}
    Image: {illegal_deposit.image}
    Town Street: {illegal_deposit.town_street}
    Created At: {illegal_deposit.created_at}
    Street Detail: {illegal_deposit.street_detail}
    """
    # Attach image if it exists
    email = EmailMessage(
        subject,
        message,
        'digital.studios587@gmail.com',
        ['xaviemiello@gmail.com'],  # Replace with admin email
    )

    if illegal_deposit.image:
        file_path = illegal_deposit.image.path
        content_type, _ = mimetypes.guess_type(file_path)
        if content_type:
            with open(file_path, 'rb') as f:
                email.attach(illegal_deposit.image.name, f.read(), content_type)
        else:
            print("Could not determine the file's content type")

    email.send()



def handle_payment(request, collection_id):
    # if request.method == 'POST':
    #     collection = get_object_or_404(EmergencyCollection, pk=collection_id)
    #     collection.paid = True
    #     collection.save()
    #     return redirect('dashboard')
    # return redirect('dashboard')
    collection = get_object_or_404(EmergencyCollection, pk=collection_id)
    if request.method == 'POST':
        collection.paid = True
        collection.save()
        return redirect('dashboard')
    else:
        return render(request, 'city/pay-emergency.html', {'collection': collection})



def submit_payment(request):
    profile = Profile.objects.get(user=request.user)
    try:
        # Assumes the string format is "description -- price XAF"
        price = profile.frequency.split(' -- ')[1].strip()  # Extracts part after '--' and trims whitespace
    except IndexError:
        # Fallback if the frequency doesn't conform to expected format
        price = "Price Not Available"

    if request.method == 'POST':
        price = request.POST.get('price')
        payment_method = request.POST.get('payment_method')

        # Create a new payment instance
        Payment.objects.create(
            user=request.user,
            price=price,
            payment_method=payment_method,
            paid=True
        )

        # Add a success message
        messages.success(request, 'Payment was successful!')

        # Reload the payment form page
        return redirect(dashboard)

    return render(request, 'city/payment.html', {'price': price, 'plan': profile.frequency})



def find_paid_users(request):
    # Get the town_street prefix from the logged-in user's profile
    user_location = request.user.profile.town_street

    # Find all users whose profiles have a town_street starting with the logged-in user's location
    # and who have at least one payment record where paid=True
    users_with_payments = User.objects.filter(
        profile__town_street__startswith=user_location,
        payments__paid=True
    ).distinct()

    return render(request, 'city/paid-user.html', {'users': users_with_payments})