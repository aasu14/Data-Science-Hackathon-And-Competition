from keras.models import model_from_json
import numpy as np 

# Training and test data 
test_file = '../input/test.csv'
model_file = '../output/digitrecognizer.model.json'
model_weights_file = '../output/digitrecognizer.model.best.hdf5'
output_file = '../output/predictions.csv'

# load json and create model
json_file = open(model_file, 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
#
# load the weights that yielded the best validation accuracy
model.load_weights(model_weights_file)

# Load evaluation data from a file and return X
def load_eval_data(file_name):
    raw_data = np.genfromtxt(file_name, delimiter=',', skip_header=1)

    raw_sample_image = raw_data[0]
    image_size = int(np.sqrt(len(raw_sample_image)))
    X_shape = (len(raw_data), image_size, image_size, 1)

    X_data = np.zeros(X_shape)
    for index, datum in enumerate(raw_data):
        X_data[index] = np.array(datum/255).reshape(image_size, image_size, 1)

    return X_data
X_eval = load_eval_data(test_file)

# Get predictions on the evaluation data
with open(output_file, 'w') as f:
    f.write('ImageId,Label\n')
    y_eval = model.predict(X_eval)
    for index, y_hat in enumerate(y_eval):
        prediction = np.argmax(y_hat)
        f.write(str(index+1)+','+str(prediction)+'\n')
    f.close()