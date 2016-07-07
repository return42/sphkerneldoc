.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/ttm/ttm_bo_api.h

.. _`ttm_place`:

struct ttm_place
================

.. c:type:: struct ttm_place


.. _`ttm_place.definition`:

Definition
----------

.. code-block:: c

    struct ttm_place {
        unsigned fpfn;
        unsigned lpfn;
        uint32_t flags;
    }

.. _`ttm_place.members`:

Members
-------

fpfn
    first valid page frame number to put the object

lpfn
    last valid page frame number to put the object

flags
    memory domain and caching flags for the object

.. _`ttm_place.description`:

Description
-----------

Structure indicating a possible place to put an object.

.. _`ttm_placement`:

struct ttm_placement
====================

.. c:type:: struct ttm_placement


.. _`ttm_placement.definition`:

Definition
----------

.. code-block:: c

    struct ttm_placement {
        unsigned num_placement;
        const struct ttm_place *placement;
        unsigned num_busy_placement;
        const struct ttm_place *busy_placement;
    }

.. _`ttm_placement.members`:

Members
-------

num_placement
    number of preferred placements

placement
    preferred placements

num_busy_placement
    number of preferred placements when need to evict buffer

busy_placement
    preferred placements when need to evict buffer

.. _`ttm_placement.description`:

Description
-----------

Structure indicating the placement you request for an object.

.. _`ttm_bus_placement`:

struct ttm_bus_placement
========================

.. c:type:: struct ttm_bus_placement


.. _`ttm_bus_placement.definition`:

Definition
----------

.. code-block:: c

    struct ttm_bus_placement {
        void *addr;
        phys_addr_t base;
        unsigned long size;
        unsigned long offset;
        bool is_iomem;
        bool io_reserved_vm;
        uint64_t io_reserved_count;
    }

.. _`ttm_bus_placement.members`:

Members
-------

addr
    mapped virtual address

base
    bus base address

size
    size in byte

offset
    offset from the base address

is_iomem
    is this io memory ?

io_reserved_vm
    The VM system has a refcount in \ ``io_reserved_count``\ 

io_reserved_count
    Refcounting the numbers of callers to ttm_mem_io_reserve

.. _`ttm_bus_placement.description`:

Description
-----------

Structure indicating the bus placement of an object.

.. _`ttm_mem_reg`:

struct ttm_mem_reg
==================

.. c:type:: struct ttm_mem_reg


.. _`ttm_mem_reg.definition`:

Definition
----------

.. code-block:: c

    struct ttm_mem_reg {
        void *mm_node;
        unsigned long start;
        unsigned long size;
        unsigned long num_pages;
        uint32_t page_alignment;
        uint32_t mem_type;
        uint32_t placement;
        struct ttm_bus_placement bus;
    }

.. _`ttm_mem_reg.members`:

Members
-------

mm_node
    Memory manager node.

start
    *undescribed*

size
    Requested size of memory region.

num_pages
    Actual size of memory region in pages.

page_alignment
    Page alignment.

mem_type
    *undescribed*

placement
    Placement flags.

bus
    Placement on io bus accessible to the CPU

.. _`ttm_mem_reg.description`:

Description
-----------

Structure indicating the placement and space resources used by a
buffer object.

.. _`ttm_bo_type`:

enum ttm_bo_type
================

.. c:type:: enum ttm_bo_type


.. _`ttm_bo_type.definition`:

Definition
----------

.. code-block:: c

    enum ttm_bo_type {
        ttm_bo_type_device,
        ttm_bo_type_kernel,
        ttm_bo_type_sg
    };

.. _`ttm_bo_type.constants`:

Constants
---------

ttm_bo_type_device
    These are 'normal' buffers that can
    be mmapped by user space. Each of these bos occupy a slot in the
    device address space, that can be used for normal vm operations.

ttm_bo_type_kernel
    These buffers are like ttm_bo_type_device buffers,
    but they cannot be accessed from user-space. For kernel-only use.

ttm_bo_type_sg
    Buffer made from dmabuf sg table shared with another
    driver.

.. _`ttm_buffer_object`:

struct ttm_buffer_object
========================

.. c:type:: struct ttm_buffer_object


.. _`ttm_buffer_object.definition`:

Definition
----------

