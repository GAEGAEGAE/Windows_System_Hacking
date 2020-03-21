sample = open('sample.m3u', "w")

contents = "A"*1008 + "B"*4 + "C"*4

sample.write(contents)

sample.close()