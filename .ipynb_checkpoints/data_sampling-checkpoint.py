import os
import pandas as pd

def verify_samples():
	base_dir = 'train_simplified'
	target_dir = 'train_sampled'
	valid_dir = 'valid_sampled'
	test_dir = 'test_sampled'
	*filelist, = os.listdir(base_dir)[1:101]

	if not os.path.exists(target_dir):
		for d in [target_dir, valid_dir, test_dir]:
			os.mkdir(d)

		for file in filelist:
			pd.read_csv(os.path.join(base_dir,file),nrows=1000).to_csv(os.path.join(target_dir,file),index=False)

		for file in filelist:
			pd.read_csv(os.path.join(base_dir,file),nrows=100,skiprows=1100).to_csv(os.path.join(test_dir,file),index=False)

		for file in filelist:
			pd.read_csv(os.path.join(base_dir,file),nrows=100,skiprows=1200).to_csv(os.path.join(valid_dir,file),index=False)