.. code-block:: c

    struct ttm_buffer_object {
        struct ttm_bo_global *glob;
        struct ttm_bo_device *bdev;
        enum ttm_bo_type type;
        void (* destroy) (struct ttm_buffer_object *);
        unsigned long num_pages;
        size_t acc_size;
        struct kref kref;
        struct kref list_kref;
        struct ttm_mem_reg mem;
        struct file *persistent_swap_storage;
        struct ttm_tt *ttm;
        bool evicted;
        atomic_t cpu_writers;
        struct list_head lru;
        struct list_head ddestroy;
        struct list_head swap;
        struct list_head io_reserve_lru;
        unsigned long priv_flags;
        struct drm_vma_offset_node vma_node;
        uint64_t offset;
        uint32_t cur_placement;
        struct sg_table *sg;
        struct reservation_object *resv;
        struct reservation_object ttm_resv;
        struct mutex wu_mutex;
    }

.. _`ttm_buffer_object.members`:

Members
-------

glob
    *undescribed*

bdev
    Pointer to the buffer object device structure.

type
    The bo type.

destroy
    Destruction function. If NULL, kfree is used.

num_pages
    Actual number of pages.

acc_size
    Accounted size for this object.

kref
    Reference count of this buffer object. When this refcount reaches
    zero, the object is put on the delayed delete list.

list_kref
    List reference count of this buffer object. This member is
    used to avoid destruction while the buffer object is still on a list.
    Lru lists may keep one refcount, the delayed delete list, and kref != 0
    keeps one refcount. When this refcount reaches zero,
    the object is destroyed.

mem
    structure describing current placement.

persistent_swap_storage
    Usually the swap storage is deleted for buffers
    pinned in physical memory. If this behaviour is not desired, this member
    holds a pointer to a persistent shmem object.

ttm
    TTM structure holding system pages.

evicted
    Whether the object was evicted without user-space knowing.

cpu_writers
    *undescribed*

lru
    List head for the lru list.

ddestroy
    List head for the delayed destroy list.

swap
    List head for swap LRU list.

io_reserve_lru
    *undescribed*

priv_flags
    Flags describing buffer object internal state.

vma_node
    Address space manager node.

offset
    The current GPU offset, which can have different meanings
    depending on the memory type. For SYSTEM type memory, it should be 0.

cur_placement
    Hint of current placement.

sg
    *undescribed*

resv
    *undescribed*

ttm_resv
    *undescribed*

wu_mutex
    Wait unreserved mutex.

.. _`ttm_buffer_object.description`:

Description
-----------

Base class for TTM buffer object, that deals with data placement and CPU
mappings. GPU mappings are really up to the driver, but for simpler GPUs
the driver can usually use the placement offset \ ``offset``\  directly as the
GPU virtual address. For drivers implementing multiple
GPU memory manager contexts, the driver should manage the address space
in these contexts separately and use these objects to get the correct
placement and caching for these GPU maps. This makes it possible to use
these objects for even quite elaborate memory management schemes.
The destroy member, the API visibility of this object makes it possible
to derive driver specific types.

.. _`ttm_bo_reference`:

ttm_bo_reference
================

.. c:function:: struct ttm_buffer_object *ttm_bo_reference(struct ttm_buffer_object *bo)

    reference a struct ttm_buffer_object

    :param struct ttm_buffer_object \*bo:
        The buffer object.

.. _`ttm_bo_reference.description`:

Description
-----------

Returns a refcounted pointer to a buffer object.

.. _`ttm_bo_wait`:

ttm_bo_wait
===========

.. c:function:: int ttm_bo_wait(struct ttm_buffer_object *bo, bool interruptible, bool no_wait)

    wait for buffer idle.

    :param struct ttm_buffer_object \*bo:
        The buffer object.

    :param bool interruptible:
        Use interruptible wait.

    :param bool no_wait:
        Return immediately if buffer is busy.

.. _`ttm_bo_wait.description`:

Description
-----------

This function must be called with the bo::mutex held, and makes
sure any previous rendering to the buffer is completed.

.. _`ttm_bo_wait.note`:

Note
----

It might be necessary to block validations before the
wait by reserving the buffer.
Returns -EBUSY if no_wait is true and the buffer is busy.
Returns -ERESTARTSYS if interrupted by a signal.

.. _`ttm_bo_validate`:

ttm_bo_validate
===============

