.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/ttm/ttm_bo_driver.h

.. _`ttm_mem_type_manager`:

struct ttm_mem_type_manager
===========================

.. c:type:: struct ttm_mem_type_manager


.. _`ttm_mem_type_manager.definition`:

Definition
----------

.. code-block:: c

    struct ttm_mem_type_manager {
        struct ttm_bo_device *bdev;
        bool has_type;
        bool use_type;
        uint32_t flags;
        uint64_t gpu_offset;
        uint64_t size;
        uint32_t available_caching;
        uint32_t default_caching;
        const struct ttm_mem_type_manager_func *func;
        void *priv;
        struct mutex io_reserve_mutex;
        bool use_io_reserve_lru;
        bool io_reserve_fastpath;
        spinlock_t move_lock;
        struct list_head io_reserve_lru;
        struct list_head lru[TTM_MAX_BO_PRIORITY];
        struct dma_fence *move;
    }

.. _`ttm_mem_type_manager.members`:

Members
-------

bdev
    *undescribed*

has_type
    The memory type has been initialized.

use_type
    The memory type is enabled.

flags
    TTM_MEMTYPE_XX flags identifying the traits of the memory
    managed by this memory type.

gpu_offset
    If used, the GPU offset of the first managed page of
    fixed memory or the first managed location in an aperture.

size
    Size of the managed region.

available_caching
    A mask of available caching types, TTM_PL_FLAG_XX,
    as defined in ttm_placement_common.h

default_caching
    The default caching policy used for a buffer object
    placed in this memory type if the user doesn't provide one.

func
    structure pointer implementing the range manager. See above

priv
    Driver private closure for \ ``func``\ .

io_reserve_mutex
    Mutex optionally protecting shared io_reserve structures

use_io_reserve_lru
    Use an lru list to try to unreserve io_mem_regions
    reserved by the TTM vm system.

io_reserve_fastpath
    Only use bdev::driver::io_mem_reserve to obtain

move_lock
    lock for move fence
    static information. bdev::driver::io_mem_free is never used.

io_reserve_lru
    Optional lru list for unreserving io mem regions.

lru
    The lru list for this memory type.

move
    The fence of the last pipelined move operation.

.. _`ttm_mem_type_manager.description`:

Description
-----------

This structure is used to identify and manage memory types for a device.
It's set up by the ttm_bo_driver::init_mem_type method.

.. _`ttm_bo_driver`:

struct ttm_bo_driver
====================

.. c:type:: struct ttm_bo_driver


.. _`ttm_bo_driver.definition`:

Definition
----------

.. code-block:: c

    struct ttm_bo_driver {
        struct ttm_tt *(*ttm_tt_create)(struct ttm_buffer_object *bo, uint32_t page_flags);
        int (*ttm_tt_populate)(struct ttm_tt *ttm, struct ttm_operation_ctx *ctx);
        void (*ttm_tt_unpopulate)(struct ttm_tt *ttm);
        int (*invalidate_caches)(struct ttm_bo_device *bdev, uint32_t flags);
        int (*init_mem_type)(struct ttm_bo_device *bdev, uint32_t type, struct ttm_mem_type_manager *man);
        bool (*eviction_valuable)(struct ttm_buffer_object *bo, const struct ttm_place *place);
        void (*evict_flags)(struct ttm_buffer_object *bo, struct ttm_placement *placement);
        int (*move)(struct ttm_buffer_object *bo, bool evict,struct ttm_operation_ctx *ctx, struct ttm_mem_reg *new_mem);
        int (*verify_access)(struct ttm_buffer_object *bo, struct file *filp);
        void (*move_notify)(struct ttm_buffer_object *bo,bool evict, struct ttm_mem_reg *new_mem);
        int (*fault_reserve_notify)(struct ttm_buffer_object *bo);
        void (*swap_notify)(struct ttm_buffer_object *bo);
        int (*io_mem_reserve)(struct ttm_bo_device *bdev, struct ttm_mem_reg *mem);
        void (*io_mem_free)(struct ttm_bo_device *bdev, struct ttm_mem_reg *mem);
        unsigned long (*io_mem_pfn)(struct ttm_buffer_object *bo, unsigned long page_offset);
        int (*access_memory)(struct ttm_buffer_object *bo, unsigned long offset, void *buf, int len, int write);
    }

