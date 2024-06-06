# 그리디 알고리즘을 사용함
# 종료지점이 빠른 순서대로 정렬 후 1번 미사일을 쏘고 그 end 지점을 저장함
# 저장된 end 지점보다 start가 빠른 다음 범위들은 앞에서 쏜 미사일에 의해 처리되었다고 이해
def solution(targets):
    # 종료 지점을 기준으로 정렬
    targets.sort(key=lambda x: x[1])

    # 첫 번째 요격 미사일 발사
    launch_count = 0
    current_end = -1

    for start, end in targets:
        if start >= current_end:
            # 새로운 요격 미사일을 발사해야 하는 경우
            launch_count += 1
            current_end = end  # 현재 요격 미사일이 커버할 수 있는 종료 지점 업데이트

    return launch_count


# 예제 사용
targets = [[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]
print(solution(targets))  # Output: 3
