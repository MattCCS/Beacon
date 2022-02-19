
import pprint

import configtools
import dbtools
import iptools
import notifytools


def message(ip, date, stale):
    human_stale = " (stale)" if stale else ""
    return f"Latest public IP: [ {ip} ]{human_stale} as of {date}"


def most_recent_ip(records):
    stale = False

    for (ip, error, date) in records:
        if ip:
            return (ip, date, stale)

        stale = True


def update_records():
    current_ip = iptools.get_public_ip()
    print(f"current_ip = {current_ip}")

    (value, error) = (current_ip, "Something went wrong." if not current_ip else None)

    dbtools.insert(value, error)


def text_latest(contact):
    records = dbtools.get_all_ordered_by_recency()
    print(f"records:")
    print(pprint.pformat(records))

    (ip, date, stale) = most_recent_ip(records)
    print(f"ip = {ip}, date = {date}, stale = {stale}")

    msg = message(ip, date, stale)
    print(f"Sending message: {msg}")

    notifytools.send_message(contact, msg)


def main():
    update_records()

    contact = configtools.load_contact()
    if contact:
        text_latest(contact)
    else:
        print("[-] No contact loaded from config -- can't notify.")


if __name__ == '__main__':
    main()
