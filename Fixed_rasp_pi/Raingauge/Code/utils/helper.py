import os
import yaml
from keras.models import Sequential
from keras.layers import LSTM, Dense, Reshape
from keras.layers import Conv2D, MaxPooling2D


def time_stamp_fnamer(tstamp):
	cdate, ctime = str(tstamp).split(" ")
	current_date = "_".join(cdate.split("-"))
	chour, cmin,csec =ctime.split(":")
	csec, cmilli = csec.split(".")
	current_time = "_".join([chour, cmin, csec, cmilli])
	current_date_time_name = "_".join([current_date, current_time])
	return current_date_time_name

def load_config(config_name):
	CONFIG_PATH = "/home/pi/fixed-pi/Raingauge/Code/config/"
	with open (os.path.join(CONFIG_PATH, config_name)) as file:
		config = yaml.safe_load(file)
	return config

def create_folder(directory):
	""""Function to create a folder in a location if it dosen not exist"""
	if not os.path.exists(directory):
		os.makedir(directory)

def create_log_file(log_folder ,log_file):
	with open(os.path.join(log_folder, log_file), "a") as f:
		f.write("")

def create_lstm_model():
	model =Sequential()
	#model.add(Conv2D(64, kernel_size=(8, 8),activation='relu', input_shape=(1025, 2657, 1)))
	#model.add(MaxPooling2D(pool_size=(8,8)))
	#model.add(Conv2D(32, kernel_size=(4, 4),activation='relu'))
	#model.add(MaxPooling2D(pool_size=(4,4)))
	#model.add(Conv2D(16, kernel_size=(2,2),activation='relu'))
	#model.add(MaxPooling2D(pool_size=(2,2)))
	#model.add(Reshape((1, -1)))
	model.add(LSTM(20))
	model.add(Dense(32))
	model.add(Dense(16))
	model.add(Dense(1))
	return model

def load_estimate_model(model_path):
	model = create_lstm_model()
	config = load_config("config.yaml")
	model.build(input_shape=config["stft_shape"])
	model.load_weights(model_path)
	return model