.. _`ttm_bo_driver.members`:

Members
-------

ttm_tt_create
    *undescribed*

ttm_tt_populate
    *undescribed*

ttm_tt_unpopulate
    *undescribed*

invalidate_caches
    Callback to invalidate read caches when a buffer object
    has been evicted.

init_mem_type
    Callback to initialize a struct ttm_mem_type_manager
    structure.

eviction_valuable
    *undescribed*

evict_flags
    Callback to obtain placement flags when a buffer is evicted.

move
    Callback for a driver to hook in accelerated functions to
    move a buffer.
    If set to NULL, a potentially slow \ :c:func:`memcpy`\  move is used.

verify_access
    *undescribed*

move_notify
    *undescribed*

fault_reserve_notify
    *undescribed*

swap_notify
    *undescribed*

io_mem_reserve
    *undescribed*

io_mem_free
    *undescribed*

io_mem_pfn
    *undescribed*

access_memory
    *undescribed*

.. _`ttm_bo_global_ref`:

struct ttm_bo_global_ref
========================

.. c:type:: struct ttm_bo_global_ref

    Argument to initialize a struct ttm_bo_global.

.. _`ttm_bo_global_ref.definition`:

Definition
----------

.. code-block:: c

    struct ttm_bo_global_ref {
        struct drm_global_reference ref;
        struct ttm_mem_global *mem_glob;
    }

.. _`ttm_bo_global_ref.members`:

Members
-------

ref
    *undescribed*

mem_glob
    *undescribed*

.. _`ttm_bo_global`:

struct ttm_bo_global
====================

.. c:type:: struct ttm_bo_global

    Buffer object driver global data.

.. _`ttm_bo_global.definition`:

Definition
----------

.. code-block:: c

    struct ttm_bo_global {
        struct kobject kobj;
        struct ttm_mem_global *mem_glob;
        struct page *dummy_read_page;
        struct mutex device_list_mutex;
        spinlock_t lru_lock;
        struct list_head device_list;
        struct list_head swap_lru[TTM_MAX_BO_PRIORITY];
        atomic_t bo_count;
    }

.. _`ttm_bo_global.members`:

Members
-------

kobj
    *undescribed*

mem_glob
    Pointer to a struct ttm_mem_global object for accounting.

dummy_read_page
    Pointer to a dummy page used for mapping requests
    of unpopulated pages.

device_list_mutex
    Mutex protecting the device list.
    This mutex is held while traversing the device list for pm options.

lru_lock
    Spinlock protecting the bo subsystem lru lists.

device_list
    List of buffer object devices.

swap_lru
    Lru list of buffer objects used for swapping.

bo_count
    *undescribed*

.. _`ttm_bo_device`:

struct ttm_bo_device
====================

.. c:type:: struct ttm_bo_device

    Buffer object driver device-specific data.

.. _`ttm_bo_device.definition`:

Definition
----------

.. code-block:: c

    struct ttm_bo_device {
        struct list_head device_list;
        struct ttm_bo_global *glob;
        struct ttm_bo_driver *driver;
        struct ttm_mem_type_manager man[TTM_NUM_MEM_TYPES];
        struct drm_vma_offset_manager vma_manager;
        struct list_head ddestroy;
        struct address_space *dev_mapping;
        struct delayed_work wq;
        bool need_dma32;
        bool no_retry;
    }

.. _`ttm_bo_device.members`:

Members
-------

device_list
    *undescribed*

glob
    *undescribed*

driver
    Pointer to a struct ttm_bo_driver struct setup by the driver.

man
    An array of mem_type_managers.

vma_manager
    Address space manager

ddestroy
    *undescribed*

dev_mapping
    A pointer to the struct address_space representing the
    device address space.

wq
    Work queue structure for the delayed delete workqueue.

need_dma32
    *undescribed*

no_retry
    Don't retry allocation if it fails

.. _`ttm_bo_device.lru_lock`:

lru_lock
--------

Spinlock that protects the buffer+device lru lists and
ddestroy lists.

.. _`ttm_lru_bulk_move_pos`:

