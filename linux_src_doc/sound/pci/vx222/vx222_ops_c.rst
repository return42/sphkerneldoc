.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/pci/vx222/vx222_ops.c

.. _`vx2_inb`:

vx2_inb
=======

.. c:function:: unsigned char vx2_inb(struct vx_core *chip, int offset)

    read a byte from the register

    :param chip:
        VX core instance
    :type chip: struct vx_core \*

    :param offset:
        register enum
    :type offset: int

.. _`vx2_outb`:

vx2_outb
========

.. c:function:: void vx2_outb(struct vx_core *chip, int offset, unsigned char val)

    write a byte on the register

    :param chip:
        VX core instance
    :type chip: struct vx_core \*

    :param offset:
        the register offset
    :type offset: int

    :param val:
        the value to write
    :type val: unsigned char

.. _`vx2_inl`:

vx2_inl
=======

.. c:function:: unsigned int vx2_inl(struct vx_core *chip, int offset)

    read a 32bit word from the register

    :param chip:
        VX core instance
    :type chip: struct vx_core \*

    :param offset:
        register enum
    :type offset: int

.. _`vx2_outl`:

vx2_outl
========

.. c:function:: void vx2_outl(struct vx_core *chip, int offset, unsigned int val)

    write a 32bit word on the register

    :param chip:
        VX core instance
    :type chip: struct vx_core \*

    :param offset:
        the register enum
    :type offset: int

    :param val:
        the value to write
    :type val: unsigned int

.. _`vx2_setup_pseudo_dma`:

vx2_setup_pseudo_dma
====================

.. c:function:: void vx2_setup_pseudo_dma(struct vx_core *chip, int do_write)

    set up the pseudo dma read/write mode.

    :param chip:
        VX core instance
    :type chip: struct vx_core \*

    :param do_write:
        0 = read, 1 = set up for DMA write
    :type do_write: int

.. This file was automatic generated / don't edit.

