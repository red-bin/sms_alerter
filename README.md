# sms_alerter

```
curl http://192.168.83.49:5000/todo1 -d data='[{"DeviceID":"Device ID!", "ContactID":"Contact ID", "Message":"MASSAGE"}]' -X PUT
```

```
$ sqlite3 conntech.db
SQLite version 3.12.2 2016-04-18 17:30:31
Enter ".help" for usage hints.
sqlite> select * from statuses ;
Device ID!|Contact ID|Device ID! Contact ID MASSAGE|[{"DeviceID":"Device ID!", "ContactID":"Contact ID",
"Message":"MASSAGE"}]
```
