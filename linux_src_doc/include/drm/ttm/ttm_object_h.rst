.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/ttm/ttm_object.h

.. _`ttm_ref_type`:

enum ttm_ref_type
=================

.. c:type:: enum ttm_ref_type


.. _`ttm_ref_type.definition`:

Definition
----------

.. code-block:: c

    enum ttm_ref_type {
        TTM_REF_USAGE,
        TTM_REF_SYNCCPU_READ,
        TTM_REF_SYNCCPU_WRITE,
        TTM_REF_NUM
    };

.. _`ttm_ref_type.constants`:

Constants
---------

TTM_REF_USAGE
    *undescribed*

TTM_REF_SYNCCPU_READ
    *undescribed*

TTM_REF_SYNCCPU_WRITE
    *undescribed*

TTM_REF_NUM
    *undescribed*

.. _`ttm_ref_type.description`:

Description
-----------

Describes what type of reference a ref object holds.

TTM_REF_USAGE is a simple refcount on a base object.

TTM_REF_SYNCCPU_READ is a SYNCCPU_READ reference on a
buffer object.

TTM_REF_SYNCCPU_WRITE is a SYNCCPU_WRITE reference on a
buffer object.

.. _`ttm_object_type`:

enum ttm_object_type
====================

.. c:type:: enum ttm_object_type


.. _`ttm_object_type.definition`:

Definition
----------

.. code-block:: c

    enum ttm_object_type {
        ttm_fence_type,
        ttm_buffer_type,
        ttm_lock_type,
        ttm_prime_type,
        ttm_driver_type0,
        ttm_driver_type1,
        ttm_driver_type2,
        ttm_driver_type3,
        ttm_driver_type4,
        ttm_driver_type5
    };

.. _`ttm_object_type.constants`:

Constants
---------

ttm_fence_type
    *undescribed*

ttm_buffer_type
    *undescribed*

ttm_lock_type
    *undescribed*

ttm_prime_type
    *undescribed*

ttm_driver_type0
    *undescribed*

ttm_driver_type1
    *undescribed*

ttm_driver_type2
    *undescribed*

ttm_driver_type3
    *undescribed*

ttm_driver_type4
    *undescribed*

ttm_driver_type5
    *undescribed*

.. _`ttm_object_type.description`:

Description
-----------

One entry per ttm object type.
Device-specific types should use the
ttm_driver_typex types.

.. _`ttm_base_object`:

struct ttm_base_object
======================

.. c:type:: struct ttm_base_object


.. _`ttm_base_object.definition`:

Definition
----------

.. code-block:: c

    struct ttm_base_object {
        struct rcu_head rhead;
        struct drm_hash_item hash;
        enum ttm_object_type object_type;
        bool shareable;
        struct ttm_object_file *tfile;
        struct kref refcount;
        void (*refcount_release) (struct ttm_base_object **base);
        void (*ref_obj_release) (struct ttm_base_object *base, enum ttm_ref_type ref_type);
    }

.. _`ttm_base_object.members`:

Members
-------

rhead
    *undescribed*

hash
    hash entry for the per-device object hash.

object_type
    *undescribed*

shareable
    Other ttm_object_files can access this object.

tfile
    Pointer to ttm_object_file of the creator.
    NULL if the object was not created by a user request.
    (kernel object).

refcount
    Number of references to this object, not
    including the hash entry. A reference to a base object can
    only be held by a ref object.

refcount_release
    A function to be called when there are
    no more references to this object. This function should
    destroy the object (or make sure destruction eventually happens),
    and when it is called, the object has
    already been taken out of the per-device hash. The parameter
    "base" should be set to NULL by the function.

ref_obj_release
    A function to be called when a reference object
    with another ttm_ref_type than TTM_REF_USAGE is deleted.
    This function may, for example, release a lock held by a user-space
    process.

.. _`ttm_base_object.description`:

Description
-----------

This struct is intended to be used as a base struct for objects that
are visible to user-space. It provides a global name, race-safe
access and refcounting, minimal access contol and hooks for unref actions.

