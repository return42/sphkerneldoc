.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/coresight/coresight-etm3x.c

.. _`coresight_timeout_etm`:

coresight_timeout_etm
=====================

.. c:function:: int coresight_timeout_etm(struct etm_drvdata *drvdata, u32 offset, int position, int value)

    loop until a bit has changed to a specific state.

    :param drvdata:
        etm's private data structure.
    :type drvdata: struct etm_drvdata \*

    :param offset:
        address of a register, starting from \ ``addr``\ .
    :type offset: u32

    :param position:
        the position of the bit of interest.
    :type position: int

    :param value:
        the value the bit should have.
    :type value: int

.. _`coresight_timeout_etm.description`:

Description
-----------

Basically the same as \ ``coresight_timeout``\  except for the register access
method where we have to account for CP14 configurations.

.. _`coresight_timeout_etm.return`:

Return
------

0 as soon as the bit has taken the desired state or -EAGAIN if
TIMEOUT_US has elapsed, which ever happens first.

.. This file was automatic generated / don't edit.

