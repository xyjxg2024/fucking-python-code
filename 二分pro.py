# #include<iostream>
# using namespace std;
# int n,m;
# int a[100007];//看题
# int l,r,mid;
# int main(){
# 	cin>>n>>m;
# 	for(int i=1;i<=n;i++){
# 		cin>>a[i];
# 		l=max(l,a[i]);//预处理，最小开销至少跟花费最大的那个月一样
# 		r+=a[i];//最大开销可能是所有的月加起来
# 	}
# 	while(l<r){//模板
# 		mid=(l+r)/2;
# 		int sum=0,cnt=0;
#         	//sum是累加当前的钱，cnt是要分成几组
# 		for(int i=1;i<=n;i++){
# 			if(sum+a[i]<=mid)//如果加上这个月的花费还比枚举到的开销小
# 				sum+=a[i];//那就继续加
# 			else sum=a[i],cnt++;//不然就要分一组出来
# 		}
# 		if(cnt>=m)l=mid+1;//可分的组数较多，说明开销还可以更大
# 		else r=mid;//开销太大导致分的组数少
# 	}
# 	cout<<l<<endl;//最后l即为答案
# 	return 0;
# }
