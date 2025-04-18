import re

def filter_log(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    filtered_lines = []
    pattern = r'Training progress:.*?(\d+)/30000'

    for line in lines:
        match = re.search(pattern, line)
        if match:
            iteration = int(match.group(1))
            if iteration % 1000 == 0 or iteration == 0:
                filtered_lines.append(line)

    with open(output_file, 'w') as f:
        f.writelines(filtered_lines)

if __name__ == "__main__":
    input_file = "result.err"
    output_file = "filtered_log.txt"
    filter_log(input_file, output_file)