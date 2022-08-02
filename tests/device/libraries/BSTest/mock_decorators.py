
env = {}

def setup(test_name):
	global env
	if test_name not in env:
		env[test_name] = {}
	func_env = env[test_name]
	def decorator(func):
		def func_wrapper():
			return func(env[test_name])
		func_env['setup'] = func_wrapper
		return func_wrapper

	return decorator



def teardown(test_name):
	global env
	if test_name not in env:
		env[test_name] = {}
	func_env = env[test_name]
	def decorator(func):
		def func_wrapper():
			return func(env[test_name])
		func_env['teardown'] = func_wrapper
		return func_wrapper

	return decorator

def setenv(test_env, key, value):
    if 'env' not in test_env:
        test_env['env'] = []
    test_env['env'] += [(key, value)]

def request_env(test_env, key):
	return test_env['request_env'](key)

def get_all_envs(test_name):
	global env
	if test_name not in env:
		return None
	return None if 'env' not in env[test_name] else env[test_name]['env']
