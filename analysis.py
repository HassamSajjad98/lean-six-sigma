"""Reproduce metrics using Python standard library only."""
import csv, math, statistics as st, json
from collections import Counter
from pathlib import Path
P=Path(__file__).parent
LSL,USL=24.95,25.05

def analyse():
    rows=list(csv.DictReader((P/'measurements.csv').open()))
    ops=list(csv.DictReader((P/'production.csv').open()))
    out={}
    for phase in ('Baseline','Improved'):
        r=[x for x in rows if x['phase']==phase]; v=[float(x['diameter_mm']) for x in r]; n=len(v)
        groups=[v[i:i+5] for i in range(0,n,5)]; ranges=[max(g)-min(g) for g in groups]; means=[st.mean(g) for g in groups]
        rb=st.mean(ranges); mu=st.mean(v); sigma=rb/2.326
        counts=Counter(x['defect'] for x in r if x['defect']!='None')
        o=[x for x in ops if x['phase']==phase]; planned=sum(float(x['planned_min']) for x in o); down=sum(float(x['downtime_min']) for x in o); total=sum(int(x['total']) for x in o); good=sum(int(x['good']) for x in o); ideal=.6
        a=(planned-down)/planned; p=ideal*total/(planned-down); q=good/total
        out[phase]=dict(n=n,mean=mu,sigma=sigma,cp=(USL-LSL)/(6*sigma),cpk=min(USL-mu,mu-LSL)/(3*sigma),ppk=min(USL-mu,mu-LSL)/(3*st.stdev(v)),defects=sum(counts.values()),rate=sum(counts.values())/n,pareto=dict(counts),availability=a,performance=p,quality=q,oee=a*p*q,downtime=down,planned=planned,total=total,good=good,means=means,ranges=ranges,x_lcl=mu-.577*rb,x_ucl=mu+.577*rb,r_ucl=2.114*rb)
    b,i=out.values(); out['economics']={'annual_volume':100000,'cost_per_defect':18,'investment':12000,'annual_savings':(b['rate']-i['rate'])*100000*18,'downtime_reduction':1-i['downtime']/b['downtime']}
    out['economics']['payback_months']=12000/out['economics']['annual_savings']*12
    return out
if __name__=='__main__': print(json.dumps(analyse(),indent=2))
