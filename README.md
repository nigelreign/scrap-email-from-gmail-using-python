# Script to allow user to get emails using python

### Step 1
Before running the script make sure you have two factor authentication disabled on your targeted email

### Step 2
Allow less secure apps

### Step 3
Add your email address and password on line 8 and 9

```
username = "test@gmail.com"
password = "tets@123"
```

### Step 4
Enter the email address to filter with on line 18

```
emails_from = "test@nigel.zulu"
```

### Step 5
Set the characters before and after the targeted character on line 20 and 21

```
char_before_target_text = "EcoCash Reference:"
char_after_target_text = "\n"
```

### Run the script

```
python3 script.py
```

### What you can do from the script:
* add the email address you want to get emails from
* specify the number of emails you want to retrieve
* get emails sent by one specific email address
* search for certain text inside the email content
