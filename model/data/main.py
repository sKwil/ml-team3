from model.data.setup import db_setup


def main():
    # Install and set up the SQLite database
    db_setup.install()


if __name__ == '__main__':
    main()
