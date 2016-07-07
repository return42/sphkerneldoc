.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/media/davinci_vpfe/vpfe_mc_capture.c

.. _`module_parm_desc`:

MODULE_PARM_DESC
================

.. c:function::  MODULE_PARM_DESC( interface, "interface 0-1:0 (default)

    and for capture raw bayer data from camera sensors such as mt9p031. At this point there is problem in co-existence of mt9p031 and tvp5146 due to i2c address collision. So set the variable below from bootargs to do either video capture or camera capture. interface = 0 - video capture (from TVP514x or such), interface = 1 - Camera capture (from mt9p031 or such) Re-visit this when we fix the co-existence issue

    :param  interface:
        *undescribed*

    :param "interface 0-1:0 (default:
        *undescribed*

.. This file was automatic generated / don't edit.

