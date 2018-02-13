.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/include/lustre_dlm_flags.h

.. _`ldlm_fl_block_granted`:

LDLM_FL_BLOCK_GRANTED
=====================

.. c:function::  LDLM_FL_BLOCK_GRANTED()

    lock added to the granted list, no questions asked.

.. _`ldlm_fl_block_conv`:

LDLM_FL_BLOCK_CONV
==================

.. c:function::  LDLM_FL_BLOCK_CONV()

    added to the conv list, no questions asked.

.. _`ldlm_fl_block_wait`:

LDLM_FL_BLOCK_WAIT
==================

.. c:function::  LDLM_FL_BLOCK_WAIT()

    added to the wait list, no questions asked.

.. _`ldlm_fl_replay`:

LDLM_FL_REPLAY
==============

.. c:function::  LDLM_FL_REPLAY()

    one of BLOCK_{GRANTED,CONV,WAIT} is set, but that is pretty dangerous.

.. _`ldlm_fl_block_nowait`:

LDLM_FL_BLOCK_NOWAIT
====================

.. c:function::  LDLM_FL_BLOCK_NOWAIT()

    callback.

.. _`ldlm_fl_cancel_on_block`:

LDLM_FL_CANCEL_ON_BLOCK
=======================

.. c:function::  LDLM_FL_CANCEL_ON_BLOCK()

    cancel notification to original lock holder, but expect no reply. This is for clients (like liblustre) that cannot be expected to reliably response to blocking AST.

.. _`ldlm_fl_deny_on_contention`:

LDLM_FL_DENY_ON_CONTENTION
==========================

.. c:function::  LDLM_FL_DENY_ON_CONTENTION()

    EUSERS if locking contention is high

.. _`ldlm_fl_ast_discard_data`:

LDLM_FL_AST_DISCARD_DATA
========================

.. c:function::  LDLM_FL_AST_DISCARD_DATA()

    locks Add FL_DISCARD to blocking ASTs

.. _`ldlm_fl_fail_loc`:

LDLM_FL_FAIL_LOC
================

.. c:function::  LDLM_FL_FAIL_LOC()

    EINTR while cp_ast sleep emulation + race with upcoming bl_ast.

.. _`ldlm_fl_skipped`:

LDLM_FL_SKIPPED
===============

.. c:function::  LDLM_FL_SKIPPED()

    handled this lock and decided to skip it.

.. _`ldlm_fl_lvb_ready`:

LDLM_FL_LVB_READY
=================

.. c:function::  LDLM_FL_LVB_READY()

    This is being added to b_size as a low-risk fix to the fact that the LVB filling happens \_after\_ the lock has been granted, so another thread can match it before the LVB has been updated.  As a dirty hack, we set LDLM_FL_LVB_READY only after we've done the LVB poop. this is only needed on LOV/OSC now, where LVB is actually used and callers must set it in input flags.

.. _`ldlm_fl_lvb_ready.description`:

Description
-----------

The proper fix is to do the granting inside of the completion AST,
which can be replaced with a LVB-aware wrapping function for OSC locks.
That change is pretty high-risk, though, and would need a lot more
testing.

.. _`ldlm_fl_kms_ignore`:

LDLM_FL_KMS_IGNORE
==================

.. c:function::  LDLM_FL_KMS_IGNORE()

    has finished the part of its cancellation that performs write back on its dirty pages.  It can remain on the granted list during this whole time. Threads racing to update the KMS after performing their writeback need to know to exclude each other's locks from the calculation as they walk the granted list.

.. _`ldlm_fl_atomic_cb`:

LDLM_FL_ATOMIC_CB
=================

.. c:function::  LDLM_FL_ATOMIC_CB()

    LDLM can run blocking callback from current context w/o involving separate thread. in order to decrease cs rate

.. _`ldlm_fl_bl_ast`:

LDLM_FL_BL_AST
==============

.. c:function::  LDLM_FL_BL_AST()

    mkdir, such that the server sends a blocking AST for conflicting locks to this client for the first operation, whereas the second operation has canceled this lock and is waiting for rpc_lock which is taken by the first operation. LDLM_FL_BL_AST is set by \ :c:func:`ldlm_callback_handler`\  in the lock to prevent the Early Lock Cancel (ELC) code from cancelling it.

.. _`ldlm_fl_bl_done`:

LDLM_FL_BL_DONE
===============

.. c:function::  LDLM_FL_BL_DONE()

    \ :c:func:`ldlm_callback_handler`\  return EINVAL to the server. It is used when ELC RPC is already prepared and is waiting for rpc_lock, too late to send a separate CANCEL RPC.

.. _`ldlm_fl_no_lru`:

LDLM_FL_NO_LRU
==============

.. c:function::  LDLM_FL_NO_LRU()

    to aging.  Used by MGC locks, they are cancelled only at unmount or by callback.

.. _`ldlm_fl_fail_notified`:

LDLM_FL_FAIL_NOTIFIED
=====================

.. c:function::  LDLM_FL_FAIL_NOTIFIED()

.. _`ldlm_fl_fail_notified.description`:

Description
-----------

Protected by lock and resource locks.

.. _`ldlm_fl_destroyed`:

LDLM_FL_DESTROYED
=================

.. c:function::  LDLM_FL_DESTROYED()

    be destroyed when last reference to them is released. Set by \ :c:func:`ldlm_lock_destroy_internal`\ .

.. _`ldlm_fl_destroyed.description`:

Description
-----------

Protected by lock and resource locks.

.. _`ldlm_fl_res_locked`:

LDLM_FL_RES_LOCKED
==================

.. c:function::  LDLM_FL_RES_LOCKED()

.. _`ldlm_fl_res_locked.description`:

Description
-----------

NB: compared with \ :c:func:`check_res_locked`\ , checking this bit is cheaper.
Also, \ :c:func:`spin_is_locked`\  is deprecated for kernel code; one reason is
because it works only for SMP so user needs to add extra macros like
LASSERT_SPIN_LOCKED for uniprocessor kernels.

.. _`ldlm_fl_waited`:

LDLM_FL_WAITED
==============

.. c:function::  LDLM_FL_WAITED()

    lock-timeout timer and it will never be reset.

.. _`ldlm_fl_waited.description`:

Description
-----------

Protected by lock and resource locks.

.. This file was automatic generated / don't edit.

