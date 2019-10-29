# ScriptsPublic
Scripts I write for different scenario.

## [deleteReparsePoints](./deleteReparsePoints.py)
Windows 10 started creating reparse points on all OneDrive files/folders after a fall creator's update. It's part of the feature that breaks usage of that folder in mutliple OSs, an issue I described on my [website](http://www.jeangjenq.com/windows-10-delete-reparse-points-in-subdirectories/).

This scripts deletes all reparse points in OneDrive folders by looping fsutill command below on every single files/folder.
```batch
fsutil reparsepoint delete "C:\Path\To\Folder"
```