struct ttm_lru_bulk_move_pos
============================

.. c:type:: struct ttm_lru_bulk_move_pos


.. _`ttm_lru_bulk_move_pos.definition`:

Definition
----------

.. code-block:: c

    struct ttm_lru_bulk_move_pos {
        struct ttm_buffer_object *first;
        struct ttm_buffer_object *last;
    }

.. _`ttm_lru_bulk_move_pos.members`:

Members
-------

first
    first BO in the bulk move range

last
    last BO in the bulk move range

.. _`ttm_lru_bulk_move_pos.description`:

Description
-----------

Positions for a lru bulk move.

.. _`ttm_lru_bulk_move`:

struct ttm_lru_bulk_move
========================

.. c:type:: struct ttm_lru_bulk_move


.. _`ttm_lru_bulk_move.definition`:

Definition
----------

.. code-block:: c

    struct ttm_lru_bulk_move {
        struct ttm_lru_bulk_move_pos tt[TTM_MAX_BO_PRIORITY];
        struct ttm_lru_bulk_move_pos vram[TTM_MAX_BO_PRIORITY];
        struct ttm_lru_bulk_move_pos swap[TTM_MAX_BO_PRIORITY];
    }

.. _`ttm_lru_bulk_move.members`:

Members
-------

tt
    first/last lru entry for BOs in the TT domain

vram
    first/last lru entry for BOs in the VRAM domain

swap
    first/last lru entry for BOs on the swap list

.. _`ttm_lru_bulk_move.description`:

Description
-----------

Helper structure for bulk moves on the LRU list.

.. _`ttm_flag_masked`:

ttm_flag_masked
===============

.. c:function:: uint32_t ttm_flag_masked(uint32_t *old, uint32_t new, uint32_t mask)

    :param old:
        Pointer to the result and original value.
    :type old: uint32_t \*

    :param new:
        New value of bits.
    :type new: uint32_t

    :param mask:
        Mask of bits to change.
    :type mask: uint32_t

.. _`ttm_flag_masked.description`:

Description
-----------

Convenience function to change a number of bits identified by a mask.

.. _`ttm_mem_reg_is_pci`:

ttm_mem_reg_is_pci
==================

.. c:function:: bool ttm_mem_reg_is_pci(struct ttm_bo_device *bdev, struct ttm_mem_reg *mem)

    :param bdev:
        Pointer to a struct ttm_bo_device.
    :type bdev: struct ttm_bo_device \*

    :param mem:
        A valid struct ttm_mem_reg.
    :type mem: struct ttm_mem_reg \*

.. _`ttm_mem_reg_is_pci.description`:

Description
-----------

Returns true if the memory described by \ ``mem``\  is PCI memory,
false otherwise.

.. _`ttm_bo_mem_space`:

ttm_bo_mem_space
================

.. c:function:: int ttm_bo_mem_space(struct ttm_buffer_object *bo, struct ttm_placement *placement, struct ttm_mem_reg *mem, struct ttm_operation_ctx *ctx)

    :param bo:
        Pointer to a struct ttm_buffer_object. the data of which
        we want to allocate space for.
    :type bo: struct ttm_buffer_object \*

    :param placement:
        *undescribed*
    :type placement: struct ttm_placement \*

    :param mem:
        A struct ttm_mem_reg.
    :type mem: struct ttm_mem_reg \*

    :param ctx:
        *undescribed*
    :type ctx: struct ttm_operation_ctx \*

.. _`ttm_bo_mem_space.description`:

Description
-----------

Allocate memory space for the buffer object pointed to by \ ``bo``\ , using
the placement flags in \ ``mem``\ , potentially evicting other idle buffer objects.
This function may sleep while waiting for space to become available.

.. _`ttm_bo_mem_space.return`:

Return
------

-EBUSY: No space available (only if no_wait == 1).
-ENOMEM: Could not allocate memory for the buffer object, either due to
fragmentation or concurrent allocators.
-ERESTARTSYS: An interruptible sleep was interrupted by a signal.

.. _`ttm_bo_device_init`:

ttm_bo_device_init
==================

