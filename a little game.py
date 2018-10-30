from random import Random
def age_choices(nums=2):
    age_lists = []
    age_all_choices_nums = '0123456789'
    age_length = len(age_all_choices_nums)-1
    random = Random()
    for i in range(nums):
        age = age_all_choices_nums[random.randint(0,age_length)]# 这里用到字符串的切片
        age_lists.append(age)
    age_str = ''.join(age_lists)
    return int(age_str)
age_of_men = age_choices()
print(age_of_men)
i = 0
while i <= 3:
    b = 1
    while b:
        try:
            a = int(input('请输入你猜测的年龄:'))
        except(IOError,ValueError):
            print('请重新输入你的年龄(必须是正整数)')
        else:
            b = 0 if isinstance(a, int) else 1
    if age_of_men == a:
        game_over = input('恭喜用户猜对了，请输入（y/n）按y退出游戏，按n游戏继续:')
        print('该用户年龄' + game_over + "岁")
        if game_over == 'y':
            print('---------game over--------')
            break
        elif game_over == 'n':
            age_of_men = age_choices()
            print('---------continue--------')
    elif age_of_men!= a:
        i += 1
        print('不好意思你没有猜对哦！请继续加油')
        if i > 2:
            print('你已经猜错三次了')
            come_on = input('请输入（y/n）按y退出游戏，按n游戏继续:')
            if come_on == 'n':
                age_if_men = age_choices()
                i = 0
                print('游戏继续')
            else:
                print('游戏结束')
                break
