import random
import string
# 验证码

print(''.join(random.sample(string.ascii_letters + string.digits, 4)))
