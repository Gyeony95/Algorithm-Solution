package baekjoon;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

//문제 : 문자열 S가 주어졌을 때, SHA-256 해시값을 구하는 프로그램을 작성하시오.
//입력 : 첫째 줄에 문자열 S가 주어진다. S는 알파벳 대문자와 소문자, 그리고 숫자로만 이루어져 있으며, 길이는 최대 50이다.

public class beakjoon10930_SHA256 {

	public static void main(String[] args) {
		System.out.println(testMD5("Baekjoon"));;
		
	}
	
	public static String testMD5(String str){

		String MD5 = ""; 

		try{

			MessageDigest md = MessageDigest.getInstance("MD5"); 
			md.update(str.getBytes()); 
			byte byteData[] = md.digest();
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

