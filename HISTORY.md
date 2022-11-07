# Changelog
This document outlines all notable changes to this project thus far. Inspired by https://keepachangelog.com/en/1.0.0/.

## [Unreleased]
- Settings menu button
- Preset alarm sounds
- Need error checking with alarm sound file upload
- Alarm needs to be able to run in the background (when app is not in focus)
- More?

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
- Started study timer project!
- Created basic UI in PyQT6
- Users can enter a number of seconds for a basic timer