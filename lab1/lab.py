import logging


logging.basicConfig(level=logging.INFO, format=False)


def main():
    try:
        with open("arr.txt") as input_file:
            arr1 = input_file.readline().split()
            arr2 = input_file.readline().split()
    except (IOError, OSError):
        logging.error("file close")
    else:
        logging.info("arr1:\t\tarr2:")
        for index, item in enumerate(arr2):
            logging.info("%s\t\t%s", arr1[index], item)


if __name__ == "__main__":
    main()
