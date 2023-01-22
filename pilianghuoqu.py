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
              "按3实现对重复文件进行文件名美化整理\n" +
              "按4实现清除程序所作的更改\n" +
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
            repeated_dict = func.new_isrepeat(files)
            for key_str, value in repeated_dict.items():

                # print(key_str)
                # print("分辨率 = %s × %s,字节大小 = %s 的条件下有 %d 个重复文件:" % (key_str[0][0],key_str[0][1], key_str[1],len(value)))
                print("\t\t在 %s 条件下有 %d 个重复的视频文件:" % (key_str, len(value)))
                for i in range(0, len(value)):

                    print("\t\t\t" + str(value[i]))

            print("\n\t=====\t============\t=====\n")

                # print(value)

        if flag == '3':
            #     # {"[(720.0, 1280.0), '3442641字节']": ['测试视频1号 - 副本 (2).mp4', '测试视频1号 - 副本.mp4', '测试视频1号.mp4']}
            files = os.listdir(file_path)
            chongfu_dict = func.new_isrepeat(files)
            # print(chongfu_dict)
            for name_list in chongfu_dict.values():
                func.new_mul_rename1(chongfu_liest=name_list, flag=1)
            func.new_mul_rename2(flag=2)

        if flag == '4':
            files = os.listdir(file_path)
            func.clearup(files)

        if flag == 'exit':
            break


main()
