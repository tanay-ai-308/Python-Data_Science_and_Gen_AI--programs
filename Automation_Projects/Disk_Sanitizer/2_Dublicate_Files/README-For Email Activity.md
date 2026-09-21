# Directory Sanitizer Email Sending (`SendMail`)

`SendMail(LogFileName, Log, Reciver)` sends one Directory Sanitizer execution report through Gmail SMTP. It is called after a cleanup run only when the command-line arguments designate an email recipient.

> The parameter is named `Reciver` in the code; this document uses “recipient.”

## Current arguments

| Argument      | Meaning                                                           |
|---------------|-------------------------------------------------------------------|
| `LogFileName` | Timestamp-derived filename, such as `Marvellous_<timestamp>.log`. |
| `Log`         | The report text returned by `CreateLog()`.                        |
| `Reciver`     | Recipient address placed in the message `To` header.              |

The command-line parser supplies an email when the third optional argument contains `@`, or when a fourth argument is supplied after a non-email third argument. It does not validate the resulting address.

## Gmail SMTP / App Password setup

The code uses Gmail's SMTP submission host (`smtp.gmail.com`) on port `587` with STARTTLS. The sending Gmail account must be able to use an App Password. In Gmail/Google Account settings, enable two-step verification for the sender account, create an App Password for mail, and use that App Password as the credential used by this script. App Password availability and organization policies are controlled by Google; see Google's official [App Password guidance](https://support.google.com/accounts/answer/185833?hl=en).

In the supplied version, both `Sender` and `AppPassword` are `None`. Email delivery therefore cannot work until they are provided. Supply them securely at runtime—for example, through environment variables or a secret manager—rather than replacing `None` with secrets in source code. Do not commit credentials, logs containing sensitive paths, or generated reports to source control.

## What `SendMail()` does

1. Sets the `From`, `To`, and subject headers. The subject is `Directory Sanitizer - Duplicate File Removal Report`.
2. Builds a plain-text report email body.
3. Calls `CreateLogFile(LogFileName, Log)` with no folder, creating a temporary log in the current working directory.
4. Reads that file as bytes, base64-encodes it as an `application/octet-stream` attachment, and attaches it using the log filename.
5. Connects to Gmail SMTP, issues `EHLO`, starts TLS, issues `EHLO` again, logs in with the configured sender and App Password, and sends the message.
6. Quits the SMTP session and removes the temporary log file.

If a separate log folder was supplied to the command, `DeleteDublicate()` also creates a saved copy there after calling `SendMail()`.

## Security and operational notes

- `Sender` and `AppPassword` are currently `None`; calling `server.login()` with them will fail. The code needs a secure configuration mechanism before email reporting can be used.
- STARTTLS protects the SMTP connection in transit after negotiation, but it does not protect a hard-coded password, the local temporary attachment, recipient access, or the report’s file paths.
- There is no exception handling around SMTP connection, authentication, sending, or temporary-file cleanup. A failure can terminate the scheduled run and may leave the temporary log behind.
- `server.send_message()` returning normally is not captured in the report. Although `--h` claims email delivery status is logged, `CreateLog()` has no email-status field. SMTP acceptance also does not prove final delivery to the recipient inbox.
- The body describes an “Errors encountered during execution” section, but `CreateLog()` does not produce one. The attachment only contains its implemented scan/deletion summary.
- The recipient address is not sanitized or fully validated by the code. Use trusted, valid addresses only.
