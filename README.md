## Overview
* Given a text file each line in the text file is individual record and can be processed independently, file size can vary from KB to GB.
* Data is ordered by date in ascending order.

## Requirements
* Input format: path to file, From date time, to date time
* Output format: 
```
[
  {
    "eventTime":"2000-01-01T03:05:58Z",
    "email":"test123@test.com",
    "sessionId":"97994694-ea5c-4da7-a4bb-d6423321ccd0"
  },
  {
    "eventTime":"2000-01-01T04:05:58Z",
    "email":"test456@test.com",
    "sessionId":"97994694-ea5c-4da7-a4bb-d6423321ccd1"
  }
]
```







