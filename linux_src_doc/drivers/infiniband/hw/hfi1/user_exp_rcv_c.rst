.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/user_exp_rcv.c

.. _`program_rcvarray`:

program_rcvarray
================

.. c:function:: int program_rcvarray(struct hfi1_filedata *fd, unsigned long vaddr, struct tid_group *grp, struct tid_pageset *sets, unsigned start, u16 count, struct page **pages, u32 *tidlist, unsigned *tididx, unsigned *pmapped)

    program an RcvArray group with receive buffers

    :param struct hfi1_filedata \*fd:
        filedata pointer

    :param unsigned long vaddr:
        starting user virtual address

    :param struct tid_group \*grp:
        RcvArray group

    :param struct tid_pageset \*sets:
        array of struct tid_pageset holding information on physically
        contiguous chunks from the user buffer

    :param unsigned start:
        starting index into sets array

    :param u16 count:
        number of struct tid_pageset's to program

    :param struct page \*\*pages:
        an array of struct page \* for the user buffer

    :param u32 \*tidlist:
        the array of u32 elements when the information about the
        programmed RcvArray entries is to be encoded.

    :param unsigned \*tididx:
        starting offset into tidlist

    :param unsigned \*pmapped:
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

