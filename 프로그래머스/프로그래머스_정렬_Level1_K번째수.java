package programers;

import java.util.Arrays;

public class ���α׷��ӽ�_����_Level1_K��°�� {

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

		 	for(int i = 0; i < commands.length; i++) {//�ุŭ �ݺ�
		 		int[] subAnswer = new int[commands[i][1] - commands[i][0] +1];
		 		int kk = commands[i][0]-1;
		 		for(int j = 0; j < subAnswer.length; j++) {//�ӽù迭�� ���̸�ŭ �ݺ�		 			
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