.. _`ttm_prime_object`:

struct ttm_prime_object
=======================

.. c:type:: struct ttm_prime_object

    Modified base object that is prime-aware

.. _`ttm_prime_object.definition`:

Definition
----------

.. code-block:: c

    struct ttm_prime_object {
        struct ttm_base_object base;
        struct mutex mutex;
        size_t size;
        enum ttm_object_type real_type;
        struct dma_buf *dma_buf;
        void (*refcount_release) (struct ttm_base_object **);
    }

.. _`ttm_prime_object.members`:

Members
-------

base
    struct ttm_base_object that we derive from

mutex
    Mutex protecting the \ ``dma_buf``\  member.

size
    Size of the dma_buf associated with this object

real_type
    Type of the underlying object. Needed since we're setting
    the value of \ ``base``\ ::object_type to ttm_prime_type

dma_buf
    Non ref-coutned pointer to a struct dma_buf created from this
    object.

refcount_release
    The underlying object's release method. Needed since
    we set \ ``base``\ ::refcount_release to our own release method.

.. _`ttm_base_object_init`:

ttm_base_object_init
====================

.. c:function:: int ttm_base_object_init(struct ttm_object_file *tfile, struct ttm_base_object *base, bool shareable, enum ttm_object_type type, void (*refcount_release)(struct ttm_base_object **), void (*ref_obj_release)(struct ttm_base_object *, enum ttm_ref_type ref_type))

    :param struct ttm_object_file \*tfile:
        Pointer to a struct ttm_object_file.

    :param struct ttm_base_object \*base:
        The struct ttm_base_object to initialize.

    :param bool shareable:
        This object is shareable with other applcations.
        (different \ ``tfile``\  pointers.)

    :param enum ttm_object_type type:
        The object type.

    :param void (\*refcount_release)(struct ttm_base_object \*\*):
        See the struct ttm_base_object description.

    :param void (\*ref_obj_release)(struct ttm_base_object \*, enum ttm_ref_type ref_type):
        See the struct ttm_base_object description.

.. _`ttm_base_object_init.description`:

Description
-----------

Initializes a struct ttm_base_object.

.. _`ttm_base_object_lookup`:

ttm_base_object_lookup
======================

.. c:function:: struct ttm_base_object *ttm_base_object_lookup(struct ttm_object_file *tfile, uint32_t key)

    :param struct ttm_object_file \*tfile:
        Pointer to a struct ttm_object_file.

    :param uint32_t key:
        Hash key

.. _`ttm_base_object_lookup.description`:

Description
-----------

Looks up a struct ttm_base_object with the key \ ``key``\ .

.. _`ttm_base_object_lookup_for_ref`:

ttm_base_object_lookup_for_ref
==============================

.. c:function:: struct ttm_base_object *ttm_base_object_lookup_for_ref(struct ttm_object_device *tdev, uint32_t key)

    :param struct ttm_object_device \*tdev:
        Pointer to a struct ttm_object_device.

    :param uint32_t key:
        Hash key

.. _`ttm_base_object_lookup_for_ref.description`:

Description
-----------

Looks up a struct ttm_base_object with the key \ ``key``\ .
This function should only be used when the struct tfile associated with the
caller doesn't yet have a reference to the base object.

.. _`ttm_base_object_unref`:

ttm_base_object_unref
=====================

.. c:function:: void ttm_base_object_unref(struct ttm_base_object **p_base)

    :param struct ttm_base_object \*\*p_base:
        Pointer to a pointer referencing a struct ttm_base_object.

.. _`ttm_base_object_unref.description`:

Description
-----------

Decrements the base object refcount and clears the pointer pointed to by
p_base.

.. _`ttm_ref_object_add`:

ttm_ref_object_add
==================

