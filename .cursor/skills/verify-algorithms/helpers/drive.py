#!/usr/bin/env python3
"""Compile real judge snippets in isolation; run mapped valid-input contracts."""
from pathlib import Path
import hashlib,json,shutil,subprocess,tempfile
ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/'artifacts/verification';OUT.mkdir(parents=True,exist_ok=True)
CASES={
'Implement Queue using Stacks.cpp':'''MyQueue q;assert(q.empty());q.push(1);q.push(2);assert(q.peek()==1);assert(q.pop()==1);q.push(3);assert(q.pop()==2);assert(q.pop()==3);assert(q.empty());''',
'Evaluate Reverse Polish Notation.cpp':'''Solution s;vector<string>a={"2","1","+","3","*"},b={"4","13","5","/","+"},c={"7","-3","/"};assert(s.evalRPN(a)==9);assert(s.evalRPN(b)==6);assert(s.evalRPN(c)==-2);''',
'Unique Paths.cpp':'''Solution s;assert(s.uniquePaths(3,7)==28);assert(s.uniquePaths(1,1)==1);assert(s.uniquePaths(1,8)==1);''',
'Minimum Path Sum.cpp':'''Solution s;vector<vector<int>>a={{1,3,1},{1,5,1},{4,2,1}},b={{5}},c={{1,2,3}};assert(s.minPathSum(a)==7);assert(s.minPathSum(b)==5);assert(s.minPathSum(c)==6);''',
'Subsets.cpp':'''Solution s;vector<int>a={1,2,3},b={};auto r=s.subsets(a);set<vector<int>>u(r.begin(),r.end());assert(r.size()==8&&u.size()==8);assert(u.count({})&&u.count({1,2,3}));auto e=s.subsets(b);assert(e.size()==1&&e[0].empty());'''
}
PREFIX='''#include <bits/stdc++.h>
using namespace std;
struct TreeNode {int val;TreeNode *left,*right;TreeNode(int x):val(x),left(nullptr),right(nullptr){}};
struct ListNode {int val;ListNode *next;ListNode(int x):val(x),next(nullptr){}};
'''
proof={'scope':'All root C++ snippets compile with explicit judge scaffolding; five mapped valid-input behavioral contracts. Not full correctness or invalid-input support.','compiler':None,'compile':[],'behavior':[],'passed':False}
scratch=Path(tempfile.mkdtemp(prefix='verify-algorithms-'))
def run(cmd):
 p=subprocess.run(cmd,cwd=scratch,capture_output=True,text=True,timeout=30);return {'command':cmd[0:1]+[Path(x).name if str(scratch) in x else x for x in cmd[1:]],'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
try:
 compiler=shutil.which('g++')
 if not compiler:raise RuntimeError('g++ missing')
 proof['compiler']=run([compiler,'--version'])['stdout'].splitlines()[0]
 sources=sorted(ROOT.glob('*.cpp'))
 if not sources:raise RuntimeError('No algorithm sources')
 for i,source in enumerate(sources):
  wrapper=scratch/f'case-{i}.cpp';wrapper.write_text(PREFIX+source.read_text()+'\nint main(){'+CASES.get(source.name,'return 0;')+'}\n')
  binary=scratch/f'case-{i}';result=run([compiler,'-std=c++17','-O1','-Wall','-Wextra',str(wrapper),'-o',str(binary)]);result.update(source=source.name,sha256=hashlib.sha256(source.read_bytes()).hexdigest());proof['compile'].append(result)
  if result['exit']!=0:raise RuntimeError('Compile failed: '+source.name)
  if source.name in CASES:
   result=run([str(binary)]);result['source']=source.name;proof['behavior'].append(result)
   if result['exit']!=0:raise RuntimeError('Behavior failed: '+source.name)
 proof['passed']=True
except Exception as e:proof['failure']=str(e)
finally:
 (OUT/'algorithms.json').write_text(json.dumps(proof,indent=2)+'\n');shutil.rmtree(scratch)
 assert (OUT/'algorithms.json').exists()
 print(json.dumps({'passed':proof['passed'],'compiled':len(proof['compile']),'behavior':len(proof['behavior']),'failure':proof.get('failure')},indent=2))
if not proof['passed']:raise SystemExit(1)
