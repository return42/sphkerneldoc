.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ldlm/ldlm_resource.c

.. _`ldlm_namespace_new`:

ldlm_namespace_new
==================

.. c:function:: struct ldlm_namespace *ldlm_namespace_new(struct obd_device *obd, char *name, enum ldlm_side client, enum ldlm_appetite apt, enum ldlm_ns_type ns_type)

    :param struct obd_device \*obd:
        *undescribed*

    :param char \*name:
        *undescribed*

    :param enum ldlm_side client:
        *undescribed*

    :param enum ldlm_appetite apt:
        *undescribed*

    :param enum ldlm_ns_type ns_type:
        *undescribed*

.. _`cleanup_resource`:

cleanup_resource
================

.. c:function:: void cleanup_resource(struct ldlm_resource *res, struct list_head *q, __u64 flags)

    :param struct ldlm_resource \*res:
        *undescribed*

    :param struct list_head \*q:
        *undescribed*

    :param __u64 flags:
        *undescribed*

.. _`cleanup_resource.description`:

Description
-----------

If flags contains FL_LOCAL_ONLY, don't try to tell the server, just
clean up.  This is currently only used for recovery, and we make
certain assumptions as a result--notably, that we shouldn't cancel
locks with refs.

.. _`ldlm_namespace_cleanup`:

ldlm_namespace_cleanup
======================

.. c:function:: int ldlm_namespace_cleanup(struct ldlm_namespace *ns, __u64 flags)

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param __u64 flags:
        *undescribed*

.. _`ldlm_namespace_cleanup.description`:

Description
-----------

Typically used during evictions when server notified client that it was
evicted and all of its state needs to be destroyed.
Also used during shutdown.

.. _`__ldlm_namespace_free`:

__ldlm_namespace_free
=====================

.. c:function:: int __ldlm_namespace_free(struct ldlm_namespace *ns, int force)

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param int force:
        *undescribed*

.. _`__ldlm_namespace_free.description`:

Description
-----------

Only used when namespace goes away, like during an unmount.

.. _`ldlm_namespace_free_prior`:

ldlm_namespace_free_prior
=========================

.. c:function:: void ldlm_namespace_free_prior(struct ldlm_namespace *ns, struct obd_import *imp, int force)

    ready for freeing. Waits for refc == 0.

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param struct obd_import \*imp:
        *undescribed*

    :param int force:
        *undescribed*

.. _`ldlm_namespace_free_prior.the-following-is-done`:

The following is done
---------------------

(0) Unregister \a ns from its list to make inaccessible for potential
users like pools thread and others;
(1) Clear all locks in \a ns.

.. _`ldlm_namespace_free_post`:

ldlm_namespace_free_post
========================

.. c:function:: void ldlm_namespace_free_post(struct ldlm_namespace *ns)

    when \ :c:func:`ldlm_namespce_free_prior`\  successfully removed all resources referencing \a ns and its refc == 0.

    :param struct ldlm_namespace \*ns:
        *undescribed*

.. _`ldlm_resource_get`:

ldlm_resource_get
=================

.. c:function:: struct ldlm_resource *ldlm_resource_get(struct ldlm_namespace *ns, struct ldlm_resource *parent, const struct ldlm_res_id *name, enum ldlm_type type, int create)

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param struct ldlm_resource \*parent:
        *undescribed*

    :param const struct ldlm_res_id \*name:
        *undescribed*

    :param enum ldlm_type type:
        *undescribed*

    :param int create:
        *undescribed*

.. _`ldlm_resource_get.args`:

Args
----

namespace with ns_lock unlocked

.. _`ldlm_resource_get.locks`:

Locks
-----

takes and releases NS hash-lock and res->lr_lock

.. _`ldlm_resource_get.return`:

Return
------

referenced, unlocked ldlm_resource or NULL

.. _`ldlm_resource_add_lock`:

ldlm_resource_add_lock
======================

.. c:function:: void ldlm_resource_add_lock(struct ldlm_resource *res, struct list_head *head, struct ldlm_lock *lock)

    :param struct ldlm_resource \*res:
        *undescribed*

    :param struct list_head \*head:
        *undescribed*

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_dump_all_namespaces`:

ldlm_dump_all_namespaces
========================

.. c:function:: void ldlm_dump_all_namespaces(enum ldlm_side client, int level)

    log.

    :param enum ldlm_side client:
        *undescribed*

    :param int level:
        *undescribed*

.. _`ldlm_namespace_dump`:

ldlm_namespace_dump
===================

.. c:function:: void ldlm_namespace_dump(int level, struct ldlm_namespace *ns)

    log.

    :param int level:
        *undescribed*

    :param struct ldlm_namespace \*ns:
        *undescribed*

.. _`ldlm_resource_dump`:

ldlm_resource_dump
==================

.. c:function:: void ldlm_resource_dump(int level, struct ldlm_resource *res)

    :param int level:
        *undescribed*

    :param struct ldlm_resource \*res:
        *undescribed*

.. This file was automatic generated / don't edit.

