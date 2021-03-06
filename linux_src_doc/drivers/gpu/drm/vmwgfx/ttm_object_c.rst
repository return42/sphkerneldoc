.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/ttm_object.c

.. _`ttm_object_device`:

struct ttm_object_device
========================

.. c:type:: struct ttm_object_device


.. _`ttm_object_device.definition`:

Definition
----------

.. code-block:: c

    struct ttm_object_device {
        spinlock_t object_lock;
        struct drm_open_hash object_hash;
        atomic_t object_count;
        struct ttm_mem_global *mem_glob;
        struct dma_buf_ops ops;
        void (*dmabuf_release)(struct dma_buf *dma_buf);
        size_t dma_buf_size;
        struct idr idr;
    }

.. _`ttm_object_device.members`:

Members
-------

object_lock
    lock that protects the object_hash hash table.

object_hash
    hash table for fast lookup of object global names.

object_count
    Per device object count.

mem_glob
    *undescribed*

ops
    *undescribed*

dmabuf_release
    *undescribed*

dma_buf_size
    *undescribed*

idr
    *undescribed*

.. _`ttm_object_device.description`:

Description
-----------

This is the per-device data structure needed for ttm object management.

.. _`ttm_ref_object`:

struct ttm_ref_object
=====================

.. c:type:: struct ttm_ref_object


.. _`ttm_ref_object.definition`:

Definition
----------

.. code-block:: c

    struct ttm_ref_object {
        struct rcu_head rcu_head;
        struct drm_hash_item hash;
        struct list_head head;
        struct kref kref;
        enum ttm_ref_type ref_type;
        struct ttm_base_object *obj;
        struct ttm_object_file *tfile;
    }

.. _`ttm_ref_object.members`:

Members
-------

rcu_head
    *undescribed*

hash
    Hash entry for the per-file object reference hash.

head
    List entry for the per-file list of ref-objects.

kref
    Ref count.

ref_type
    Type of ref object.

obj
    Base object this ref object is referencing.

tfile
    *undescribed*

.. _`ttm_ref_object.description`:

Description
-----------

This is similar to an idr object, but it also has a hash table entry
that allows lookup with a pointer to the referenced object as a key. In
that way, one can easily detect whether a base object is referenced by
a particular ttm_object_file. It also carries a ref count to avoid creating
multiple ref objects if a ttm_object_file references the same base
object more than once.

.. _`ttm_base_object_noref_lookup`:

ttm_base_object_noref_lookup
============================

.. c:function:: struct ttm_base_object *ttm_base_object_noref_lookup(struct ttm_object_file *tfile, uint32_t key)

    look up a base object without reference

    :param tfile:
        The struct ttm_object_file the object is registered with.
    :type tfile: struct ttm_object_file \*

    :param key:
        The object handle.
    :type key: uint32_t

.. _`ttm_base_object_noref_lookup.description`:

Description
-----------

This function looks up a ttm base object and returns a pointer to it
without refcounting the pointer. The returned pointer is only valid
until \ :c:func:`ttm_base_object_noref_release`\  is called, and the object
pointed to by the returned pointer may be doomed. Any persistent usage
of the object requires a refcount to be taken using \ :c:func:`kref_get_unless_zero`\ .
Iff this function returns successfully it needs to be paired with
\ :c:func:`ttm_base_object_noref_release`\  and no sleeping- or scheduling functions
may be called inbetween these function callse.

.. _`ttm_base_object_noref_lookup.return`:

Return
------

A pointer to the object if successful or NULL otherwise.

.. _`ttm_ref_object_exists`:

ttm_ref_object_exists
=====================

.. c:function:: bool ttm_ref_object_exists(struct ttm_object_file *tfile, struct ttm_base_object *base)

    Check whether a caller has a valid ref object (has opened) a base object.

    :param tfile:
        Pointer to a struct ttm_object_file identifying the caller.
    :type tfile: struct ttm_object_file \*

    :param base:
        Pointer to a struct base object.
    :type base: struct ttm_base_object \*

.. _`ttm_ref_object_exists.description`:

Description
-----------

Checks wether the caller identified by \ ``tfile``\  has put a valid USAGE
reference object on the base object identified by \ ``base``\ .

.. _`get_dma_buf_unless_doomed`:

get_dma_buf_unless_doomed
=========================

