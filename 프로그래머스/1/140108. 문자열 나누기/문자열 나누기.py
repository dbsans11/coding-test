def solution(s):
	answer = 0
	x = ''
	x_cnt = 0
	other_cnt = 0

	for char in s:
		if x_cnt == 0 and other_cnt == 0:
			x = char

		if char == x:
			x_cnt += 1
		else:
			other_cnt += 1

		if x_cnt == other_cnt:
			answer += 1
			x_cnt = 0
			other_cnt = 0

	if x_cnt > 0 or other_cnt >0:
		answer += 1

	return answer