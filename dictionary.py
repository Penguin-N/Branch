import pandas as pd

df_train = pd.read_csv('D:\VSCODE\SmartEar\Librimix\\train_100.tsv')
df_dev = pd.read_csv('D:\VSCODE\SmartEar\Librimix\dev_100.tsv')

target_ID = pd.concat([df_train[['target_ID']],df_dev[['target_ID']]],ignore_index=True)

spk_dic = {}
for i in range(len(target_ID)):
    speaker_ID = str(target_ID.loc[i,'target_ID'])
    if not spk_dic.get(speaker_ID,False):
        spk_dic[speaker_ID] = 1
    else:
        spk_dic[speaker_ID] = spk_dic[speaker_ID] + 1
        
with open('D:\VSCODE\SmartEar\Librimix\\file.txt', 'w') as file:
    for key, value in spk_dic.items():
        file.write(key)
        file.write(' ')
        file.write(str(value))
        file.write('\n')