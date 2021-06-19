# Assignment
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
* Notes and Hints
1. Check sample1.txt for sample input data.
2. Think about edge cases
3. Think about how to write the application with constant memory consumption regardless of file size.
4. Think about how to utilise multiple CPU cores.
5. Applicationcan be either a console app or a Web API.
6. The submitted code should be production-grade code. Your submission will be judged on code quality as well as correctness
