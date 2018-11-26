.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_diag.c

.. _`qib_diagpkt_write`:

qib_diagpkt_write
=================

.. c:function:: ssize_t qib_diagpkt_write(struct file *fp, const char __user *data, size_t count, loff_t *off)

    write an IB packet

    :param fp:
        the diag data device file pointer
    :type fp: struct file \*

    :param data:
        qib_diag_pkt structure saying where to get the packet
    :type data: const char __user \*

    :param count:
        size of data to write
    :type count: size_t

    :param off:
        unused by this code
    :type off: loff_t \*

.. This file was automatic generated / don't edit.

