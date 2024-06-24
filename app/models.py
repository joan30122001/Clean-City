from django.db import models
from django.contrib.auth.models import User


class EmergencyCollection(models.Model):
    TOWN_CHOICES = [
        ('Yaounde, Bastos', 'Yaounde, Bastos'),
        ('Yaounde, Nkolbisson', 'Yaounde, Nkolbisson'),
        ('Yaounde, Ngoa-Ekelle', 'Yaounde, Ngoa-Ekelle'),
        ('Yaounde, Mvog-Ada', 'Yaounde, Mvog-Ada'),
        ('Yaounde, Mvog-Mbi', 'Yaounde, Mvog-Mbi'),
        ('Yaounde, Etoudi', 'Yaounde, Etoudi'),
        ('Yaounde, Nsam', 'Yaounde, Nsam'),
        ('Yaounde, Essos', 'Yaounde, Essos'),
        ('Yaounde, Biyemassi', 'Yaounde, Biyemassi'),
        ('Yaounde, Mendong', 'Yaounde, Mendong'),
        ('Yaounde, Emana', 'Yaounde, Emana'),
        ('Yaounde, Ahala', 'Yaounde, Ahala'),
        ('Yaounde, Oyom-Abang', 'Yaounde, Oyom-Abang'),
        ('Yaounde, Nkolndongo', 'Yaounde, Nkolndongo'),
        ('Yaounde, Ekounou', 'Yaounde, Ekounou'),
        ('Yaounde, Obili', 'Yaounde, Obili'),
        ('Yaounde, Etoa-Meki', 'Yaounde, Etoa-Meki'),
        ('Yaounde, Melen', 'Yaounde, Melen'),
        ('Yaounde, Odza', 'Yaounde, Odza'),
        ('Yaounde, Mfandena', 'Yaounde, Mfandena'),
        ('Yaounde, Biyem-Assi', 'Yaounde, Biyem-Assi'),
        ('Yaounde, Nkol-Eton', 'Yaounde, Nkol-Eton'),
        ('Yaounde, Mvan', 'Yaounde, Mvan'),
        ('Yaounde, Tsinga', 'Yaounde, Tsinga'),
        ('Yaounde, Messa', 'Yaounde, Messa'),
        ('Yaounde, Simbock', 'Yaounde, Simbock'),
        ('Yaounde, Ngousso', 'Yaounde, Ngousso'),
        ('Yaounde, Etoug-Ebe', 'Yaounde, Etoug-Ebe'),
        ('Yaounde, Anguissa', 'Yaounde, Anguissa'),
        ('Yaounde, Awae', 'Yaounde, Awae'),
        ('Yaounde, Nfandena', 'Yaounde, Nfandena'),
        ('Yaounde, Biassi', 'Yaounde, Biassi'),
        ('Yaounde, Efoulan', 'Yaounde, Efoulan'),
        ('Yaounde, Essomba', 'Yaounde, Essomba'),
        ('Yaounde, Olezoa', 'Yaounde, Olezoa'),
        ('Yaounde, Nyom', 'Yaounde, Nyom'),
        ('Yaounde, Mimboman', 'Yaounde, Mimboman'),
        ('Yaounde, Nkolmesseng', 'Yaounde, Nkolmesseng'),
        ('Yaounde, Madagascar', 'Yaounde, Madagascar'),
        ('Yaounde, Tsinga', 'Yaounde, Tsinga'),
        ('Yaounde, Elig-Essono', 'Yaounde, Elig-Essono'),
        ('Yaounde, Simbok', 'Yaounde, Simbok'),
        ('Yaounde, Mbankolo', 'Yaounde, Mbankolo'),
        ('Yaounde, Ekoumdoum', 'Yaounde, Ekoumdoum'),
        ('Yaounde, Nkoabang', 'Yaounde, Nkoabang'),
        ('Yaounde, Nkoldongo', 'Yaounde, Nkoldongo'),
        ('Yaounde, Abattoir', 'Yaounde, Abattoir'),
        ('Yaounde, Odza', 'Yaounde, Odza'),
        ('Yaounde, Cite Verte', 'Yaounde, Cite Verte'),
        ('Yaounde, Ngousso', 'Yaounde, Ngousso'),
        ('Yaounde, Nkomo', 'Yaounde, Nkomo'),
        ('Douala, Nkomo', 'Douala, Nkomo'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emergency_collections')
    image = models.ImageField(upload_to='emergency_images/')
    description = models.TextField()
    # town_street = models.CharField(max_length=255)
    town_street = models.CharField(max_length=255, choices=TOWN_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    street_detail = models.CharField(max_length=255)
    price = models.CharField(max_length=255, null=True, blank=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'EmergencyCollection {self.id} by {self.user.username}'



class Payment(models.Model):
    # PAYMENT_CHOICES = [
    #     ('MonetBill', 'MonetBill'),
    #     ('Orange Money', 'Orange Money'),
    #     ('MTN Mobile Money', 'MTN Mobile Money'),
    # ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    # emergency_collect = models.ForeignKey(EmergencyCollection, on_delete=models.CASCADE, related_name='payments')
    price = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=100)
    # payment_method = models.CharField(max_length=255, choices=PAYMENT_CHOICES)
    # transaction_code = models.CharField(max_length=100)
    # status = models.CharField(max_length=50)
    # description = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.payment_method}"



class Profile(models.Model):
    FREQUENCY_CHOICES = [
        ('once a week -- 1000 XAF', 'once a week -- 1000 XAF'),
        ('twice a week -- 2500 XAF', 'twice a week -- 2500 XAF'),
        ('three times a week -- 5000 XAF', 'three times a week -- 5000 XAF'),
    ]

    TOWN_CHOICES = [
        ('Yaounde, Bastos', 'Yaounde, Bastos'),
        ('Yaounde, Nkolbisson', 'Yaounde, Nkolbisson'),
        ('Yaounde, Ngoa-Ekelle', 'Yaounde, Ngoa-Ekelle'),
        ('Yaounde, Mvog-Ada', 'Yaounde, Mvog-Ada'),
        ('Yaounde, Mvog-Mbi', 'Yaounde, Mvog-Mbi'),
        ('Yaounde, Etoudi', 'Yaounde, Etoudi'),
        ('Yaounde, Nsam', 'Yaounde, Nsam'),
        ('Yaounde, Essos', 'Yaounde, Essos'),
        ('Yaounde, Biyemassi', 'Yaounde, Biyemassi'),
        ('Yaounde, Mendong', 'Yaounde, Mendong'),
        ('Yaounde, Emana', 'Yaounde, Emana'),
        ('Yaounde, Ahala', 'Yaounde, Ahala'),
        ('Yaounde, Oyom-Abang', 'Yaounde, Oyom-Abang'),
        ('Yaounde, Nkolndongo', 'Yaounde, Nkolndongo'),
        ('Yaounde, Ekounou', 'Yaounde, Ekounou'),
        ('Yaounde, Obili', 'Yaounde, Obili'),
        ('Yaounde, Etoa-Meki', 'Yaounde, Etoa-Meki'),
        ('Yaounde, Melen', 'Yaounde, Melen'),
        ('Yaounde, Odza', 'Yaounde, Odza'),
        ('Yaounde, Mfandena', 'Yaounde, Mfandena'),
        ('Yaounde, Biyem-Assi', 'Yaounde, Biyem-Assi'),
        ('Yaounde, Nkol-Eton', 'Yaounde, Nkol-Eton'),
        ('Yaounde, Mvan', 'Yaounde, Mvan'),
        ('Yaounde, Tsinga', 'Yaounde, Tsinga'),
        ('Yaounde, Messa', 'Yaounde, Messa'),
        ('Yaounde, Simbock', 'Yaounde, Simbock'),
        ('Yaounde, Ngousso', 'Yaounde, Ngousso'),
        ('Yaounde, Etoug-Ebe', 'Yaounde, Etoug-Ebe'),
        ('Yaounde, Anguissa', 'Yaounde, Anguissa'),
        ('Yaounde, Awae', 'Yaounde, Awae'),
        ('Yaounde, Nfandena', 'Yaounde, Nfandena'),
        ('Yaounde, Biassi', 'Yaounde, Biassi'),
        ('Yaounde, Efoulan', 'Yaounde, Efoulan'),
        ('Yaounde, Essomba', 'Yaounde, Essomba'),
        ('Yaounde, Olezoa', 'Yaounde, Olezoa'),
        ('Yaounde, Nyom', 'Yaounde, Nyom'),
        ('Yaounde, Mimboman', 'Yaounde, Mimboman'),
        ('Yaounde, Nkolmesseng', 'Yaounde, Nkolmesseng'),
        ('Yaounde, Madagascar', 'Yaounde, Madagascar'),
        ('Yaounde, Tsinga', 'Yaounde, Tsinga'),
        ('Yaounde, Elig-Essono', 'Yaounde, Elig-Essono'),
        ('Yaounde, Simbok', 'Yaounde, Simbok'),
        ('Yaounde, Mbankolo', 'Yaounde, Mbankolo'),
        ('Yaounde, Ekoumdoum', 'Yaounde, Ekoumdoum'),
        ('Yaounde, Nkoabang', 'Yaounde, Nkoabang'),
        ('Yaounde, Nkoldongo', 'Yaounde, Nkoldongo'),
        ('Yaounde, Abattoir', 'Yaounde, Abattoir'),
        ('Yaounde, Odza', 'Yaounde, Odza'),
        ('Yaounde, Cite Verte', 'Yaounde, Cite Verte'),
        ('Yaounde, Ngousso', 'Yaounde, Ngousso'),
        ('Yaounde, Nkomo', 'Yaounde, Nkomo'),
        ('Douala, Nkomo', 'Douala, Nkomo'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, blank=True)
    frequency = models.CharField(max_length=255, choices=FREQUENCY_CHOICES)
    town_street = models.CharField(max_length=255, choices=TOWN_CHOICES)
    street_detail = models.CharField(max_length=255)
    profile_image = models.ImageField(default='users/default-avatar.png', upload_to='users/', null=True, blank=True)

    def __str__(self):
        return self.user.username



class CompanyProfile(models.Model):
    LOCATION_CHOICES = [
        ('Yaounde', 'Yaounde'),
        ('Douala', 'Douala'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
    company_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    location = models.CharField(max_length=255, choices=LOCATION_CHOICES)
    profile_image = models.ImageField(default='users/default-avatar.png', upload_to='users/', null=True, blank=True)

    def __str__(self):
        return self.user.username



class IllegalDeposit(models.Model):
    TOWN_CHOICES = [
        ('Yaounde, Bastos', 'Yaounde, Bastos'),
        ('Yaounde, Nkolbisson', 'Yaounde, Nkolbisson'),
        ('Yaounde, Ngoa-Ekelle', 'Yaounde, Ngoa-Ekelle'),
        ('Yaounde, Mvog-Ada', 'Yaounde, Mvog-Ada'),
        ('Yaounde, Mvog-Mbi', 'Yaounde, Mvog-Mbi'),
        ('Yaounde, Etoudi', 'Yaounde, Etoudi'),
        ('Yaounde, Nsam', 'Yaounde, Nsam'),
        ('Yaounde, Essos', 'Yaounde, Essos'),
        ('Yaounde, Biyemassi', 'Yaounde, Biyemassi'),
        ('Yaounde, Mendong', 'Yaounde, Mendong'),
        ('Yaounde, Emana', 'Yaounde, Emana'),
        ('Yaounde, Ahala', 'Yaounde, Ahala'),
        ('Yaounde, Oyom-Abang', 'Yaounde, Oyom-Abang'),
        ('Yaounde, Nkolndongo', 'Yaounde, Nkolndongo'),
        ('Yaounde, Ekounou', 'Yaounde, Ekounou'),
        ('Yaounde, Obili', 'Yaounde, Obili'),
        ('Yaounde, Etoa-Meki', 'Yaounde, Etoa-Meki'),
        ('Yaounde, Melen', 'Yaounde, Melen'),
        ('Yaounde, Odza', 'Yaounde, Odza'),
        ('Yaounde, Mfandena', 'Yaounde, Mfandena'),
        ('Yaounde, Biyem-Assi', 'Yaounde, Biyem-Assi'),
        ('Yaounde, Nkol-Eton', 'Yaounde, Nkol-Eton'),
        ('Yaounde, Mvan', 'Yaounde, Mvan'),
        ('Yaounde, Tsinga', 'Yaounde, Tsinga'),
        ('Yaounde, Messa', 'Yaounde, Messa'),
        ('Yaounde, Simbock', 'Yaounde, Simbock'),
        ('Yaounde, Ngousso', 'Yaounde, Ngousso'),
        ('Yaounde, Etoug-Ebe', 'Yaounde, Etoug-Ebe'),
        ('Yaounde, Anguissa', 'Yaounde, Anguissa'),
        ('Yaounde, Awae', 'Yaounde, Awae'),
        ('Yaounde, Nfandena', 'Yaounde, Nfandena'),
        ('Yaounde, Biassi', 'Yaounde, Biassi'),
        ('Yaounde, Efoulan', 'Yaounde, Efoulan'),
        ('Yaounde, Essomba', 'Yaounde, Essomba'),
        ('Yaounde, Olezoa', 'Yaounde, Olezoa'),
        ('Yaounde, Nyom', 'Yaounde, Nyom'),
        ('Yaounde, Mimboman', 'Yaounde, Mimboman'),
        ('Yaounde, Nkolmesseng', 'Yaounde, Nkolmesseng'),
        ('Yaounde, Madagascar', 'Yaounde, Madagascar'),
        ('Yaounde, Tsinga', 'Yaounde, Tsinga'),
        ('Yaounde, Elig-Essono', 'Yaounde, Elig-Essono'),
        ('Yaounde, Simbok', 'Yaounde, Simbok'),
        ('Yaounde, Mbankolo', 'Yaounde, Mbankolo'),
        ('Yaounde, Ekoumdoum', 'Yaounde, Ekoumdoum'),
        ('Yaounde, Nkoabang', 'Yaounde, Nkoabang'),
        ('Yaounde, Nkoldongo', 'Yaounde, Nkoldongo'),
        ('Yaounde, Abattoir', 'Yaounde, Abattoir'),
        ('Yaounde, Odza', 'Yaounde, Odza'),
        ('Yaounde, Cite Verte', 'Yaounde, Cite Verte'),
        ('Yaounde, Ngousso', 'Yaounde, Ngousso'),
        ('Yaounde, Nkomo', 'Yaounde, Nkomo'),
        ('Douala, Nkomo', 'Douala, Nkomo'),
    ]

    image = models.ImageField(upload_to='illegal_deposit_images/')
    description = models.TextField()
    town_street = models.CharField(max_length=255, choices=TOWN_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    street_detail = models.CharField(max_length=255)

    def __str__(self):
        return self.town_street
