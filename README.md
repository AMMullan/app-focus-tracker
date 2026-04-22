# App Focus Tracker

A macOS utility that monitors and logs application focus changes, providing detailed information about which applications are active and for how long.

Based on https://github.com/gimmickyboot/AppInFocus

## Features

- **Real-time monitoring**: Tracks active application changes every second
- **Detailed app information**: Displays app name, bundle ID, process ID, and localized name
- **Duration tracking**: Shows how long each application was active
- **Timestamp logging**: Records when each focus change occurred

## Requirements

- macOS (uses AppKit framework)
- Python 3.10+
- uv package manager

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   uv add pyobjc
   ```

## Usage

Run the script using uv:

```bash
uv run main.py
```

The output will show:
- Initial application when starting
- Each application change with timestamp
- Duration the previous application was active
- Detailed app metadata (bundle ID, PID)

### Sample Output

```
Initial App: Visual Studio Code (Bundle: com.microsoft.VSCode, PID: 1234) at 14:30:15
App Changed: Safari (Bundle: com.apple.Safari, PID: 5678) at 14:30:42 (previous app was active for 27.3s)
App Changed: SecurityAgent (Bundle: com.apple.SecurityAgent, PID: 9012) at 14:31:05 (previous app was active for 23.1s)
```

## Use Cases

- **Productivity tracking**: Monitor time spent in different applications
- **Security monitoring**: Track unexpected application launches (e.g., SecurityAgent)
- **Development debugging**: Understand application focus behavior
- **Time management**: Analyze application usage patterns

## Stopping the Script

Press `Ctrl+C` to stop monitoring.

## Notes

- The script requires macOS accessibility permissions if monitoring system applications
- Bundle IDs help identify applications that may have generic display names
- The tool runs continuously until manually stopped
