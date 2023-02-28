% Gs={[2 1;1 2;3 2;2 3;4 3;3 4;4 1;]
% [0 4;1 0;1 4;0 4;1 0;4 1;]
% [4 3;4 2;4 1;0 4;4 0;]
% };
% Q=[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,;
% 0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,;
% 0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,;
% 0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,;
% 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,;
% 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,;
% 0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,;
% 0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,;
% 0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,;
% 0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,;
% 0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,;
% 0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,;
% 0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,;
% 0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,;
% 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,;
% 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,;
% 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,;
% 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,;
% 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,;
% 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,;
% ]

c=[
0,0.965,0,0,0,0.95,0,0,0,0,0,0,0,0,0,0,0,0,0,0;
0.965,0,0.963,0,0,0,0.966,0.931,0,0,0,0,0,0,0,0,0,0,0,0;
0,0.963,0,0,0,0,0.96,0,0,0,0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0.96,0,0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,0.972,0.966,0,0,0,0,0,0,0,0,0,0;
0.95,0,0,0,0,0,0.977,0,0,0,0.974,0.964,0,0,0,0,0,0,0,0;
0,0.966,0.96,0,0,0.977,0,0.962,0,0,0.982,0.983,0,0,0,0,0,0,0,0;
0,0.931,0,0,0,0,0.962,0,0.963,0,0,0,0.979,0,0,0,0,0,0,0;
0,0,0,0.96,0.972,0,0,0.963,0,0.978,0,0,0.95,0.97,0,0,0,0,0,0;
0,0,0,0,0.966,0,0,0,0.978,0,0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0.974,0.982,0,0,0,0,0.966,0,0,0,0.972,0,0,0,0;
0,0,0,0,0,0.964,0.983,0,0,0,0.966,0,0.952,0,0,0,0.982,0.982,0,0;
0,0,0,0,0,0,0,0.979,0.95,0,0,0.952,0,0.969,0,0,0.971,0,0,0;
0,0,0,0,0,0,0,0,0.97,0,0,0,0.969,0,0.967,0,0,0,0.974,0.973;
0,0,0,0,0,0,0,0,0,0,0,0,0,0.967,0,0,0,0,0.982,0.979;
0,0,0,0,0,0,0,0,0,0,0.972,0,0,0,0,0,0.965,0,0,0;
0,0,0,0,0,0,0,0,0,0,0,0.982,0.971,0,0,0.965,0,0.979,0,0;
0,0,0,0,0,0,0,0,0,0,0,0.982,0,0,0,0,0.979,0,0.977,0;
0,0,0,0,0,0,0,0,0,0,0,0,0,0.974,0.982,0,0,0.977,0,0;
0,0,0,0,0,0,0,0,0,0,0,0,0,0.973,0.979,0,0,0,0,0;
]
m=int32([0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0;
1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0;
0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0;
1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0;
0,1,1,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0;
0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0;
0,0,0,1,1,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0;
0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0;
0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0;
0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,0,1,1,0,0;
0,0,0,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,0;
0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,1;
0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1;
0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0;
0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,0,0;
0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0;
0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0;
0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0;
])
%%


% clear classes
% obj = py.importlib.import_module('shortestPath');
% py.importlib.reload(obj)

format compact;
fid=fopen('./result111.txt', 'w+');
fprintf(fid,'%s\n',"total_time, cost, cache, swap_count");
py.importlib.import_module('qmapsdp')
dirstr = '/home/jianghui/qmap/';
files=py.qmapsdp.filelist(dirstr);
for f =1:length(files)
    if f<6
        continue
    end
    result=py.qmapsdp.func(dirstr,files{f});
    fprintf(fid,'%s \n ',string(files{f}));
    res=result{1};
    Gs=cell(1,length(res));
    for i = 1:length(res)
        a=zeros(length(res{i}),2);
        for j =1:length(res{i})
            a(j,1)=res{i}{j}{1};
            a(j,2)=res{i}{j}{2};
        end
        Gs{i}=a;
    end
%     ini=result{2};
    tsa_ini_path='/home/jianghui/qmap/tsa_ini/';
    ini_path=strcat(tsa_ini_path,string(files{f}));
    ini=py.qmapsdp.fun_inimaping(ini_path);
    Q=zeros(length(ini),length(ini));
    for i =1:length(ini)
        for j =1:length(ini)
            Q(i,j)=ini{i}{j};
        end
    end
    