.. c:function:: int ttm_bo_validate(struct ttm_buffer_object *bo, struct ttm_placement *placement, bool interruptible, bool no_wait_gpu)

    :param struct ttm_buffer_object \*bo:
        The buffer object.

    :param struct ttm_placement \*placement:
        Proposed placement for the buffer object.

    :param bool interruptible:
        Sleep interruptible if sleeping.

    :param bool no_wait_gpu:
        Return immediately if the GPU is busy.

.. _`ttm_bo_validate.description`:

Description
-----------

Changes placement and caching policy of the buffer object
according proposed placement.
Returns
-EINVAL on invalid proposed placement.
-ENOMEM on out-of-memory condition.
-EBUSY if no_wait is true and buffer busy.
-ERESTARTSYS if interrupted by a signal.

.. _`ttm_bo_unref`:

ttm_bo_unref
============

.. c:function:: void ttm_bo_unref(struct ttm_buffer_object **bo)

    :param struct ttm_buffer_object \*\*bo:
        The buffer object.

.. _`ttm_bo_unref.description`:

Description
-----------

Unreference and clear a pointer to a buffer object.

.. _`ttm_bo_list_ref_sub`:

ttm_bo_list_ref_sub
===================

.. c:function:: void ttm_bo_list_ref_sub(struct ttm_buffer_object *bo, int count, bool never_free)

    :param struct ttm_buffer_object \*bo:
        The buffer object.

    :param int count:
        The number of references with which to decrease \ ``bo``\ ::list_kref;

    :param bool never_free:
        The refcount should not reach zero with this operation.

.. _`ttm_bo_list_ref_sub.description`:

Description
-----------

Release \ ``count``\  lru list references to this buffer object.

.. _`ttm_bo_add_to_lru`:

ttm_bo_add_to_lru
=================

.. c:function:: void ttm_bo_add_to_lru(struct ttm_buffer_object *bo)

    :param struct ttm_buffer_object \*bo:
        The buffer object.

.. _`ttm_bo_add_to_lru.description`:

Description
-----------

Add this bo to the relevant mem type lru and, if it's backed by
system pages (ttms) to the swap list.
This function must be called with struct ttm_bo_global::lru_lock held, and
is typically called immediately prior to unreserving a bo.

.. _`ttm_bo_del_from_lru`:

ttm_bo_del_from_lru
===================

.. c:function:: int ttm_bo_del_from_lru(struct ttm_buffer_object *bo)

    :param struct ttm_buffer_object \*bo:
        The buffer object.

.. _`ttm_bo_del_from_lru.description`:

Description
-----------

Remove this bo from all lru lists used to lookup and reserve an object.
This function must be called with struct ttm_bo_global::lru_lock held,
and is usually called just immediately after the bo has been reserved to
avoid recursive reservation from lru lists.

.. _`ttm_bo_move_to_lru_tail`:

ttm_bo_move_to_lru_tail
=======================

.. c:function:: void ttm_bo_move_to_lru_tail(struct ttm_buffer_object *bo)

    :param struct ttm_buffer_object \*bo:
        The buffer object.

.. _`ttm_bo_move_to_lru_tail.description`:

Description
-----------

Move this BO to the tail of all lru lists used to lookup and reserve an
object. This function must be called with struct ttm_bo_global::lru_lock
held, and is used to make a BO less likely to be considered for eviction.

.. _`ttm_bo_lock_delayed_workqueue`:

ttm_bo_lock_delayed_workqueue
=============================

.. c:function:: int ttm_bo_lock_delayed_workqueue(struct ttm_bo_device *bdev)

    :param struct ttm_bo_device \*bdev:
        *undescribed*

.. _`ttm_bo_lock_delayed_workqueue.description`:

Description
-----------

Prevent the delayed workqueue from running.
Returns
True if the workqueue was queued at the time

.. _`ttm_bo_unlock_delayed_workqueue`:

ttm_bo_unlock_delayed_workqueue
===============================

.. c:function:: void ttm_bo_unlock_delayed_workqueue(struct ttm_bo_device *bdev, int resched)

    :param struct ttm_bo_device \*bdev:
        *undescribed*

    :param int resched:
        *undescribed*

.. _`ttm_bo_unlock_delayed_workqueue.description`:

Description
-----------

Allows the delayed workqueue to run.

.. _`ttm_bo_synccpu_write_grab`:

ttm_bo_synccpu_write_grab
=========================

