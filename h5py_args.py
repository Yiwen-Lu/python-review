import h5py
import numpy as np
import os
import argparse


def name_list(data):
	nameList = []
	for i in range(10):
		for j in range(10):
			for k in range(10):
				nameList.append(str(i)+str(j)+str(k))
	return nameList[:len(data)]


def split_data(data, frame_num):
	frame_list = name_list(data)
	for i in range(0, len(data), frame_num):
		if i == len(data) // frame_num * frame_num:
			frames = data[i:]
			frame_idx = frame_list[i] + '_' + frame_list[-1]
		else:
			frames = data[i: i+frame_num]
			frame_idx = frame_list[i] + '_' + frame_list[i + frame_num - 1]
		splitted_data_file_name = frame_idx + '_input.h5'
		split_f = h5py.File(splitted_data_file_name, 'w')
		group = split_f.create_group('exported_data')
		group.create_dataset(name=splitted_data_file_name[:-2], data=frames)
		split_f.close()


def main(args):
	# import data
	raw_f = h5py.File(args.raw_data_file_name, 'r')
	raw_data = np.array(raw_f['exported_data'])
	# split data
	split_data(raw_data, args.frame_num)
	print('done!')


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--raw_data_file_name', type=str, 
		default='20180629_sofosbuvir_t48_206_adj_Input.h5', 
		help='file name of raw data to split')
	parser.add_argument('--frame_num', type=int, default=5, 
		help='number of frames after split')
	args = parser.parse_args()
	main(args)
