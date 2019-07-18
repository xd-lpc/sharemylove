public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        
       int index[] = { 0, 0 };

		int len = numbers.length;
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

		for (int i = 0; i < len; i++) {

			map.put(numbers[i], i );

		}
		
		
		for(int i = 0;i < len;i++){
			
			if(map.get(target - numbers[i]) != null && map.get(target - numbers[i]) > i){
				index[0] = i;
				index[1] = map.get(target - numbers[i]);
				
			}
			
			
		
			
		}
		

		return index;
        
    }

public static void main(String agrs[]){
    int[] numbers = {0,4,3,0} ;
    int target = 0;
    int[] result = twoSum(numbers, target);
    System.out.println("index1="+result[0]+", index2="+result[1]);
    //index1=1, index2=2
}



}