.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/file_ops.c

.. _`complete_subctxt`:

complete_subctxt
================

.. c:function:: int complete_subctxt(struct hfi1_filedata *fd)

    :param struct hfi1_filedata \*fd:
        valid filedata pointer

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

    :param struct hfi1_filedata \*fd:
        valid filedata pointer

    :param const struct hfi1_user_info \*uinfo:
        user info to compare base context with

    :param struct hfi1_ctxtdata \*uctxt:
        context to compare uinfo to.

.. _`match_ctxt.description`:

Description
-----------

Compare the given context with the given information to see if it
can be used for a sub context.

.. _`find_sub_ctxt`:

find_sub_ctxt
=============

.. c:function:: int find_sub_ctxt(struct hfi1_filedata *fd, const struct hfi1_user_info *uinfo)

    :param struct hfi1_filedata \*fd:
        valid filedata pointer

    :param const struct hfi1_user_info \*uinfo:
        matching info to use to find a possible context to share.

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

.. _`manage_rcvq`:

manage_rcvq
===========

.. c:function:: int manage_rcvq(struct hfi1_ctxtdata *uctxt, u16 subctxt, int start_stop)

    manage a context's receive queue

    :param struct hfi1_ctxtdata \*uctxt:
        the context

    :param u16 subctxt:
        the sub-context

    :param int start_stop:
        action to carry out

.. _`manage_rcvq.description`:

Description
-----------

start_stop == 0 disables receive on the context, for use in queue
overflow conditions.  start_stop==1 re-enables, to be used to
re-init the software copy of the head register

.. This file was automatic generated / don't edit.

