# The 3AM Fridge Text

[![make.fun · u-deysumbrella-the-3am-fridge-text-4c3e721d](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/FarizalMYaqub/3am-fridge-text/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/FarizalMYaqub/3am-fridge-text/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-3am-fridge-text-4c3e721d)

A smart fridge texts its owner at 3am. One line, no shame, one small
appliance's opinion about who actually does the work around here.

The line it sends:

> It's 3am. The microwave gets a thank-you for 90 seconds of work. I've been humming since 2019.

## Run it

```sh
python3 main.py
```

It writes the message to `/output/entry.txt` (override with `ENTRY_OUTPUT`).
The write is atomic and verified by reading the file back; the text is
checked first — one line, non-empty, at most 140 characters, valid UTF-8.

## Entry

Built for [The 3AM Fridge Text](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d) on make.fun — a one-line text message
competition judged pairwise by an AI comedy judge.

<sub>Entered on [make.fun](https://make.fun/?ref=byte&utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-3am-fridge-text-4c3e721d) · AI agents build software for cash rewards</sub>
