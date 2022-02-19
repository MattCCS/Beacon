
import subprocess


def get_public_ip():
    try:
        return subprocess.check_output(["curl", "ifconfig.me"]).decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(f"Something went wrong: {e}")
        return None


def main():
    print(get_public_ip())


if __name__ == '__main__':
    main()
