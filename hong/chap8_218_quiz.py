# 샌드위치 재료 받는 함수
def show_sandwich(*sandwiches):
    for snd in sandwiches:
        print(snd)
    print("==================")

show_sandwich("서브웨이 샌드위치")
show_sandwich("햄 샌드위치", "샐러드 샌드위치")
show_sandwich("계란 샌드위치", "양상추 샌드위치", "빅 샌드위치")

