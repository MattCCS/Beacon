#!/usr/bin/env osascript -l JavaScript

function sendText(phoneNumber, textMessage) {
    console.log(phoneNumber, textMessage);
    var messages = Application("Messages");

    var targetBuddy;
    try {
        targetBuddy = messages.buddies.where({handle: phoneNumber}).first()
    } catch (err) {
        throw "Buddy not in contacts.";
    }

    messages.send(textMessage, {"to": targetBuddy});
}

function run(argv) {
    var phoneNumber = argv[0];
    var textMessage = argv[1];

    if (phoneNumber.length === 10) {
        phoneNumber = "+1" + phoneNumber;
    }

    sendText(phoneNumber, textMessage);
}
