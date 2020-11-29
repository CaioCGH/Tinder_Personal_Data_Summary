## Tinder_Personal_Data_Summary

This scrip uses a specific JSON report file sent by Tinder in 11/2020. It may not work if Tinder changes data shape.

- Request your data from Tinder in https://www.help.tinder.com/hc/en-us/articles/115005626726-How-do-I-request-a-copy-of-my-personal-data-
This may take a few days.
- Extract components and have `data.json` in the same folder as this repository `summary_builder.py`
- Run `python3 summary_builder.py`
- It will show summary in terminal and write to a file named `my_summary.json`.