# Anaconda

conda upgrade --all



创建环境

conda create -n env_name list of packages。

在这里，-n env_name 设置环境的名称（-n 是指名称），而 list of packages 是要安装在环境中的包的列表。conda  create -n my_env numpy。

conda create -n py3 python=3 

进入环境

OSX/Linux：source activate my_env 

Windows：activate my_env

在环境中安装包

conda install package_name

离开环境

OSX/Linux：source deactivate 

Windows：deactivate

列出环境

conda env list 

删除环境

conda env remove -n env_name

保存和加载环境

conda env export > environment.yaml 将包保存为 YAML

conda env export 输出环境中的所有包的名称（包括 Python 版本）。

environment.yaml 将导出的文本写入到 YAML 文件 environment.yaml 中

conda env create -f environment.yaml。这会创建一个新环境，而且它具有在 environment.yaml 中列出的同样的库