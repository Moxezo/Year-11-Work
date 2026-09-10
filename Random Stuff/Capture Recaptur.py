import random
estlist = []
marklist = ["marked","unmarked"]
weights = [30,160]
unmarked = 0
marked = 0
sample = 0
while sample < 12:
    samplemarked = 0
    sampleunmarked = 0
    capture = random.choices(marklist, weights=weights, k=20)

    samplemarked = capture.count("marked")
    sampleunmarked = capture.count("unmarked")

    if samplemarked != 0:
        estimate = (30*20) / samplemarked
        estlist.append(estimate)
        marked += samplemarked
        unmarked += sampleunmarked
    else:
        continue
    sample += 1
    print(f"Sample {sample}:")
    print(f"Marked: {samplemarked}")
    print(f"Unmarked: {sampleunmarked}")
print(f"Avg Marked: {marked/12}")
print(f"Avg Unmarked: {unmarked/12}")
print(f"Estimated population: {round(sum(estlist)/12)}")