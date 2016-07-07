.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb/subr.c

.. _`t1_wait_op_done`:

t1_wait_op_done
===============

.. c:function:: int t1_wait_op_done(adapter_t *adapter, int reg, u32 mask, int polarity, int attempts, int delay)

    wait until an operation is completed

    :param adapter_t \*adapter:
        the adapter performing the operation

    :param int reg:
        the register to check for completion

    :param u32 mask:
        a single-bit field within \ ``reg``\  that indicates completion

    :param int polarity:
        the value of the field when the operation is completed

    :param int attempts:
        number of check iterations

    :param int delay:
        delay in usecs between iterations

.. _`t1_wait_op_done.description`:

Description
-----------

Wait until an operation is completed by checking a bit in a register
up to \ ``attempts``\  times.  Returns \ ``0``\  if the operation completes and \ ``1``\ 
otherwise.

.. This file was automatic generated / don't edit.

