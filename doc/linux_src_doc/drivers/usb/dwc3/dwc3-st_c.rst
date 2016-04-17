.. -*- coding: utf-8; mode: rst -*-

=========
dwc3-st.c
=========


.. _`clkrst_ctrl`:

CLKRST_CTRL
===========

.. c:function:: CLKRST_CTRL ()

    st.c Support for dwc3 platform devices on ST Microelectronics platforms



.. _`clkrst_ctrl.description`:

Description
-----------


This is a small driver for the dwc3 to provide the glue logic
to configure the controller. Tested on STi platforms.

Copyright (C) 2014 Stmicroelectronics



.. _`clkrst_ctrl.author`:

Author
------

Giuseppe Cavallaro <peppe.cavallaro\ ``st``\ .com>



.. _`clkrst_ctrl.contributors`:

Contributors
------------

Aymen Bouattay <aymen.bouattay\ ``st``\ .com>
Peter Griffin <peter.griffin\ ``linaro``\ .org>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

Inspired by dwc3-omap.c and dwc3-exynos.c.



.. _`st_dwc3`:

struct st_dwc3
==============

.. c:type:: st_dwc3

    dwc3-st driver private structure


.. _`st_dwc3.definition`:

Definition
----------

.. code-block:: c

  struct st_dwc3 {
    struct device * dev;
    void __iomem * glue_base;
    struct regmap * regmap;
    int syscfg_reg_off;
    enum usb_dr_mode dr_mode;
    struct reset_control * rstc_pwrdn;
    struct reset_control * rstc_rst;
  };


.. _`st_dwc3.members`:

Members
-------

:``dev``:
    device pointer

:``glue_base``:
    ioaddr for the glue registers

:``regmap``:
    regmap pointer for getting syscfg

:``syscfg_reg_off``:
    usb syscfg control offset

:``dr_mode``:
    drd static host/device config

:``rstc_pwrdn``:
    rest controller for powerdown signal

:``rstc_rst``:
    reset controller for softreset signal




.. _`st_dwc3_drd_init`:

st_dwc3_drd_init
================

.. c:function:: int st_dwc3_drd_init (struct st_dwc3 *dwc3_data)

    :param struct st_dwc3 \*dwc3_data:
        driver private structure



.. _`st_dwc3_drd_init.description`:

Description
-----------

this function is to program the port as either host or device
according to the static configuration passed from devicetree.
OTG and dual role are not yet supported!



.. _`st_dwc3_init`:

st_dwc3_init
============

.. c:function:: void st_dwc3_init (struct st_dwc3 *dwc3_data)

    :param struct st_dwc3 \*dwc3_data:
        driver private structure

