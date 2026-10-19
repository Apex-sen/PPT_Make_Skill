#!/usr/bin/env python3
"""Scan text for multiple variants of terms listed in a JSON map."""
import argparse,json,re
from pathlib import Path
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--text',required=True);p.add_argument('--map',required=True,help='JSON: canonical term -> list of variants');a=p.parse_args();txt=Path(a.text).read_text(encoding='utf-8',errors='replace');mp=json.loads(Path(a.map).read_text(encoding='utf-8'));issues=[]
 for canonical,variants in mp.items():
  found=[v for v in variants if v and re.search(re.escape(v),txt,re.I)]
  if len(found)>1:issues.append({'canonical':canonical,'found_variants':found})
 print(json.dumps({'count':len(issues),'issues':issues},ensure_ascii=False,indent=2))
 if issues:raise SystemExit(1)
if __name__=='__main__':main()
