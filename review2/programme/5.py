# 把输入的待处理字符串前后的空格字符删除
aStr = input().strip()
# 把输入的要删除的字符前后的空格字符删除
delete_chars = input().strip()
print("result:",
      aStr.replace(delete_chars.upper(), "").replace(delete_chars.lower(), ""))
