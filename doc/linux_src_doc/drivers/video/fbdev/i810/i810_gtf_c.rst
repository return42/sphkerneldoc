.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/i810/i810_gtf.c

.. _`i810fb_encode_registers`:

i810fb_encode_registers
=======================

.. c:function:: void i810fb_encode_registers(const struct fb_var_screeninfo *var, struct i810fb_par *par, u32 xres, u32 yres)

    encode \ ``var``\  to hardware register values

    :param const struct fb_var_screeninfo \*var:
        pointer to var structure

    :param struct i810fb_par \*par:
        pointer to hardware par structure

    :param u32 xres:
        *undescribed*

    :param u32 yres:
        *undescribed*

.. _`i810fb_encode_registers.description`:

Description
-----------

Timing values in \ ``var``\  will be converted to appropriate
register values of \ ``par``\ .

.. _`i810_get_watermark`:

i810_get_watermark
==================

.. c:function:: u32 i810_get_watermark(const struct fb_var_screeninfo *var, struct i810fb_par *par)

    gets watermark

    :param const struct fb_var_screeninfo \*var:
        pointer to fb_var_screeninfo

    :param struct i810fb_par \*par:
        pointer to i810fb_par structure

.. _`i810_get_watermark.description`:

Description
-----------

Gets the required watermark based on
pixelclock and RAMBUS frequency.

.. _`i810_get_watermark.return`:

Return
------

watermark

.. This file was automatic generated / don't edit.

