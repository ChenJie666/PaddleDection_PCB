import json
import collections
from matplotlib import pyplot as plt

'''
首先需要检查样本信息，包括 ①样本中标注的种类数量是否相近 ②锚框宽高比 ③锚框占整个图片的比例
'''

# 加载解析json文件
with open('./PCB_DATASET/Annotations/train.json') as f:
    data = json.load(f)

# 保存图片信息
imgs = {}
for img in data['images']:
    imgs[img['id']] = {
        'height': img['height'],
        'width': img['width'],
        'area': img['height'] * img['width']
    }

# 计算标注信息
hw_ratios = []
area_ratios = []
cate_count = collections.defaultdict(int)
for anno in data['annotations']:
    hw_ratios.append(anno['bbox'][3] / anno['bbox'][2])
    area_ratios.append(anno['area'] / imgs[anno['image_id']]['area'])
    cate_count[anno['category_id']] += 1

print(cate_count, len(data['annotations'])/len(data['images']))

plt.hist(hw_ratios, bins=100, range=[0, 2])
plt.show()

plt.hist(area_ratios, bins=100, range=[0, 0.005])
plt.show()
