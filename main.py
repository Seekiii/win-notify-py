from winotify import Notification, audio
import os

path = os.path.abspath(os.getcwd())

img = "img.png" #IMG name

notify = Notification(
	app_id="Seekii", 
	title="How to make windows 10 notification in python.",
	msg="Follow me on github:",
	duration="long",
	icon=r"{}\{}".format(path,img)
)

notify.add_actions(label="Open Github",launch="https://github.com/seekiii") #Add button in notification.

notify.set_audio(audio.Default, loop=False) #Make sound.
notify.show() #Show notification.