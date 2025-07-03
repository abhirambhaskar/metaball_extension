#!/usr/bin/env python3
import inkex
from inkex import etree
from inkex.elements import BaseElement, ShapeElement, Defs
from inkex.elements._filters import Filter  # Only import Filter, not primitives

class MetaballEffect(inkex.EffectExtension):

    def add_arguments(self, parser):
        parser.add_argument("--blur", type=float, default=20.0, help="Gaussian blur radius")
        parser.add_argument("--threshold", type=float, default=0.5, help="Alpha threshold 0–1")

    def effect(self):
        if not self.svg.selection:
            inkex.errormsg("Select at least one object.")
            return

        blur_val = self.options.blur
        thr = self.options.threshold
        offset = thr * 255

        # Get or create <defs>
        defs = self.svg.defs
        if defs is None:
            defs = Defs()
            self.svg.getroot().append(defs)

        #  Use correct unique ID generator
        filter_id = self.svg.get_unique_id("metaball")
        filt = Filter(id=filter_id)
        filt.label = "Metaball Filter"

        # Add Gaussian blur
        filt.add_primitive("feGaussianBlur", stdDeviation=str(blur_val))


        # ------------Add ColorMatrix-------
        # Add color matrix thresholding
        values = (
            "1 0 0 0 0 "
            "0 1 0 0 0 "
            "0 0 1 0 0 "
            f"0 0 0 256 {-offset}"
        )
        filt.add_primitive("feColorMatrix", type="matrix", values=values)



        # ------------Add ComponentTransfer------->>>>>>>>>>>>>>>>>>>>>>
        #SVG_FILTER_NS = "http://www.w3.org/2000/svg"

        #fe_func_a = etree.Element(f"{{{SVG_FILTER_NS}}}feFuncA")
        #fe_func_a.set("type", "table")
        #fe_func_a.set("tableValues", "0 0 0 0 0 0 1 1 1 1 1 1")

        #component_transfer = filt.add_primitive("feComponentTransfer")
        #component_transfer.append(fe_func_a)
        # ---------------------------------------->>>>>>>>>>>>>>>>>>>>>>

        defs.append(filt)

        # Apply filter to selected elements
        for elem in self.svg.selection.filter(ShapeElement):
            elem.style['filter'] = f"url(#{filter_id})"

        #self.msg(f"Metaball filter applied (blur={blur_val}, threshold={thr})")

if __name__ == "__main__":
    MetaballEffect().run()
