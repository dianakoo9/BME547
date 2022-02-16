import logging

def analyze_data_file(filename):
    in_file = open(filename, 'r')
    keep_reading = True
    line_number = 0
    while keep_reading:
        data_line = in_file.readline()
        if data_line == "":
            keep_reading = False
        else:
            line_number += 1
            process_line(data_line, line_number)
    in_file.close()

def process_line(data_line, line_number):
    data_points = data_line.strip("\n").split(",")
    if len(data_points) < 5:
        logging.warning("The line {} has less than 5 data points".format(line_number))
    data_numbers = [float(i) for i in data_points]
    if any(i < 0 for i in data_numbers): # Are any entries less than 0?
        logging.error("The line {} had a negative numbers".format(line_number))
        return
    if all(1.0 <= i <= 4.0 for i in data_numbers): # Are all entries between 1.0 and 4.0?
        pass
    else:
        logging.info("Line {} was out of range".format(line_number))

if __name__ == "__main__":
    logging.basicConfig(filename = "log_example.log", filemode = "w", level = logging.WARNING)
    analyze_data_file("tsh_data.txt")
