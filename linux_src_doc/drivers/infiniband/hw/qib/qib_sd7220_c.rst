.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_sd7220.c

.. _`qib_sd7220_reg_mod`:

qib_sd7220_reg_mod
==================

.. c:function:: int qib_sd7220_reg_mod(struct qib_devdata *dd, int sdnum, u32 loc, u32 wd, u32 mask)

    modify SERDES register

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

    :param sdnum:
        which SERDES to access
    :type sdnum: int

    :param loc:
        location - channel, element, register, as packed by \ :c:func:`EPB_LOC`\  macro.
    :type loc: u32

    :param wd:
        Write Data - value to set in register
    :type wd: u32

    :param mask:
        ones where data should be spliced into reg.
    :type mask: u32

.. _`qib_sd7220_reg_mod.description`:

Description
-----------

Basic register read/modify/write, with un-needed acesses elided. That is,
a mask of zero will prevent write, while a mask of 0xFF will prevent read.
returns current (presumed, if a write was done) contents of selected
register, or <0 if errors.

.. This file was automatic generated / don't edit.

