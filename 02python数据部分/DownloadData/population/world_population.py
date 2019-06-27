import json
import pygal.maps.world
from DownloadData.population import countries


# 读取数据文件population_data.json（不知哪儿可以加载数据文件，需要的可以留言）
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f) # 将json格式转换为python识别格式

cc_populations = {} # 用于存储人口数据
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010': # 提取2010年的数据
        country_name = pop_dict['Country Name']
        # 将格式不统一的人口数据转换为浮点型，再转换为int型统一格式，供pygal绘图使用
        population = int(float(pop_dict['Value']))
        #print(country_name)
        code = countries.get_country_code(country_name)
        # 按国别码提取正确的国家和对应人口数据
        if code:
            cc_populations[code] = population
            print(cc_populations)
# #根据人口数量将国家分成三组，0-1千万，1千万-10亿，10亿以上
# cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}
# for cc,pop in cc_populations.items():
#     if pop < 10000000:
#         cc_pops_1[cc] = pop
#     elif pop < 1000000000:
#         cc_pops_2[cc] = pop
#     else:
#         cc_pops_3[cc] = pop
#
# wm = pygal.maps.world.World() # 生成世界地图实例
# wm.title = 'World Population in 2010, by Country' # 设置标题
# wm.add('1-10m',cc_pops_1) # 添加0——1千万的国家和人口
# wm.add('10m-1bn',cc_pops_2) # 添加1千万——10亿的国家和人口
# wm.add('>bn',cc_pops_3) # 添加10亿以上的国家和人口
# # 渲染视图到文件，通过浏览器可查看
# wm.render_to_file('americas.svg')