.. c:function:: int ttm_bo_device_init(struct ttm_bo_device *bdev, struct ttm_bo_global *glob, struct ttm_bo_driver *driver, struct address_space *mapping, uint64_t file_page_offset, bool need_dma32)

    :param bdev:
        A pointer to a struct ttm_bo_device to initialize.
    :type bdev: struct ttm_bo_device \*

    :param glob:
        A pointer to an initialized struct ttm_bo_global.
    :type glob: struct ttm_bo_global \*

    :param driver:
        A pointer to a struct ttm_bo_driver set up by the caller.
    :type driver: struct ttm_bo_driver \*

    :param mapping:
        The address space to use for this bo.
    :type mapping: struct address_space \*

    :param file_page_offset:
        Offset into the device address space that is available
        for buffer data. This ensures compatibility with other users of the
        address space.
    :type file_page_offset: uint64_t

    :param need_dma32:
        *undescribed*
    :type need_dma32: bool

.. _`ttm_bo_device_init.return`:

Return
------

!0: Failure.

.. _`ttm_bo_unmap_virtual`:

ttm_bo_unmap_virtual
====================

.. c:function:: void ttm_bo_unmap_virtual(struct ttm_buffer_object *bo)

    :param bo:
        tear down the virtual mappings for this BO
    :type bo: struct ttm_buffer_object \*

.. _`ttm_bo_unmap_virtual_locked`:

ttm_bo_unmap_virtual_locked
===========================

.. c:function:: void ttm_bo_unmap_virtual_locked(struct ttm_buffer_object *bo)

    :param bo:
        tear down the virtual mappings for this BO
    :type bo: struct ttm_buffer_object \*

.. _`ttm_bo_unmap_virtual_locked.description`:

Description
-----------

The caller must take ttm_mem_io_lock before calling this function.

.. _`__ttm_bo_reserve`:

\__ttm_bo_reserve
=================

.. c:function:: int __ttm_bo_reserve(struct ttm_buffer_object *bo, bool interruptible, bool no_wait, struct ww_acquire_ctx *ticket)

    :param bo:
        A pointer to a struct ttm_buffer_object.
    :type bo: struct ttm_buffer_object \*

    :param interruptible:
        Sleep interruptible if waiting.
    :type interruptible: bool

    :param no_wait:
        Don't sleep while trying to reserve, rather return -EBUSY.
    :type no_wait: bool

    :param ticket:
        ticket used to acquire the ww_mutex.
    :type ticket: struct ww_acquire_ctx \*

.. _`__ttm_bo_reserve.description`:

Description
-----------

Will not remove reserved buffers from the lru lists.
Otherwise identical to ttm_bo_reserve.

.. _`__ttm_bo_reserve.return`:

Return
------

-EDEADLK: The reservation may cause a deadlock.
Release all buffer reservations, wait for \ ``bo``\  to become unreserved and
try again. (only if use_sequence == 1).
-ERESTARTSYS: A wait for the buffer to become unreserved was interrupted by
a signal. Release all buffer reservations and return to user-space.
-EBUSY: The function needed to sleep, but \ ``no_wait``\  was true
-EALREADY: Bo already reserved using \ ``ticket``\ . This error code will only
be returned if \ ``use_ticket``\  is set to true.

.. _`ttm_bo_reserve`:

ttm_bo_reserve
==============

.. c:function:: int ttm_bo_reserve(struct ttm_buffer_object *bo, bool interruptible, bool no_wait, struct ww_acquire_ctx *ticket)

    :param bo:
        A pointer to a struct ttm_buffer_object.
    :type bo: struct ttm_buffer_object \*

    :param interruptible:
        Sleep interruptible if waiting.
    :type interruptible: bool

    :param no_wait:
        Don't sleep while trying to reserve, rather return -EBUSY.
    :type no_wait: bool

    :param ticket:
        ticket used to acquire the ww_mutex.
    :type ticket: struct ww_acquire_ctx \*

.. _`ttm_bo_reserve.description`:

Description
-----------

Locks a buffer object for validation. (Or prevents other processes from
locking it for validation) and removes it from lru lists, while taking
a number of measures to prevent deadlocks.

Deadlocks may occur when two processes try to reserve multiple buffers in
different order, either by will or as a result of a buffer being evicted
to make room for a buffer already reserved. (Buffers are reserved before
they are evicted). The following algorithm prevents such deadlocks from

