from plyer import notification # type: ignore

# Send notification
notification.notify(
    title='Reminder',
    message='Take a break and stretch',
    app_name='Python Notifier',
    timeout=10  # Duration in seconds
)

# This code uses the Plyer library to send a desktop notification.
# It creates a notification with a title and message, which will appear on the user's desktop.
# The notification will automatically disappear after a specified timeout period.
# Plyer is a cross-platform library that provides a simple API for accessing various platform-specific features,
# including notifications, file management, and more.

