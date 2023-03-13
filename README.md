# Awesome-K210
收集关于K210的MaixPy开发和SDK IDE开发等的软硬件入门资料，帮助初学者快速了解、学习和入门K210。

K210 是 RISC-V 64 位双核处理器，集成了可运行神经网络算法的硬件 IP核，以及其它常用外设。其可直接跑 kmodel 格式模型，此模型可从 TensorFlow 模型转换为 TFlite 模型、TFLite 模型转换为 K210 的 kmodel 模型 而得到。

## 有关K210学习和实例的github仓库枚举

### kendryte 官方 Github 仓库

-   https://github.com/kendryte —— 梦开始的地方，源头，包括 K210 的 c 语言开发 IDE 及其丰富的历程 SDK，包含裸机和 FreeRTOS 两版。
-   https://github.com/kendryte/kendryte-standalone-demo —— c 语言开发 IDE 下的丰富历程，kendryte 名下另有 FreeRTOS 版本。
-   https://github.com/kendryte/kendryte-doc-standalone-programming-guide —— c 语言开发 IDE 下的裸机编程手册，kendryte 名下另有 FreeRTOS 版本。

### 嘉楠官网

- https://www.canaan-creative.com/developer SDK、HDK 等下载。
- [嘉楠开发者社区 (canaan-creative.com)](https://developer.canaan-creative.com/index.html?channel=developer#/model/library) 模型库。

### sipeed 官方 Github 仓库

-   https://github.com/sipeed/MaixPy —— 发扬光大，microPython 语言开发 IDE —— MaixPy。
-   https://github.com/sipeed/MaixPy_scripts —— MaixPy 的丰富历程。
-   MaixPy 的编程手册：[Github 地址（旧版）](https://github.com/sipeed/MaixPy_DOC)，[Github 地址（新版）](https://github.com/sipeed/sipeed_wiki/tree/main/docs/soft/maixpy/zh)，[网页版（推荐）](https://wiki.sipeed.com/soft/maixpy/zh/index.html)。

-   [Sipeed 资料导航](https://blog.sipeed.com/)。
-   [MaixPy - Sipeed 开源社区](https://bbs.sipeed.com/cate/16/seq/1) —— MaixPy 论坛。
-   [Sipeed MaixHub – sipeed AI 模型平台](https://maixhub.com/)。

### 各路网友大佬神经网络教程

*p.s 菩萨保佑链接别随随便便就挂掉，找这么多不容易。*

-   [K210 MaixPy 从入门到飞升--AI视觉篇--完全教程（以及一些小问题处理比如内存不足）-次世代BUG池 (neucrack.com)](https://neucrack.com/p/325) 比较完整的入门教程。
    -   [K210 kmodel 模型储存数据结构-次世代BUG池 (neucrack.com)](https://neucrack.com/p/307)。[K210 从flash实时加载大模型-次世代BUG池 (neucrack.com)](https://neucrack.com/p/313)。
    -   [K210 kflash ISP 下载程序流程-次世代BUG池 (neucrack.com)](https://neucrack.com/p/312)。[k210 kfpkg 打包 多个bin文件打包, 打包原理-次世代BUG池 (neucrack.com)](https://neucrack.com/p/158)。
    -   [K210+MLX90640红外热像仪-次世代BUG池 (neucrack.com)](https://neucrack.com/p/189)。[K210上用MaixPy写个简单的云台程序: 高性价比的人脸跟随云台-次世代BUG池 (neucrack.com)](https://neucrack.com/p/308)。
    
-   [K210_Top嵌入式的博客-CSDN博客](https://blog.csdn.net/qq_45396672/category_10809105.html)。
-   [神器！K210开发板运行神经网络模型（保姆级教程）_ JeckXu的博客-CSDN博客 _k210和openmv哪个好用](https://blog.csdn.net/qq_45396672/article/details/117390991)。
-   [K210模型转换，运行MNIST于MAIX开发板（完整攻略） (360doc.com)](http://www.360doc.com/content/19/1217/09/40492717_880267082.shtml)。
-   [【实战】K210训练与部署YOLO目标检测模型_MSTIFIY的博客-CSDN博客_k210 yolo](https://blog.csdn.net/qq_39784672/article/details/118528303)。
-   [K210Mx-yolov3模型训练和物体识别 - 百度文库 (baidu.com)](https://wenku.baidu.com/view/01ae372cf48a6529647d27284b73f242336c312d.html)。
-   [ 致小白的K210模型训练与运用_创客@小白的博客-CSDN博客_k210模型训练](https://blog.csdn.net/moshanghuaw/article/details/113172455)。
-   [mushroom-x/K210_Tutorial: K210基础入门教程 edit by Kyle阿凯 (github.com)](https://github.com/mushroom-x/K210_Tutorial) 系列文章教程。
-   [肥罗-阿勇创造中心-造物记(Makelog) (dfrobot.com.cn)](https://makelog.dfrobot.com.cn/user-1696-1.html) 这位写了很多 K210 教程文章，但不过是图形化编程。
-   [《基于RISC-V的人工智能应用开发 RISC-V 构架人工智能芯片 K210 应用开发教程书籍 Ke》廖义奎刘炽何佳煜【摘要 书评 试读】- 京东图书 (jd.com)](https://item.jd.com/10050217687380.html) 书。
-   [TonyZ1Min/yolo-for-k210 (github.com)](https://github.com/TonyZ1Min/yolo-for-k210) 此教程可以完整的在Win完成：制作数据集、训练yolo、转换成k210可用的Kmodel文件。

### 各路网友大佬实例

-   [elloza/awesome-k210: A curated list of awesome K210 hardware, projects and resources. (github.com)](https://github.com/elloza/awesome-k210)。
-   [YOLO训练教程-K210实现20分类目标检测_哔哩哔哩_bilibili](https://www.bilibili.com/video/av541276627)，完整软硬件开源方案，[硬件设计](https://github.com/SEASKY-Master/SEASKY_K210)，[软件设计](https://github.com/SEASKY-Master/Yolo-for-k210)。
-   [1658608470/Learn_MaixPy: 学习使用Sipeed公司的Maix Go开发板过程中实际测试过的一些小项目合集(github.com)](https://github.com/1658608470/Learn_MaixPy)。
-   [LZBUAV/K210_Python: Kendryte K210人工智能芯片应用程序集合，包括人脸检测、颜色检测、目标检测和分类、二维码和Apriltag代码检测以及和ArduPilot飞控软件的通信。这些应用程序已部署到无人机终端。This repository is a collection of applications for the Kendryte K210 AI chip which include face detection, color detection, object detection and classification, QR code and Apriltag code detection ,and communication with the ArduPilot flight software. Finally, we can deploy these applications to the UAV terminals and make drones more intelligent. (github.com)](https://github.com/LZBUAV/K210_Python)。
-   [超迷你的智能摄像头A-Eye,(github.com)](https://github.com/peng-zhihui/A-Eye)。
-   [zhen8838/K210_Yolo_framework: Yolo v3 framework base on tensorflow, support multiple models, multiple datasets, any number of output layers, any number of anchors, model prune, and portable model to K210 ! (github.com)](https://github.com/zhen8838/K210_Yolo_framework)。
-   [andriyadi/MaixPy-TrashClassifier: A simple trash/waste classifier developed using MaixPy (a MicroPython framework) to run on K210 MCU on Sipeed's Maix dev board (github.com)](https://github.com/andriyadi/MaixPy-TrashClassifier)。
-   [lemariva/MaixPy_YoloV2: YOLOv2 object detector training for a MAix-board (github.com)](https://github.com/lemariva/MaixPy_YoloV2)。

