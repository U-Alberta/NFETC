from optparse import OptionParser
from task import Task
import logging
from model_param_space import param_space_dict

def parse_args(parser):
	parser.add_option("-m", "--model", dest="model_name", type="string")
	parser.add_option("-d", "--data", dest="data_name", type="string")
	parser.add_option("-r", "--runs", dest="runs", type="int", default=5)
	parser.add_option("-e", "--epoch", dest="epoch", default=False, action="store_true")
	options, args = parser.parse_args()
	return options, args

def main(options):
	logger = logging.getLogger()
	logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s', level=logging.INFO)
	params_dict = param_space_dict[options.model_name]
	task = Task(options.model_name, options.data_name, options.runs, param_dict, logger)
	if options.epoch:
		task.refit()
	else:
		task.evaluate()

if __name__ == "__main__":
	parser = OptionParser()
	options, args = parse_args(parser)
	main(options)
