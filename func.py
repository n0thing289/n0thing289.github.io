import os
import cv2
import math
import re
file_path = os.getcwd()

def get_video_frame_size(file_name):
    """获取视频分辨率，并返回视频分辨率"""
    cap = cv2.VideoCapture(file_name)

    file_frame_size = cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # print(file_frame_size[0], file_frame_size[1])
    return file_frame_size


def get_video_byte(file_name):
    """获取视频的字节大小"""
    video_byte_size = os.path.getsize(file_name)
    video_byte_size = "%d字节" % video_byte_size
    return video_byte_size


def get_sep_file(file_name):
    """获取视频的名字和后缀名"""

    video_sep_name = os.path.splitext(file_name)[0], os.path.splitext(file_name)[1]
    # get_sep_file[0]给前缀
    # get_sep_file[1]给后缀
    return video_sep_name


def bianli_(files_list):
    """拿到遍历中收集的数据，存储在字典中 {filename:[(分辨率)，字节大小]}"""

    all_video_info = {}

    for f in files_list:

        file_hozhui = get_sep_file(f)[1]

        if file_hozhui == '.mp4':
            video_name = get_sep_file(f)[0] + file_hozhui

            # 拿到字节大小
            video_byte_size = get_video_byte(f)

            # 拿到分辨率大小

            video_frame_size = get_video_frame_size(f)
            all_video_info[video_name] = [video_frame_size, video_byte_size]

    return all_video_info


def is_repeat(files_list):
    """判断重复，用两个字典循环遍历判断重复的分辨率，字节大小，由于文件名不能重名，和字典的键一样"""
    all_videos_info = bianli_(files_list)
    if len(all_videos_info) != 1:
        first_frame_size1 = None
        first_frame_size2 = None
        first_video_byte1 = None
        first_video_byte2 = None
        key1 = None
        key2 = None
        value2 = None
        for (key1, value1) in all_videos_info.items():
            first_frame_size1 = value1[0]
            first_video_byte1 = value1[1]

            for (key2, value2) in all_videos_info.items():
                first_frame_size2 = value2[0]
                first_video_byte2 = value2[1]

            if first_frame_size1 == first_frame_size2:

                if first_video_byte1 == first_video_byte2:
                    print("\t\t%s 和 %s 这个文件分辨率和大小都相同" % (key1, key2), value2)

                else:
                    print("\t\t%s 和 %s 这个文件分辨率相同" % (key1, key2), value2)
    else:
        print("\t\t此目录下只有一个视频文件无法进行多个视频查重")


def mul_rename(files_list, input_name):
    all_video_info = bianli_(files_list)
    flag = input("按1在原来的名字增加字符,按2批量删去输入的字符,按下2之后在源码100行中修改删除的模式 asign")
    new_video_name = ""
    for old_video_name_key in all_video_info.keys():
        file_hozhui = get_sep_file(old_video_name_key)[1]
        file_name = get_sep_file(old_video_name_key)[0]
        if flag == '1':
            # 视频名

            new_video_name = file_name + input_name + file_hozhui
            os.rename(old_video_name_key, new_video_name)

        elif flag == '2':
            if input_name not in file_name:
                print("%s 此文件名不包含%s" % (file_name, input_name))
            else:
                # asign = 默认3 删除指定的字符串，1删指定字符串之前的所有，2为删除指定字符串之后的所有（会补后缀）
                new_text = text_splitor(file_name=file_name, input_name=input_name, asign=3)
                new_video_name = new_text
                if ".mp4" not in new_video_name:
                    new_video_name += file_hozhui
                os.rename(old_video_name_key, new_video_name)

        print("%s >>> %s" % (old_video_name_key, new_video_name))


def text_splitor(file_name, input_name, asign):
    # file_name = 'test_video_2美女视频meinv666.mp4'
    # input_name = "meinv"

    input_name_len = len(input_name)
    input_name_be = file_name.index(input_name)  # m的索引 第16
    input_name_af = input_name_be + input_name_len  # v的索引 第20

    before_name = file_name[:input_name_be]
    after_name = file_name[input_name_af:]
    # print(before_name)
    # print(after_name)
    #
    # print(file_name.split(file_name[input_name_be:input_name_af]))
    # 得到不要meinv两边的字符串列表，[0]给前面名字，[1]给后面的名字
    text_list = file_name.split(file_name[input_name_be:input_name_af])
    text = text_list[0] + text_list[1]
    asign = 3
    # asign = 默认3 删除指定的字符串，1删指定字符串之前的所有，2为删除指定字符串之后的所有（会补后缀）

    if asign == 1:
        return text_list[1]

    if asign == 2:
        return text_list[0]

    if asign == 3:
        return text


