from django.db import models
from django.contrib.auth.models import AbstractUser

# ------------------
# Role Model
# ------------------
class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return self.role_name


# ------------------
# User Model
# ------------------
class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username


# ------------------
# Player Model
# ------------------
class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


# ------------------
# Owner Model
# ------------------
class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


# ------------------
# Futsal Ground Model
# ------------------
class FutsalGround(models.Model):
    futsal_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    ground_size = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# ------------------
# Document Model
# ------------------
class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    futsal = models.ForeignKey(FutsalGround, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=50)
    document_url = models.URLField()


# ------------------
# Booking Model
# ------------------
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    futsal = models.ForeignKey(FutsalGround, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    booking_type = models.CharField(max_length=50)


# ------------------
# Payment Model
# ------------------
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


# ------------------
# Team Member Model
# ------------------
class TeamMember(models.Model):
    team_member_id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    player_position = models.CharField(max_length=50)


# ------------------
# Join Request Model
# ------------------
class JoinRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    request_status = models.CharField(max_length=50)


# ------------------
# Connection Model
# ------------------
class Connection(models.Model):
    connection_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50)


# ------------------
# Player Connection Model
# ------------------
class PlayerConnection(models.Model):
    player_connection_id = models.AutoField(primary_key=True)
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    connection_date = models.DateField()


# ------------------
# Chat Model
# ------------------
class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message_text = models.TextField()
    message_time = models.DateTimeField(auto_now_add=True)
    chat_type = models.CharField(max_length=50)


# ------------------
# Notification Model
# ------------------
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=50)
    notification_date = models.DateTimeField(auto_now_add=True)


# ------------------
# Loyalty Model
# ------------------
class Loyalty(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True)
    total_matches = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    
