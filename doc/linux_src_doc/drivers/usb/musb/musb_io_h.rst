.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/musb/musb_io.h

.. _`musb_io`:

struct musb_io
==============

.. c:type:: struct musb_io

    IO functions for MUSB

.. _`musb_io.definition`:

Definition
----------

.. code-block:: c

    struct musb_io {
        u32 quirks;
        u32 (* ep_offset) (u8 epnum, u16 offset);
        void (* ep_select) (void __iomem *mbase, u8 epnum);
        u32 (* fifo_offset) (u8 epnum);
        void (* read_fifo) (struct musb_hw_ep *hw_ep, u16 len, u8 *buf);
        void (* write_fifo) (struct musb_hw_ep *hw_ep, u16 len, const u8 *buf);
        u32 (* busctl_offset) (u8 epnum, u16 offset);
    }

.. _`musb_io.members`:

Members
-------

quirks
    platform specific flags

ep_offset
    platform specific function to get end point offset

ep_select
    platform specific function to select end point

fifo_offset
    platform specific function to get fifo offset

read_fifo
    platform specific function to read fifo

write_fifo
    platform specific function to write fifo

busctl_offset
    platform specific function to get busctl offset

.. This file was automatic generated / don't edit.

