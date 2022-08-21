import pandas as pd

df = pd.read_csv('D:\VSCODE\SmartEar\Librimix\Test.csv')
mixture_ID = df[['mixture_ID']]
mixture_ID.columns=['source_2_speaker_ID']
for i in range(len(mixture_ID)):
    target_ID = mixture_ID.loc[i,'source_2_speaker_ID']
    target_ID = target_ID[target_ID.find('_')+1:target_ID.find('-',target_ID.find('_'))]
    mixture_ID.loc[i,'source_2_speaker_ID'] = target_ID
target_ID = mixture_ID
new_df = pd.concat([df,target_ID],axis=1)
new_df.to_csv('D:\VSCODE\SmartEar\Librimix\Train_100.csv',index=False,sep=',',header=None)