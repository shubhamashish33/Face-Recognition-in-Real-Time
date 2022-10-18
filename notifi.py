# from win10toast import ToastNotifier
# toast = ToastNotifier()
# toast.show_toast(
#     "Notification",
#     "Notification body",
#     duration=10,
#     threaded=True,
# )
# toast.close()


from winotify import Notification,audio

toast = Notification(app_id="MyApp", title="MyApp", msg="Hello World!",duration="short")

toast.set_audio(audio.Default,loop=False)

toast.show()
