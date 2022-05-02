from model.product import model


def main() -> None:
    """
    Train the final ML model and save it in a pickle file.

    :return: None
    """

    model.process()


if __name__ == '__main__':
    main()
