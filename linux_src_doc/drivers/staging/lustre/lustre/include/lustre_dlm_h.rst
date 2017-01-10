.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/include/lustre_dlm.h

.. _`ldlm_cb_blocking`:

LDLM_CB_BLOCKING
================

.. c:function::  LDLM_CB_BLOCKING()

    indicate which operation should be performed.

.. _`ns_connect_cancelset`:

ns_connect_cancelset
====================

.. c:function:: int ns_connect_cancelset(struct ldlm_namespace *ns)

    :param struct ldlm_namespace \*ns:
        *undescribed*

.. _`ns_connect_lru_resize`:

ns_connect_lru_resize
=====================

.. c:function:: int ns_connect_lru_resize(struct ldlm_namespace *ns)

    :param struct ldlm_namespace \*ns:
        *undescribed*

.. _`ldlm_gid_any`:

LDLM_GID_ANY
============

.. c:function::  LDLM_GID_ANY()

.. _`ldlm_debug_nolock`:

LDLM_DEBUG_NOLOCK
=================

.. c:function::  LDLM_DEBUG_NOLOCK( format,  a...)

    For the cases where we do not have actual lock to print along with a debugging message that is ldlm-related

    :param  format:
        *undescribed*

    :param  a...:
        variable arguments

.. _`ldlm_lock_debug`:

ldlm_lock_debug
===============

.. c:function::  ldlm_lock_debug( msgdata,  mask,  cdls,  lock,  fmt,  a...)

    \see LDLM_DEBUG

    :param  msgdata:
        *undescribed*

    :param  mask:
        *undescribed*

    :param  cdls:
        *undescribed*

    :param  lock:
        *undescribed*

    :param  fmt:
        *undescribed*

    :param  a...:
        variable arguments

.. _`ldlm_debug_limit`:

LDLM_DEBUG_LIMIT
================

.. c:function::  LDLM_DEBUG_LIMIT( mask,  lock,  fmt,  a...)

    limited version of lock printing function.

    :param  mask:
        *undescribed*

    :param  lock:
        *undescribed*

    :param  fmt:
        *undescribed*

    :param  a...:
        variable arguments

.. _`ldlm_iter_continue`:

LDLM_ITER_CONTINUE
==================

.. c:function::  LDLM_ITER_CONTINUE()

    Also used during deciding of lock grants and cancellations.

.. _`ldlm_handle2lock`:

ldlm_handle2lock
================

.. c:function:: struct ldlm_lock *ldlm_handle2lock(const struct lustre_handle *h)

    :param const struct lustre_handle \*h:
        *undescribed*

.. _`ldlm_res_lvbo_update`:

ldlm_res_lvbo_update
====================

.. c:function:: int ldlm_res_lvbo_update(struct ldlm_resource *res, struct ptlrpc_request *r, int increase)

    data from request \a r

    :param struct ldlm_resource \*res:
        *undescribed*

    :param struct ptlrpc_request \*r:
        *undescribed*

    :param int increase:
        *undescribed*

.. _`ldlm_lock_put`:

LDLM_LOCK_PUT
=============

.. c:function::  LDLM_LOCK_PUT( lock)

    __ldlm_handle2lock().

    :param  lock:
        *undescribed*

.. _`ldlm_lock_release`:

LDLM_LOCK_RELEASE
=================

.. c:function::  LDLM_LOCK_RELEASE( lock)

    LDLM_LOCK_PUT()).

    :param  lock:
        *undescribed*

.. This file was automatic generated / don't edit.

