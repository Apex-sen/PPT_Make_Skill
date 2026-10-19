#!/usr/bin/env python3
"""Render a math expression with Matplotlib MathText as a transparent PNG."""
import argparse
from pathlib import Path
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--tex',required=True,help='MathText-compatible expression without surrounding $');p.add_argument('--output',required=True);p.add_argument('--fontsize',type=float,default=24);p.add_argument('--color',default='#202020');p.add_argument('--dpi',type=int,default=300);a=p.parse_args()
 fig=plt.figure();fig.patch.set_alpha(0);t=fig.text(0,0,'$'+a.tex+'$',fontsize=a.fontsize,color=a.color);fig.canvas.draw();bbox=t.get_window_extent(renderer=fig.canvas.get_renderer()).expanded(1.08,1.2);bbox=bbox.transformed(fig.dpi_scale_trans.inverted());out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,dpi=a.dpi,transparent=True,bbox_inches=bbox,pad_inches=.03);plt.close(fig);print(out)
if __name__=='__main__':main()
