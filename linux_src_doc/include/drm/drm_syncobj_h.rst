.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_syncobj.h

.. _`drm_syncobj`:

struct drm_syncobj
==================

.. c:type:: struct drm_syncobj

    sync object.

.. _`drm_syncobj.definition`:

Definition
----------

.. code-block:: c

    struct drm_syncobj {
        struct kref refcount;
        struct dma_fence __rcu *fence;
        struct list_head cb_list;
        spinlock_t lock;
        struct file *file;
    }

.. _`drm_syncobj.members`:

Members
-------

refcount
    Reference count of this object.

fence
    NULL or a pointer to the fence bound to this object.

    This field should not be used directly. Use \ :c:func:`drm_syncobj_fence_get`\ 
    and \ :c:func:`drm_syncobj_replace_fence`\  instead.

cb_list
    List of callbacks to call when the \ :c:type:`struct fence <fence>`\  gets replaced.

lock
    Protects \ :c:type:`struct cb_list <cb_list>`\  and write-locks \ :c:type:`struct fence <fence>`\ .

file
    A file backing for this syncobj.

.. _`drm_syncobj.description`:

Description
-----------

This structure defines a generic sync object which wraps a \ :c:type:`struct dma_fence <dma_fence>`\ .

.. _`drm_syncobj_cb`:

struct drm_syncobj_cb
=====================

.. c:type:: struct drm_syncobj_cb

    callback for drm_syncobj_add_callback

.. _`drm_syncobj_cb.definition`:

Definition
----------

.. code-block:: c

    struct drm_syncobj_cb {
        struct list_head node;
        drm_syncobj_func_t func;
    }

.. _`drm_syncobj_cb.members`:

Members
-------

node
    used by drm_syncob_add_callback to append this struct to
    \ :c:type:`drm_syncobj.cb_list <drm_syncobj>`\ 

func
    drm_syncobj_func_t to call

.. _`drm_syncobj_cb.description`:

Description
-----------

This struct will be initialized by drm_syncobj_add_callback, additional
data can be passed along by embedding drm_syncobj_cb in another struct.
The callback will get called the next time drm_syncobj_replace_fence is
called.

.. _`drm_syncobj_get`:

drm_syncobj_get
===============

.. c:function:: void drm_syncobj_get(struct drm_syncobj *obj)

    acquire a syncobj reference

    :param struct drm_syncobj \*obj:
        sync object

.. _`drm_syncobj_get.description`:

Description
-----------

This acquires an additional reference to \ ``obj``\ . It is illegal to call this
without already holding a reference. No locks required.

.. _`drm_syncobj_put`:

drm_syncobj_put
===============

.. c:function:: void drm_syncobj_put(struct drm_syncobj *obj)

    release a reference to a sync object.

    :param struct drm_syncobj \*obj:
        sync object.

.. _`drm_syncobj_fence_get`:

drm_syncobj_fence_get
=====================

.. c:function:: struct dma_fence *drm_syncobj_fence_get(struct drm_syncobj *syncobj)

    get a reference to a fence in a sync object

    :param struct drm_syncobj \*syncobj:
        sync object.

.. _`drm_syncobj_fence_get.description`:

Description
-----------

This acquires additional reference to \ :c:type:`drm_syncobj.fence <drm_syncobj>`\  contained in \ ``obj``\ ,
if not NULL. It is illegal to call this without already holding a reference.
No locks required.

.. _`drm_syncobj_fence_get.return`:

Return
------

Either the fence of \ ``obj``\  or NULL if there's none.

.. This file was automatic generated / don't edit.

