# TA-line-notify-8-x
Splunk Line notify TA that is compatible with Splunk 8.x (origin from https://splunkbase.splunk.com/app/4614/)
**To be used correctly, please ensure the Line Notify folder name is `TA-line-notify-8-x`**

## Installation Guide

Method 1 - Using git clone

1. `cd $SPLUNK_HOME/etc/apps`
2. `git clone https://github.com/dogqqq/TA-line-notify-8-x.git`
3. restart/start the Splunk


Method 2 - Download from github

1. Download directly from github page
2. Unzip the `.zip` file you just downloaded
3. Rename `TA-line-notify-8-x-main` to `TA-line-notify-8-x`
4. Move the whole folder to `$SPLUNK_HOME/etc/apps/`
5. restart/start the Splunk

## Use Guide

- When saving inline search to alert, choose Line Notify Alert
- Line token
  -  Must sign up and get `access token` from https://notify-bot.line.me/ first
- Message kind
  - `Raw`
    - Send event notify with _raw data
    - Unnecessary to fill `Fields`
  - `Custom`
    - Send event notify with specific field
    - Necessary to fill the `Fields`
