import random
gold=0
count1=0
while True:
    choice = input("是否要玩猜骰子游戏？需要消耗5金币，Y（是）N（否）")
    match (choice):
        case 'Y':
            if (gold < 5):
                choice2 = input("对不起，金币不足，是否选择充值？Y(是)N（否）")
                if (choice2 == 'Y'):
                    recharge_amount=True
                    while recharge_amount:
                        count = int(input("请选择您要充值的金币数量，必须是10的倍数才可以："))
                        if (count % 10 != 0):
                            print("对不起充值的金币数量不合法，必须为10的倍数才可以,请重新你输入！")
                        elif (count % 10==0):
                            gold += count*2
                            print("充值成功!")
                            recharge_amount = False
                elif (choice2 == 'N'):
                    print("感谢您的参与，游戏结束！")
                    print("您现在的金币数量为：" + str(gold))
                    print("共玩了" + str(count1) + "局游戏")
                    break
                else:
                    print("输入不合法，请输入Y或者N")
            elif(gold>=5):
                print("您现在的金币数量为："+str(gold))
                gold -= 5
                print("消耗5金币，开始游戏赠一个金币！")
                gold+=1
                print("您现在的金币数量为：" + str(gold))
                print("游戏开始！")
                count1+=1
                dice1=random.randint(1,6)
                dice2=random.randint(1,6)
                result=dice1+dice2
                guess = input("请猜大小（超出6点以上为大，否则为小,请输入中文‘大’或‘小’，否则视为猜错）：")
                match(guess):
                    case '大':
                        if(result>6):
                            print("恭喜您猜对了！奖励金币两枚")
                            gold+=2
                            print("您现在的金币数量为：" + str(gold))
                        elif(result<=6):
                            print("很遗憾您猜错了")
                            print("您现在的金币数量为：" + str(gold))
                    case '小':
                        if (result <= 6):
                            print("恭喜您猜对了！奖励金币两枚")
                            gold += 2
                            print("您现在的金币数量为：" + str(gold))
                        elif (result > 6):
                            print("很遗憾您猜错了")
                            print("您现在的金币数量为：" + str(gold))
                    case _:
                        print("输入不合法，视为您猜错了！")
                        print("您现在的金币数量为：" + str(gold))
        case 'N':
            print("退出游戏！")
            print("您现在的金币数量为：" + str(gold))
            print("共玩了"+str(count1)+"局游戏")
            break
        case _:
            print("输入不合法，请重新输入：")





