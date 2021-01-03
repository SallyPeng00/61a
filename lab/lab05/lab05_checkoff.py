def partitions_options(total, biggest_num):
	if total == 0:
		return [[]]
	elif total < 0:
		return []
	if biggest_num == 0:
		return []
	else:
		with_biggest = partitions_options(total-biggest_num, min(biggest_num, total-biggest_num))
		without_biggest = partitions_options(total, biggest_num-1)
		with_biggest = [[biggest_num] + elem for elem in with_biggest]
		return with_biggest + without_biggest


[[1,1,1], [2,1]]

