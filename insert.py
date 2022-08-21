import pandas as pd

df_body1 = pd.read_csv('D:\VSCODE\SmartEar\Librimix\\train_100_data1.csv')
df_body2 = pd.read_csv('D:\VSCODE\SmartEar\Librimix\\train_100_data2.csv')
df_body1.columns = ['mixture_ID','mixture_path','source_1_path','source_2_path','noise_path','length','target_speaker_ID']
df_body1.columns = ['mixture_ID','mixture_path','source_1_path','source_2_path','noise_path','length','target_speaker_ID']
df3 = pd.concat([df_body1,df_body2],ignore_index=True)
df3.to_csv('D:\VSCODE\SmartEar\Librimix\data.txt',index=False,sep=' ',header=None)
print(df3)

# 做一次修改

#做第二次修改

#Git 真是个好应用



# 测试pull 与 push
