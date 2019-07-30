import re
txt = "Kaguya. Kaguya sama. Kaguya sama Wants to be Confessed To. Kaguya Sama. Kaguya Sama Wants to be Confessed To."
txt = "." + txt
# print(txt)
print(re.findall(r"([^.]*?Kaguya sama[^.]*\.)",txt, re.IGNORECASE))