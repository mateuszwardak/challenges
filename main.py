import matplotlib.pyplot as plt


DEFAULT_INPUT_FILE_PATH = 'challenge_attachments/2_census_2009b'
RESULT_FILE_NAME = 'graph.png'

# based on Benford's Law Wikipedia page: https://en.wikipedia.org/wiki/Benford%27s_law
EXPECTED_DATA_DISTRIBUTION = (30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6)

# TODO:
#  tests
#  database
#  project structure cleanup - divide into separate challenges


def open_file(get_path_from_user=False):
    file_path = DEFAULT_INPUT_FILE_PATH

    if get_path_from_user:
        file_path = input("Please specify your file's path (relative to project's root, "
                          "without preceding slash, eg: 'files/input_file.txt'): ")

    try:
        file = open(file_path)
        return file.read()
    except FileNotFoundError:
        print("File not found.")
        if input("Do you want to try again? y/n: ").lower() == 'y':
            return open_file(get_path_from_user)
        else:
            exit()


def get_number_from_line(line, i=0):
    line_columns = line.split()

    try:
        relevant_number = int(line_columns[i])
        return relevant_number
    except ValueError:
        # if proper number is not found in a column, check next column recursively
        return get_number_from_line(line, i + 1)
    except IndexError:
        # no number found in a line probably means end of file or irrelevant spacing line - ignore it
        return


def get_keys():
    return tuple(range(1, 10))


def prepare_data(data_list):
    print("Preparing graph data...")
    digits = get_keys()
    number_sum = 0
    data = []

    # first, we prepare 'digit_counts' dict and set each digit's count to 0, so we can add to it
    digit_counts = {}
    for key in digits:
        digit_counts[key] = 0

    # then, we fill the data in
    for n in data_list:
        digit_counts[n] += 1
        number_sum += 1

    # and get percentage value of each digit's count
    for key, value in digit_counts.items():
        data.append(round((value / number_sum) * 100, 1))

    return data


def make_graph(data):
    print("Drawing result graph...")
    keys = get_keys()
    x_pos = [i for i, _ in enumerate(keys)]
    expected_data = EXPECTED_DATA_DISTRIBUTION

    overlapping_data = {'x': [], 'y': []}
    for i, value in enumerate(data):
        if data[i] == expected_data[i]:
            overlapping_data['x'].append(i)
            overlapping_data['y'].append(value)

    plt.bar(x_pos, data, alpha=0.7, color='red', label='input data')
    plt.bar(x_pos, expected_data, alpha=0.2, color='green', label='expected distribution')
    plt.plot(overlapping_data['x'], overlapping_data['y'], 'g*', label='matching')

    plt.title("Leading digit distribution")
    plt.xlabel("Leading digit")
    plt.ylabel("Percentage of occurence (%)")

    plt.xticks(x_pos, keys)
    plt.legend()
    plt.savefig(RESULT_FILE_NAME)


leading_digits = []
attachment_content = open_file(input("Do you want to supply your own file? y/n: ").lower() == 'y')
print("Reading file...")
for file_line in attachment_content.split('\n')[1:]:
    number = get_number_from_line(file_line)
    if number is not None:
        print('number', number)
        leading_digit = str(number)[0]
        leading_digits.append(int(leading_digit))

graph_data = prepare_data(leading_digits)
make_graph(graph_data)
print("Done.")
