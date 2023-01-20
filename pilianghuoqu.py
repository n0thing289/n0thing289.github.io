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
            func.new_isrepeat(files)




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
