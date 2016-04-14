.. -*- coding: utf-8; mode: rst -*-

=========
drm_gem.c
=========

.. _`drm_gem_init`:

drm_gem_init
============

.. c:function:: int drm_gem_init (struct drm_device *dev)

    Initialize the GEM device fields

    :param struct drm_device \*dev:
        drm_devic structure to initialize


.. _`drm_gem_object_init`:

drm_gem_object_init
===================

.. c:function:: int drm_gem_object_init (struct drm_device *dev, struct drm_gem_object *obj, size_t size)

    initialize an allocated shmem-backed GEM object

    :param struct drm_device \*dev:
        drm_device the object should be initialized for

    :param struct drm_gem_object \*obj:
        drm_gem_object to initialize

    :param size_t size:
        object size


.. _`drm_gem_object_init.description`:

Description
-----------

Initialize an already allocated GEM object of the specified size with
shmfs backing store.


.. _`drm_gem_private_object_init`:

drm_gem_private_object_init
===========================

.. c:function:: void drm_gem_private_object_init (struct drm_device *dev, struct drm_gem_object *obj, size_t size)

    initialize an allocated private GEM object

    :param struct drm_device \*dev:
        drm_device the object should be initialized for

    :param struct drm_gem_object \*obj:
        drm_gem_object to initialize

    :param size_t size:
        object size


.. _`drm_gem_private_object_init.description`:

Description
-----------

Initialize an already allocated GEM object of the specified size with
no GEM provided backing store. Instead the caller is responsible for
backing the object and handling it.


.. _`drm_gem_object_handle_free`:

drm_gem_object_handle_free
==========================

.. c:function:: void drm_gem_object_handle_free (struct drm_gem_object *obj)

    release resources bound to userspace handles

    :param struct drm_gem_object \*obj:
        GEM object to clean up.


.. _`drm_gem_object_handle_free.description`:

Description
-----------

Called after the last handle to the object has been closed

Removes any name for the object. Note that this must be
called before drm_gem_object_free or we'll be touching
freed memory


.. _`drm_gem_handle_delete`:

drm_gem_handle_delete
=====================

.. c:function:: int drm_gem_handle_delete (struct drm_file *filp, u32 handle)

    deletes the given file-private handle

    :param struct drm_file \*filp:
        drm file-private structure to use for the handle look up

    :param u32 handle:
        userspace handle to delete


.. _`drm_gem_handle_delete.description`:

Description
-----------

Removes the GEM handle from the ``filp`` lookup table which has been added with
:c:func:`drm_gem_handle_create`. If this is the last handle also cleans up linked
resources like GEM names.


.. _`drm_gem_dumb_destroy`:

drm_gem_dumb_destroy
====================

.. c:function:: int drm_gem_dumb_destroy (struct drm_file *file, struct drm_device *dev, uint32_t handle)

    dumb fb callback helper for gem based drivers

    :param struct drm_file \*file:
        drm file-private structure to remove the dumb handle from

    :param struct drm_device \*dev:
        corresponding drm_device

    :param uint32_t handle:
        the dumb handle to remove


.. _`drm_gem_dumb_destroy.description`:

Description
-----------

This implements the ->dumb_destroy kms driver callback for drivers which use
gem to manage their backing storage.


.. _`drm_gem_handle_create_tail`:

drm_gem_handle_create_tail
==========================

.. c:function:: int drm_gem_handle_create_tail (struct drm_file *file_priv, struct drm_gem_object *obj, u32 *handlep)

    internal functions to create a handle

    :param struct drm_file \*file_priv:
        drm file-private structure to register the handle for

    :param struct drm_gem_object \*obj:
        object to register

    :param u32 \*handlep:
        pointer to return the created handle to the caller


.. _`drm_gem_handle_create_tail.description`:

Description
-----------

This expects the dev->object_name_lock to be held already and will drop it
before returning. Used to avoid races in establishing new handles when
importing an object from either an flink name or a dma-buf.

Handles must be release again through :c:func:`drm_gem_handle_delete`. This is done
when userspace closes ``file_priv`` for all attached handles, or through the
GEM_CLOSE ioctl for individual handles.


.. _`drm_gem_handle_create`:

drm_gem_handle_create
=====================

.. c:function:: int drm_gem_handle_create (struct drm_file *file_priv, struct drm_gem_object *obj, u32 *handlep)

    create a gem handle for an object

    :param struct drm_file \*file_priv:
        drm file-private structure to register the handle for

    :param struct drm_gem_object \*obj:
        object to register

    :param u32 \*handlep:
        pionter to return the created handle to the caller


.. _`drm_gem_handle_create.description`:

Description
-----------

Create a handle for this object. This adds a handle reference
to the object, which includes a regular reference count. Callers
will likely want to dereference the object afterwards.


.. _`drm_gem_free_mmap_offset`:

drm_gem_free_mmap_offset
========================

.. c:function:: void drm_gem_free_mmap_offset (struct drm_gem_object *obj)

    release a fake mmap offset for an object

    :param struct drm_gem_object \*obj:
        obj in question


