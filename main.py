from controller import *

def main():
    application = QApplication([])
    window = Controller()
    window.show()

    application.exec()

if __name__ == '__main__':
    main()