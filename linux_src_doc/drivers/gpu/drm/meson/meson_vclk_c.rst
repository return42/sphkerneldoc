.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/meson/meson_vclk.c

.. _`video-clocks`:

Video Clocks
============

VCLK is the "Pixel Clock" frequency generator from a dedicated PLL.
We handle the following encodings :

- CVBS 27MHz generator via the VCLK2 to the VENCI and VDAC blocks
- HDMI Pixel Clocks generation

What is missing :

- Genenate Pixel clocks for 2K/4K 10bit formats

Clock generator scheme :

.. code::

   __________   _________            _____
  |          | |         |          |     |--ENCI
  | HDMI PLL |-| PLL_DIV |--- VCLK--|     |--ENCL
  |__________| |_________| \        | MUX |--ENCP
                            --VCLK2-|     |--VDAC
                                    |_____|--HDMI-TX

Final clocks can take input for either VCLK or VCLK2, but
VCLK is the preferred path for HDMI clocking and VCLK2 is the
preferred path for CVBS VDAC clocking.

VCLK and VCLK2 have fixed divided clocks paths for /1, /2, /4, /6 or /12.

The PLL_DIV can achieve an additional fractional dividing like
1.5, 3.5, 3.75... to generate special 2K and 4K 10bit clocks.

.. This file was automatic generated / don't edit.

