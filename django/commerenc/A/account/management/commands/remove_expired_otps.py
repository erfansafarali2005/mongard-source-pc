from django.core.management import BaseCommand
from account.models import OTPCode
from datetime import datetime , timedelta
import pytz

class Command(BaseCommand):
    help = 'remove all expired otp codes'

    def handle(self , *args ,**kwargs):
        expired_time = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)
        OTPCode.objects.filter(created__lt=expired_time).delete()
        self.stdout.write('successfully deleted the expired OTP codes')