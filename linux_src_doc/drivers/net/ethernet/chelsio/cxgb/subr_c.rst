.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb/subr.c

.. _`t1_wait_op_done`:

t1_wait_op_done
===============

.. c:function:: int t1_wait_op_done(adapter_t *adapter, int reg, u32 mask, int polarity, int attempts, int delay)

    wait until an operation is completed

    :param adapter:
        the adapter performing the operation
    :type adapter: adapter_t \*

    :param reg:
        the register to check for completion
    :type reg: int

    :param mask:
        a single-bit field within \ ``reg``\  that indicates completion
    :type mask: u32

    :param polarity:
        the value of the field when the operation is completed
    :type polarity: int

    :param attempts:
        number of check iterations
    :type attempts: int

    :param delay:
        delay in usecs between iterations
    :type delay: int

.. _`t1_wait_op_done.description`:

Description
-----------

Wait until an operation is completed by checking a bit in a register
up to \ ``attempts``\  times.  Returns \ ``0``\  if the operation completes and \ ``1``\ 
otherwise.

.. This file was automatic generated / don't edit.

