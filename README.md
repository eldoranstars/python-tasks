## HOW change PATH in all files.
change "#!Your/Python/Path" to path "which python" on your PC in script below.

```
sed -i 's/#!\/c\/Users\/AngryBear\/AppData\/Local\/Microsoft\/WindowsApps\/python/#!Your\/Python\/Path/g' *py
```

then use it!
