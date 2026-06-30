# Behavioral Detection

Working with a Red Team member, two behavioral indicators consistently
appeared in malicious PowerShell scripts:

1.  Longer-than-normal executable content.
2.  Lower whitespace density caused by compression and obfuscation.

Rather than searching for known malware signatures, the solution
identified scripts whose behavior differed significantly from normal
administrative activity, making it useful even when signatures were
unavailable.
