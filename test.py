from datasets.base_dataset import BaseDataset
import torch

base_dataset = BaseDataset(None, 'mpi-inf-3dhp', is_train=False)
dataloader = torch.utils.data.DataLoader(base_dataset, batch_size = 5, shuffle = False)
dataiter = iter(dataloader)
items = dataiter.next()
print(items.keys())
print(items['keypoints'][0])
print(items['imgname'][0])