.. c:function:: int ttm_ref_object_add(struct ttm_object_file *tfile, struct ttm_base_object *base, enum ttm_ref_type ref_type, bool *existed, bool require_existed)

    :param struct ttm_object_file \*tfile:
        A struct ttm_object_file representing the application owning the
        ref_object.

    :param struct ttm_base_object \*base:
        The base object to reference.

    :param enum ttm_ref_type ref_type:
        The type of reference.

    :param bool \*existed:
        Upon completion, indicates that an identical reference object
        already existed, and the refcount was upped on that object instead.

    :param bool require_existed:
        Fail with -EPERM if an identical ref object didn't
        already exist.

.. _`ttm_ref_object_add.description`:

Description
-----------

Checks that the base object is shareable and adds a ref object to it.

Adding a ref object to a base object is basically like referencing the
base object, but a user-space application holds the reference. When the
file corresponding to \ ``tfile``\  is closed, all its reference objects are
deleted. A reference object can have different types depending on what
it's intended for. It can be refcounting to prevent object destruction,
When user-space takes a lock, it can add a ref object to that lock to
make sure the lock is released if the application dies. A ref object
will hold a single reference on a base object.

.. _`ttm_ref_object_base_unref`:

ttm_ref_object_base_unref
=========================

.. c:function:: int ttm_ref_object_base_unref(struct ttm_object_file *tfile, unsigned long key, enum ttm_ref_type ref_type)

    :param struct ttm_object_file \*tfile:
        *undescribed*

    :param unsigned long key:
        Key representing the base object.

    :param enum ttm_ref_type ref_type:
        Ref type of the ref object to be dereferenced.

.. _`ttm_ref_object_base_unref.description`:

Description
-----------

Unreference a ref object with type \ ``ref_type``\ 
on the base object identified by \ ``key``\ . If there are no duplicate
references, the ref object will be destroyed and the base object
will be unreferenced.

.. _`ttm_object_file_init`:

ttm_object_file_init
====================

.. c:function:: struct ttm_object_file *ttm_object_file_init(struct ttm_object_device *tdev, unsigned int hash_order)

    initialize a struct ttm_object file

    :param struct ttm_object_device \*tdev:
        A struct ttm_object device this file is initialized on.

    :param unsigned int hash_order:
        Order of the hash table used to hold the reference objects.

.. _`ttm_object_file_init.description`:

Description
-----------

This is typically called by the file_ops::open function.

.. _`ttm_object_file_release`:

ttm_object_file_release
=======================

.. c:function:: void ttm_object_file_release(struct ttm_object_file **p_tfile)

    release data held by a ttm_object_file

    :param struct ttm_object_file \*\*p_tfile:
        Pointer to pointer to the ttm_object_file object to release.
        \*p_tfile will be set to NULL by this function.

.. _`ttm_object_file_release.description`:

Description
-----------

Releases all data associated by a ttm_object_file.
Typically called from file_ops::release. The caller must
ensure that there are no concurrent users of tfile.

.. _`ttm_object_device_init`:

ttm_object_device_init
======================

.. c:function:: struct ttm_object_device *ttm_object_device_init(struct ttm_mem_global *mem_glob, unsigned int hash_order, const struct dma_buf_ops *ops)

    initialize a struct ttm_object_device

    :param struct ttm_mem_global \*mem_glob:
        struct ttm_mem_global for memory accounting.

    :param unsigned int hash_order:
        Order of hash table used to hash the base objects.

    :param const struct dma_buf_ops \*ops:
        DMA buf ops for prime objects of this device.

.. _`ttm_object_device_init.description`:

Description
-----------

This function is typically called on device initialization to prepare
data structures needed for ttm base and ref objects.

.. _`ttm_object_device_release`:

ttm_object_device_release
=========================

.. c:function:: void ttm_object_device_release(struct ttm_object_device **p_tdev)

    release data held by a ttm_object_device

    :param struct ttm_object_device \*\*p_tdev:
        Pointer to pointer to the ttm_object_device object to release.
        \*p_tdev will be set to NULL by this function.

.. _`ttm_object_device_release.description`:

Description
-----------

Releases all data associated by a ttm_object_device.
Typically called from driver::unload before the destruction of the
device private data structure.

.. This file was automatic generated / don't edit.

