public class maxmode{

  public static int mode(int[] a){
    int count=0;
    int m=a[0];
    for(int i=0;i<a.length;i++){
      if(count==0){
        count=a[i];
        count=1;
      }else if(m !=a[i]){
        count--;
      }else{
        count++;
      }
    }
    return m;
  }

  public static void main(String[] args){
    int a[]={2, 8, 2, 8,18,1,1,6,8};
    int m=mode(a);
    System.out.println(m);
  }
}
