from Heuristic import ACO  # 导入ACO算法
from Draw import GridFig, IterationGraph  # 导入栅格图、迭代图的绘制模块
from Map import Map  # 导入地图文件读取模块
import matplotlib.pylab as mpl

# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
m = Map()
m.load_map_file('input/map.txt')  # 读取地图文件
pathList = list([])
startPoints = [[0, 1], [3, 17], [37, 38]]
endPoints = [[25, 23]]
endPoint = endPoints[0]
gridFig = GridFig(map_data=m.data)  # 初始化栅格图绘制模块
gridFig.save('output/GridGraph.jpg')  # 保存地图栅格图数据为GridGraph.jpg
for i in range(len(startPoints)):
    print("第" + str(i + 1) + "条路径: 起点:[" + str(startPoints[i][0]) + "],[" + str(
        startPoints[i][1]) + "]终点:[" + str(
        endPoint[0]) + "],[" + str(endPoint[1]) + "]")
    # startPoint = [0, 1]
    start = startPoints[i].copy()
    end = endPoint.copy()
    start.reverse()
    end.reverse()
    # 初始化ACO，不调整任何参数的情况下，仅提供地图数据即可，本行中数据由Map.data提供
    aco = ACO(map_data=m.data, start=start, end=end, max_iter=120, ant_num=50)
    aco.run(show_process=True)  # 迭代运行
    # gridFig = ShanGeTu(map_data=m.data)  # 初始化栅格图绘制模块
    # gridFig.save('output/GridGraph.jpg')  # 保存地图栅格图数据为GridGraph.jpg
    # gridFig.draw_way(aco.way_data_best)
    path = aco.way_data_best
    pathList.insert(0, path)
    # gridFig.save('output/result.jpg')  # 保存结果栅格图数据为result.jpg
    # gridFig.show()
    iterationFig = IterationGraph(data_list=[aco.generation_aver, aco.generation_best],  # 绘制数据: 每代平均、每代最优路径信息
                                  style_list=['--r', '-.g'],  # 线型 (规则同plt.plot()中的线型规则)
                                  legend_list=['每代平均', '每代最优'],  # 图例 (可选参数，可以不写)
                                  xLabel='迭代次数',  # x轴标签，默认“x”
                                  yLabel='路径长度'  # y轴标签，默认“y”
                                  )  # 初始化迭代图绘制模块
    # iterationFig.save('output/IterationGraph.jpg')  # 迭代图
    iterationFig.show()

result = GridFig(map_data=m.data, startPoints=startPoints, endPoints=endPoints)  # 初始化栅格图绘制模块
for i in range(len(pathList)):
    result.draw_way(pathList[i])  # 栅格图中依次加入路径
result.save('output/result.jpg')  # 保存结果栅格图数据为result.jpg
result.show()
