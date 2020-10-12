#include<iostream>
#include<cstdlib>
#define SIZE 20

using namespace std;

int graph[SIZE][SIZE];
int visited[SIZE],stack[SIZE];
int i, j, num, st, top = 0, count = 0;

void push(int n)
{
    top++;
    stack[top]=n;
}

int pop()
{
    int n=stack[top];
    top--;
    return n;
}

void dfs(int st, int num)
{
    //mark vertex element as visited
    int check=0;
    visited[count]=st;
    for (i = st; i < num; i++)
    {
        //check if edge between neighboring vertices exist
        if (graph[st][i]==1)
        {
            for(j=0; j<=count; j++)
            {   
                //check if neighboring vertices already visited
                if(i==visited[j])
                    check=1;
            }
            if (check==0)
            {
                //if not visited push in stack
                push(i);
            }
        }
    }
    count++;
    int x =pop();
    if(count==SIZE)
    {
        return;
    }
    
    //recursive call with top vertex in  stack
    dfs(x ,num);
}

int main()
{
    cout<<"\t\t DFS SEARCH!!"<<endl<<endl;
    cout<<"Enter no. of vertices: ";
    cin>>num;
    cout<<"Enter the Edges that exists among all possible edges in the matrix."<<endl;
    cout<<"Enter 1 if edge exists and 0 if it does not."<<endl<<endl;
    for(i=0;i<num;i++)
    {
        for(j=i;j<num;j++)
        {
            cout<<"Edge between "<<i<<" & "<<j<<" = ";
            cin>>graph[i][j];
        }
    }
    cout<<"\n\nEnter start point: ";
    cin>>st;
    dfs(st, num);
    //print visited array
    cout<<"Visited: ";
    for ( i = 0; i < num; i++)
    {
    cout<<visited[i]<<"\t";
    }
    return 0;
}



