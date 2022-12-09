#
# from PIL import Image
#
# foo = Image.open('favicon (1).ico')  # My image is a 200x374 jpeg that is 102kb large
# foo.size  # (200, 374)
#
# # downsize the image with an ANTIALIAS filter (gives the highest quality)
# foo = foo.resize((32, 32), Image.ANTIALIAS)
#
# foo.save('favicon (2).ico', quality=100)  # The saved downsized image size is 24.8kb
#
# foo.save('favicon (2).ico', optimize=True, quality=100)  # The saved downsized image size is 22.9kb
