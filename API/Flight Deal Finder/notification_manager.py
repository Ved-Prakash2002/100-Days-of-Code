from twilio.rest import Client  # Importing the Twilio client for sending SMS messages.
import smtplib  # Importing smtplib to handle email sending functionality.


class NotificationManager:
    """
    A class to handle sending notifications via SMS and email.
    """

    def __init__(self, account_sid, auth_token, from_phone, to_phone):
        """
        Initializes the NotificationManager instance with the required credentials and configurations.

        Parameters:
        - account_sid: Twilio Account SID for authentication.
        - auth_token: Twilio Auth Token for authentication.
        - from_phone: The phone number from which SMS will be sent (Twilio number).
        - to_phone: The recipient phone number for SMS notifications.
        """
        self.client = Client(account_sid, auth_token)  # Initialize Twilio Client.
        self.from_phone = from_phone  # Store the sender's phone number.
        self.to_phone = to_phone  # Store the recipient's phone number.
        self.my_email = "t4481219@gmail.com"  # Email address used for sending notifications.
        self.password = "iqqy huvp dzhu nooe"  # App-specific password for the email account (sensitive information).

    def send_sms(self, message):
        """
        Sends an SMS notification using the Twilio API.

        Parameters:
        - message: The message text to send via SMS.
        """
        # Create and send the SMS message.
        message = self.client.messages.create(
            body=message,  # The text of the SMS message.
            from_=self.from_phone,  # The Twilio phone number sending the message.
            to=self.to_phone  # The recipient's phone number.
        )
        # Print confirmation with the message SID for tracking purposes.
        print(f"Message sent: {message.sid}")

    def send_emails(self, email, message):
        """
        Sends an email notification using an SMTP server.

        Parameters:
        - email: The recipient's email address.
        - message: The content of the email message.
        """
        # Open a connection to the Gmail SMTP server.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Start TLS encryption for secure communication.
            connection.login(self.my_email, self.password)  # Log in to the email account.

            # Send the email with the specified sender, recipient, and message content.
            connection.sendmail(
                from_addr=self.my_email,  # Sender's email address.
                to_addrs=email,  # Recipient's email address.
                msg=message  # Email message content.
            )
            connection.close()  # Close the connection to the SMTP server.
