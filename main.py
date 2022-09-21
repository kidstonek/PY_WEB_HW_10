from models import Record, Contact, EmailContact, PhoneContact, AddressContact

rec = Record(first_name='Steve', last_name='Buscemi').save()

rec1 = EmailContact(contact=rec)
rec1.email = 'asd@gmail.com'
rec1.save()
