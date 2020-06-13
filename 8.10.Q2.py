import logging

def devide(x1, x2):
    try:
        return x1 / x2
    except ZeroDivisionError:
        logging.exception('Zero divide error %s/%s', x1, x2)
    except:
        logging.exception('Exception')

if __name__ == '__main__':
    devide(1, 0) 