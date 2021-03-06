.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/cirrusfb.c

.. _`cirrusfb_dbg_print_regs`:

cirrusfb_dbg_print_regs
=======================

.. c:function:: void cirrusfb_dbg_print_regs(struct fb_info *info, caddr_t regbase, enum cirrusfb_dbg_reg_class reg_class,  ...)

    :param info:
        *undescribed*
    :type info: struct fb_info \*

    :param regbase:
        *undescribed*
    :type regbase: caddr_t

    :param reg_class:
        type of registers to read: \ ``CRT``\ , or \ ``SEQ``\ 
    :type reg_class: enum cirrusfb_dbg_reg_class

    :param ellipsis ellipsis:
        variable arguments

.. _`cirrusfb_dbg_print_regs.description`:

Description
-----------

Dumps the given list of VGA CRTC registers.  If \ ``base``\  is \ ``NULL``\ ,
old-style I/O ports are queried for information, otherwise MMIO is
used at the given \ ``base``\  address to query the information.

.. _`cirrusfb_dbg_reg_dump`:

cirrusfb_dbg_reg_dump
=====================

.. c:function:: void cirrusfb_dbg_reg_dump(struct fb_info *info, caddr_t regbase)

    :param info:
        *undescribed*
    :type info: struct fb_info \*

    :param regbase:
        *undescribed*
    :type regbase: caddr_t

.. _`cirrusfb_dbg_reg_dump.description`:

Description
-----------

Dumps a list of interesting VGA and CIRRUSFB registers.  If \ ``base``\  is \ ``NULL``\ ,
old-style I/O ports are queried for information, otherwise MMIO is
used at the given \ ``base``\  address to query the information.

.. This file was automatic generated / don't edit.

