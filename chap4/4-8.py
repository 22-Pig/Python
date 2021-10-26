PASS = 60

score = int(input('请输入成绩: '))
print('你输入的成绩是{}'.format(score))

if score < PASS:
    print('很遗憾，这个成绩没有及格。')
else:
    print('祝贺你，这个成绩及格了。')
print('再见')
