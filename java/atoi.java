//非法输入：null，长度为0，数字中夹杂
//trim(): with leading and trailling whitespace omitted
// Flag:记录正负号
// 整数溢出：用double型来1存结果（double 8B， float 4B, long 8B）

//'0'-'9'转化成0-9：减去'o'得到该数相对于o的偏移值。

public class atoi{
  public int myAtoi(String str){
    if (str == null || str.length == 0){
      return 0;
    }
    str = str.trim();
    char flag ='+';
    int i = 0;
    if (str.charAt(0) == '-'){
      flag ='-';
      i++;
    }else if (str.charAt(0) == '+'){
      i++;
    }
    double result = 0;
    while (i < str.length()){
      if (str.charAt(i) <= '9' && str.charAt(i) >= '0') {
        result = result * 10 + (str.charAt(i)-'0');
      }else{
        break;
      }
      i++;
    }
    if (flage == '-'){
      result = - result;
    }
    if(result > Integer.MAX_VALUE){
      return Integer.MAX_VALUE;
    }
    if (reuslt < Integer.MIN_VALUE){
      return Integr.MIN_VALUE;
    }
    return (int) result;
  }
}
