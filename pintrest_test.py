from py3pin.Pinterest import Pinterest


email="um.waqas.khan@gmail.com"
pass_word="ARuFT7j.J!LRPxy"


user_name="umwaqaskhan"
pinterest = Pinterest(email=email,
                      password=pass_word,
                      username='umwaqaskhan',
   )

pinterest.login()

# pinterest.upload_pin(board_id="", section_id=None, image_file='news/AI_represents_a_01.jpg',
#                                 description='this is auto pin', title='a bot did this', link='https://www.google.com/')

# data=pinterest.pin(board_id="", section_id=None, image_url="https://images.pexels.com/photos/16796362/pexels-photo-16796362/free-photo-of-pic-du-midi-de-bigorre-in-pyrenees-with-observatory-at-the-top.jpeg?auto=compress&cs=tinysrgb&w=1600&lazy=load",
#                          alt_text="test", description="this is auto pi", title="this is auto pi", link="https://www.google.com/")
# print(data)


pinterest.delete_pin(pin_id="1148277236222894858")

print("done")