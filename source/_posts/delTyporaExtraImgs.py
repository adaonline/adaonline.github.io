import glob
import os
from pathlib import Path

md_dir = ""
imgs_dir = ""


# 将此文件放入typora下面
def delImagesExtraInTypora(md_dir, imgs_dir):
    if not md_dir:
        md_dir = Path(__file__).resolve().parent
    if not imgs_dir:
        imgs_dir = Path(__file__).resolve().parent.parent
        imgs_dir = (imgs_dir / "images").__str__()
    print("md文件所在目录 %s\n图像所在目录 %s" % (md_dir, imgs_dir))
    images_files = {}
    for dirpath, dirs, files in os.walk(imgs_dir):
        for filename in files:
            if filename.endswith('png'):
                img_tip = [os.path.join(dirpath, filename), filename, 0]
                images_files[filename] = img_tip
    md_files = glob.glob(os.path.join(md_dir, '*.md'))
    for filename in md_files:
        with open(filename, 'r', encoding='utf-8') as md:
            text = md.read()
            for filename, img_tip in images_files.items():
                if text.find(img_tip[1]) != -1:
                    img_tip[2] = 1
    print(images_files)
    has_del = False
    for filename, img_tip in images_files.items():
        if img_tip[2] == 0:
            print("删除图片%s\n" % img_tip[0])
            os.remove(img_tip[0])
            has_del = True
    if not has_del:
        print("无图片需要删除，脚本执行完毕，按回车键退出。")
    else:
        print("已经删除多余图片，脚本执行完毕，按回车键退出。")
    input()


print("==========删除Typora没有引用到的额外图片===============")
delImagesExtraInTypora(md_dir, imgs_dir)