.. _`ttm_bo_reserve.occurring`:

occurring
---------

Processes attempting to reserve multiple buffers other than for eviction,
(typically execbuf), should first obtain a unique 32-bit
validation sequence number,
and call this function with \ ``use_ticket``\  == 1 and \ ``ticket->stamp``\  == the unique
sequence number. If upon call of this function, the buffer object is already
reserved, the validation sequence is checked against the validation
sequence of the process currently reserving the buffer,
and if the current validation sequence is greater than that of the process
holding the reservation, the function returns -EDEADLK. Otherwise it sleeps
waiting for the buffer to become unreserved, after which it retries
reserving.
The caller should, when receiving an -EDEADLK error
release all its buffer reservations, wait for \ ``bo``\  to become unreserved, and
then rerun the validation with the same validation sequence. This procedure
will always guarantee that the process with the lowest validation sequence
will eventually succeed, preventing both deadlocks and starvation.

.. _`ttm_bo_reserve.return`:

Return
------

-EDEADLK: The reservation may cause a deadlock.
Release all buffer reservations, wait for \ ``bo``\  to become unreserved and
try again. (only if use_sequence == 1).
-ERESTARTSYS: A wait for the buffer to become unreserved was interrupted by
a signal. Release all buffer reservations and return to user-space.
-EBUSY: The function needed to sleep, but \ ``no_wait``\  was true
-EALREADY: Bo already reserved using \ ``ticket``\ . This error code will only
be returned if \ ``use_ticket``\  is set to true.

.. _`ttm_bo_reserve_slowpath`:

ttm_bo_reserve_slowpath
=======================

.. c:function:: int ttm_bo_reserve_slowpath(struct ttm_buffer_object *bo, bool interruptible, struct ww_acquire_ctx *ticket)

    :param bo:
        A pointer to a struct ttm_buffer_object.
    :type bo: struct ttm_buffer_object \*

    :param interruptible:
        Sleep interruptible if waiting.
    :type interruptible: bool

    :param ticket:
        *undescribed*
    :type ticket: struct ww_acquire_ctx \*

.. _`ttm_bo_reserve_slowpath.description`:

Description
-----------

This is called after ttm_bo_reserve returns -EAGAIN and we backed off
from all our other reservations. Because there are no other reservations
held by us, this function cannot deadlock any more.

.. _`ttm_bo_unreserve`:

ttm_bo_unreserve
================

.. c:function:: void ttm_bo_unreserve(struct ttm_buffer_object *bo)

    :param bo:
        A pointer to a struct ttm_buffer_object.
    :type bo: struct ttm_buffer_object \*

.. _`ttm_bo_unreserve.description`:

Description
-----------

Unreserve a previous reservation of \ ``bo``\ .

.. _`ttm_bo_move_ttm`:

ttm_bo_move_ttm
===============

.. c:function:: int ttm_bo_move_ttm(struct ttm_buffer_object *bo, struct ttm_operation_ctx *ctx, struct ttm_mem_reg *new_mem)

    :param bo:
        A pointer to a struct ttm_buffer_object.
    :type bo: struct ttm_buffer_object \*

    :param ctx:
        *undescribed*
    :type ctx: struct ttm_operation_ctx \*

    :param new_mem:
        struct ttm_mem_reg indicating where to move.
    :type new_mem: struct ttm_mem_reg \*

.. _`ttm_bo_move_ttm.description`:

Description
-----------

Optimized move function for a buffer object with both old and
new placement backed by a TTM. The function will, if successful,
free any old aperture space, and set (@new_mem)->mm_node to NULL,
and update the (@bo)->mem placement flags. If unsuccessful, the old
data remains untouched, and it's up to the caller to free the
memory space indicated by \ ``new_mem``\ .

.. _`ttm_bo_move_ttm.return`:

Return
------

!0: Failure.

.. _`ttm_bo_move_memcpy`:

ttm_bo_move_memcpy
==================