.. c:function:: int ttm_bo_synccpu_write_grab(struct ttm_buffer_object *bo, bool no_wait)

    :param struct ttm_buffer_object \*bo:
        The buffer object:

    :param bool no_wait:
        Return immediately if buffer is busy.

.. _`ttm_bo_synccpu_write_grab.description`:

Description
-----------

Synchronizes a buffer object for CPU RW access. This means
command submission that affects the buffer will return -EBUSY
until ttm_bo_synccpu_write_release is called.

Returns
-EBUSY if the buffer is busy and no_wait is true.
-ERESTARTSYS if interrupted by a signal.

.. _`ttm_bo_synccpu_write_release`:

ttm_bo_synccpu_write_release
============================

.. c:function:: void ttm_bo_synccpu_write_release(struct ttm_buffer_object *bo)

    :param struct ttm_buffer_object \*bo:
        The buffer object.

.. _`ttm_bo_synccpu_write_release.description`:

Description
-----------

Releases a synccpu lock.

.. _`ttm_bo_acc_size`:

ttm_bo_acc_size
===============

.. c:function:: size_t ttm_bo_acc_size(struct ttm_bo_device *bdev, unsigned long bo_size, unsigned struct_size)

    :param struct ttm_bo_device \*bdev:
        Pointer to a ttm_bo_device struct.

    :param unsigned long bo_size:
        size of the buffer object in byte.

    :param unsigned struct_size:
        size of the structure holding buffer object datas

.. _`ttm_bo_acc_size.description`:

Description
-----------

Returns size to account for a buffer object

.. _`ttm_bo_init`:

ttm_bo_init
===========

