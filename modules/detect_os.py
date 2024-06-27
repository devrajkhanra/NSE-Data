import platform


def detect_os():
    os_name = platform.system()
    os_details = platform.uname()

    print(f"Operating System: {os_name}")
    print(f"Details: {os_details}")

    return os_name
