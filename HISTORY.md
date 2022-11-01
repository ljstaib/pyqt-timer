# Changelog
This document outlines all notable changes to this project thus far. Inspired by https://keepachangelog.com/en/1.0.0/.

## [Unreleased]
- Settings menu button
  - Custom alarm sounds
  - Switch between light/dark theme
- Need to fix alarm sound needing to play in full before user is given control of program again
- More?

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