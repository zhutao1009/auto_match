import os
import pandas as pd
from datetime import datetime

script_dir = os.path.dirname(os.path.abspath(__file__))
    
# print("脚本所在目录:", script_dir)
#    file_path = os.path.join(script_dir, filename)

def get_family_and_gender_by_id(file_path, search_id):
    # 读取文件
    df = pd.read_csv(file_path, sep="\t",dtype=str)
    df['ID'] = df['ID'].astype(str)
    search_id = str(search_id)
    
    # 去除ID列中的前导和尾随空格
    df['ID'] = df['ID'].str.strip()
    # 查找对应的行
    result_row = df[df['ID'] == search_id]
    # 检查是否找到对应的行
    if not result_row.empty:
        result_dict = {
            '家系': result_row['家系'].values[0],
            '性别': result_row['性别'].values[0],
            'ID':search_id
        }
        return result_dict
    else:
        return None

# 示例用法
# id_path = 'F:\\大口黑鲈2025年家系构建\\第二次分池\\id.tsv'

id_path=os.path.join(script_dir, "id.tsv")

search_id = str(input("请输入要查询的ID: "))
result = get_family_and_gender_by_id(id_path, search_id)
#print(result["ID"])  # 输出对应ID的家系和性别信息


def filter_and_update_hatchery_pools(file_path, family, parent_type, id_value):
    # 读取文件
    df = pd.read_csv(file_path, sep="\t", dtype=str)
    # 过滤符合条件的行
    filtered_df = df[(df['家系'] == family) & (df['亲本类型'] == parent_type) & (df['have_fish'] == 'no_fish')]
    
    # 检查是否有符合条件的孵化池
    if not filtered_df.empty:
        # 选取第一个符合条件的孵化池
        first_pool = filtered_df.iloc[0]['孵化池']
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        # 修改对应孵化池的状态，并增加性别信息的判断
        df.loc[(df['孵化池'] == first_pool) & (df['亲本类型'] == parent_type), 'have_fish'] = id_value
        df.loc[(df['孵化池'] == first_pool) & (df['亲本类型'] == parent_type), '修改时间'] = current_time
        
        # 将修改后的数据存入文件
        df.to_csv(file_path, sep="\t", index=False)
        
        return first_pool
    else:
        return None

# 示例用法
file_path = os.path.join(script_dir,"pool_info.tsv")
family = result["家系"]
parent_type = result["性别"]
id_value = result["ID"]
pool_assign = filter_and_update_hatchery_pools(file_path, family, parent_type, id_value)
print(pool_assign)  # 输出修改状态的孵化池




