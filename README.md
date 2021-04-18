# EmailPlayGround

## email_sender.py

This is the python file which send the simple text email. In this smtp module and EmailMessage class we are using.

* EmailMessage: It is the dictionary of headers which are using to wrap the sender name, subject of email and content to be send through email. 
* smtplib: It is the module which has SMTP object which opens the connection for smtp protocol mail server. I am using the google mail server. 587  is the default mail submission port. When an email client or outgoing server is submitting an email to be routed by a proper mail server, it should always use SMTP port 587 as the default port.
This port, coupled with TLS encryption, will ensure that email is submitted securely.

- with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp: Opens the connection of mail server and close when is not in use.

- smtp.ehlo(): Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server to identify itself when connecting to another email server to start the process of sending an email. It is followed with the sending email server's domain name. The EHLO command tells the receiving server it supports extensions compatible with ESMTP.

- smtp.starttls(): starttls encrpts the communication between two machines. Gmail by default always use TLS.

- smtp.login('me@gmail.com','me_pass'): Login in mail server for sender.
- smtp.send(email): sends out the EmailMessage instance or object.

## email_sender_.py
To attach the html file for dynamic environment.

