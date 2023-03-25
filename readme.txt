核心配置文件yolov3.cfg在cfg文件夹下

数据集相关文件存放在data文件夹下
其中/samples存放的是测试图片
/VOCDevkit里包括VOC2007，里面是数据集图片和标注的xml文件，以及数据集的分割
另外，/VOCdevkit里还有归一化、resize等操作代码
data目录下还有room.data和room.names等必要配置文件

output文件夹下是测试集的测试结果
weights目录是原始的权重文件(yolov3.pt)、模型效果最好的权重文件（best.pt）和最后一轮的权重文件(last.pt)
不过因为以上文件过大，没有包含在内

主目录下
train.py 训练入口
detect.py 批量测试
models.py  模型加载
kmeans.py 聚类算法生成anchors box大小