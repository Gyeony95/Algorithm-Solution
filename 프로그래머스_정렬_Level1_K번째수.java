package programers;

import java.util.Arrays;

public class 프로그래머스_정렬_Level1_K번째수 {

	public static void main(String[] args) {
        int[] array = {5,8,1, 5, 2, 6, 3, 7, 4};
        int[][] commands = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}, {3, 7, 2}};
        
        solution(array,commands );
// 		for(int k = 0; k < solution(array,commands ).length; k ++) {
//			System.out.println(solution(array,commands )[k]);
//		}
	}
	 public static int[] solution(int[] array, int[][] commands) {
	        int[] answer = new int[commands.length];

		 	for(int i = 0; i < commands.length; i++) {//행만큼 반복
		 		int[] subAnswer = new int[commands[i][1] - commands[i][0] +1];
		 		int kk = commands[i][0]-1;
		 		for(int j = 0; j < subAnswer.length; j++) {//임시배열의 길이만큼 반복		 			
		 			subAnswer[j] = array[j+kk];		 			
		 		}	 		
		 		
		 		Arrays.sort(subAnswer);
		 		answer[i] = subAnswer[commands[i][2]-1];
		 		System.out.println("subAnswer[commands[i][2]-1]"+subAnswer[commands[i][2]-1]);
		 		System.out.println("commands[i][2]"+commands[i][2]);
		 	for(int k = 0; k < subAnswer.length; k ++) {
				System.out.println("subAnswer"+"k"+k+"   "+subAnswer[k]);
			}
		 	}	 
	        return answer;
	    }



}
