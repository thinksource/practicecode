public class RotatedSortedArray{
  public int search(int A[], int target){
    int first =0, last = A.length-1;
    while(first != last){
      int mid= (first + last)/2;
      if (A[mid] == target)
        return mid;
      if (A[first] <= A[mid]){
        if(A[first] <= target && target < A[mid])
          last = mid;
        else
          first = mid + 1;
      }else{
        if (A[mid]< target && target <= A[last-1])
          first = mid + 1;
        else
          last = mid;
      }
    }
    return -1;
  }

  public static int searchr(int A[], int target){
    return searchBinary(A, 0, A.length-1, target);
  }

  public static int searchBinary(int A[], int s, int e, int target){
    int mid = (s+e)/2;
    if(A[mid] == target)
      return mid;
    if (s >= e){
      if(target > A[mid] && target <= A[e]){
        return searchBinary(A, mid+1, e, target);
      }else
        return searchBinary(A, s, mid-1, target);
    }else{
      if(target >= A[s] && target < A[mid])
        return searchBinary(A, s, mid-1, target);
      else
        return searchBinary(A, mid+1, e, target);
    }
  }
}
