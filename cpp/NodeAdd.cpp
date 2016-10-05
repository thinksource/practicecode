typedef struct tagSNode
{
  int value;
  tagSNode* pNext;
  tageSNode(int v): value(v),pNext(NULL){}
}SNode;

int main(int argc, char* argv[]){
  SNode* pHead1=new SNode(0);
  int i;
  for(i =0; i<6; i++){
    SNode* p = new SNode(rand() % 1);
  }
}

SNode Add(SNode* pHead1, SNode* pHead2){
  SNode* pSum = pSum;
  SNode* pTail = pSum;
  SNode* p1= pHead->pNext;
  SNode* p2= pHead->pNext;
  SNode* pCur;
  int carry = 0;
  int value;
  while (p1 && p2){
    value=p1->value+p2->value+carry;
    carry= value / 10;
    value %= 10;
    pCur = new SNode(value);
    pTail->pNext = pCur;
    pTail=pCur;
    p1=p1->pNext;
    p2=p2->pNext;
  }
  SNode* p=p1?p1:p2;
  while (p){
    value=p->value+carry;
    carry= value / 10;
    value %= 10;
    pCur = new SNode(value);
    pTail->pNext = pCur;
    pTail=pCur;
    p=p->pNext;
  }
  if (carry !=0)
    pTail->pNext= new SNode(carry);
  return pSum;
}
