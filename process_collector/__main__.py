from process_collector import privilege_check
from process_collector import process_operations


def main():
    privilege_check.privilege_check()
    process_operations.create_info_file()


if __name__ == "__main__":
    main()
