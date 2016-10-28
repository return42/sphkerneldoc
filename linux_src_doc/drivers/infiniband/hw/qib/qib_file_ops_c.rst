.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_file_ops.c

.. _`qib_tid_update`:

qib_tid_update
==============

.. c:function:: int qib_tid_update(struct qib_ctxtdata *rcd, struct file *fp, const struct qib_tid_info *ti)

    update a context TID

    :param struct qib_ctxtdata \*rcd:
        the context

    :param struct file \*fp:
        the qib device file

    :param const struct qib_tid_info \*ti:
        the TID information

.. _`qib_tid_update.description`:

Description
-----------

The new implementation as of Oct 2004 is that the driver assigns
the tid and returns it to the caller.   To reduce search time, we
keep a cursor for each context, walking the shadow tid array to find
one that's not in use.

For now, if we can't allocate the full list, we fail, although
in the long run, we'll allocate as many as we can, and the
caller will deal with that by trying the remaining pages later.
That means that when we fail, we have to mark the tids as not in
use again, in our shadow copy.

It's up to the caller to free the tids when they are done.
We'll unlock the pages as they free them.

Also, right now we are locking one page at a time, but since
the intended use of this routine is for a single group of
virtually contiguous pages, that should change to improve
performance.

.. _`qib_tid_free`:

qib_tid_free
============

.. c:function:: int qib_tid_free(struct qib_ctxtdata *rcd, unsigned subctxt, const struct qib_tid_info *ti)

    free a context TID

    :param struct qib_ctxtdata \*rcd:
        the context

    :param unsigned subctxt:
        the subcontext

    :param const struct qib_tid_info \*ti:
        the TID info

.. _`qib_tid_free.description`:

Description
-----------

right now we are unlocking one page at a time, but since
the intended use of this routine is for a single group of
virtually contiguous pages, that should change to improve
performance.  We check that the TID is in range for this context
but otherwise don't check validity; if user has an error and
frees the wrong tid, it's only their own data that can thereby
be corrupted.  We do check that the TID was in use, for sanity
We always use our idea of the saved address, not the address that
they pass in to us.

.. _`qib_set_part_key`:

qib_set_part_key
================

.. c:function:: int qib_set_part_key(struct qib_ctxtdata *rcd, u16 key)

    set a partition key

    :param struct qib_ctxtdata \*rcd:
        the context

    :param u16 key:
        the key

.. _`qib_set_part_key.description`:

Description
-----------

We can have up to 4 active at a time (other than the default, which is
always allowed).  This is somewhat tricky, since multiple contexts may set
the same key, so we reference count them, and clean up at exit.  All 4
partition keys are packed into a single qlogic_ib register.  It's an
error for a process to set the same pkey multiple times.  We provide no
mechanism to de-allocate a pkey at this time, we may eventually need to
do that.  I've used the atomic operations, and no locking, and only make
a single pass through what's available.  This should be more than
adequate for some time. I'll think about spinlocks or the like if and as
it's necessary.

.. _`qib_manage_rcvq`:

qib_manage_rcvq
===============

.. c:function:: int qib_manage_rcvq(struct qib_ctxtdata *rcd, unsigned subctxt, int start_stop)

    manage a context's receive queue

    :param struct qib_ctxtdata \*rcd:
        the context

    :param unsigned subctxt:
        the subcontext

    :param int start_stop:
        action to carry out

.. _`qib_manage_rcvq.description`:

Description
-----------

start_stop == 0 disables receive on the context, for use in queue
overflow conditions.  start_stop==1 re-enables, to be used to
re-init the software copy of the head register

.. _`qib_mmapf`:

qib_mmapf
=========

.. c:function:: int qib_mmapf(struct file *fp, struct vm_area_struct *vma)

    mmap various structures into user space

    :param struct file \*fp:
        the file pointer

    :param struct vm_area_struct \*vma:
        the VM area

.. _`qib_mmapf.description`:

Description
-----------

We use this to have a shared buffer between the kernel and the user code
for the rcvhdr queue, egr buffers, and the per-context user regs and pio
buffers in the chip.  We have the open and close entries so we can bump
the ref count and keep the driver from being unloaded while still mapped.

.. _`unlock_expected_tids`:

unlock_expected_tids
====================

.. c:function:: void unlock_expected_tids(struct qib_ctxtdata *rcd)

    unlock any expected TID entries context still had in use

    :param struct qib_ctxtdata \*rcd:
        ctxt

.. _`unlock_expected_tids.description`:

Description
-----------

We don't actually update the chip here, because we do a bulk update
below, using f_clear_tids.

.. This file was automatic generated / don't edit.

