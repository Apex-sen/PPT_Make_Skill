#!/usr/bin/env python3
"""Export PPTX to PDF with LibreOffice and optionally render each page as PNG."""
import argparse,subprocess,shutil
from pathlib import Path
import fitz
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--pptx',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--png',action='store_true');p.add_argument('--dpi',type=int,default=150);a=p.parse_args();lo=shutil.which('libreoffice') or shutil.which('soffice')
 if not lo:raise SystemExit('LibreOffice not found; export PDF manually from PowerPoint.')
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True);subprocess.run([lo,'--headless','--convert-to','pdf','--outdir',str(out),str(Path(a.pptx).resolve())],check=True);pdf=out/(Path(a.pptx).stem+'.pdf');print('PDF:',pdf)
 if a.png:
  doc=fitz.open(pdf);sc=a.dpi/72
  for i,pg in enumerate(doc,1):pg.get_pixmap(matrix=fitz.Matrix(sc,sc),alpha=False).save(out/f'slide-{i:02d}.png')
  print(f'Rendered {len(doc)} pages')
if __name__=='__main__':main()
