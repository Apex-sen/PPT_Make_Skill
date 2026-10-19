#!/usr/bin/env python3
import argparse,json
from pathlib import Path
import fitz
from PIL import Image,ImageDraw
def main():
 p=argparse.ArgumentParser(description='Render a PDF page or crop a region (PDF points).');p.add_argument('--pdf',required=True);p.add_argument('--page',type=int,required=True);p.add_argument('--rect',nargs=4,type=float);p.add_argument('--padding-pt',type=float,default=12);p.add_argument('--dpi',type=int,default=360);p.add_argument('--output',required=True);p.add_argument('--preview');p.add_argument('--metadata');a=p.parse_args()
 d=fitz.open(a.pdf)
 if not 1<=a.page<=len(d):raise SystemExit(f'page must be 1..{len(d)}')
 pg=d[a.page-1];full=pg.rect;r=fitz.Rect(a.rect) if a.rect else full
 if a.rect:r=fitz.Rect(r.x0-a.padding_pt,r.y0-a.padding_pt,r.x1+a.padding_pt,r.y1+a.padding_pt)&full
 scale=a.dpi/72;pix=pg.get_pixmap(matrix=fitz.Matrix(scale,scale),clip=r,alpha=False);out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);pix.save(out)
 if a.preview and a.rect:
  pp=pg.get_pixmap(matrix=fitz.Matrix(1.2,1.2),alpha=False);im=Image.frombytes('RGB',[pp.width,pp.height],pp.samples);dr=ImageDraw.Draw(im);f=im.width/full.width;rr=fitz.Rect(a.rect);dr.rectangle([rr.x0*f,rr.y0*f,rr.x1*f,rr.y1*f],outline='red',width=4);Path(a.preview).parent.mkdir(parents=True,exist_ok=True);im.save(a.preview)
 meta={'pdf':a.pdf,'page':a.page,'page_rect_pt':list(full),'requested_rect_pt':a.rect,'padding_pt':a.padding_pt if a.rect else 0,'actual_rect_pt':list(r),'dpi':a.dpi,'output':str(out)}
 if a.metadata:Path(a.metadata).write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps(meta,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
