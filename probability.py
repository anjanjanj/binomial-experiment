import random
from statistics import mean

P = 0.001
LOOPS = 100000
NUM_TRIALS = 100

loop_results = list()

for i in range(LOOPS):
    trials = list()

    for i in range(NUM_TRIALS):
        value = random.random()
        trials.append(value <= P)

    total_trials_made = len(trials)
    total_true = trials.count(True)
    loop_data = {
        "total_trials_made": total_trials_made,
        "total_true": total_true,
        "total_false": total_trials_made - total_true
    }
    loop_results.append(loop_data)

avg_total_trials_made = mean([loop['total_trials_made'] for loop in loop_results])
avg_total_true = mean([loop['total_true'] for loop in loop_results])
avg_total_false = mean([loop['total_false'] for loop in loop_results])
loops_with_true = [loop['total_true'] >= 1 for loop in loop_results].count(True) / LOOPS

print("loops made          = " + str(LOOPS))
print("avg trials          = {}".format(avg_total_trials_made))
print("avg True count      = " + str(avg_total_true))
print("avg False count     = " + str(avg_total_false))
print("loops with >=1 True = " + str(loops_with_true * 100) + "%")