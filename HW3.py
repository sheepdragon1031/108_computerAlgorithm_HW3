from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askinteger
from random import randint
from collections import defaultdict 

import base64

hello = b'iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAACkUlEQVR42uyai3GDMAyGQyegGzACnaCMkBHoBhkhnSAj0A2SDaAT0E6QbEA3cOXW6XEpBtnImMv9utOllxjF/qKHLTdRSm0gdnkAAgACIAACIAACIAACIAgAARAAARAAARAAARBEAFCSJINKkpLuSTtSZbQz76W25zhKkpFWPbtaz6Q75vPuoluuPmqxlZK2yi76s9RznjlpN2K7CrFWaUAHNS0HT0Atw3YpDSjxbdoPuaziG3uk579cvIdeWsbQD7L7NAYoWpKmLy8chueO5reB7KKKrQnQJdDYn9AJZHc5QBT7enINY2hjxrqItsvJWSdxFxKuYlOlWJmE6zPPcsJuN7WFiF7me5DOAws4OyZyG6TOsr/KQziDaJm/mcy2V1V0+T0JeXxqqlrWC9mGGy3O6wwFaI0SdR+EMg9AEAACIAByqViZb+/prgFdN6qb306j3lTWs0BJ76Qjw0ktO+3ad60PQhMrfM9YwqK7lUPe4j+/OR40cDaqJeJ+xo80JsWih1WTBAcb8ysKrb+TfowQKy3v55wbBkk49FJbQusqr4snadL9hEtXC3nO1G1HG6UfxIj5oDnJlHPOVVAerWGmvYQxwc70hiTh7Bidy3/3ZFE6isxf8epNhUCl4n5ftYqWKzMP3IIquaFnquXO0sZ1yn/RWq69SuK6GdPXORfSz4HPnk1bNXO0+UZze5HqKIodNYwnHVVcOUivNcStxj4CGFYhWAWgXgmuF4JzdMhn6wDUm1DpmFyVY7IvQqeTRdod2v2F8lNn/gcpW+rUsOi9mAmFwlSo3Pw9JQ3p+8bhgnAMkPM613BxOBQqc2FEB4SmPQSAAAiAAAiAAAiAAAiAIAAEQAAEQAAEQPco3wIMADOXgFhOTghuAAAAAElFTkSuQmCC'
master = Tk()
 
class Graph: 
  
    def __init__(self,vertices): 
        self.V= vertices # No. of vertices 
        self.graph = []  # default dictionary  
                         # to store graph 
        

    # function to add an edge to graph 
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    # A utility function to find set of an element i 
    # (uses path compression technique) 
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    # A function that does union of two sets of x and y 
    # (uses union by rank) 
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 

        # Attach smaller rank tree under root of  
        # high rank tree (Union by Rank) 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 

        # If ranks are same, then make one as root  
        # and increment its rank by one 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's  
        # algorithm 
    def KruskalMST(self): 

        result =[] #This will store the resultant MST 

        i = 0 # An index variable, used for sorted edges 
        e = 0 # An index variable, used for result[] 

            # Step 1:  Sort all the edges in non-decreasing  
                # order of their 
                # weight.  If we are not allowed to change the  
                # given graph, we can create a copy of graph 
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 

        parent = [] ; rank = [] 

        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
    
        # Number of edges to be taken is equal to V-1 
        while e < self.V -1 : 

            # Step 2: Pick the smallest edge and increment  
            # the index for next iteration 
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 

            # If including this edge does't cause cycle,  
            # include it in result and increment the index 
            # of result for next edge 
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
            # Else discard the edge 
        return result
        # print the contents of result[] to display the built MST 
        # 感謝提供 https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