t0=cputime;
swap_count=0;
cc=0;
totalcost=1; 
memo = struct();
adjointpos = allAdjoinPos(m);
for s=1:length(Gs)
disp(s+"****************************");
t2=cputime;
G=Gs{s}
constraint = [] ;
target = 0;
vars = [];
l = size(G);
record = [];
for i=1:l(1:1)
    g = G(i,:);
    %找到要待运算两个qbit当前映射的位置
    pos = findAllPos(Q,g);
    pos1 = findAllPos1(Q,g);
    lens = size(pos);
    %找到从当前位置移动到所有相邻位置上所有可能的变换矩阵（路径）
    path_constranit1 = 0;
    path_constranit2 = 0;
    QT = zeros(length(Q));
    for p = 1:lens(1,1)
        limit=1;
        for n =1:10
        if isfield(memo,"p"+int64(pos(p,1)-1)+int64(pos(p,2)-1))
            temp = memo.("p"+int64(pos(p,1)-1)+int64(pos(p,2)-1));
            cc=cc+1;
            r = temp{1};
            resQ = temp{2};
            cost = temp{3};
            rlen = temp{4};
            break;
        else
            [r,resQ,cost,rlen] = AllQ(m,[pos(p,1)-1,pos(p,2)-1],c,adjointpos,limit);
             if rlen>0
                temp = cell(1,4);
                temp{1} = r;
                temp{2} = resQ;
                temp{3} = cost;
                temp{4} = rlen;
                memo.("p"+int64(pos(p,1)-1)+int64(pos(p,2)-1)) = temp;
                break;
            else
                limit=limit-0.02;
                continue;
             end
        end
           
        end
        if n==10
        temp = cell(1,4);
        temp{1} = r;
        temp{2} = resQ;
        temp{3} = cost;
        temp{4}=rlen;
        memo.("p"+int64(pos(p,1)-1)+int64(pos(p,2)-1)) = temp;    
        end
        rr=rlen;
        %添加约束,更新Q
        if rr >2
            rr=2;
        end
        x = binvar(rr, 1);
        for j = 1:rr
            record = [record, struct("path",r{j},"cost",cost{j}(1))];
            vars = [vars,x(j)];
            a = Q(pos1(p,1),g(1,1)+1);
            b = Q(pos1(p,2),g(1,2)+1);
            v=min([a,b,x(j)]);
            path_constranit1 = path_constranit1 + v;
            path_constranit2 = path_constranit2 + x(j);
            target = target + (cost{j}(1)) *  v;
            Qj = double(resQ{j}) * Q;
            Qj_m = maskMatrix1(Qj,v);
            Qj_n=elementWiseMin(Qj,Qj_m);
            QT = QT + Qj_n;
        end
    end
    Q = QT;
    constraint = [constraint, path_constranit1 == 1];
    constraint = [constraint, path_constranit2 == 1];
end
target =-target;
disp("solve......the time of model:"+(cputime-t2));
disp("the number of variables:"+length(vars));
ops = sdpsettings('solver','gurobi','showprogress',0);

% ops = sdpsettings('solver', 'Gurobi+', 'verbose', 2, 'debug', 2);
% ops.gurobi.NonConvex = 2;
optimize(constraint,target,ops);
t1=cputime-t2;
vars = double(vars)
target = double(target)
% saveampl(constraint,target,'mymodel');
cost=1; 
for i=1:length(vars)
    if vars(i)==1
      cost=cost*record(i).cost;     
      disp("True: the "+i+"-th path, the cost: "+record(i).cost+" the path: "+record(i).path);
%       fprintf(fid,'%s\n',"the "+i+"-th path, the cost: "+record(i).cost+" the path: "+record(i).path);
      swap_count=swap_count+length(strsplit(record(i).path,'|'))-2;
    end
end
totalcost=totalcost*cost;
disp("the rate of success: "+cost);
disp("runtime:"+t1);
Q=double(Q);
end
fprintf(fid,'%s\n',(cputime-t0)+" "+totalcost+" "+cc+" "+swap_count);

disp("total time:"+(cputime-t0)+" cost:"+totalcost+" cc:"+cc+" swap count:"+swap_count);
end
fclose(fid);
%%
 
%给出当前的映射矩阵和待运算的两个qbit返回待运算的两个qbit可能在的所有位置
%%
function f = findAllPos(Q, g)
    p = [];
    q = [];
    p_c = 0;
    q_c = 0;
    f = [];
  
    for i = 1:length(Q(:,g(1,1)+1))
     
        if strcmpi(class(Q(i,g(1,1)+1)),'sdpvar') 
            p_c = p_c + 1;
            p(p_c) = i;
        elseif double(Q(i,g(1,1)+1)) == 1
            p_c = p_c + 1;
            p(p_c) = i;
        end
    end
    for i = 1:length(Q(:,g(1,2)+1))
        if strcmpi(class(Q(i,g(1,2)+1)),'sdpvar')
            q_c = q_c + 1;
            q(q_c) = i;
        elseif double(Q(i,g(1,2)+1)) == 1 
            q_c = q_c + 1;
            q(q_c) = i;
        end
    end
    c = 0;
    if length(p) ~=0 && length(q) ~=0
       for i = 1:length(p)
           for j = 1:length(q)
               if p(i) ~= q(j)
                   c = c+1;
                   if p(i) > q(j)
                       f(c,1) = q(j);
                       f(c,2) = p(i);
                   else
                       f(c,1) = p(i);
                       f(c,2) = q(j);
                   end
               end
           end
       end
    end
