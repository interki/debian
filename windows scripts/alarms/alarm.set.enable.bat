Schtasks /change /st 05:15 /tn "Alarm\Volume Up"
Schtasks /change /st 05:16 /tn "Alarm\Un-mute"
Schtasks /change /st 05:20 /tn "Alarm\a"
Schtasks /change /st 05:30 /tn "Alarm\al"

Schtasks /change /tn "Alarm\a" /ENABLE
Schtasks /change /tn "Alarm\al" /ENABLE
Schtasks /change /tn "Alarm\Volume Up" /ENABLE
Schtasks /change /tn "Alarm\Un-mute" /ENABLE
PAUSE