def main():
    circle_size = 30
    canvas_width = 500
    canvas_height = 500
    circle_num = 0
    someLine = 0
    online = 0
    coordinate = []
    linkData = [ ]
    Guardian = False
    mouse = 0
    MX, MY = 0 , 0
    Data = []
    Total = []

    

    print('[說明]滑鼠左鍵畫線、滑鼠右鍵畫圈、滑鼠中鍵檢查')
    def mousedown( event ):
        nonlocal MX, MY, Guardian, online, mouse
        MX = event.x
        MY = event.y
        i = -1
        
        for space  in coordinate:
            i += 1
            if (space[0] < MX & MX < space[2]) & (space[1] < MY & MY < space[3]):
                mouse = i
                print('[動作]滑鼠點下了圓圈:',i)
       
            
    def mouseup( event ):
        nonlocal MX, MY, Guardian, online, mouse, circle_num
        MX = event.x
        MY = event.y
        i = -1
        for space in coordinate:
            i += 1
            if (space[0] < MX & MX < space[2]) & (space[1] < MY & MY < space[3]):
                print('[動作]滑鼠點下了圓圈:', i,' 並和', mouse, '形成了連線')
                value = askinteger("askinteger", "加入權狀值", minvalue=0, maxvalue=120)
                #value = randint(0, 9)
                x1, y1 = coordinate[i][0], coordinate[i][1]
                x2, y2 = coordinate[mouse][0], coordinate[mouse][1]
                xy, yx = x2 - x1 , y2 - y1
                x ,y = circle_size , circle_size
                if xy > circle_size :
                    y = circle_size * 2
                if yx > circle_size :
                    x = circle_size * 2
                if xy < -circle_size:
                    y = circle_size * 0
                if yx < -circle_size:
                    x = circle_size * 0    
                canvas.create_text( (x1+x2) *0.5 + x,
                 (y1+y2) *0.5 + y,
                    text=value, fill='blue')
                linkData.append( [ mouse, i, value])
                linkData.append( [ i, mouse, value])
                online += 1
            
            
        Guardian = False   
    def deep( event):
        nonlocal linkData,online,circle_num,Data,Total
        print('[執行]開始執行MST')
        
        g = Graph(circle_num) 
        for arr in range(len(linkData)):
            g.addEdge( linkData[arr][0], linkData[arr][1], linkData[arr][2])
            g.addEdge( linkData[arr][1], linkData[arr][0], linkData[arr][2])
        MST = g.KruskalMST()
        for u,v,weight in MST: 
            x1, y1 = ( coordinate[u][0] + circle_size ), ( coordinate[u][1] + circle_size )
            x2, y2 = ( coordinate[v][0] + circle_size ), ( coordinate[v][1] + circle_size )
            canvas.create_line(x1, y1, x2, y2, fill='red') 
            # print ("%d -- %d == %d" % (u,v,weight)) 
        print('[執行]結束')
        # print('------------------------')

        
    def mousemove( event ):
        nonlocal MX, MY
        canvas.create_line( MX, MY, event.x, event.y, fill = 'gray')
        MX = event.x
        MY = event.y

    def circle( event ):
        nonlocal circle_size, circle_num
        x1, y1 = ( event.x - circle_size ), ( event.y - circle_size )
        x2, y2 = ( event.x + circle_size ), ( event.y + circle_size )
        canvas.create_oval(x1, y1, x2, y2)
        canvas.create_text( (x1+x2) * 0.5, (y1+y2) * 0.5,text = circle_num, fill = 'green')
        coordinate.append([x1, y1, x2 , y2])
        circle_num += 1
        # print([x1, y1, x2 , y2])

    
    master.title( "HW2 python" )
    # C:\Windows\System32\@WindowsHelloFaceToastIcon.png
    img = PhotoImage(data= hello) 
    master.tk.call('wm', 'iconphoto', master._w, img)

    canvas = Canvas(master,  width = canvas_width, height = canvas_height)
    canvas.pack(expand = TRUE, fill = BOTH)
    # canvas.create_image(50, 50,image = img)
    canvas.bind("<Button-1>", mousedown)
    canvas.bind("<B1-Motion>", mousemove)
    canvas.bind("<ButtonRelease-1>", mouseup)
    canvas.bind("<Button-2>", deep)
    canvas.bind("<Button-3>", circle )
    
    # message = Label( master, text = "Press and Drag the mouse to draw" )
    # message.pack( side = BOTTOM )
    master.mainloop()

main()