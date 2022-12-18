# statatics mp3 files duration in same directory

```py
# pip install mutagen
import sys
import os
from mutagen.mp3 import MP3

def mutagen_length(path):
    try:
        audio = MP3(path)
        length = audio.info.length
        return length
    except:
        return None

if __name__ == '__main__':
	assert os.path.isdir(sys.argv[-1])
	total_duration = 0
	for root, dirs, files in os.walk(sys.argv[-1]):
		for file in files:
			total_duration += mutagen_length(os.path.join(root,file))
		
	print("total duration minutes: " + str(total_duration/60))
```
