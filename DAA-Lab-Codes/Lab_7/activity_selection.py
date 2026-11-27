def activity_selection(start,finish):
    n=len(start)
    activites=sorted(zip(start,finish,range(n)),key=lambda x:x[1])
    finish_time=-1
    selected_activities=[]
    for s,f,id,in activites:
        if s>=finish_time:
            finish_time=f
            selected_activities.append(id)
    print("selected activities:",selected_activities)

start=[1,3,5,2,7,6]
finish=[5,6,8,4,9,8]
activity_selection(start,finish)