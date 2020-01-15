from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Group, Route, Cafe
from .forms import GroupForm, RouteForm
import numpy as np
from .RunDijkstra_t import Run

# Create your views here.

"""
8000にアクセスした時
index.htmlを表示する
"""
def index(request):
    return render(request, 'blog/index.html')


"""
index.htmlの待ち合わせボタンを押した時:
   else文を実行してselect.htmlを表示する

select.htmlでSaveボタンを押した時:
   先頭のif文を実行して
      ・select.htmlのフォームに入力された内容を取得、値の正誤チェックを行う
      ・正誤チェックをクリアしたらデータベース(Group)に値を保存する
      ・map.htmlにリダイレクトする
"""
def select(request):
    errorM = ""
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            if group.destination and group.landmark==-1 and group.exitmark==-1:
                 form = GroupForm()
                 errorM = "入力が正しくありません"
                 return render(request, 'blog/select.html', {'form': form, 'errorM': errorM})
            group.save()
            return redirect('map', pk=group.pk)
        else:
            form = GroupForm()
            return render(request, 'blog/select.html', {'form': form, 'errorM': errorM})

    else:
        form = GroupForm()
        return render(request, 'blog/select.html', {'form': form, 'errorM': errorM})



def FileRead(t):
    #ファイルを読み込む
    file_data = open("/home/nanako/nanako.pythonanywhere.com/" + t, "r")
    #file_data = open(t, "r")
    firstline = True
    #読み込んだファイルを1行ずつ表示
    exit = []
    for line in file_data:
        data = line.split(' ')#空白文字で区切る
        userval = str(data[0])#データベースに入れる値
        dbval = int(data[1])#ユーザーが見る値
        exit.append([dbval, userval])#出口
    #開いたファイルを閉じる
    file_data.close()
    return(exit)


"""
改札場合わけのためのファイル読み込み
startrout.txtを読み込む
"""
def GateFileRead():
    #ファイルを読み込む
    file_data = open("/home/nanako/nanako.pythonanywhere.com/startroute.txt", "r")
    #file_data = open("startroute.txt", "r")
    firstline = True
    #読み込んだファイルを1行ずつ表示
    StationSize = []
    for line in file_data:
        data = line.split(' ')#空白文字で区切る
        station = int(data[0])#駅のノード
        gate = int(data[1])#改札のノード
        dis = int(data[2])#駅から改札までの距離
        StationSize.append([station, gate, dis])#各駅の改札までの距離情報
    #開いたファイルを閉じる
    file_data.close()
    return(StationSize)


"""
最適解を待ち合わせポイントに変換
"""
def point(meet_node):
    #ファイルを読み込む
    file_data = open("/home/nanako/nanako.pythonanywhere.com/point.txt", "r")
    #file_data = open("point.txt", "r")
    firstline = True
    #読み込んだファイルを1行ずつ表示
    MeetToPoint = []
    for line in file_data:
        data = line.split(' ')#空白文字で区切る
        meet = int(data[0])#駅のノード
        point = int(data[1])#改札のノード
        MeetToPoint.append([meet,point])#各駅の改札までの距離情報
    #開いたファイルを閉じる
    file_data.close()
    #pの初期値
    p = []
    #meetの情報をpointに変換
    c = []
    for m in meet_node:
        pp = -1
        for item in MeetToPoint:
            if item[0] == m: #待ち合わせポイントがある時
                pp = item[1]#待ち合わせ場所
        if pp == -1: #待ち合わせポイントがない時
            c.append(m)
        else:
            c.append(pp)
    p.append(c) #ケース別で格納
    #値を返す
    return p


    """
 改札番号を改札名に変更
"""
def name(kaisatu):
    #ファイルを読み込む
    file_data = open("/home/nanako/nanako.pythonanywhere.com/kaisatu.txt", "r")
    #file_data = open("kaisatu.txt", "r")
    firstline = True
    #読み込んだファイルを1行ずつ表示
    KaisatuName = []
    for line in file_data:
        data = line.split(' ')#空白文字で区切る
        node = int(data[0])#改札のノード
        name = data[1]#改札名
        KaisatuName.append([node,name])
    #開いたファイルを閉じる
    file_data.close()

    #kaisatuを名前に変換
    Kname = []
    for node in kaisatu:
        for item in KaisatuName:
            if item[0] == node:
                k = item[1]
                Kname.append([k])
    print(Kname)
    return(Kname)


"""
 重複しているものを消去する
"""
def checker(meet):
    a = []
    for i in meet:
        b = list(set(i))
        a.append(b)
    return a


"""
select.htmlやadd.htmlでSaveボタンを押した時のリダイレクト先。
Groupテーブル、Routeテーブルから必要なオブジェクトを取り出し、
そのオブジェクトをmap.htmlに与えて表示させる
"""
def map(request, pk):
    group = get_object_or_404(Group, pk=pk)
    routes = Route.objects.filter(number=pk)
    length = routes.count()
    dest = False #目的地の有無
    mark = 0 #ランドマークor出口のノード番号
    meet = [-100, -100, -100]
    join = []
    one = []
    kaisatuname = []
    routebox = []
    sort_routbox = []

    #路線が同じ人数を計算
    rn = np.zeros(12)
    for r in routes:
        rn[r.route] = rn[r.route] +1

    print("rn: "+str(rn))
    for index in range(len(rn)):
        if rn[index]!=0:
            routebox.extend([[int(rn[index]),index]])
    print("routebox: "+str(routebox))
    sort_routebox=sorted(routebox, key=lambda x:x[0], reverse=True)
    print("sort_routebox2: "+str(sort_routebox))

    route = []
    Routemarks = FileRead("route.txt")
    for land in Routemarks:
        for n in range(len(sort_routebox)):
            if sort_routebox[n][1] == land[0]:
                route.extend([[land[1],sort_routebox[n][0]]])

    landmark = "なし"
    if group.destination:
        dest = True
        if group.landmark != -1:
            mark = group.landmark
            Landmarks = FileRead("landmark.txt")
            for land in Landmarks:
                if mark == land[0]:
                    landmark = land[1]
        else:
            mark = group.exitmark
            Exitmarks = FileRead("exit.txt")
            for land in Exitmarks:
                if mark == land[0]:
                    landmark = land[1]

    p = []#使用する駅
    for r in routes:
        p.append(r.route)

    route_gate = []
    if length == group.people:
        meet, kaisatu, one = Run(p, mark, dest) #待ち合わせの最適解
        kaisatuname = name(kaisatu)
        for n in range(len(route)):
            route_gate.extend([[route[n],kaisatuname[n]]])
        meet2 = point(meet)
        finalmeet = checker(meet2) #最終的に返す目的地の配列
        print("point利用"+str(finalmeet))
        meet = finalmeet
    return render(request, 'blog/map.html', {'landmark': landmark,'route': route, 'group': group, 'routes': routes, 'meet': meet, 'route_gate': route_gate, 'length': length, 'pathList_near': one,})



"""
mapページ内の追加ボタンを押した時
"""
def add_route(request, pk):
    errorM = "路線を選択してください"
    group = get_object_or_404(Group, pk=pk)
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            route = form.save(commit="False")
            if route.route==-1:
                form = RouteForm()
                return render(request, 'blog/add_route.html', {'form': form, 'errorM': errorM})
            route.number = pk
            route.save()
            return redirect('map', pk=route.number)
        else:
            form = RouteForm()
            return render(request, 'blog/add_route.html', {'form': form, 'errorM': errorM})
    else:
        form = RouteForm()
        return render(request, 'blog/add_route.html', {'form': form, 'errorM': errorM})
