import sys
sys.path.append('/Users/brendan/HW/455/uwimg')
from uwimg import *

def softmax_model(inputs, outputs):
    l = [make_layer(inputs, outputs, SOFTMAX)]
    return make_model(l)

def neural_net(inputs, outputs):
    # print inputs
    l = [   make_layer(inputs, 64, LRELU),
            make_layer(64, outputs, SOFTMAX)]
    return make_model(l)

print("loading data...")
train = load_classification_data("sprites.train", "labels.txt", 1)
test  = load_classification_data("sprites.test", "labels.txt", 1)
print("done")
print

print("training model...")
batch = 64
iters = 1000
rate = 0.1
momentum = .9
decay = 0.0005

m = neural_net(train.X.cols, train.y.cols) #softmax_model(train.X.cols, train.y.cols)
train_model(m, train, batch, iters, rate, momentum, decay)
print("done")
print

print("evaluating model...")
print("training accuracy: %f", accuracy_model(m, train))
print("test accuracy:     %f", accuracy_model(m, test))


