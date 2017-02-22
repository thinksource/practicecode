public class Solution{

  public int majorityNumber(ArrayList<Integer> nums){
    int count =0, candiate=-1;
    for(int i=0; i<nums.size();i++){
      if (count==0){
        candiate=nums.get(i);
        count == 1;
      }else if (candiate == nums.get(i)){
        count++;
      }else{
        count--;
      }
    }
    if (count >0) return candiate;
    else return None;
  }
}
