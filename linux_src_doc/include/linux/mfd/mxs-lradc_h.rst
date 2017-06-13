.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/mxs-lradc.h

.. _`mxs_lradc`:

struct mxs_lradc
================

.. c:type:: struct mxs_lradc


.. _`mxs_lradc.definition`:

Definition
----------

.. code-block:: c

    struct mxs_lradc {
        enum mxs_lradc_id soc;
        struct clk *clk;
        u8 buffer_vchans;
        enum mxs_lradc_ts_wires touchscreen_wire;
        bool use_touchbutton;
    }

.. _`mxs_lradc.members`:

Members
-------

soc
    soc type (IMX23 or IMX28)

clk
    2 kHz clock for delay units

buffer_vchans
    channels that can be used during buffered capture

touchscreen_wire
    touchscreen type (4-wire or 5-wire)

use_touchbutton
    button state (on or off)

.. This file was automatic generated / don't edit.

