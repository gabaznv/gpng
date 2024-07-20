# g[abai]png 

The greatest extensions for images for those who want to save storage or want to waste storage

# How good is gpng?

<h3>Saving storage</h3>

| Image | .png | .gpng | Saved Storage |
| ----- | ---- | ----- | ------------- |
| 720p Forest | 4MB | 1MB | 75% |
| 1080p Screenshot | 111KB | 53KB | 52.2523% |
| 4K Burj Khalifa | 6MB | 4MB | 33.3333% |

<h3>Wasing storage</h3>

| Image | .png | .gpng | Wasted Storage |
| ----- | ---- | ----- | -------------- |
| 720p Forest | 4MB | 22MB | 450% |
| 1080p Screenshot | 111KB | 13MB | 11611.7% |
| 4K Burj Khalifa | 6MB | 102MB | 1600% |

# How does it work

When the program converts the png to gpng it archives it, and when you open the image the gpng file will unarchive somewhere in the memory

# Usage

When using to Save Storage
```bat
convert.exe image.png image.gpng true
```

When using to Waste Storage
```bat
convert.exe image.png image.gpng false
```

When trying to open image
```bat
convert.exe image.gpng
```

When trying to convert gpng to image
```bat
convert.exe image.gpng image.png
```

<h3>⚠️If you try to run the program without the boolean then it will waste storage⚠️</h3>

# Examples

```bat
convert.exe C:\Users\gabaihype\Desktop\gpng\dubai4k.png dubai4k.gpng true
convert.exe dubai4k.gpng
```

```bat
convert.exe C:\Users\gabaihype\Desktop\gpng\dubai4k.png dubai4k.gpng false
convert.exe dubai4k.gpng
```

# Why
i dont even know, i just had the idea of making this

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/P5P610O2U7)
