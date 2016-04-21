import re
import smtplib

from django.conf import settings
from django.core.mail.utils import DNS_NAME
from django.core.mail.backends.smtp import EmailBackend

POSTSAFE_ON = getattr(settings, 'POSTSAFE_WHITELIST_ON', True)
WHITELISTED_EMAILS = getattr(settings, 'POSTSAFE_WHITELISTED_EMAILS', [r'.+@gmail\.com$', r'cdelguercio@gmail\.com$', ])


class SSLEmailBackend(EmailBackend):
    def open(self):
        if self.connection:
            return False
        try:
            self.connection = smtplib.SMTP_SSL(self.host, self.port, local_hostname=DNS_NAME.get_fqdn())
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except:
            if not self.fail_silently:
                raise

    def send_messages(self, email_messages):
        white_emails = []
        for email in email_messages:
            whitelisted = self.filter_for_whitelisted_email_address(email)
            if whitelisted:
                white_emails.append(whitelisted)
        return super(SSLEmailBackend, self).send_messages(white_emails)

    def filter_for_whitelisted_email_address(self, email):
        if POSTSAFE_ON:
            addresses = email.to
            for address in email.to:
                if not any([re.search(whitelisted, address) for whitelisted in WHITELISTED_EMAILS]):
                    addresses.remove(address)

            email.to = addresses

        return email