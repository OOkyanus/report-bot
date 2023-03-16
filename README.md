# Report-Bot
In order to use report-bot you should:
1. Get an App Password for your Gmail account.
>An App Password is a 16-digit passcode that gives a less secure app or device permission to access your Google Account. App Passwords can only be used with accounts that have 2-Step Verification. See [Google Account Help](https://support.google.com/accounts/answer/185833?hl=en) for detailed information.
>
>**In order to set an App Password:**
>> 1.  Go to your  [Google Account](https://myaccount.google.com/).
>> 2.  Select  **Security**.
>> 3.  Under "Signing in to Google," select  **App Passwords**. You may need to sign in. If you don’t have this option, it might be because 2-Step Verification is not set up for your account.
>>4.  At the bottom, choose  **Select app**  and choose the app you're using. Then choose the device you’re using with **Select device** and tap **Generate**.
>>5.  Follow the instructions to enter the App Password. The App Password is the 16-character code in the yellow bar on your device.
>>6.  **Copy** your App Password then tap  **Done**.
2. Save your login info through, `setReporterInfo(path)` only once. 
>Use your Gmail address and your (copied) App Password for _"sender email"_ and _"app-password"_ input fields respectively. The _"receiver email_" can be set as any email address. The registered receiver email address will be used as the default address which the notifications will be sent to (You can later change the receiver email). You can use the same address for both _"sender email"_ and _"receiver email"_. Finally enter the default subject to the _"subject"_ input field (You can again change the subject later).

> **Note:** `setReporterInfo(path)` is going to save your info as "RPRTR . INFO" to the specified path. The ".INFO" extension is faux, it is just a pickled dictionary. Your info is stored as a ".INFO" file only to make it not visible as a plain text. Therefore, you should be aware of lack of credential security when using report-bot. 
4. Instantiate report-bot with `bot=Reporter(path)`, where path argument is the directory that contains your "RPRTR . INFO".
5. Use `bot.sendmail(text_message='a message',img_file='...path2image/imagename.extention', subject='My Extremely Original Subject', receiver_email='receiver@anymail.com')` to send messages. 
> **Note:** If you do not specify _subject_ and _receiver_email_ arguments, the default values are going to be used. You do not have to attach an image to send an email, you can leave the argument as _None_.
