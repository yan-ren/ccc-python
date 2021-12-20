import subprocess
from os import listdir
from os.path import isfile, join

PYTHON_VERSION = 'python3'
TEST_SRC = 'src/s2012s1.py'
TEST_DATA_PATH = 'test/s2012/s1/'


def setup(path):
    output = []
    all_files = [join(path, f) for f in listdir(path) if 'in' in f and isfile(join(path, f))]
    all_files.sort()
    for file in all_files:
        output.append((file, file.replace('.in', '.out')))
    return output


def run(test_script, input_file):
    with open(input_file, 'r') as f:
        input_value = f.read()
    result = subprocess.run([PYTHON_VERSION, test_script], input=input_value.encode('utf-8'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result


def compare(result, expected, src):
    with open(expected, 'rb') as f:
        expected_result = f.read()
    if result.stderr != b'':
        print('FAIL: test should not returned stderr:', result.stderr, 'src:', src)
    if result.stdout.decode('utf8') == expected_result.decode('utf8'):
        print('PASS', expected)
    else:
        print('FAIL: expected:', expected_result, ' got:', result.stdout, 'src:', src)


if __name__ == '__main__':
    test_data_set = setup(TEST_DATA_PATH)
    for data in test_data_set:
        result = run(TEST_SRC, data[0])
        compare(result, data[1], data[0])