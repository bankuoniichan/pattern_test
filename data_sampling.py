import os
import pandas as pd

def verify_samples():
	base_dir = 'train_simplified'
	target_dir = 'train_sampled'
	valid_dir = 'valid_sampled'
	test_dir = 'test_sampled'

	if not os.path.exists(target_dir):
		
		*filelist, = os.listdir(base_dir)
		*filelist, = sorted(filter(lambda x:x[0]!='.',filelist),key=lambda x:x.lower())
		filelist = filelist[:100]

		with open('sampling_log.txt','w') as FILE:
			print(*filelist,sep='\n',file=FILE)

		for d in [target_dir, valid_dir, test_dir]:
			os.mkdir(d)

		for file in filelist:
			pd.read_csv(os.path.join(base_dir,file),nrows=2000).to_csv(os.path.join(target_dir,file),index=False)

		for file in filelist:
			pd.read_csv(os.path.join(base_dir,file),nrows=100,skiprows=2100).to_csv(os.path.join(test_dir,file),index=False)

		for file in filelist:
			pd.read_csv(os.path.join(base_dir,file),nrows=100,skiprows=2200).to_csv(os.path.join(valid_dir,file),index=False)


if __name__=='__main__':
	print('Verifying ....')
	verify_samples()