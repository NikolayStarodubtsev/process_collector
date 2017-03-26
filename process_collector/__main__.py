from process_collector import utils
from process_collector import process_operations


def main():
    utils.privilege_check()
    process_operations.create_info_file()


if __name__ == "__main__":
    main()
