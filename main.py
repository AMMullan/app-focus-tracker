#!/usr/bin/env python3

# adapted from https://github.com/gimmickyboot/AppInFocus

import time
from dataclasses import dataclass
from datetime import datetime

from AppKit import NSWorkspace


@dataclass
class AppInfo:
    name: str
    bundle_id: str
    path: str
    pid: int
    localized_name: str


def get_app_info(app_info_dict: dict) -> AppInfo:
    return AppInfo(
        name=app_info_dict.get('NSApplicationName', 'Unknown'),
        bundle_id=app_info_dict.get('NSApplicationBundleIdentifier', 'Unknown'),
        path=app_info_dict.get('NSApplicationPath', 'Unknown'),
        pid=app_info_dict.get('NSApplicationProcessIdentifier', 0),
        localized_name=app_info_dict.get('NSApplicationLocalizedName', 'Unknown'),
    )


def format_app_info(app: AppInfo, timestamp: str, duration: float | None = None) -> str:
    base_info = f'{app.name} (Bundle: {app.bundle_id}, PID: {app.pid})'

    if duration is not None:
        return f'App Changed: {base_info} at {timestamp} (previous app was active for {duration:.1f}s)'

    return f'Initial App: {base_info} at {timestamp}'


def win_focus() -> None:
    current_app: AppInfo | None = None
    app_start_time: datetime | None = None

    while True:
        active_app_info = NSWorkspace.sharedWorkspace().activeApplication()
        active_app = get_app_info(active_app_info)

        if current_app is None or active_app.name != current_app.name:
            now = datetime.now()
            timestamp = now.strftime('%H:%M:%S')

            if current_app is not None:
                duration = (now - app_start_time).total_seconds()
                print(format_app_info(active_app, timestamp, duration))
            else:
                print(format_app_info(active_app, timestamp))

            current_app = active_app
            app_start_time = now

        time.sleep(1)


if __name__ == '__main__':
    try:
        win_focus()
    except KeyboardInterrupt:
        print('\nStopped.')
