.. -*- coding: utf-8; mode: rst -*-

===========
auo_k190x.c
===========


.. _`rgb565_to_gray4`:

rgb565_to_gray4
===============

.. c:function:: int rgb565_to_gray4 (u16 data, struct fb_var_screeninfo *var)

    :param u16 data:

        *undescribed*

    :param struct fb_var_screeninfo \*var:

        *undescribed*



.. _`rgb565_to_gray4.description`:

Description
-----------

does roughly (0.3 * R + 0.6 G + 0.1 B) / 2

