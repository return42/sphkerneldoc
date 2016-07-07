.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_sd7220.c

.. _`qib_sd7220_reg_mod`:

qib_sd7220_reg_mod
==================

.. c:function:: int qib_sd7220_reg_mod(struct qib_devdata *dd, int sdnum, u32 loc, u32 wd, u32 mask)

    modify SERDES register

    :param struct qib_devdata \*dd:
        the qlogic_ib device

    :param int sdnum:
        which SERDES to access

    :param u32 loc:
        location - channel, element, register, as packed by \ :c:func:`EPB_LOC`\  macro.

    :param u32 wd:
        Write Data - value to set in register

    :param u32 mask:
        ones where data should be spliced into reg.

.. _`qib_sd7220_reg_mod.description`:

Description
-----------

Basic register read/modify/write, with un-needed acesses elided. That is,
a mask of zero will prevent write, while a mask of 0xFF will prevent read.
returns current (presumed, if a write was done) contents of selected
register, or <0 if errors.

.. This file was automatic generated / don't edit.

