import json

#think of standard way to list timed messages

messages = [
        ("Please feel free to tweet your projects, software, and hardware "
            "to https://twitter.com/amperture !! We'd all love to see your "
            "hard work!"),
        ("Remember that GhostyAmp loves playing with Christmas colors! Give "
            "him the !xmas command to watch him play!"),
        ("Ever thought about accepting Bitcoins on your stream but want "
            "tip notifications to pop up? Ask Amp about CoinJerk!")
]
with open("messages.json", "w") as f:
    json.dump(messages, f, indent=2)