end
function f = findAllPos1(Q, g)
    p = [];
    q = [];
    p_c = 0;
    q_c = 0;
    f = [];
  
    for i = 1:length(Q(:,g(1,1)+1))
     
        if strcmpi(class(Q(i,g(1,1)+1)),'sdpvar') 
            p_c = p_c + 1;
            p(p_c) = i;
        elseif double(Q(i,g(1,1)+1)) == 1
            p_c = p_c + 1;
            p(p_c) = i;
        end
    end
    for i = 1:length(Q(:,g(1,2)+1))
        if strcmpi(class(Q(i,g(1,2)+1)),'sdpvar')
            q_c = q_c + 1;
            q(q_c) = i;
        elseif double(Q(i,g(1,2)+1)) == 1 
            q_c = q_c + 1;
            q(q_c) = i;
        end
    end
    c = 0;
    if length(p) ~=0 && length(q) ~=0
       for i = 1:length(p)
           for j = 1:length(q)
               if p(i) ~= q(j)
                   c = c+1;
                   f(c,1) = p(i);
                   f(c,2) = q(j);
                
               end
           end
       end
    end
end
function f = allAdjoinPos(m)
    f = [];
    c = 0;
    for i = 1:length(m)
        for j = 1:(length(m)-i)
            if m(i,i+j) == 1
                c = c + 1;
                f(c,1) = i;
                f(c,2) = i+j;
            end
        end
    end
end
function [r,Qt,cost] = shortestPath(m,s,t,c)
    P = py.sys.path; 
    M = py.list();
    for i = 1:length(m)
        M.append(py.list(m(i,:)));
    end
    res = py.shortestPath.shortestPath(M,py.list(s),py.list(t));
    r = "| ";
    Qt = eye(length(m));
    cost = 1;
    for i = 1:length(res)
        r = r+ "Q"+ int64(res{i}{1})+"-->"+ "Q"+ int64(res{i}{2}) + " | ";
        
        T = transformMatrix(res{i}{1}+1,res{i}{2}+1,length(m));
        Qt = T * Qt;
        cost = cost * c(res{i}{1}+1,res{i}{2}+1);
    end
end

function f = transformMatrix(a,b,N)
    f = eye(N);
    t = f(a,:);
    f(a,:) = f(b,:);
    f(b,:) = t;
end

%找到从当前位置移动到所有相邻位置上所有可能的变换矩阵（路径）
function [re,res,cost,count] = AllQ(m, s, c,p,limit)
    re = cell(1,length(p));
    res = cell(1,length(p));
    cost = cell(1,length(p));
    count=1;
    t3=cputime;
    for i = 1:length(p)
        [r Qt price] = shortestPath(m,int32(s) ,int32([p(i,1)-1 p(i,2)-1]),c);
        if price<limit
            continue;
        end
        re{count} = r;
        res{count}= int64(Qt);
        cost{count} = price;
        count=count+1;
    end
    t4=cputime-t3;
    count=count-1;
end

function f = swapString(path)
    f = "";
    for i = 1:length(path)
        f = f + "Q"+path(i,1)+"-->"+"Q"+path(i,2)+"|";
    end

end
%给一个矩阵返回ta的掩码矩阵（不为0的位置置为1）
function f = maskMatrix(M)
    f = zeros(length(M));
    for i = 1:length(M)
        for j = 1:length(M(i,:))
            if strcmpi(class(M(i,j)),'sdpvar')
                 f(i,j) = 1;
            elseif double(M(i,j)) == 1
                 f(i,j) = 1;
            end
        end
    end
end
function f = maskMatrix1(M,a)
Qj=ones(length(M));
f=Qj*a;
end
function Q1 = elementWiseMin(Q,Qj)
    l = length(Q);
    Q1 = binvar(l);
    for i = 1:length(Q)
        for j = 1:length(Q(i,:))
                Q1(i,j) = 0;
            if strcmpi(class(Q(i,j)),'sdpvar')
                Q1(i,j) = min([Q(i,j), Qj(i,j)]);
            elseif double(Q(i,j)) == 1
                Q1(i,j) = min([Q(i,j), Qj(i,j)]);
            end
        end
    end
end