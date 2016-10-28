.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ldlm/ldlm_lockd.c

.. _`ldlm_handle_bl_callback`:

ldlm_handle_bl_callback
=======================

.. c:function:: void ldlm_handle_bl_callback(struct ldlm_namespace *ns, struct ldlm_lock_desc *ld, struct ldlm_lock *lock)

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param struct ldlm_lock_desc \*ld:
        *undescribed*

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_handle_bl_callback.description`:

Description
-----------

This can only happen on client side.

.. _`ldlm_handle_cp_callback`:

ldlm_handle_cp_callback
=======================

.. c:function:: void ldlm_handle_cp_callback(struct ptlrpc_request *req, struct ldlm_namespace *ns, struct ldlm_request *dlm_req, struct ldlm_lock *lock)

    :param struct ptlrpc_request \*req:
        *undescribed*

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param struct ldlm_request \*dlm_req:
        *undescribed*

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_handle_cp_callback.description`:

Description
-----------

This only can happen on client side.

.. _`ldlm_handle_gl_callback`:

ldlm_handle_gl_callback
=======================

.. c:function:: void ldlm_handle_gl_callback(struct ptlrpc_request *req, struct ldlm_namespace *ns, struct ldlm_request *dlm_req, struct ldlm_lock *lock)

    :param struct ptlrpc_request \*req:
        *undescribed*

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param struct ldlm_request \*dlm_req:
        *undescribed*

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_handle_gl_callback.description`:

Description
-----------

This only can happen on client side.  After handling the glimpse AST
we also consider dropping the lock here if it is unused locally for a
long time.

.. _`ldlm_bl_to_thread`:

ldlm_bl_to_thread
=================

.. c:function:: int ldlm_bl_to_thread(struct ldlm_namespace *ns, struct ldlm_lock_desc *ld, struct ldlm_lock *lock, struct list_head *cancels, int count, enum ldlm_cancel_flags cancel_flags)

    for later processing by a blocking thread.  If \a count is zero, then the lock referenced as \a lock is queued instead.

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param struct ldlm_lock_desc \*ld:
        *undescribed*

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param struct list_head \*cancels:
        *undescribed*

    :param int count:
        *undescribed*

    :param enum ldlm_cancel_flags cancel_flags:
        *undescribed*

.. _`ldlm_bl_to_thread.description`:

Description
-----------

The blocking thread would then call ->l_blocking_ast callback in the lock.
If list addition fails an error is returned and caller is supposed to
call ->l_blocking_ast itself.

.. _`ldlm_bl_thread_main`:

ldlm_bl_thread_main
===================

.. c:function:: int ldlm_bl_thread_main(void *arg)

    :param void \*arg:
        *undescribed*

.. _`ldlm_bl_thread_main.description`:

Description
-----------

Callers put locks into its queue by calling ldlm_bl_to_thread.
This thread in the end ends up doing actual call to ->l_blocking_ast
for queued locks.

.. This file was automatic generated / don't edit.

