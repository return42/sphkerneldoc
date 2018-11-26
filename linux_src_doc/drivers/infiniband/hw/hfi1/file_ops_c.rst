.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/file_ops.c

.. _`complete_subctxt`:

complete_subctxt
================

.. c:function:: int complete_subctxt(struct hfi1_filedata *fd)

    :param fd:
        valid filedata pointer
    :type fd: struct hfi1_filedata \*

.. _`complete_subctxt.description`:

Description
-----------

Sub-context info can only be set up after the base context
has been completed.  This is indicated by the clearing of the
HFI1_CTXT_BASE_UINIT bit.

Wait for the bit to be cleared, and then complete the subcontext
initialization.

.. _`match_ctxt`:

match_ctxt
==========

.. c:function:: int match_ctxt(struct hfi1_filedata *fd, const struct hfi1_user_info *uinfo, struct hfi1_ctxtdata *uctxt)

    :param fd:
        valid filedata pointer
    :type fd: struct hfi1_filedata \*

    :param uinfo:
        user info to compare base context with
    :type uinfo: const struct hfi1_user_info \*

    :param uctxt:
        context to compare uinfo to.
    :type uctxt: struct hfi1_ctxtdata \*

.. _`match_ctxt.description`:

Description
-----------

Compare the given context with the given information to see if it
can be used for a sub context.

.. _`find_sub_ctxt`:

find_sub_ctxt
=============

.. c:function:: int find_sub_ctxt(struct hfi1_filedata *fd, const struct hfi1_user_info *uinfo)

    :param fd:
        valid filedata pointer
    :type fd: struct hfi1_filedata \*

    :param uinfo:
        matching info to use to find a possible context to share.
    :type uinfo: const struct hfi1_user_info \*

.. _`find_sub_ctxt.description`:

Description
-----------

The hfi1_mutex must be held when this function is called.  It is
necessary to ensure serialized creation of shared contexts.

.. _`find_sub_ctxt.return`:

Return
------

0      No sub-context found
1      Subcontext found and allocated
errno  EINVAL (incorrect parameters)
EBUSY (all sub contexts in use)

.. _`user_exp_rcv_setup`:

user_exp_rcv_setup
==================

.. c:function:: int user_exp_rcv_setup(struct hfi1_filedata *fd, unsigned long arg, u32 len)

    Set up the given tid rcv list

    :param fd:
        file data of the current driver instance
    :type fd: struct hfi1_filedata \*

    :param arg:
        ioctl argumnent for user space information
    :type arg: unsigned long

    :param len:
        length of data structure associated with ioctl command
    :type len: u32

.. _`user_exp_rcv_setup.description`:

Description
-----------

Wrapper to validate ioctl information before doing \_rcv_setup.

.. _`user_exp_rcv_clear`:

user_exp_rcv_clear
==================

.. c:function:: int user_exp_rcv_clear(struct hfi1_filedata *fd, unsigned long arg, u32 len)

    Clear the given tid rcv list

    :param fd:
        file data of the current driver instance
    :type fd: struct hfi1_filedata \*

    :param arg:
        ioctl argumnent for user space information
    :type arg: unsigned long

    :param len:
        length of data structure associated with ioctl command
    :type len: u32

.. _`user_exp_rcv_clear.description`:

Description
-----------

The \ :c:func:`hfi1_user_exp_rcv_clear`\  can be called from the error path.  Because
of this, we need to use this wrapper to copy the user space information
before doing the clear.

.. _`user_exp_rcv_invalid`:

user_exp_rcv_invalid
====================

.. c:function:: int user_exp_rcv_invalid(struct hfi1_filedata *fd, unsigned long arg, u32 len)

    Invalidate the given tid rcv list

    :param fd:
        file data of the current driver instance
    :type fd: struct hfi1_filedata \*

    :param arg:
        ioctl argumnent for user space information
    :type arg: unsigned long

    :param len:
        length of data structure associated with ioctl command
    :type len: u32

.. _`user_exp_rcv_invalid.description`:

Description
-----------

Wrapper to validate ioctl information before doing \_rcv_invalid.

.. _`manage_rcvq`:

manage_rcvq
===========

.. c:function:: int manage_rcvq(struct hfi1_ctxtdata *uctxt, u16 subctxt, unsigned long arg)

    manage a context's receive queue

    :param uctxt:
        the context
    :type uctxt: struct hfi1_ctxtdata \*

    :param subctxt:
        the sub-context
    :type subctxt: u16

    :param arg:
        *undescribed*
    :type arg: unsigned long

.. _`manage_rcvq.description`:

Description
-----------

start_stop == 0 disables receive on the context, for use in queue
overflow conditions.  start_stop==1 re-enables, to be used to
re-init the software copy of the head register

.. _`ctxt_reset`:

ctxt_reset
==========

.. c:function:: int ctxt_reset(struct hfi1_ctxtdata *uctxt)

    Reset the user context

    :param uctxt:
        valid user context
    :type uctxt: struct hfi1_ctxtdata \*

.. This file was automatic generated / don't edit.

