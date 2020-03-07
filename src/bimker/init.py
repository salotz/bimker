import click

import pkgutil
import os
import os.path as osp

from . import (
    CONFIG_DIR,
)


@click.command()
@click.option("--config", default=None, type=click.Path(exists=True))
def cli(config):

    # make the bimker configuration dir
    os.makedirs(CONFIG_DIR)

    ## Generate or link to the config file
    config_path = osp.join(CONFIG_DIR, 'config.py')
    if config is None:
        # generate the default config.py file
        config_str = pkgutil.get_data(__name__,
                                      'profile_config/config.py')

        with open(config_path, 'wb') as wf:
            wf.write(config_str)

    else:
        os.symlink(config, config_path)

    # then generate the default env.sh file
    env_str = pkgutil.get_data(__name__,
                                  'env_script/env.sh')

    env_path = osp.join(CONFIG_DIR, 'env.sh')
    with open(env_path, 'wb') as wf:
        wf.write(env_str)


if __name__ == "__main__":

    cli()
