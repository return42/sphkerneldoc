.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/iocontext.h

.. _`get_io_context_active`:

get_io_context_active
=====================

.. c:function:: void get_io_context_active(struct io_context *ioc)

    get active reference on ioc

    :param ioc:
        ioc of interest
    :type ioc: struct io_context \*

.. _`get_io_context_active.description`:

Description
-----------

Only iocs with active reference can issue new IOs.  This function
acquires an active reference on \ ``ioc``\ .  The caller must already have an
active reference on \ ``ioc``\ .

.. This file was automatic generated / don't edit.

