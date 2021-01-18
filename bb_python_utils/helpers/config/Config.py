from envparse import env


def load_env(env_path=None, file_type='env'):
    try:
        if file_type == 'env':
            env.read_envfile(env_path)
    except Exception as e:
        raise e
