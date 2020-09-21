import math
from torch.autograd import Variable
from utils import *
from model import *

directory = "files/"
content_file = directory + "content.wav"
style_file = directory + "style.wav"

content, sr = wav2spectrum(content_file)
style, sr = wav2spectrum(style_file)
torch_content = torch.from_numpy(content)[None, None, :, :]
torch_style = torch.from_numpy(style)[None, None, :, :]
copy_model = RandomCNN()
copy_model.eval()

content_var = Variable(torch_content, requires_grad=False).float()
style_var = Variable(torch_style, requires_grad=False).float()
content = copy_model(content_var)
style = copy_model(style_var)

learn_rate = 0.003
G_var = Variable(torch.randn(torch_content.shape) * 1e-3, requires_grad=True)
optimize = torch.optim.Adam([G_var])
