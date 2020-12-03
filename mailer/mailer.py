from decouple import config
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


    
# Argument is 'Donation' object from 'animals' app
def send_recpt(donation):
    
    message = Mail(
        from_email = 'roar@wildheart.foundation',
        to_emails = donation.email,
        # subject = f'Your Donation to {donation.wish.animal.name}',
        html_content = '<strong>Hey thanks for donating.</strong>'
    )
    
    message.dynamic_template_data = {
        'subject': f'Your Donation to {donation.wish.animal.name}',
        'name': donation.first_name,
        'city': 'Denver'
    }
    message.template_id = 'd-397bbaeafd9e4933934aa42d1826d7fc'
    
    try:
        sg = SendGridAPIClient(config('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.body)    