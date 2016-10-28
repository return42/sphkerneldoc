.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/uaccess.h

.. _`probe_kernel_address`:

probe_kernel_address
====================

.. c:function::  probe_kernel_address( addr,  retval)

    safely attempt to read from a location

    :param  addr:
        address to read from

    :param  retval:
        read into this variable

.. _`probe_kernel_address.description`:

Description
-----------

Returns 0 on success, or -EFAULT.

.. This file was automatic generated / don't edit.

