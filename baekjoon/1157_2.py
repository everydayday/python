
# alphabet = input()
alphabet = "zbaaa"

# 비교 시 모든 알파벳 소문자로 변경
# 처음 case
count = 1
most_alph = alphabet[0].upper()
for alpha in alphabet[1:]:
    if alpha.lower() == most_alph.lower():
        count += 1


# 모든 case 비교
# 한 글자일 시 하나만 출력
if len(alphabet) != 1:
    for idx, alpha in enumerate(alphabet,start=1): # 1번 index 부터 시작
        temp_count = 1  # 자기 자신 갯수
        for alpha2 in alphabet[idx+1:]:       # idx + 1 부터 시작
            print("alpha2 ",alpha2)
            if alpha.lower() == alpha2.lower() :
                temp_count += 1
        print("temp_count:", temp_count)
        print("alphabet[idx+1:]", alphabet[idx+1:])
        print("=" * 10)
        if temp_count > count :
            count = temp_count
            most_alph = alpha.upper()
        if temp_count == count :
            most_alph = "?"

print(most_alph)


