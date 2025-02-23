import numpy as np

class BaysianBelief:

    def __init__(self, wake:float, sleep:float, attention_peak:float):
        self.avg_wake_time = wake
        self.avg_sleep_time = sleep
        self.peak_attention = attention_peak

if __name__=="__main__":
    print("Now I am changing the IDE!")
