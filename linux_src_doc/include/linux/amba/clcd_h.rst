.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/amba/clcd.h

.. _`clcd_vendor_data`:

struct clcd_vendor_data
=======================

.. c:type:: struct clcd_vendor_data

    holds hardware (IP-block) vendor-specific variant information

.. _`clcd_vendor_data.definition`:

Definition
----------

.. code-block:: c

    struct clcd_vendor_data {
        bool clock_timregs;
        bool packed_24_bit_pixels;
        bool st_bitmux_control;
        int (*init_board)(struct amba_device *adev,struct clcd_board *board);
        int (*init_panel)(struct clcd_fb *fb,struct device_node *panel);
    }

.. _`clcd_vendor_data.members`:

Members
-------

clock_timregs
    the CLCD needs to be clocked when accessing the
    timer registers, or the hardware will hang.

packed_24_bit_pixels
    this variant supports 24bit packed pixel data,
    so that RGB accesses 3 bytes at a time, not just on even 32bit
    boundaries, packing the pixel data in memory. ST Microelectronics
    have this.

st_bitmux_control
    ST Microelectronics have implemented output
    bit line multiplexing into the CLCD control register. This indicates
    that we need to use this.

init_board
    custom board init function for this variant

init_panel
    custom panel init function for this variant

.. This file was automatic generated / don't edit.

