import os
import run_nerf
import run_nerf_helpers

basedir = './logs'
expname = 'lego_example'
config = os.path.join(basedir, expname, 'config.txt')

parser = run_nerf.config_parser()
ft_str = '--ft_path {}'.format(os.path.join(basedir, expname, 'model_200000.npy'))
args = parser.parse_args('--config {} '.format(config) + ft_str)

print(args)
