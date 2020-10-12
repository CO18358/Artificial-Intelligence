#include<iostream>
#include<cstdlib>
#define SIZE 20

using namespace std;

int graph[SIZE][SIZE];
int visited[SIZE],queue[SIZE];
int i, j, num, front = 0, rear = -1,st;

void bfs(int v)
{
	for(i = 1; i <= num; i++)
	if(graph[v][i]==1 && visited[i]!=1)
	queue[++rear] = i;
	if(front <= rear)
	{
		visited[queue[front]] = 1;
		bfs(queue[front++]);
	}
}

int main()
{
	cout<<"\t\t DFS SEARCH!!"<<endl<<endl;
	cout<<"Enter no. of vertices: ";
	cin>>num;
	for(i=1; i <= num; i++)
	{
	queue[i] = 0;
	visited[i] = 0;
	}
	cout<<"Enter the Edges that exists among all possible edges in the matrix."<<endl;
	cout<<"Enter 1 if edge exists and 0 if it does not."<<endl<<endl;
	for(i=0;i<num;i++)
	{
		for(j=0;j<num;j++)
		{
		cout<<"Edge between "<<i<<" & "<<j<<" = ";
			cin>>graph[i][j];
		}
	}
 	cout<<"\n\nEnter start point: "<<endl;
	cin>>st;
	bfs(st);
	cout<<endl<<"Traversable Nodes:";
	for(i=0; i < num; i++)
	{
		if(visited[i]==1)
			cout<<i<"\t";
		else
		{
			cout<<endl<<"BFS not Possible! Every node can't be traversed.";
			break;
		}
	}
	
	return 0;
}

