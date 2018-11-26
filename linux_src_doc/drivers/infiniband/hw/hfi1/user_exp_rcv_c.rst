.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/user_exp_rcv.c

.. _`unpin_rcv_pages`:

unpin_rcv_pages
===============

.. c:function:: void unpin_rcv_pages(struct hfi1_filedata *fd, struct tid_user_buf *tidbuf, struct tid_rb_node *node, unsigned int idx, unsigned int npages, bool mapped)

    :param fd:
        *undescribed*
    :type fd: struct hfi1_filedata \*

    :param tidbuf:
        *undescribed*
    :type tidbuf: struct tid_user_buf \*

    :param node:
        *undescribed*
    :type node: struct tid_rb_node \*

    :param idx:
        *undescribed*
    :type idx: unsigned int

    :param npages:
        *undescribed*
    :type npages: unsigned int

    :param mapped:
        *undescribed*
    :type mapped: bool

.. _`unpin_rcv_pages.description`:

Description
-----------

\ ``mapped``\  - true if the pages have been DMA mapped. false otherwise.
\ ``idx``\  - Index of the first page to unpin.
\ ``npages``\  - No of pages to unpin.

If the pages have been DMA mapped (indicated by mapped parameter), their
info will be passed via a struct tid_rb_node. If they haven't been mapped,
their info will be passed via a struct tid_user_buf.

.. _`pin_rcv_pages`:

pin_rcv_pages
=============

.. c:function:: int pin_rcv_pages(struct hfi1_filedata *fd, struct tid_user_buf *tidbuf)

    :param fd:
        *undescribed*
    :type fd: struct hfi1_filedata \*

    :param tidbuf:
        *undescribed*
    :type tidbuf: struct tid_user_buf \*

.. _`program_rcvarray`:

program_rcvarray
================

.. c:function:: int program_rcvarray(struct hfi1_filedata *fd, struct tid_user_buf *tbuf, struct tid_group *grp, unsigned int start, u16 count, u32 *tidlist, unsigned int *tididx, unsigned int *pmapped)

    program an RcvArray group with receive buffers

    :param fd:
        filedata pointer
    :type fd: struct hfi1_filedata \*

    :param tbuf:
        pointer to struct tid_user_buf that has the user buffer starting
        virtual address, buffer length, page pointers, pagesets (array of
        struct tid_pageset holding information on physically contiguous
        chunks from the user buffer), and other fields.
    :type tbuf: struct tid_user_buf \*

    :param grp:
        RcvArray group
    :type grp: struct tid_group \*

    :param start:
        starting index into sets array
    :type start: unsigned int

    :param count:
        number of struct tid_pageset's to program
    :type count: u16

    :param tidlist:
        the array of u32 elements when the information about the
        programmed RcvArray entries is to be encoded.
    :type tidlist: u32 \*

    :param tididx:
        starting offset into tidlist
    :type tididx: unsigned int \*

    :param pmapped:
        (output parameter) number of pages programmed into the RcvArray
        entries.
    :type pmapped: unsigned int \*

.. _`program_rcvarray.description`:

Description
-----------

This function will program up to 'count' number of RcvArray entries from the
group 'grp'. To make best use of write-combining writes, the function will
perform writes to the unused RcvArray entries which will be ignored by the
HW. Each RcvArray entry will be programmed with a physically contiguous
buffer chunk from the user's virtual buffer.

.. _`program_rcvarray.return`:

Return
------

-EINVAL if the requested count is larger than the size of the group,
-ENOMEM or -EFAULT on error from \ :c:func:`set_rcvarray_entry`\ , or
number of RcvArray entries programmed.

.. This file was automatic generated / don't edit.

