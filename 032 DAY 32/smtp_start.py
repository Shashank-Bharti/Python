import smtplib 

my_email = "smtp.testpersonal2004@gmail.com"
my_pass = #truncated

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()

connection.login(user=my_email,password=my_pass)
connection.sendmail(
    from_addr=my_email,to_addrs=["techra.byte54@gmail.com","shashankbharti899@gmail.com"],
    msg="Subject:test\n\nKYA HAAL CHAL!")
connection.close()
print("Email sent successfully")