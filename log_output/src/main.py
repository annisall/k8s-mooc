import random
import string
import time
import schedule
import logger



def print_random_str(rand_str):
    LOGGER.info(rand_str)

if __name__ == "__main__":
    LOGGER = logger.get_logger(__name__)
    rand_list = random.choices(string.ascii_letters + string.digits + string.punctuation, k = 24)
    rand_str = ''.join(rand_list)
    schedule.every(5).seconds.do(print_random_str, rand_str = rand_str)

    while True:
        schedule.run_pending()
        time.sleep(1)