.. c:function:: bool get_dma_buf_unless_doomed(struct dma_buf *dmabuf)

    get a dma_buf reference if possible.

    :param dmabuf:
        *undescribed*
    :type dmabuf: struct dma_buf \*

.. _`get_dma_buf_unless_doomed.description`:

Description
-----------

Obtain a file reference from a lookup structure that doesn't refcount
the file, but synchronizes with its release method to make sure it has
not been freed yet. See for example kref_get_unless_zero documentation.
Returns true if refcounting succeeds, false otherwise.

Nobody really wants this as a public API yet, so let it mature here
for some time...

.. _`ttm_prime_refcount_release`:

ttm_prime_refcount_release
==========================

.. c:function:: void ttm_prime_refcount_release(struct ttm_base_object **p_base)

    refcount release method for a prime object.

    :param p_base:
        Pointer to ttm_base_object pointer.
    :type p_base: struct ttm_base_object \*\*

.. _`ttm_prime_refcount_release.description`:

Description
-----------

This is a wrapper that calls the refcount_release founction of the
underlying object. At the same time it cleans up the prime object.
This function is called when all references to the base object we
derive from are gone.

.. _`ttm_prime_dmabuf_release`:

ttm_prime_dmabuf_release
========================

.. c:function:: void ttm_prime_dmabuf_release(struct dma_buf *dma_buf)

    Release method for the dma-bufs we export

    :param dma_buf:
        *undescribed*
    :type dma_buf: struct dma_buf \*

.. _`ttm_prime_dmabuf_release.description`:

Description
-----------

This function first calls the dma_buf release method the driver
provides. Then it cleans up our dma_buf pointer used for lookup,
and finally releases the reference the dma_buf has on our base
object.

.. _`ttm_prime_fd_to_handle`:

ttm_prime_fd_to_handle
======================

.. c:function:: int ttm_prime_fd_to_handle(struct ttm_object_file *tfile, int fd, u32 *handle)

    Get a base object handle from a prime fd

    :param tfile:
        A struct ttm_object_file identifying the caller.
    :type tfile: struct ttm_object_file \*

    :param fd:
        The prime / dmabuf fd.
    :type fd: int

    :param handle:
        The returned handle.
    :type handle: u32 \*

.. _`ttm_prime_fd_to_handle.description`:

Description
-----------

This function returns a handle to an object that previously exported
a dma-buf. Note that we don't handle imports yet, because we simply
have no consumers of that implementation.

.. _`ttm_prime_handle_to_fd`:

ttm_prime_handle_to_fd
======================

.. c:function:: int ttm_prime_handle_to_fd(struct ttm_object_file *tfile, uint32_t handle, uint32_t flags, int *prime_fd)

    Return a dma_buf fd from a ttm prime object

    :param tfile:
        Struct ttm_object_file identifying the caller.
    :type tfile: struct ttm_object_file \*

    :param handle:
        Handle to the object we're exporting from.
    :type handle: uint32_t

    :param flags:
        flags for dma-buf creation. We just pass them on.
    :type flags: uint32_t

    :param prime_fd:
        The returned file descriptor.
    :type prime_fd: int \*

.. _`ttm_prime_object_init`:

ttm_prime_object_init
=====================

.. c:function:: int ttm_prime_object_init(struct ttm_object_file *tfile, size_t size, struct ttm_prime_object *prime, bool shareable, enum ttm_object_type type, void (*refcount_release)(struct ttm_base_object **), void (*ref_obj_release)(struct ttm_base_object *, enum ttm_ref_type ref_type))

    Initialize a ttm_prime_object

    :param tfile:
        struct ttm_object_file identifying the caller
    :type tfile: struct ttm_object_file \*

    :param size:
        The size of the dma_bufs we export.
    :type size: size_t

    :param prime:
        The object to be initialized.
    :type prime: struct ttm_prime_object \*

    :param shareable:
        See ttm_base_object_init
    :type shareable: bool

    :param type:
        See ttm_base_object_init
    :type type: enum ttm_object_type

    :param void (\*refcount_release)(struct ttm_base_object \*\*):
        See ttm_base_object_init

    :param void (\*ref_obj_release)(struct ttm_base_object \*, enum ttm_ref_type ref_type):
        See ttm_base_object_init

.. _`ttm_prime_object_init.description`:

Description
-----------

Initializes an object which is compatible with the drm_prime model
for data sharing between processes and devices.

.. This file was automatic generated / don't edit.

