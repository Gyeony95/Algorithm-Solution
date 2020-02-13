package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.StringTokenizer;

//해싱
//https://www.acmicpc.net/problem/10927
//문제 : 문자열 S가 주어졌을 때, MD5 해시값을 구하는 프로그램을 작성하시오.
//입력 : 첫째 줄에 문자열 S가 주어진다. S는 알파벳 대문자와 소문자, 그리고 숫자로만 이루어져 있으며, 길이는 최대 50이다.

public class beakjoon10927_MD5 {	  
	public static void main(String[] args) throws IOException {
		 BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer token = new StringTokenizer(br.readLine());
		System.out.println(testMD5(token.nextToken()));;
	
	}
	public static String testMD5(String str){
		String MD5 = ""; 
		try{
			//MessageDigest 인스턴스 생성
			MessageDigest md = MessageDigest.getInstance("MD5"); //MD5형식으로 암호화 한다는 의미
			//해시값 업데이트 -> 업데이트 호출 할때마다 MD5내부에 digest값이 갱신됨 최종적으로 digest()메서드를 호출하면 그 값을 가져올수있음
			md.update(str.getBytes()); 
			byte byteData[] = md.digest();//값 가져옴
			StringBuffer sb = new StringBuffer(); 
			for(int i = 0 ; i < byteData.length ; i++){
				sb.append(Integer.toString((byteData[i]&0xff) + 0x100, 16).substring(1));
			}
			MD5 = sb.toString();
		}catch(NoSuchAlgorithmException e){
			e.printStackTrace(); 
			MD5 = null; 
		}
		return MD5;
	}

}

