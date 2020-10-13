"""



"""
FILE_NAME = 'student_info.txt'
MAX = 50
MIN = 1
IOERROR_MES = "Cannot open file on file system."


def write_to_file(*args):
    try:
        with open(FILE_NAME, 'a') as f:
            f.write('{}, {}:\t'.format(args[1], args[0]))
            for i in args[2]:
                f.write('{}\t'.format(i))
            f.write("\n")
    except IOError:
        print(IOERROR_MES)


def get_student_info(**kwargs):
    print("Welcome, {} {}!".format(kwargs['first_name'], kwargs['last_name']))
    scores = []
    num = 0
    while num != -1:
        try:
            num = float(input("Enter a score between {} and {}, (-1 to exit)".format(MIN, MAX)))
            if num == -1:
                break
            elif num < MIN or num > MAX:
                raise ValueError("Score must be between {} and {}".format(MIN, MAX))
            else:
                scores.append(num)
        except ValueError as err:
            print(err)
    write_to_file(kwargs['first_name'], kwargs['last_name'], scores)


def read_from_file():
    try:
        with open(FILE_NAME, 'r') as f:
            read_line = f.read()
            print(read_line)
    except IOError:
        print(IOERROR_MES)


if __name__ == '__main__':
    get_student_info(first_name="Maximum", last_name="Shannon")
    get_student_info(first_name="Minimum", last_name="Polo")
    input("Hold...")
    read_from_file()
    input('Press any key to end.')
