import random
import main
import time
from write_log import *

repeat_time = 0

while (True):

    try:
        repeat_time += 1
        write_all_log(str(repeat_time) + "회째 실행!")

        main.main()  # main.py 실행

        write_all_log("1시간 휴식..")
        # time.sleep(3)
        time.sleep(60 * 60)
        write_all_log("/")

        random_time_sleep = random.randrange(60 * 60)
        # random_time_sleep = 3

        if random_time_sleep < 60:
            print(str(random_time_sleep) + "초 추가로 휴식.. (랜덤 결과)")
        else:
            print(str(random_time_sleep // 60) + "분 " + str(random_time_sleep % 60) + "초 추가로 휴식.. (랜덤 결과)")

        time.sleep(random_time_sleep)
        write_all_log("/")
        write_all_log("끝.")
        write_all_log("\n====================================================")
        write_all_log("====================================================\n")


    except Exception as e:
        error = str(e)
        write_all_log("\n\n\t***에러가 발생하였습니다ㅠㅠ")
        write_all_log(error + "\n")

        random_time_sleep = random.randrange(60 * 30)
        if random_time_sleep < 60:
            write_all_log(str(random_time_sleep) + "초 추가로 휴식.. (랜덤 결과) - 에러 휴식")
        else:
            write_all_log(
                str(random_time_sleep // 60) + "분 " + str(random_time_sleep % 60) + "초 추가로 휴식.. (랜덤 결과) - 에러 휴식")

        time.sleep(random_time_sleep)
        write_all_log("/")