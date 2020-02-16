package programers;

import java.awt.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Set;

import javax.swing.text.html.HTMLDocument.Iterator;

import com.sun.javafx.collections.MappingChange.Map;

//주소 : https://programmers.co.kr/learn/courses/30/lessons/42579


public class 프로그래머스_해시_베스트앨범 {

	public static void main(String[] args) {
		String[] genres = { "pop", "pop", "asd", "pop", "classic", "pop", "asd" };
		int[] plays = { 5000, 5000, 4000, 500011, 123456, 5000, 4000 };

		int[] arr = solution(genres, plays);

		for (int i = 0; i < arr.length; i++) {
			System.out.println(arr[i]);
		}
	}

	static HashMap<String, Integer> baseHm = new HashMap<String, Integer>();// 해시맵선언
	static HashMap<String, Integer> firstHm = new HashMap<String, Integer>();// 그 카테고리의 가장 큰수
	static HashMap<String, Integer> secondHm = new HashMap<String, Integer>();// 그카테고리의 두번쨰로 큰수
	static HashMap<Integer, Integer> indexHm = new HashMap<Integer, Integer>();// 인덱스 저장 위치
	static HashMap<Integer, Integer> subIndexHm = new HashMap<Integer, Integer>();// 인덱스 저장 위치

	public static int[] solution(String[] genres, int[] plays) {

		String[] genresList = new String[genres.length]; // 최대갯수인 장르의 길이만큼 배열생성
		int k = 0;// 장르리스트의 인덱스역할이자 장르의 종류 갯수

		// 각 재생횟수가 몇번째 인덱스에 있는지
		for (int i = 0; i < plays.length; i++) {// 인덱스 저장위치 해시맵에 저장
			if (indexHm.getOrDefault(plays[i], -1) == -1) {// 처음임
				indexHm.put(plays[i], i);//그냥 그자리에 넣음
			} else {// 해당하는 재생수 값이 들어온게 처음이 아니면
				indexSet(indexHm.get(plays[i]), i);//값을 넣을자리를 찾을때까지 재귀함수를 실행
			}
		}

		for (int i = 0; i < genres.length; i++) {
			// baseHm에의해 각 카테고리의 총재생수를 구할 수 있음
			if (baseHm.getOrDefault(genres[i], -1) == -1) {// 처음들어가는 값일때
				baseHm.put(genres[i], plays[i]);
				genresList[k] = genres[i];// 장르가 중복없이 배열에 들어감
				k++;
			} else {// 처음들어온 값이 아닐때
				baseHm.put(genres[i], baseHm.get(genres[i]) + plays[i]);// 총재생 수 더해서 덮어쓰기
			}
			// 아래 조건문을 통해 각 카테고리의 첫번째로 큰 수와 두번째로 큰 수를 얻어올 수 있음
			if (firstHm.getOrDefault(genres[i], -1) == -1) {// 퍼스트해시맵 처음
				firstHm.put(genres[i], plays[i]);
			} else {// 처음 아닐때
				if (firstHm.get(genres[i]) > plays[i]) {// 새로들어온값보다 기존에 있던 값이 클때
					if (secondHm.getOrDefault(genres[i], -1) == -1) {// 세컨드해시맵 처음
						secondHm.put(genres[i], plays[i]);
					} else {// 세컨드 해시맵도 처음 아닐때
						if (secondHm.get(genres[i]) >= plays[i]) {// 새로 들어온값보다 기존에 있던값이 클때

						} else {// 새로들어온값이 더 클때
							secondHm.put(genres[i], plays[i]);
						}
					}
				} else if (firstHm.get(genres[i]) == plays[i]) {// 기존값과 같을때
					secondHm.put(genres[i], plays[i]);// 세컨드에 넣어버림
				} else {// 기존에 있던 값보다 새로들어온값이 클때
					secondHm.put(genres[i], firstHm.get(genres[i]));// 첫번째에 있던 값을 두번째로 옮기고
					firstHm.put(genres[i], plays[i]);// 새로들어온 값을 첫번째로 넣어줌
				}
			}
		}

		// baseHm에 있는 키들을 value의 값 순서대로 나열함
		ArrayList<String> keySetList = new ArrayList<>(baseHm.keySet());
		Collections.sort(keySetList, (o1, o2) -> (baseHm.get(o2).compareTo(baseHm.get(o1))));

		int[] answer = new int[k * 2];//임시로 쓸 배열임 정답에 사용할 배열은 따로 만들거
		for (int i = 0; i < k * 2; i++) {//일단 값의 비교를위해 배열 전부에 더미값인 -1을 넣어줌
			answer[i] = -1;
		}

		for (String key : keySetList) {//위에서 정렬한 ArrayList를 순차적으로 반복함
			for (int i = 0; i < k * 2; i++) {
				if (answer[i] == -1) {// 빈인덱스라는의미
					answer[i] = indexHm.get(firstHm.get(key));
					for (int j = 0; j < i; j++) {
						if (answer[j] == indexHm.get(firstHm.get(key))) {
							answer[i] = subIndexHm.get(indexHm.get(firstHm.get(key)));
							break;
						}
					}
					if (indexHm.getOrDefault(secondHm.get(key), -1) != -1) {// 키에대한 두번째 큰수가 있다면
						i++;
						answer[i] = indexHm.get(secondHm.get(key));// 다음인덱스에 두번째로 큰값에대한 인덱스를 넣어줌
						for (int j = 0; j < i; j++) {
							if (answer[j] == indexHm.get(secondHm.get(key))) {
								answer[i] = subIndexHm.get(indexHm.get(secondHm.get(key)));
								break;
							}
						}
						break;
					} else {
						break;
					}
				}
			}

		}
		int realLength = 0;//실제 정답의 배열이 될 크기
		for (int i = 0; i < k * 2; i++) {//임시배열answer에서 더미로 넣어놓은 -1들을 제외한 길이를 구함
			if (answer[i] == -1) {
				break;
			} else {
				realLength++;
			}
		}

		int[] realanswer = new int[realLength];//실제 정답길이만큼의 배열생성
		for (int i = 0; i < realanswer.length; i++) {
			realanswer[i] = answer[i];//답을 넣어줌
		}

		return realanswer;
	}

	public static void indexSet(int key, int value) {//재귀함수
		if (subIndexHm.getOrDefault(key, -1) == -1) {//키로들어온걸로 get했을때 -1이 리턴되면 비어있다는의미
			subIndexHm.put(key, value);//비어잇으면 put함
		} else {//비어있지않음
			indexSet(subIndexHm.get(key), value);//키로 들어온부분이 빈값이 아니라면 빈값이 아닌걸 키값으로 다시 indexSet 호출함, value는 같음
		}
	}

}