"""
程序可以将指定目录下的视频文件，将分辨率比如1024*768，作为文件名写入到文件名后部，
比如TOM.mp4变成 TOM1024-768.mp4  。另外，对于疑似重复的文件，大小、格式、播放时长一样（如果播放时长不好取样），
就在文件头部上0000-zzzz，比如TOM1024-768.mp4和JACK1024-768.mp4疑似重复，则都变成0000-TOM1024-768.mp4和0000-JACK1024-768.mp4，
三个一样，则三个也是这样。第二组就变成1111- ，依次类推，到ZZZZ后可以轮回使用0000

需求分析
    1.将分辨率写入文件名，比如TOM.mp4变成 TOM1024-768.mp4
    2.将分辨率，字节大小和格式三个都一样的视频，在它们的文件名开头写入0000-zzzz这种格式
"""

def new_mul_rename1(chongfu_liest, flag=1):
    # 0000 1111 2222 3333 4444 5555 6666 7777 8888 9999 aaaa
    if flag == 1:
        x = 0
        for infokey in chongfu_liest:
            x += 1
            qian_name = kaitou_name_operator(n=x)
            re_name = qian_name
            name_list = infokey.split(".")
            name_list.insert(0, re_name)
            name_list.insert(-1, ".")
            # print(name_list)
            name = ""
            for n in name_list:
                name += n
            os.rename(infokey, name)


def new_mul_rename2(flag = 2):
    if flag == 2:
        files = os.listdir(file_path)
        all_video_info = bianli_(files)
        # TODO 解决升级new_isrepeat()后,修改名字的bug
        for info_key, info_value in all_video_info.items():
            name_list = info_key.split('.')  # ["767","750-1000.","mp4"]
            # print(name_list)

            # 在何时插入
            video_frame = info_value[0]

            re_name = str(int(video_frame[0])) + "-" + str(int(video_frame[1])) + "."
            name_list.insert(-1, re_name)
            # print(name_list)
            name = ""
            for n in name_list:
                name += n
            # print(name)
            # print(info_key)# 别忘了是在新得基础上拆成列表
            os.rename(info_key, name)





def new_isrepeat(files):

    all_videos_info = bianli_(files)  # {filename:[(分辨率)，字节大小]}
    # 1. 转成列表进行处理
    fileNamelist = [] # 这两个的唯一重要的关系就是索引
    valuelist = []

    for key, value in all_videos_info.items():
        fileNamelist.append(key)
        valuelist.append(value)


    # print(fileNamelist)
    # print(valuelist)
    # 2. 改进匹配机制（之前实现的算法弊端很大）
    # 1 2 3 4 5 个视频文件
    # 1 -> 2 3 4 5
    # 2 -> 3 4 5
    # 3 -> 4 5
    # 4 -> 5
    # 两两匹配他们的valuelist的元素值, 由上可见,5个视频文件,有4趟,
    # 第一趟匹配4轮
    # 第二趟匹配3轮
    # ...
    repeated_dict = {}  # {"[(720.0, 1280.0), '3442641字节']": ['测试视频1号 - 副本 (2).mp4', '测试视频1号 - 副本.mp4', '测试视频1号.mp4']}
    for i in range(len(valuelist)-1):
        # print(i)
        for j in range(i+1, len(valuelist)):
            # print(j,end='')
            if valuelist[i] == valuelist[j]:
                if str(valuelist[i]) not in repeated_dict.keys():
                    repeated_dict[str(valuelist[i])] = []
                    repeated_dict[str(valuelist[i])].append(fileNamelist[i])
                    repeated_dict[str(valuelist[i])].append(fileNamelist[j])
                else:
                    if fileNamelist[i] in repeated_dict[str(valuelist[i])]:
                        pass
                    else:
                        repeated_dict[str(valuelist[i])].append(fileNamelist[i])

                    if fileNamelist[j] in repeated_dict[str(valuelist[i])]:
                        pass
                    else:
                        repeated_dict[str(valuelist[i])].append(fileNamelist[j])
        # print()

    # print(repeated_dict)
    #        {"[(720.0, 1280.0), '3442641字节']": ['测试视频1号.mp4', '测试视频1号.mp4'], "[(720.0, 1280.0), '5223270字节']": ['测试视频2号.mp4', '测试视频2号.mp4'], "[(1024.0, 576.0), '2953045字节']": ['测试视频3号 - 副本.mp4', '测试视频3号.mp4']}
    #n[]     {"[(720.0, 1280.0), '3442641字节']": ['测试视频1号.mp4', '测试视频1号.mp4'], "[(720.0, 1280.0), '5223270字节']": ['测试视频2号 - 副本.mp4', '测试视频2号 - 副本.mp4', '测试视频2号 - 副本.mp4', '测试视频2号.mp4', '测试视频2号.mp4', '测试视频2号.mp4'], "[(1024.0, 576.0), '2953045字节']": ['测试视频3号 - 副本.mp4', '测试视频3号 - 副本.mp4', '测试视频3号 - 副本.mp4', '测试视频3号.mp4']}
    #if-else {"[(720.0, 1280.0), '3442641字节']": ['测试视频1号.mp4', '测试视频1号.mp4'], "[(720.0, 1280.0), '5223270字节']": ['测试视频2号 - 副本.mp4', '测试视频2号 - 副本.mp4', '测试视频2号.mp4'], "[(1024.0, 576.0), '2953045字节']": ['测试视频3号 - 副本.mp4', '测试视频3号 - 副本.mp4']}
    #i+1     {"[(720.0, 1280.0), '5223270字节']": ['测试视频2号 - 副本.mp4', '测试视频2号.mp4'], "[(1024.0, 576.0), '2953045字节']": ['测试视频3号 - 副本.mp4', '测试视频3号.mp4']}

    # TODO 为啥自己原本的没有嘞??? solved!
    # {"[(720.0, 1280.0), '3442641字节']": ['测试视频1号 - 副本 (2).mp4', '测试视频1号 - 副本.mp4'], "[(720.0, 1280.0), '5223270字节']": ['测试视频2号 - 副本 (2).mp4', '测试视频2号 - 副本 (3).mp4', '测试视频2号 - 副本.mp4', '测试视频2号.mp4'], "[(1024.0, 576.0), '2953045字节']": ['测试视频3号 - 副本.mp4', '测试视频3号.mp4']}
    # {"[(720.0, 1280.0), '3442641字节']": ['测试视频1号 - 副本 (2).mp4', '测试视频1号 - 副本.mp4'], "[(720.0, 1280.0), '5223270字节']": ['测试视频2号 - 副本 (2).mp4', '测试视频2号 - 副本 (3).mp4', '测试视频2号 - 副本 - 副本.mp4', '测试视频2号 - 副本.mp4'], "[(1024.0, 576.0), '2953045字节']": ['测试视频3号 - 副本.mp4', '测试视频3号.mp4']}
    # {"[(720.0, 1280.0), '3442641字节']": ['测试视频1号 - 副本 (2).mp4', '测试视频1号 - 副本.mp4', '测试视频1号.mp4'], "[(720.0, 1280.0), '5223270字节']": ['测试视频2号 - 副本 (2).mp4', '测试视频2号 - 副本 (3).mp4', '测试视频2号 - 副本 - 副本.mp4', '测试视频2号 - 副本.mp4', '测试视频2号.mp4'], "[(1024.0, 576.0), '2953045字节']": ['测试视频3号 - 副本.mp4', '测试视频3号.mp4']}

    return repeated_dict
