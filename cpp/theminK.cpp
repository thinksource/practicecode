#include<stdio.h>
#include<algorithm>

using namespace std;

int partition(int arr[], int s, int e){
	  int x = arr[s];
	  int r = e+1;
	  int l = s;
	  while(l < r){
	    while(l<e && arr[++l] <= x);
	     while(r>s && arr[--r] > x);
	        if(l >= r) break;
	        swap(arr[r],  arr[l]);
	    }
	    arr[s] = arr[r];
	    arr[r] = x;
	    return r;
	}
	int k;
	void minK(int arr[],int start,int end){
	  if(start >= end) return;
	  int index = partition(arr,start,end);
	  if(index == k) return;
	  //类似二分的思想，比快速排序要少一个递归
	  if(index > k) minK(arr,start,index-1);
	    else minK(arr,index+1,end);
    }
	const int M = 200001;
	int n,arr[M];

int main(){
	  while(scanf("%d%d",&n, &k) != EOF){
	    for(int i=0; i<n; i++){
	        scanf("%d", &arr[i]);
	      }
	    --k;
	   minK(arr,0,n-1);
	   sort(arr,arr+k+1);//输出结果需要是排序的
	     for(int i=0; i<k; i++)
	       printf("%d ",arr[i]);
	    printf("%d\n",arr[k]);
	    }
	    return 0;
	}
