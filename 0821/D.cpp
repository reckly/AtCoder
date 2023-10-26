#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n,p,q,r;
    cin>>n>>p>>q>>r;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }

    int current = 0;
    int pp=p;
    int qq=q;
    int rr=r;
    int flag=0;
    for(int i=0;i<n;i++){
        current=i;
        while(pp>0){
            pp-=a[current];
            if(pp<0){
                break;
            }else if(pp==0){
                current++;
                if(current==n){
                    break;//ここです
                }
                while(qq>0){
                    qq-=a[current];
                    if(qq<0){
                        break;
                    }else if(qq==0){
                        current++;
                        while(rr>0){
                            rr-=a[current];
                            if(rr<0){
                                break;
                            }else if(rr==0){
                                cout<<"Yes"<<endl;
                                flag=1;
                                break;
                            }else{
                                break;
                            }
                        }
                    }else{
                        current++;
                    }
                }
            }else{
                current++;
            }
        }
        if(flag==1){
            break;
        }
        pp=p;
        qq=q;
        rr=r;
    }
    if(flag==0){
        cout<<"No"<<endl;
    }
}