import subprocess
from os import listdir
from os.path import isfile, join

# using / for both windows and macos
TEST_SRC = "src/junior/j2012/j5.py"
TEST_DATA_PATH = "test/j2012/j5/"
# use python or python3 depends on PATH setup
# for example, in windows, check what's the python path that is added to PATH env variable
# in macos, check what is added in /usr/local/bin, most of time for python3 is python3
PYTHON_VERSION = "python3"


def setup(path):
    """Given a path of directory containing the test data files, return a list of path for each .in file

    Args:
        path (string): a string contains the path of source data files
    Returns:
        list: a list of source data file path
    """
    output = []
    all_files = [
        join(path, f) for f in listdir(path) if "in" in f and isfile(join(path, f))
    ]
    all_files.sort()
    for file in all_files:
        output.append((file, file.replace(".in", ".out")))
    return output


def run(test_script, input_file):
    """Run test script with the input data file as stdin

    Args:
        test_script (string): file path
        input_file (string): file path

    Returns:
        CompletedProcess[bytes]:
    """
    with open(input_file, "r") as f:
        input_value = f.read()
    result = subprocess.run(
        [PYTHON_VERSION, test_script],
        input=input_value.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result


def compare(result, output_file, input_file):
    """Compare test result with the expected output file

    Args:
        result (CompletedProcess[bytes]): [description]
        output_file (string): file path
        input_file (string): file path

    Returns:
        bool:
    """
    with open(output_file, "rb") as f:
        expected_result = f.read()
    if result.stderr != b"":
        print(
            "FAIL: test should not returned stderr:",
            result.stderr,
            "input_file:",
            input_file,
        )
        return False

    # Normalize newline characters to '\n'
    normalized_result = result.stdout.decode("utf8").replace('\r\n', '\n')
    normalized_expected = expected_result.decode("utf8").replace('\r\n', '\n')

    if normalized_result == normalized_expected:
        print("PASS", output_file)
        return True
    else:
        print(
            "FAIL: expected:",
            expected_result,
            " got:",
            result.stdout,
            "input_file:",
            input_file,
        )
        return False


if __name__ == "__main__":
    test_data_set = setup(TEST_DATA_PATH)
    test_counter = 0
    passed = 0
    failed = 0
    for data in test_data_set:
        test_counter += 1
        result = run(TEST_SRC, data[0])
        if compare(result, data[1], data[0]):
            passed += 1
        else:
            failed += 1
    print("===========================================================")
    print(f"Run {test_counter} tests, PASS: {passed}, FAILED: {failed}")
