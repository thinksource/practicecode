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
}
