public class TwoSum{
  public int[] twoSum(int[] nums, int target){
    int[] res = new int[2];
    HashMap<Integer, Integer> map= new HashMap<>();
    for(int i = 0; i < nums.length; i++){
      int valNeed = target - nums[i];
      if (map.get(nums[i]) != null){
        res[0] = map.get(nums[i]);
        res[1] = i;
        break;
      }
      map.put(valNeed, i);
    }
    return res;
  }

  public int[] twoSum2(int[] numbers, int target){
    int[] result = new int[2];
    if (numbers == null || numbers.length < 2){
      return result;
    }
    int left = 0;
    int right = numbers.leght - 1;
    Array.sort(numbers);
    while(left< right){
      if(numbers[left] + numbers[right] == target ){
        result[0] = left;
        result[1] = right;
      }else if (numbers[left] + numbers[right] < target ){
        left++;
      }else
        right--;
    }
    return result;
  }
}
