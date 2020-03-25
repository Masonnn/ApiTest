# while True:
#     test_num = input('请输入1-10之间的任意整数：')
#     if test_num.isdigit():
#         real_num = int(test_num)
#         if 10>=real_num>0=1:
#             print('输入在1-10之间')
#         else:
#             print('输入 不 在1-10之间')
#     elif test_num == 'quit':
#         print('退出')
#         break
#     else:
#         print('非法输入')
#         continue


# if len(test_str) == 10:
#     print('长度等于10')
# elif len(test_str) < 10:
#     print('长度小于10')
# else:
#     print('长度大于10')


print((i % 2 == 0) for i in range(1, 101))
