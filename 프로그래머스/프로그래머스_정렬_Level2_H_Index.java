package programers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.StringTokenizer;

public class 프로그래머스_정렬_Level2_H_Index {

	public static void main(String[] args) {
		int[] arr = { 3, 3, 3, 5, 5, 5, 5 };
		System.out.println(solution(arr));
		;

	}

	public static int solution(int[] citations) {
		int answer = 0;
		
		Arrays.sort(citations);
		for (int i = 0; i < citations.length; i++) {
		
			if (citations.length - i <= citations[i]) {
				answer = citations.length - i;
				break;
			}
		}

		return answer;
	}

}
