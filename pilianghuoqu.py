import os
import sys
import func

file_path = os.getcwd()
files = os.listdir(file_path)

print(file_path)


def main():
    """主程序"""
    while True:
        print("***************************************************\n" +
              "欢迎使用视频查询小程序\n" +
              "按1启动当前目录下的所有视频查询分辨率：\n" +
              "按2进行当前目录下的查重服务\n" +
              "\n" +
              "按4实现对重复文件进行文件名美化整理\n" +
              "按5实现清除程序所作的更改\n" +
              "按exit推出程序\n"
              "***************************************************")
        flag = input()
        if flag == '1':
            files = os.listdir(file_path)
            all_video_info = func.bianli_(files)
            num = 0
            print("\n\t=====\t结果如下\t=====\n")
            for (key, value) in all_video_info.items():
                first_frame_size = value[0]
                print("\t\t%s 的分辨率是 %d x %d" %
                      (key, first_frame_size[0], first_frame_size[1]))
                num += 1
            print("\n\t=====\t共查询到 %d 个视频文件，视频分辨率如上面所示\t=====\n" % num)

        if flag == '2':
            files = os.listdir(file_path)
            print("\n\t=====\t重复文件结果如下\t=====\n")
            chongfuList = func.new_isrepeat(files)
            video_name_list = chongfuList[0]
            video_frame_list = chongfuList[1]
            video_byte_list = chongfuList[2]
            waiting_list = [[], []]
            # for j in range(0,len(video_name_list)):
            #     flag_dict[video_name_list[i]] = str(video_frame_list[i]) +"-"+ str(video_byte_list[i])
            value_list = []
            #TODO 实现分类整合的功能A
            for i in range(0, len(video_name_list)):
                value_list.append(str(video_frame_list[i]) + "-" + str(video_byte_list[i]))

            # for i in range(0, len(video_name_list)):
            #     # print("分辨率和字节为：%s %s" % ())
            #     # print("\t\t" + "分辨率为%s, 字节为%s的重复文件有: " % (str(video_frame_list[i]), video_byte_list[i]))
            #
            #     k = value_list.count(value_list[i])
            #     # 找重复次数的索引,并且用列表存起来文件名
            #     if k >= 2:
            #
            #         waiting_list[0].append(list())
            #         waiting_list[1].append(list())
            #         waiting_list[0][l].append(video_name_list[i])
            #         waiting_list[1][l].append(str(video_frame_list[i]) + "-" + str(video_byte_list[i]))
            #         l += 1
            #     # 统一先输出有重复次数的索引对应的文件名
            #
            #     # 再输出其他无重复次数的索引对应的文件名
            #
            #     print(waiting_list)
            for i in range(0, len(video_name_list)):

                print("\t\t" + "分辨率为%s, 字节为%s的重复文件有: %s"% (str(video_frame_list[i]), video_byte_list[i], str(video_name_list[i])))
            print("\n\t=====\t=====\t=====\n")

        # if flag == '3':
        #     files = os.listdir(file_path)
        #     input_name = input("请输入要批量修改后的名字")
        #
        #     func.mul_rename(files, input_name)

        if flag == '4':
            files = os.listdir(file_path)
            chongfuList = func.new_isrepeat(files)
            video_name_list2 = chongfuList[0]
            func.new_mul_rename(files, chongfu_liest=video_name_list2, flag=1)

            files = os.listdir(file_path)
            chongfuList = func.new_isrepeat(files)
            video_name_list2 = chongfuList[0]
            func.new_mul_rename(files, chongfu_liest=video_name_list2, flag=2)
            # func.new_isrepeat(files)
            # print(func.kaitou_name_operator(75))

        if flag == '5':
            files = os.listdir(file_path)
            func.clearup(files)

        if flag == 'exit':
            break


main()
