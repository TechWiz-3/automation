import yagmail

yag = yagmail.SMTP('programmingplus1@gmail.com')
contents = [
    "This is the body, and here is just text http://somedomain/image.png",
    "You can find an audio file attached.", '/local/path/to/song.mp3'
]
yag.send('programmingplus1@gmail.com', 'Test', contents)

# Alternatively, with a simple one-liner:
#yagmail.SMTP('mygmailusername').send('to@someone.com', 'subject', contents)
