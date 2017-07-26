# tianchi_gy_contest
比赛链接：https://tianchi.aliyun.com/competition/introduction.htm?spm=5176.100066.0.0.3f6e7d83JQwooH&raceId=231598
初赛截至日期：8.12
比赛截至之前大家可以自行提交，8月初组织大家组队（如果有望进入复赛的话\xiao cry）

关于code：输入不是指程序运行的参数而是指需要依赖的数据，我已经为各位coder分配了代码插槽(请各放各的文件夹中),并且自备start.sh脚本（可以一行命令，运行不了我会找你的...），方便别人使用，另外就是不限语言但是建议用python。

关于update: 如果发现有好的建议或代码实现问题请跟我联系并更新wiki, 每次update完毕都要把代码和中间产出(mid文件夹)的内容都同步到github上。

关于data: data都是sample数据,规范格式和命名使用,如果需要使用数据请大家通过官方下载或者运行其他同学的代码生成。

一起努力拿个好成绩

***

1. etl(昕元 润冶)

1.1异常travel_time过滤(考虑最近道路与最近时间)

输入：data/origin/*

输出: data/mid/etl.data
(data/mid/etl.data存储格式与gy_contest_link_traveltime_training_data.txt 相同)

昕元: 遍历每个时间片进行topo维度数据清洗（一段时间片观察其topo通行时间合理性）
润冶: 遍历每条link进行时间维度数据清洗（一条links观察全段时间通行时间合理性）

***

2. feat(明慧 慧强)

2.1时间特征
2.2道路特征

输入:
1.data/origin
2.data/mid/etl.data

输出:data/mid/feat.data(见code)


***

3. train_eval(腾飞 泽军)

3.1 train:每个links训练两个XGBmodel并调参数(一个为5月份特征数据训练出的model(用于评估)一个为全数据训练的model)

输入：data/mid/feats
输出：data/mid/model/[linkid].model, data/mid/model/evaluate_[linkid].model

3.2 evaluate:

输入: 1.data/mid/model 2.data/origin/gy_contest_link_info.txt
输出(最后预测数据＋五月份8:00-10:00的MAPE值): data/res/output.data ＋ double(后台输出)
***