.. _`drm_gem_free_mmap_offset.description`:

Description
-----------

This routine frees fake offsets allocated by :c:func:`drm_gem_create_mmap_offset`.


.. _`drm_gem_create_mmap_offset_size`:

drm_gem_create_mmap_offset_size
===============================

.. c:function:: int drm_gem_create_mmap_offset_size (struct drm_gem_object *obj, size_t size)

    create a fake mmap offset for an object

    :param struct drm_gem_object \*obj:
        obj in question

    :param size_t size:
        the virtual size


.. _`drm_gem_create_mmap_offset_size.description`:

Description
-----------

GEM memory mapping works by handing back to userspace a fake mmap offset
it can use in a subsequent mmap(2) call.  The DRM core code then looks
up the object based on the offset and sets up the various memory mapping
structures.

This routine allocates and attaches a fake offset for ``obj``\ , in cases where
the virtual size differs from the physical size (ie. obj->size).  Otherwise
just use :c:func:`drm_gem_create_mmap_offset`.


.. _`drm_gem_create_mmap_offset`:

drm_gem_create_mmap_offset
==========================

.. c:function:: int drm_gem_create_mmap_offset (struct drm_gem_object *obj)

    create a fake mmap offset for an object

    :param struct drm_gem_object \*obj:
        obj in question


.. _`drm_gem_create_mmap_offset.description`:

Description
-----------

GEM memory mapping works by handing back to userspace a fake mmap offset
it can use in a subsequent mmap(2) call.  The DRM core code then looks
up the object based on the offset and sets up the various memory mapping
structures.

This routine allocates and attaches a fake offset for ``obj``\ .


.. _`drm_gem_get_pages`:

drm_gem_get_pages
=================

.. c:function:: struct page **drm_gem_get_pages (struct drm_gem_object *obj)

    helper to allocate backing pages for a GEM object from shmem

    :param struct drm_gem_object \*obj:
        obj in question


.. _`drm_gem_get_pages.description`:

Description
-----------

This reads the page-array of the shmem-backing storage of the given gem
object. An array of pages is returned. If a page is not allocated or
swapped-out, this will allocate/swap-in the required pages. Note that the
whole object is covered by the page-array and pinned in memory.

Use :c:func:`drm_gem_put_pages` to release the array and unpin all pages.

This uses the GFP-mask set on the shmem-mapping (see :c:func:`mapping_set_gfp_mask`).
If you require other GFP-masks, you have to do those allocations yourself.

Note that you are not allowed to change gfp-zones during runtime. That is,
:c:func:`shmem_read_mapping_page_gfp` must be called with the same gfp_zone(gfp) as
set during initialization. If you have special zone constraints, set them
after :c:func:`drm_gem_init_object` via :c:func:`mapping_set_gfp_mask`. shmem-core takes care
to keep pages in the required zone during swap-in.


.. _`drm_gem_put_pages`:

drm_gem_put_pages
=================

.. c:function:: void drm_gem_put_pages (struct drm_gem_object *obj, struct page **pages, bool dirty, bool accessed)

    helper to free backing pages for a GEM object

    :param struct drm_gem_object \*obj:
        obj in question

    :param struct page \*\*pages:
        pages to free

    :param bool dirty:
        if true, pages will be marked as dirty

    :param bool accessed:
        if true, the pages will be marked as accessed


.. _`drm_gem_object_lookup`:

drm_gem_object_lookup
=====================

.. c:function:: struct drm_gem_object *drm_gem_object_lookup (struct drm_device *dev, struct drm_file *filp, u32 handle)

    look up a GEM object from it's handle

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_file \*filp:
        DRM file private date

    :param u32 handle:
        userspace handle


.. _`drm_gem_object_lookup.description`:

Description
-----------

Returns:

A reference to the object named by the handle if such exists on ``filp``\ , NULL
otherwise.


.. _`drm_gem_close_ioctl`:

drm_gem_close_ioctl
===================

.. c:function:: int drm_gem_close_ioctl (struct drm_device *dev, void *data, struct drm_file *file_priv)

    implementation of the GEM_CLOSE ioctl

    :param struct drm_device \*dev:
        drm_device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        drm file-private structure


.. _`drm_gem_close_ioctl.description`:

Description
-----------

Releases the handle to an mm object.


.. _`drm_gem_flink_ioctl`:

drm_gem_flink_ioctl
===================

.. c:function:: int drm_gem_flink_ioctl (struct drm_device *dev, void *data, struct drm_file *file_priv)

    implementation of the GEM_FLINK ioctl

    :param struct drm_device \*dev:
        drm_device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        drm file-private structure


.. _`drm_gem_flink_ioctl.description`:

Description
-----------

Create a global name for an object, returning the name.

Note that the name does not hold a reference; when the object
is freed, the name goes away.


.. _`drm_gem_open_ioctl`:

drm_gem_open_ioctl
==================

