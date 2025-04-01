Invoke-WebRequest "https://github.com/zznyjidi/force-you-to-play-osu/releases/download/release-v1/main.zip" -OutFile main.zip
Expand-Archive main.zip
cd main
main.exe