.. c:function:: int ttm_bo_move_memcpy(struct ttm_buffer_object *bo, struct ttm_operation_ctx *ctx, struct ttm_mem_reg *new_mem)

    :param bo:
        A pointer to a struct ttm_buffer_object.
    :type bo: struct ttm_buffer_object \*

    :param ctx:
        *undescribed*
    :type ctx: struct ttm_operation_ctx \*

    :param new_mem:
        struct ttm_mem_reg indicating where to move.
    :type new_mem: struct ttm_mem_reg \*

.. _`ttm_bo_move_memcpy.description`:

Description
-----------

Fallback move function for a mappable buffer object in mappable memory.
The function will, if successful,
free any old aperture space, and set (@new_mem)->mm_node to NULL,
and update the (@bo)->mem placement flags. If unsuccessful, the old
data remains untouched, and it's up to the caller to free the
memory space indicated by \ ``new_mem``\ .

.. _`ttm_bo_move_memcpy.return`:

Return
------

!0: Failure.

.. _`ttm_bo_free_old_node`:

ttm_bo_free_old_node
====================

.. c:function:: void ttm_bo_free_old_node(struct ttm_buffer_object *bo)

    :param bo:
        A pointer to a struct ttm_buffer_object.
    :type bo: struct ttm_buffer_object \*

.. _`ttm_bo_free_old_node.description`:

Description
-----------

Utility function to free an old placement after a successful move.

.. _`ttm_bo_move_accel_cleanup`:

ttm_bo_move_accel_cleanup
=========================

.. c:function:: int ttm_bo_move_accel_cleanup(struct ttm_buffer_object *bo, struct dma_fence *fence, bool evict, struct ttm_mem_reg *new_mem)

    :param bo:
        A pointer to a struct ttm_buffer_object.
    :type bo: struct ttm_buffer_object \*

    :param fence:
        A fence object that signals when moving is complete.
    :type fence: struct dma_fence \*

    :param evict:
        This is an evict move. Don't return until the buffer is idle.
    :type evict: bool

    :param new_mem:
        struct ttm_mem_reg indicating where to move.
    :type new_mem: struct ttm_mem_reg \*

.. _`ttm_bo_move_accel_cleanup.description`:

Description
-----------

Accelerated move function to be called when an accelerated move
has been scheduled. The function will create a new temporary buffer object
representing the old placement, and put the sync object on both buffer
objects. After that the newly created buffer object is unref'd to be
destroyed when the move is complete. This will help pipeline
buffer moves.

.. _`ttm_bo_pipeline_move`:

ttm_bo_pipeline_move
====================

.. c:function:: int ttm_bo_pipeline_move(struct ttm_buffer_object *bo, struct dma_fence *fence, bool evict, struct ttm_mem_reg *new_mem)

    :param bo:
        A pointer to a struct ttm_buffer_object.
    :type bo: struct ttm_buffer_object \*

    :param fence:
        A fence object that signals when moving is complete.
    :type fence: struct dma_fence \*

    :param evict:
        This is an evict move. Don't return until the buffer is idle.
    :type evict: bool

    :param new_mem:
        struct ttm_mem_reg indicating where to move.
    :type new_mem: struct ttm_mem_reg \*

.. _`ttm_bo_pipeline_move.description`:

Description
-----------

Function for pipelining accelerated moves. Either free the memory
immediately or hang it on a temporary buffer object.

.. _`ttm_bo_pipeline_gutting`:

ttm_bo_pipeline_gutting
=======================

.. c:function:: int ttm_bo_pipeline_gutting(struct ttm_buffer_object *bo)

    :param bo:
        A pointer to a struct ttm_buffer_object.
    :type bo: struct ttm_buffer_object \*

.. _`ttm_bo_pipeline_gutting.description`:

Description
-----------

Pipelined gutting a BO of it's backing store.

.. _`ttm_io_prot`:

ttm_io_prot
===========

.. c:function:: pgprot_t ttm_io_prot(uint32_t caching_flags, pgprot_t tmp)

    :param caching_flags:
        *undescribed*
    :type caching_flags: uint32_t

    :param tmp:
        Page protection flag for a normal, cached mapping.
    :type tmp: pgprot_t

.. _`ttm_io_prot.description`:

Description
-----------

Utility function that returns the pgprot_t that should be used for
setting up a PTE with the caching model indicated by \ ``c_state``\ .

.. This file was automatic generated / don't edit.

