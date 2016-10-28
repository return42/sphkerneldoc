.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_diag.c

.. _`qib_diagpkt_write`:

qib_diagpkt_write
=================

.. c:function:: ssize_t qib_diagpkt_write(struct file *fp, const char __user *data, size_t count, loff_t *off)

    write an IB packet

    :param struct file \*fp:
        the diag data device file pointer

    :param const char __user \*data:
        qib_diag_pkt structure saying where to get the packet

    :param size_t count:
        size of data to write

    :param loff_t \*off:
        unused by this code

.. This file was automatic generated / don't edit.