.. c:function:: int drm_gem_open_ioctl (struct drm_device *dev, void *data, struct drm_file *file_priv)

    implementation of the GEM_OPEN ioctl

    :param struct drm_device \*dev:
        drm_device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        drm file-private structure


.. _`drm_gem_open_ioctl.description`:

Description
-----------

Open an object using the global name, returning a handle and the size.

This handle (of course) holds a reference to the object, so the object
will not go away until the handle is deleted.


.. _`drm_gem_open`:

drm_gem_open
============

.. c:function:: void drm_gem_open (struct drm_device *dev, struct drm_file *file_private)

    initalizes GEM file-private structures at devnode open time

    :param struct drm_device \*dev:
        drm_device which is being opened by userspace

    :param struct drm_file \*file_private:
        drm file-private structure to set up


.. _`drm_gem_open.description`:

Description
-----------

Called at device open time, sets up the structure for handling refcounting
of mm objects.


.. _`drm_gem_release`:

drm_gem_release
===============

.. c:function:: void drm_gem_release (struct drm_device *dev, struct drm_file *file_private)

    release file-private GEM resources

    :param struct drm_device \*dev:
        drm_device which is being closed by userspace

    :param struct drm_file \*file_private:
        drm file-private structure to clean up


.. _`drm_gem_release.description`:

Description
-----------

Called at close time when the filp is going away.

Releases any remaining references on objects by this filp.


.. _`drm_gem_object_free`:

drm_gem_object_free
===================

.. c:function:: void drm_gem_object_free (struct kref *kref)

    free a GEM object

    :param struct kref \*kref:
        kref of the object to free


.. _`drm_gem_object_free.description`:

Description
-----------

Called after the last reference to the object has been lost.
Must be called holding struct_ mutex

Frees the object


.. _`drm_gem_vm_open`:

drm_gem_vm_open
===============

.. c:function:: void drm_gem_vm_open (struct vm_area_struct *vma)

    vma->ops->open implementation for GEM

    :param struct vm_area_struct \*vma:
        VM area structure


.. _`drm_gem_vm_open.description`:

Description
-----------

This function implements the #vm_operations_struct :c:func:`open` callback for GEM
drivers. This must be used together with :c:func:`drm_gem_vm_close`.


.. _`drm_gem_vm_close`:

drm_gem_vm_close
================

.. c:function:: void drm_gem_vm_close (struct vm_area_struct *vma)

    vma->ops->close implementation for GEM

    :param struct vm_area_struct \*vma:
        VM area structure


.. _`drm_gem_vm_close.description`:

Description
-----------

This function implements the #vm_operations_struct :c:func:`close` callback for GEM
drivers. This must be used together with :c:func:`drm_gem_vm_open`.


.. _`drm_gem_mmap_obj`:

drm_gem_mmap_obj
================

.. c:function:: int drm_gem_mmap_obj (struct drm_gem_object *obj, unsigned long obj_size, struct vm_area_struct *vma)

    memory map a GEM object

    :param struct drm_gem_object \*obj:
        the GEM object to map

    :param unsigned long obj_size:
        the object size to be mapped, in bytes

    :param struct vm_area_struct \*vma:
        VMA for the area to be mapped


.. _`drm_gem_mmap_obj.description`:

Description
-----------

Set up the VMA to prepare mapping of the GEM object using the gem_vm_ops
provided by the driver. Depending on their requirements, drivers can either
provide a fault handler in their gem_vm_ops (in which case any accesses to
the object will be trapped, to perform migration, GTT binding, surface
register allocation, or performance monitoring), or mmap the buffer memory
synchronously after calling drm_gem_mmap_obj.

This function is mainly intended to implement the DMABUF mmap operation, when
the GEM object is not looked up based on its fake offset. To implement the
DRM mmap operation, drivers should use the :c:func:`drm_gem_mmap` function.

:c:func:`drm_gem_mmap_obj` assumes the user is granted access to the buffer while
:c:func:`drm_gem_mmap` prevents unprivileged users from mapping random objects. So
callers must verify access restrictions before calling this helper.

Return 0 or success or -EINVAL if the object size is smaller than the VMA
size, or if no gem_vm_ops are provided.


.. _`drm_gem_mmap`:

drm_gem_mmap
============

.. c:function:: int drm_gem_mmap (struct file *filp, struct vm_area_struct *vma)

    memory map routine for GEM objects

    :param struct file \*filp:
        DRM file pointer

    :param struct vm_area_struct \*vma:
        VMA for the area to be mapped


.. _`drm_gem_mmap.description`:

Description
-----------

If a driver supports GEM object mapping, mmap calls on the DRM file
descriptor will end up here.

Look up the GEM object based on the offset passed in (vma->vm_pgoff will
contain the fake offset we created when the GTT map ioctl was called on
the object) and map it with a call to :c:func:`drm_gem_mmap_obj`.

If the caller is not granted access to the buffer object, the mmap will fail
with EACCES. Please see the vma manager for more information.