.. c:function:: int ttm_bo_init(struct ttm_bo_device *bdev, struct ttm_buffer_object *bo, unsigned long size, enum ttm_bo_type type, struct ttm_placement *placement, uint32_t page_alignment, bool interrubtible, struct file *persistent_swap_storage, size_t acc_size, struct sg_table *sg, struct reservation_object *resv, void (*) destroy (struct ttm_buffer_object *)

    :param struct ttm_bo_device \*bdev:
        Pointer to a ttm_bo_device struct.

    :param struct ttm_buffer_object \*bo:
        Pointer to a ttm_buffer_object to be initialized.

    :param unsigned long size:
        Requested size of buffer object.

    :param enum ttm_bo_type type:
        Requested type of buffer object.

    :param struct ttm_placement \*placement:
        *undescribed*

    :param uint32_t page_alignment:
        Data alignment in pages.

    :param bool interrubtible:
        *undescribed*

    :param struct file \*persistent_swap_storage:
        Usually the swap storage is deleted for buffers
        pinned in physical memory. If this behaviour is not desired, this member
        holds a pointer to a persistent shmem object. Typically, this would
        point to the shmem object backing a GEM object if TTM is used to back a
        GEM user interface.

    :param size_t acc_size:
        Accounted size for this object.

    :param struct sg_table \*sg:
        *undescribed*

    :param struct reservation_object \*resv:
        Pointer to a reservation_object, or NULL to let ttm allocate one.

    :param (void (\*) destroy (struct ttm_buffer_object \*):
        Destroy function. Use NULL for \ :c:func:`kfree`\ .

.. _`ttm_bo_init.description`:

Description
-----------

This function initializes a pre-allocated struct ttm_buffer_object.
As this object may be part of a larger structure, this function,
together with the \ ``destroy``\  function,
enables driver-specific objects derived from a ttm_buffer_object.
On successful return, the object kref and list_kref are set to 1.
If a failure occurs, the function will call the \ ``destroy``\  function, or
\ :c:func:`kfree`\  if \ ``destroy``\  is NULL. Thus, after a failure, dereferencing \ ``bo``\  is
illegal and will likely cause memory corruption.

Returns
-ENOMEM: Out of memory.
-EINVAL: Invalid placement flags.
-ERESTARTSYS: Interrupted by signal while sleeping waiting for resources.

.. _`ttm_bo_create`:

ttm_bo_create
=============

.. c:function:: int ttm_bo_create(struct ttm_bo_device *bdev, unsigned long size, enum ttm_bo_type type, struct ttm_placement *placement, uint32_t page_alignment, bool interruptible, struct file *persistent_swap_storage, struct ttm_buffer_object **p_bo)

    :param struct ttm_bo_device \*bdev:
        Pointer to a ttm_bo_device struct.

    :param unsigned long size:
        Requested size of buffer object.

    :param enum ttm_bo_type type:
        Requested type of buffer object.

    :param struct ttm_placement \*placement:
        Initial placement.

    :param uint32_t page_alignment:
        Data alignment in pages.

    :param bool interruptible:
        If needing to sleep while waiting for GPU resources,
        sleep interruptible.

    :param struct file \*persistent_swap_storage:
        Usually the swap storage is deleted for buffers
        pinned in physical memory. If this behaviour is not desired, this member
        holds a pointer to a persistent shmem object. Typically, this would
        point to the shmem object backing a GEM object if TTM is used to back a
        GEM user interface.

    :param struct ttm_buffer_object \*\*p_bo:
        On successful completion \*p_bo points to the created object.

.. _`ttm_bo_create.description`:

Description
-----------

This function allocates a ttm_buffer_object, and then calls ttm_bo_init
on that object. The destroy function is set to \ :c:func:`kfree`\ .
Returns
-ENOMEM: Out of memory.
-EINVAL: Invalid placement flags.
-ERESTARTSYS: Interrupted by signal while waiting for resources.

.. _`ttm_bo_init_mm`:

ttm_bo_init_mm
==============

.. c:function:: int ttm_bo_init_mm(struct ttm_bo_device *bdev, unsigned type, unsigned long p_size)

    :param struct ttm_bo_device \*bdev:
        Pointer to a ttm_bo_device struct.

    :param unsigned type:
        *undescribed*

    :param unsigned long p_size:
        size managed area in pages.

.. _`ttm_bo_init_mm.description`:

Description
-----------

Initialize a manager for a given memory type.

.. _`ttm_bo_init_mm.note`:

Note
----

if part of driver firstopen, it must be protected from a
potentially racing lastclose.

.. _`ttm_bo_init_mm.return`:

Return
------

-EINVAL: invalid size or memory type.
-ENOMEM: Not enough memory.
May also return driver-specified errors.

.. _`ttm_bo_clean_mm`:

ttm_bo_clean_mm
===============

.. c:function:: int ttm_bo_clean_mm(struct ttm_bo_device *bdev, unsigned mem_type)

    :param struct ttm_bo_device \*bdev:
        Pointer to a ttm_bo_device struct.

    :param unsigned mem_type:
        The memory type.

.. _`ttm_bo_clean_mm.description`:

Description
-----------

Take down a manager for a given memory type after first walking
the LRU list to evict any buffers left alive.

Normally, this function is part of \ :c:func:`lastclose`\  or \ :c:func:`unload`\ , and at that
point there shouldn't be any buffers left created by user-space, since
there should've been removed by the file descriptor \ :c:func:`release`\  method.
However, before this function is run, make sure to signal all sync objects,
and verify that the delayed delete queue is empty. The driver must also
make sure that there are no NO_EVICT buffers present in this memory type
when the call is made.

If this function is part of a VT switch, the caller must make sure that
there are no appications currently validating buffers before this
function is called. The caller can do that by first taking the
struct ttm_bo_device::ttm_lock in write mode.

.. _`ttm_bo_clean_mm.return`:

Return
------

-EINVAL: invalid or uninitialized memory type.
-EBUSY: There are still buffers left in this memory type.

.. _`ttm_bo_evict_mm`:

ttm_bo_evict_mm
===============

.. c:function:: int ttm_bo_evict_mm(struct ttm_bo_device *bdev, unsigned mem_type)

    :param struct ttm_bo_device \*bdev:
        Pointer to a ttm_bo_device struct.

    :param unsigned mem_type:
        The memory type.

.. _`ttm_bo_evict_mm.description`:

Description
-----------

Evicts all buffers on the lru list of the memory type.
This is normally part of a VT switch or an
out-of-memory-space-due-to-fragmentation handler.
The caller must make sure that there are no other processes
currently validating buffers, and can do that by taking the
struct ttm_bo_device::ttm_lock in write mode.

.. _`ttm_bo_evict_mm.return`:

Return
------

-EINVAL: Invalid or uninitialized memory type.
-ERESTARTSYS: The call was interrupted by a signal while waiting to
evict a buffer.

.. _`ttm_kmap_obj_virtual`:

ttm_kmap_obj_virtual
====================

.. c:function:: void *ttm_kmap_obj_virtual(struct ttm_bo_kmap_obj *map, bool *is_iomem)

    :param struct ttm_bo_kmap_obj \*map:
        A struct ttm_bo_kmap_obj returned from ttm_bo_kmap.

    :param bool \*is_iomem:
        Pointer to an integer that on return indicates 1 if the
        virtual map is io memory, 0 if normal memory.

.. _`ttm_kmap_obj_virtual.description`:

Description
-----------

Returns the virtual address of a buffer object area mapped by ttm_bo_kmap.
If \*is_iomem is 1 on return, the virtual address points to an io memory area,
that should strictly be accessed by the \ :c:func:`iowriteXX`\  and similar functions.

.. _`ttm_bo_kmap`:

ttm_bo_kmap
===========

.. c:function:: int ttm_bo_kmap(struct ttm_buffer_object *bo, unsigned long start_page, unsigned long num_pages, struct ttm_bo_kmap_obj *map)

    :param struct ttm_buffer_object \*bo:
        The buffer object.

    :param unsigned long start_page:
        The first page to map.

    :param unsigned long num_pages:
        Number of pages to map.

    :param struct ttm_bo_kmap_obj \*map:
        pointer to a struct ttm_bo_kmap_obj representing the map.

.. _`ttm_bo_kmap.description`:

Description
-----------

Sets up a kernel virtual mapping, using ioremap, vmap or kmap to the
data in the buffer object. The ttm_kmap_obj_virtual function can then be
used to obtain a virtual address to the data.

Returns
-ENOMEM: Out of memory.
-EINVAL: Invalid range.

.. _`ttm_bo_kunmap`:

ttm_bo_kunmap
=============

.. c:function:: void ttm_bo_kunmap(struct ttm_bo_kmap_obj *map)

    :param struct ttm_bo_kmap_obj \*map:
        Object describing the map to unmap.

.. _`ttm_bo_kunmap.description`:

Description
-----------

Unmaps a kernel map set up by ttm_bo_kmap.

.. _`ttm_fbdev_mmap`:

ttm_fbdev_mmap
==============

.. c:function:: int ttm_fbdev_mmap(struct vm_area_struct *vma, struct ttm_buffer_object *bo)

    mmap fbdev memory backed by a ttm buffer object.

    :param struct vm_area_struct \*vma:
        vma as input from the fbdev mmap method.

    :param struct ttm_buffer_object \*bo:
        The bo backing the address space. The address space will
        have the same size as the bo, and start at offset 0.

.. _`ttm_fbdev_mmap.description`:

Description
-----------

This function is intended to be called by the fbdev mmap method
if the fbdev address space is to be backed by a bo.

.. _`ttm_bo_mmap`:

ttm_bo_mmap
===========

.. c:function:: int ttm_bo_mmap(struct file *filp, struct vm_area_struct *vma, struct ttm_bo_device *bdev)

    mmap out of the ttm device address space.

    :param struct file \*filp:
        filp as input from the mmap method.

    :param struct vm_area_struct \*vma:
        vma as input from the mmap method.

    :param struct ttm_bo_device \*bdev:
        Pointer to the ttm_bo_device with the address space manager.

.. _`ttm_bo_mmap.description`:

Description
-----------

This function is intended to be called by the device mmap method.
if the device address space is to be backed by the bo manager.

.. _`ttm_bo_io`:

ttm_bo_io
=========

.. c:function:: ssize_t ttm_bo_io(struct ttm_bo_device *bdev, struct file *filp, const char __user *wbuf, char __user *rbuf, size_t count, loff_t *f_pos, bool write)

    :param struct ttm_bo_device \*bdev:
        Pointer to the struct ttm_bo_device.

    :param struct file \*filp:
        Pointer to the struct file attempting to read / write.

    :param const char __user \*wbuf:
        User-space pointer to address of buffer to write. NULL on read.

    :param char __user \*rbuf:
        User-space pointer to address of buffer to read into.
        Null on write.

    :param size_t count:
        Number of bytes to read / write.

    :param loff_t \*f_pos:
        Pointer to current file position.

    :param bool write:
        1 for read, 0 for write.

.. _`ttm_bo_io.description`:

Description
-----------

This function implements read / write into ttm buffer objects, and is
intended to
be called from the fops::read and fops::write method.

.. _`ttm_bo_io.return`:

Return
------

See man (2) write, man(2) read. In particular,
the function may return -ERESTARTSYS if
interrupted by a signal.

.. This file was automatic generated / don't edit.

