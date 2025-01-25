import subprocess

def ping(host):
    # Run the ping command
    result = subprocess.run(['ping', '-c', '4', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Decode the output and error
    output = result.stdout.decode('utf-8')
    error = result.stderr.decode('utf-8')
    # Return the result
    if result.returncode == 0:
        return output
    else:
        return error

if __name__ == "__main__":
    host = "google.com"  # Replace with the desired host
    response = ping(host)
    print(response)
