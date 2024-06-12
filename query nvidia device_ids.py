import requests

def check_device_in_driver(driver_version, device_id):
    url = f'https://us.download.nvidia.com/XFree86/Linux-x86_64/{driver_version}/README/supportedchips.html'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return

    page_text = response.text

    if device_id in page_text:
        print(f"Device ID {device_id} is supported by driver version {driver_version}.")
    else:
        print(f"Device ID {device_id} is NOT supported by driver version {driver_version}.")

if __name__ == "__main__":
    driver_version = input("Enter the driver version: ")
    device_id = input("Enter the device ID: ").upper()  # Convert input to uppercase
    check_device_in_driver(driver_version, device_id)
