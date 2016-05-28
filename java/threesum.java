public class threesum{
  public List<List<integer>> threeSum(int[] nums){
    if(nums == null || nums.length < 3){
      return res;
    }

    Arrays.sort(nums);
    for(int i =0; i < nums.length - 2; i++){
      if (i != 0 && nums[i] != nums [i-1]){
        continue;
      }
      int left = i + 1;
      int right = nums.length - 1;
      while (left < right){
        int sum = nums[left] + nums[right] + nums[i];
        if (sum == 0){
          List<Integer> list = new ArrayList();
          list.add(nums[i]);
          list.add(nums[left]);
          list.add(nums[right]);
          res.add(list);
          left++;
          right--;
          while(left < right && nums[left] == nums[left-1]){
            left++;
          }
          while(left < right && nums[right] == nums[right+1]){
            right--;
          }

        }else if(sum < 0){
          left++;
        }else{
          right--;
        }
      }
    }
    return res;
  }
}
