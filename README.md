# 鱼类1：1配对自动分配方案

- id.tsv记录了每一条鱼对应的家系、性别信息

- pool_info.tsv记录了每一个孵化池应该放哪些家系的鱼

- find_pool.py 找到合适的水池，并及时更新pool_info.tsv文件

- **用法**
  
  在命令行中输入`python.exe find_pool.py` 回车，程序会提示输入`ID`，输入`ID`后回车，程序决定鱼池分配，并将分配信息同步到屏幕和更新到`pool_info.tsv`文件。
