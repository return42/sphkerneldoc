.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/user_exp_rcv.c

.. _`unpin_rcv_pages`:

unpin_rcv_pages
===============

.. c:function:: void unpin_rcv_pages(struct hfi1_filedata *fd, struct tid_user_buf *tidbuf, struct tid_rb_node *node, unsigned int idx, unsigned int npages, bool mapped)

    :param struct hfi1_filedata \*fd:
        *undescribed*

    :param struct tid_user_buf \*tidbuf:
        *undescribed*

    :param struct tid_rb_node \*node:
        *undescribed*

    :param unsigned int idx:
        *undescribed*

    :param unsigned int npages:
        *undescribed*

    :param bool mapped:
        *undescribed*

.. _`unpin_rcv_pages.description`:

Description
-----------

@mapped - true if the pages have been DMA mapped. false otherwise.
\ ``idx``\  - Index of the first page to unpin.
\ ``npages``\  - No of pages to unpin.

If the pages have been DMA mapped (indicated by mapped parameter), their
info will be passed via a struct tid_rb_node. If they haven't been mapped,
their info will be passed via a struct tid_user_buf.

.. _`pin_rcv_pages`:

pin_rcv_pages
=============

.. c:function:: int pin_rcv_pages(struct hfi1_filedata *fd, struct tid_user_buf *tidbuf)

    :param struct hfi1_filedata \*fd:
        *undescribed*

    :param struct tid_user_buf \*tidbuf:
        *undescribed*

.. _`program_rcvarray`:

program_rcvarray
================

.. c:function:: int program_rcvarray(struct hfi1_filedata *fd, struct tid_user_buf *tbuf, struct tid_group *grp, unsigned int start, u16 count, u32 *tidlist, unsigned int *tididx, unsigned int *pmapped)

    program an RcvArray group with receive buffers

    :param struct hfi1_filedata \*fd:
        filedata pointer

    :param struct tid_user_buf \*tbuf:
        pointer to struct tid_user_buf that has the user buffer starting
        virtual address, buffer length, page pointers, pagesets (array of
        struct tid_pageset holding information on physically contiguous
        chunks from the user buffer), and other fields.

    :param struct tid_group \*grp:
        RcvArray group

    :param unsigned int start:
        starting index into sets array

    :param u16 count:
        number of struct tid_pageset's to program

    :param u32 \*tidlist:
        the array of u32 elements when the information about the
        programmed RcvArray entries is to be encoded.

    :param unsigned int \*tididx:
        starting offset into tidlist

    :param unsigned int \*pmapped:
        (output parameter) number of pages programmed into the RcvArray
        entries.

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

