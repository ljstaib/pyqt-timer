# Changelog
This document outlines all notable changes to this project thus far. Inspired by https://keepachangelog.com/en/1.0.0/.

## [0.2.0] - 2022-11-17
### Added
- Ocean theme
- New preset sound: SciFi

### Changed
- Tweaked dark theme to better show text in time entry dialog
- Updated UI elements for a cleaner look

### Fixed
- Display bugs with new timer synchronization

## [0.1.9] - 2022-11-15
### In Progress
- Upon further use, the timer was having synchronization problems related to when the program was minimized/not in focus
- Work is currently being done to fix this issue

## [0.1.8] - 2022-11-10
### Fixed
- Custom sound implementation is fixed. To use a custom alarm sound, upload it with the "Add Custom..." button and use it with the "Custom" button under the "Sounds" menu.
- Accepted filetypes are still .mp3 and .wav

### Changed
- For time entry window, a user can now leave 1 or 2 out of the 3 fields blank and they will be saved as 0's. If all 3 fields are blank, an error message is displayed.
- Ex: only setting "5" under minutes will set the timer to 00:05:00 instead of leaving to an error.

## [0.1.7] - 2022-11-9
### Changed
- Sound menu updated. Still in progress and new presets need to be added.
- Custom sound implementation flawed at the moment and needs to be fixed.
  
### Fixed
- Verification: Timer runs perfectly fine in the background after more testing was done

## [0.1.6] - 2022-11-6
### Fixed
- "Change Alarm" button now tells user if they uploaded a custom audio file with a bad file type

## [0.1.5] - 2022-11-4
### Added
- "Change Alarm" button allows you to upload .mp3 or .wav files in place of the default alarm
  
### Fixed
- Alarm no longer needs to play in full before user is given back control of program
  
## [0.1.4] - 2022-11-3
### Fixed
- Updated light and dark modes

## [0.1.3] - 2022-11-2
### Added
- Menu button "Themes" under Settings with "Light" and "Dark" themes
  - Added 2 PyQT spreadsheet files
  - Still working on coloring (right now too contrasting)
  - Need to fix UI

## [0.1.2] - 2022-11-1
### Added
- Menu buttons "Settings" and "Set Time"
  - "Settings" is currently non-functional
  - "Set Time" replaced the "Set Time" button as a way to access the time input dialog

### Changed
- Made UI much more compact

## [0.1.1] - 2022-10-31
### Added
- Alarm sound when timer is done
- Error text for invalid input
- requirements.txt and .gitignore

### Changed
- UI slightly modified for time input dialog

### Fixed
- Input parsing should be working as intended

## [0.1.0] - 2022-10-29
### Added
- Created basic timer in form HH:MM:SS

### Changed
- UI, specifically of the timer

### Fixed
- Connected time entry dialog properly with main window

## [0.0.2] - 2022-10-28
### Added
- Custom dialog window so a user can enter hours, minutes, seconds
- Added a restart button to restart the timer with the current values

### Changed
- UI
- Name of "Reset" button to "Stop"

## [0.0.1] - 2022-10-27
### Added
- Started timer project!
- Created basic UI in PyQT6
- Users can enter a number of seconds for a basic timer