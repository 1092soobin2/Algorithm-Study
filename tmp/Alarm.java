import java.util.Deque;
import java.util.HashMap;
import java.util.ArrayDeque;


public class Alarm {
	private String[] ip_group;
	private int num_of_ip;

	public Alarm() {
		String[] new_ip_group = {"123.456.789.000", "456.678.123.000"};
		this.ip_group = new_ip_group;
		this.num_of_ip = 2;
	}

	public void parse_data(String data) {

		int threshold = 100;

		// Deque<Integer> deque = new ArrayDeque<Integer>(); 				// 20초 확인 배열
		// deque.addLast(threshold * 2);
		// deque.addLast(threshold * 2);
		// deque.addLast(threshold * 2);
		// deque.addLast(threshold * 2);
		// deque.addLast(threshold * 2);
		// deque.addLast(threshold * 2);
		
		// deque.addLast(10);
		// deque.removeFirst();


		/* [주소] = [데크] */
		HashMap<String, Deque<Integer>> hashMap = new HashMap<>();

		for (int i = 0 ; i < num_of_ip; i++) {
			/* 30초 비교 */
			Deque<Integer> deque = new ArrayDeque<Integer>();
			deque.addLast(threshold * 2);
			deque.addLast(threshold * 2);
			deque.addLast(threshold * 2);
			deque.addLast(threshold * 2);
			deque.addLast(threshold * 2);
			deque.addLast(threshold * 2);
			
			hashMap.put(ip_group[i], deque);
		}

		String[] splittedData = data.split(";");
		for (int i = 0; i < num_of_ip; i++) {
			hashMap.get(ip_group[i]).addLast(Integer.parseInt(splittedData[i]));
			hashMap.get(ip_group[i]).removeLast();

		}
		
		for (int i = 0; i < num_of_ip; i++) {
			System.out.println("after dequeing" + hashMap.get(ip_group[i]));
		}

		
     
	}
	
}