def kaitou_name_operator(n):
    """
    1 -- 0000    10 -- aaaa
    2 -- 1111
    3 -- 2222
    4 -- 3333
    5 -- 4444
    """
    # 以36为一个循环
    jixunhuanshu = 36
    shang = math.ceil(n / 36)  #
    k = 0
    z = 0
    while (z <= shang):
        if n == 0:
            int_name_1 = "0000"
            return int_name_1
        elif n <= (10 + k) and n >= (1 + k):
            object_int = 1111
            beshu = n - (1 + k)
            int_name = object_int * beshu
            if int_name == 0:
                name_0000 = str(int_name) * 4

                # print(int_name)
                return name_0000
            else:
                return str(int_name)

        elif n > (10 + k) and n <= (36 + k):  # 第11个重复文件开始
            """ 
            11 -- a
            """
            zimu_index = n - (11 + k)
            zm = [chr(i) for i in range(97, 123)]
            final_zimu = zm[zimu_index] * 4
            # print(final_zimu)
            # Final_zimu = final_zimu
            return final_zimu
        k += jixunhuanshu
        z += 1

    # return INT_NAME_1 or INT_NAME_2 or Final_zimu


def clearup(files):
    """用于清除我所做的更改"""
    result1_name = None
    result2_name = None
    x = None
    print("\n\t=====\t撤销操作结果如下\t=====\n")
    for i in files:
        if ".mp4" in i:
            result1_name = re.findall(r"^(\d{4})", i)[0]
            x = i.replace(result1_name, "")

            result2_name = re.findall(r"(\d*?-.*\d*?)\.", i)[0]
            x = x.replace(result2_name, "")



            print("\t\t" + i + " --> " + x)
            # os.rename(i, x)
    print("\n\t=====\t============\t=====\n")

    # TODOFinished 解决撤销时的新bug
    """
        00000000one(1)720-1280720-1280.mp4 --> one(1)720-.mp4
		00000000three(1)720-1280720-1280.mp4 --> three(1)720-.mp4
		00000000two(1)1024-5761024-576.mp4 --> two(1)1024-.mp4
		11111111one(2)720-1280720-1280.mp4 --> one(2)720-.mp4
		11111111three(2)720-1280720-1280.mp4 --> three(2)720-.mp4
		11111111two(2)1024-5761024-576.mp4 --> two(2)1024-.mp4
    """
