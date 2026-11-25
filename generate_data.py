import random,csv,sys,json
from pathlib import Path
p=Path(__file__).resolve().parent; random.seed(42)
with (p/'measurements.csv').open('w',newline='') as f:
 w=csv.writer(f); w.writerow(['phase','sample_id','subgroup','diameter_mm','defect'])
 for phase,mu,sd,other in [('Baseline',25.012,.023,.035),('Improved',25.001,.010,.008)]:
  for j in range(500):
   x=round(random.gauss(mu,sd),4); u=random.random(); defect='Oversize' if x>25.05 else 'Undersize' if x<24.95 else 'Surface finish' if u<other*.6 else 'Burr' if u<other else 'None'; w.writerow([phase,j+1,j//5+1,x,defect])
with (p/'production.csv').open('w',newline='') as f:
 w=csv.writer(f); w.writerow(['phase','shift','planned_min','downtime_min','total','good'])
 for phase,down,total,defects in [('Baseline',120,500,45),('Improved',60,660,7)]:
  for j in range(10):
   d=down+random.randint(-8,8); t=total+random.randint(-10,10); bad=defects+random.randint(-3,3); w.writerow([phase,j+1,480,d,t,t-bad])
sys.path.insert(0,str(p)); from analysis import analyse
m=analyse(); (p/'metrics.json').write_text(json.dumps(m)); print(json.dumps({k:{a:b for a,b in v.items() if a not in ('means','ranges')} for k,v in m.items()},indent=2))
