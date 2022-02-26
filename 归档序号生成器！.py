
for Times in range(1000000000):
  issuesType = int(input("Bug修复：1\n设定引入：2\n数据调整：3\n请选择issue类型："))
  if issuesType == 1:
    IssuesType = "Bug修复"
    Archiveformat = "修复了的Bug"
    break
  elif issuesType == 2:
    IssuesType = "设定引入"
    Archiveformat = ""
    break
  elif issuesType == 3:
    IssuesType = "数据调整"
    Archiveformat = ""
    break
  else:
    issuesType=0
    print ("issue类型赋值失败，请重试")
# 判断issue类型，如果不是输入1,2,3这3个数值就提示重新输入
for Times in range(1000000000):
  issueOurin = int(input("外部单子：1\n内部单子：2\n请选择issue位置："))
  if issueOurin == 1:
     IssueOurin = "外"
     break
  elif issueOurin == 2:
     IssueOurin = "内"
     break
  else:
     IssueOurin = 0
     print ("issue位置赋值失败，请重试")
# 判断issue是内部还是外部，如果不是输入1,2这2个数值就提示重新输入

if issuesType<=3 or issuesType>=1 and issueOurin>=1 or issueOurin<=2:
    # 判断前边两个输入条件是否满足，虽然前边已经优化过，现在没必要在这里判断了，但是我懒得的改动了
    SerialNum = int(input("输入issue归档起始序号："))
    VerisonNun = str(input("输入版本号0.99."))
    IssuesNum = int(input("请输入issue归档单号："))
    for Times in range(1000000000):
       RangeTimes = int(input("输入循环次数（数值不能超过1000）:"))
       # 防止手贱输入超过1000以上的数值导致cpu着火
       if RangeTimes<=1000:
        for i in range(SerialNum, SerialNum + RangeTimes + 1):
           print("|" + str(i) + "" + "|" + "" + "(" + str(IssuesType) + ")" + str(Archiveformat) + "                                       " + "[" + str(IssueOurin) + "部Issue#" +str(IssuesNum)+ "] " + "||0.99.90" + str(VerisonNun) + "|")
           data = open("归档预备.md", 'w+')
           # 打印结果
           for i in range(SerialNum, SerialNum + RangeTimes + 1):
               # 我没想到i要怎么用英语表述，是用来输出的中间量
              print("|" + str(i) + "" + "|" + "" + "(" + str(IssuesType) + ")" + str(Archiveformat) + "                                       " + "[" + str(IssueOurin) + "部Issue#" +str(IssuesNum)+ "] " + "||0.99.90" + str(VerisonNun) + "|", file=data)
           data.close()
        print("输出完成，请检查此py文件根目录下的'归档预备.md'文件")
        # 打印结果到此py文件下目录的“归档预备.md”
        break
        # 跳出循环，防止循环1000000000次，然后自动退出程序
       else:
          print("输入的循环次数过高，请重试")
          # 防止手贱输入超过1000以上的数值导致cpu着火
          p=p+1
          x=x+1
          # md我到底写这两行要干嘛
else:
   exit(0)
   # 此处应该没用了