#include<bits/stdc++.h>
using namespace std;

int inverseGCD(int a, int m)
{
    int m0 = m, t, q;
    int x0 = 0, x1 = 1;
 
    if (m == 1)
       return 0;

    while (a > 1)
    {
        q = a / m;
 
        t = m;
 
        
        
        m = a % m, a = t;
 
        t = x0;
 
        x0 = x1 - q * x0;
 
        x1 = t;
    }
 
    if (x1 < 0)
       x1 += m0;
 
    return x1;
}
 
int main()
{
int val[3],rem[3];
int i;
val[0]=3;
val[1]=5;
val[2]=7;

rem[0]=2;
rem[1]=3;
rem[2]=2;

long long prod=1;
for(i=0;i<3;i++)
prod = prod * val[i];

int div[3];

for(i=0;i<3;i++)
{
div[i] = prod / val[i];
}

long long ans = 0;
for(i=0;i<3;i++)
{
ans = ans + (rem[i]*div[i]*inverseGCD(div[i],val[i]));
}
cout<<ans%prod<<endl;
return 0;
}
