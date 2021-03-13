## 测试端口

```Python
import telnetlib
tn = telnetlib.Telnet(host="192.168.111.128", port="22", timeout=4)
result = tn.read_until(b"\n", timeout=5).decode()
import re
if re.match(r"ssh", result.lower()):
   print("host存活")
```

如果`telnetlib.Telnet`没有爆错说明端口正常