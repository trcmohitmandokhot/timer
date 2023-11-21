import time

CLOCK_INTERVAL = 1


def check_validity_timer_start(timer_value):
    if isinstance(timer_value, int) and timer_value > 0:
        return True
    else:
        print("timer_start user entry invalid")
        return False


def update_display(val):
    print(val)


def countdown_logic(timer_start, timer_go, valid_timer_start):
    # Countdown Logic
    timer_now = timer_start

    while timer_go and valid_timer_start:
        update_display(timer_now)
        timer_now = timer_now - 1
        if timer_now < 0:
            timer_go = False
            break
        else:
            time.sleep(CLOCK_INTERVAL)  # 1ms accuracy.


def run_countdown_timer():
    # User Input
    timer_start = 10
    timer_go = True

    valid_timer_start = check_validity_timer_start(timer_start)
    countdown_logic(timer_start, timer_go, valid_timer_start)


if __name__ == "__main__":
    run_countdown_timer()
