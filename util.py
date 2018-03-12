# constants
RESNET50 = "resnet50"
RESNET101 = "resnet101"
VGG16 = "vgg16"
EPOCH = "epoch"
MODEL = "model"
STATE_DICT = "state_dict"
VAL_ACCURACY = "val_accuracy"
BEST_VAL_ACCURACY = "best_val_accuracy"
VAL_LOSS = "val_loss"
BEST_VAL_LOSS = "best_val_loss"
TRAIN = "train"
TEST = "test"
VAL = "val"

# config
train_dir = "data/train/"
val_dir = "data/val"
test_dir = "data/test"
batch_size = 32
image_size = 224
num_workers = 2
model_name = RESNET101
use_cuda = True
num_epochs = 20
learning_rate = 1e-3
early_stopping_criteria = 5

