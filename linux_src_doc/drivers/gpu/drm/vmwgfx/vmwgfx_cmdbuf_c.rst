.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_cmdbuf.c

.. _`vmw_cmdbuf_context`:

struct vmw_cmdbuf_context
=========================

.. c:type:: struct vmw_cmdbuf_context

    Command buffer context queues

.. _`vmw_cmdbuf_context.definition`:

Definition
----------

.. code-block:: c

    struct vmw_cmdbuf_context {
        struct list_head submitted;
        struct list_head hw_submitted;
        struct list_head preempted;
        unsigned num_hw_submitted;
        bool block_submission;
    }

.. _`vmw_cmdbuf_context.members`:

Members
-------

submitted
    List of command buffers that have been submitted to the
    manager but not yet submitted to hardware.

hw_submitted
    List of command buffers submitted to hardware.

preempted
    List of preempted command buffers.

num_hw_submitted
    Number of buffers currently being processed by hardware

block_submission
    *undescribed*

.. _`vmw_cmdbuf_man`:

struct vmw_cmdbuf_man
=====================

.. c:type:: struct vmw_cmdbuf_man

    - Command buffer manager

.. _`vmw_cmdbuf_man.definition`:

Definition
----------

.. code-block:: c

    struct vmw_cmdbuf_man {
        struct mutex cur_mutex;
        struct mutex space_mutex;
        struct mutex error_mutex;
        struct work_struct work;
        struct vmw_private *dev_priv;
        struct vmw_cmdbuf_context ctx[SVGA_CB_CONTEXT_MAX];
        struct list_head error;
        struct drm_mm mm;
        struct ttm_buffer_object *cmd_space;
        struct ttm_bo_kmap_obj map_obj;
        u8 *map;
        struct vmw_cmdbuf_header *cur;
        size_t cur_pos;
        size_t default_size;
        unsigned max_hw_submitted;
        spinlock_t lock;
        struct dma_pool *headers;
        struct dma_pool *dheaders;
        wait_queue_head_t alloc_queue;
        wait_queue_head_t idle_queue;
        bool irq_on;
        bool using_mob;
        bool has_pool;
        dma_addr_t handle;
        size_t size;
        u32 num_contexts;
    }

.. _`vmw_cmdbuf_man.members`:

Members
-------

cur_mutex
    Mutex protecting the command buffer used for incremental small
    kernel command submissions, \ ``cur``\ .

space_mutex
    Mutex to protect against starvation when we allocate
    main pool buffer space.

error_mutex
    Mutex to serialize the work queue error handling.
    Note this is not needed if the same workqueue handler
    can't race with itself...

work
    A struct work_struct implementeing command buffer error handling.
    Immutable.

dev_priv
    Pointer to the device private struct. Immutable.

ctx
    Array of command buffer context queues. The queues and the context
    data is protected by \ ``lock``\ .

error
    List of command buffers that have caused device errors.
    Protected by \ ``lock``\ .

mm
    Range manager for the command buffer space. Manager allocations and
    frees are protected by \ ``lock``\ .

cmd_space
    Buffer object for the command buffer space, unless we were
    able to make a contigous coherent DMA memory allocation, \ ``handle``\ . Immutable.

map_obj
    Mapping state for \ ``cmd_space``\ . Immutable.

map
    Pointer to command buffer space. May be a mapped buffer object or
    a contigous coherent DMA memory allocation. Immutable.

cur
    Command buffer for small kernel command submissions. Protected by
    the \ ``cur_mutex``\ .

cur_pos
    Space already used in \ ``cur``\ . Protected by \ ``cur_mutex``\ .

default_size
    Default size for the \ ``cur``\  command buffer. Immutable.

max_hw_submitted
    Max number of in-flight command buffers the device can
    handle. Immutable.

lock
    Spinlock protecting command submission queues.

headers
    *undescribed*

dheaders
    Pool of DMA memory for device command buffer headers with trailing
    space for inline data. Internal protection.

alloc_queue
    Wait queue for processes waiting to allocate command buffer
    space.

idle_queue
    Wait queue for processes waiting for command buffer idle.

irq_on
    Whether the process function has requested irq to be turned on.
    Protected by \ ``lock``\ .

using_mob
    Whether the command buffer space is a MOB or a contigous DMA
    allocation. Immutable.

has_pool
    Has a large pool of DMA memory which allows larger allocations.
    Typically this is false only during bootstrap.

handle
    DMA address handle for the command buffer space if \ ``using_mob``\  is
    false. Immutable.

size
    The size of the command buffer space. Immutable.

num_contexts
    Number of contexts actually enabled.

.. _`vmw_cmdbuf_header`:

struct vmw_cmdbuf_header
========================

.. c:type:: struct vmw_cmdbuf_header

    Command buffer metadata

.. _`vmw_cmdbuf_header.definition`:

Definition
----------

.. code-block:: c

    struct vmw_cmdbuf_header {
        struct vmw_cmdbuf_man *man;
        SVGACBHeader *cb_header;
        SVGACBContext cb_context;
        struct list_head list;
        struct drm_mm_node node;
        dma_addr_t handle;
        u8 *cmd;
        size_t size;
        size_t reserved;
        bool inline_space;
    }

.. _`vmw_cmdbuf_header.members`:

Members
-------

man
    The command buffer manager.

cb_header
    Device command buffer header, allocated from a DMA pool.

cb_context
    The device command buffer context.

list
    List head for attaching to the manager lists.

node
    The range manager node.
    \ ``handle``\ . The DMA address of \ ``cb_header``\ . Handed to the device on command
    buffer submission.

handle
    *undescribed*

cmd
    Pointer to the command buffer space of this buffer.

size
    Size of the command buffer space of this buffer.

reserved
    Reserved space of this buffer.

inline_space
    Whether inline command buffer space is used.

.. _`vmw_cmdbuf_dheader`:

struct vmw_cmdbuf_dheader
=========================

.. c:type:: struct vmw_cmdbuf_dheader

    Device command buffer header with inline command buffer space.

.. _`vmw_cmdbuf_dheader.definition`:

Definition
----------

.. code-block:: c

    struct vmw_cmdbuf_dheader {
        SVGACBHeader cb_header;
        u8 cmd[VMW_CMDBUF_INLINE_SIZE] __aligned(VMW_CMDBUF_INLINE_ALIGN);
    }

.. _`vmw_cmdbuf_dheader.members`:

Members
-------

cb_header
    Device command buffer header.

cmd
    Inline command buffer space.

.. _`vmw_cmdbuf_alloc_info`:

struct vmw_cmdbuf_alloc_info
============================

.. c:type:: struct vmw_cmdbuf_alloc_info

    Command buffer space allocation metadata

.. _`vmw_cmdbuf_alloc_info.definition`:

Definition
----------

.. code-block:: c

    struct vmw_cmdbuf_alloc_info {
        size_t page_size;
        struct drm_mm_node *node;
        bool done;
    }

.. _`vmw_cmdbuf_alloc_info.members`:

Members
-------

page_size
    Size of requested command buffer space in pages.

node
    Pointer to the range manager node.

done
    True if this allocation has succeeded.

.. _`vmw_cmdbuf_cur_lock`:

vmw_cmdbuf_cur_lock
===================

.. c:function:: int vmw_cmdbuf_cur_lock(struct vmw_cmdbuf_man *man, bool interruptible)

    Helper to lock the cur_mutex.

    :param man:
        The range manager.
    :type man: struct vmw_cmdbuf_man \*

    :param interruptible:
        Whether to wait interruptible when locking.
    :type interruptible: bool

.. _`vmw_cmdbuf_cur_unlock`:

vmw_cmdbuf_cur_unlock
=====================

.. c:function:: void vmw_cmdbuf_cur_unlock(struct vmw_cmdbuf_man *man)

    Helper to unlock the cur_mutex.

    :param man:
        The range manager.
    :type man: struct vmw_cmdbuf_man \*

.. _`vmw_cmdbuf_header_inline_free`:

vmw_cmdbuf_header_inline_free
=============================

.. c:function:: void vmw_cmdbuf_header_inline_free(struct vmw_cmdbuf_header *header)

    Free a struct vmw_cmdbuf_header that has been used for the device context with inline command buffers. Need not be called locked.

    :param header:
        Pointer to the header to free.
    :type header: struct vmw_cmdbuf_header \*

.. _`__vmw_cmdbuf_header_free`:

\__vmw_cmdbuf_header_free
=========================

.. c:function:: void __vmw_cmdbuf_header_free(struct vmw_cmdbuf_header *header)

    Free a struct vmw_cmdbuf_header  and its associated structures.

    :param header:
        *undescribed*
    :type header: struct vmw_cmdbuf_header \*

.. _`__vmw_cmdbuf_header_free.header`:

header
------

Pointer to the header to free.

For internal use. Must be called with man::lock held.

.. _`vmw_cmdbuf_header_free`:

vmw_cmdbuf_header_free
======================

.. c:function:: void vmw_cmdbuf_header_free(struct vmw_cmdbuf_header *header)

    Free a struct vmw_cmdbuf_header  and its associated structures.

    :param header:
        Pointer to the header to free.
    :type header: struct vmw_cmdbuf_header \*

.. _`vmw_cmdbuf_header_submit`:

vmw_cmdbuf_header_submit
========================

.. c:function:: int vmw_cmdbuf_header_submit(struct vmw_cmdbuf_header *header)

    Submit a command buffer to hardware.

    :param header:
        The header of the buffer to submit.
    :type header: struct vmw_cmdbuf_header \*

.. _`vmw_cmdbuf_ctx_init`:

vmw_cmdbuf_ctx_init
===================

.. c:function:: void vmw_cmdbuf_ctx_init(struct vmw_cmdbuf_context *ctx)

    Initialize a command buffer context.

    :param ctx:
        The command buffer context to initialize
    :type ctx: struct vmw_cmdbuf_context \*

.. _`vmw_cmdbuf_ctx_submit`:

vmw_cmdbuf_ctx_submit
=====================

.. c:function:: void vmw_cmdbuf_ctx_submit(struct vmw_cmdbuf_man *man, struct vmw_cmdbuf_context *ctx)

    Submit command buffers from a command buffer context.

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

    :param ctx:
        The command buffer context.
    :type ctx: struct vmw_cmdbuf_context \*

.. _`vmw_cmdbuf_ctx_submit.description`:

Description
-----------

Submits command buffers to hardware until there are no more command
buffers to submit or the hardware can't handle more command buffers.

.. _`vmw_cmdbuf_ctx_process`:

vmw_cmdbuf_ctx_process
======================

.. c:function:: void vmw_cmdbuf_ctx_process(struct vmw_cmdbuf_man *man, struct vmw_cmdbuf_context *ctx, int *notempty)

    Process a command buffer context.

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

    :param ctx:
        The command buffer context.
    :type ctx: struct vmw_cmdbuf_context \*

    :param notempty:
        *undescribed*
    :type notempty: int \*

.. _`vmw_cmdbuf_ctx_process.description`:

Description
-----------

Submit command buffers to hardware if possible, and process finished
buffers. Typically freeing them, but on preemption or error take
appropriate action. Wake up waiters if appropriate.

.. _`vmw_cmdbuf_man_process`:

vmw_cmdbuf_man_process
======================

.. c:function:: void vmw_cmdbuf_man_process(struct vmw_cmdbuf_man *man)

    Process all command buffer contexts and switch on and off irqs as appropriate.

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

.. _`vmw_cmdbuf_man_process.description`:

Description
-----------

Calls \ :c:func:`vmw_cmdbuf_ctx_process`\  on all contexts. If any context has
command buffers left that are not submitted to hardware, Make sure
IRQ handling is turned on. Otherwise, make sure it's turned off.

.. _`vmw_cmdbuf_ctx_add`:

vmw_cmdbuf_ctx_add
==================

.. c:function:: void vmw_cmdbuf_ctx_add(struct vmw_cmdbuf_man *man, struct vmw_cmdbuf_header *header, SVGACBContext cb_context)

    Schedule a command buffer for submission on a command buffer context

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

    :param header:
        The header of the buffer to submit.
    :type header: struct vmw_cmdbuf_header \*

    :param cb_context:
        The command buffer context to use.
    :type cb_context: SVGACBContext

.. _`vmw_cmdbuf_ctx_add.description`:

Description
-----------

This function adds \ ``header``\  to the "submitted" queue of the command
buffer context identified by \ ``cb_context``\ . It then calls the command buffer
manager processing to potentially submit the buffer to hardware.
\ ``man->lock``\  needs to be held when calling this function.

.. _`vmw_cmdbuf_irqthread`:

vmw_cmdbuf_irqthread
====================

.. c:function:: void vmw_cmdbuf_irqthread(struct vmw_cmdbuf_man *man)

    The main part of the command buffer interrupt handler implemented as a threaded irq task.

    :param man:
        Pointer to the command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

.. _`vmw_cmdbuf_irqthread.description`:

Description
-----------

The bottom half of the interrupt handler simply calls into the
command buffer processor to free finished buffers and submit any
queued buffers to hardware.

.. _`vmw_cmdbuf_work_func`:

vmw_cmdbuf_work_func
====================

.. c:function:: void vmw_cmdbuf_work_func(struct work_struct *work)

    The deferred work function that handles command buffer errors.

    :param work:
        The work func closure argument.
    :type work: struct work_struct \*

.. _`vmw_cmdbuf_work_func.description`:

Description
-----------

Restarting the command buffer context after an error requires process
context, so it is deferred to this work function.

.. _`vmw_cmdbuf_man_idle`:

vmw_cmdbuf_man_idle
===================

.. c:function:: bool vmw_cmdbuf_man_idle(struct vmw_cmdbuf_man *man, bool check_preempted)

    Check whether the command buffer manager is idle.

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

    :param check_preempted:
        Check also the preempted queue for pending command buffers.
    :type check_preempted: bool

.. _`__vmw_cmdbuf_cur_flush`:

\__vmw_cmdbuf_cur_flush
=======================

.. c:function:: void __vmw_cmdbuf_cur_flush(struct vmw_cmdbuf_man *man)

    Flush the current command buffer for small kernel command submissions

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

.. _`__vmw_cmdbuf_cur_flush.description`:

Description
-----------

Flushes the current command buffer without allocating a new one. A new one
is automatically allocated when needed. Call with \ ``man->cur_mutex``\  held.

.. _`vmw_cmdbuf_cur_flush`:

vmw_cmdbuf_cur_flush
====================

.. c:function:: int vmw_cmdbuf_cur_flush(struct vmw_cmdbuf_man *man, bool interruptible)

    Flush the current command buffer for small kernel command submissions

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

    :param interruptible:
        Whether to sleep interruptible when sleeping.
    :type interruptible: bool

.. _`vmw_cmdbuf_cur_flush.description`:

Description
-----------

Flushes the current command buffer without allocating a new one. A new one
is automatically allocated when needed.

.. _`vmw_cmdbuf_idle`:

vmw_cmdbuf_idle
===============

.. c:function:: int vmw_cmdbuf_idle(struct vmw_cmdbuf_man *man, bool interruptible, unsigned long timeout)

    Wait for command buffer manager idle.

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

    :param interruptible:
        Sleep interruptible while waiting.
    :type interruptible: bool

    :param timeout:
        Time out after this many ticks.
    :type timeout: unsigned long

.. _`vmw_cmdbuf_idle.description`:

Description
-----------

Wait until the command buffer manager has processed all command buffers,
or until a timeout occurs. If a timeout occurs, the function will return
-EBUSY.

.. _`vmw_cmdbuf_try_alloc`:

vmw_cmdbuf_try_alloc
====================

.. c:function:: bool vmw_cmdbuf_try_alloc(struct vmw_cmdbuf_man *man, struct vmw_cmdbuf_alloc_info *info)

    Try to allocate buffer space from the main pool.

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

    :param info:
        Allocation info. Will hold the size on entry and allocated mm node
        on successful return.
    :type info: struct vmw_cmdbuf_alloc_info \*

.. _`vmw_cmdbuf_try_alloc.description`:

Description
-----------

Try to allocate buffer space from the main pool. Returns true if succeeded.
If a fatal error was hit, the error code is returned in \ ``info->ret``\ .

.. _`vmw_cmdbuf_alloc_space`:

vmw_cmdbuf_alloc_space
======================

.. c:function:: int vmw_cmdbuf_alloc_space(struct vmw_cmdbuf_man *man, struct drm_mm_node *node, size_t size, bool interruptible)

    Allocate buffer space from the main pool.

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

    :param node:
        Pointer to pre-allocated range-manager node.
    :type node: struct drm_mm_node \*

    :param size:
        The size of the allocation.
    :type size: size_t

    :param interruptible:
        Whether to sleep interruptible while waiting for space.
    :type interruptible: bool

.. _`vmw_cmdbuf_alloc_space.description`:

Description
-----------

This function allocates buffer space from the main pool, and if there is
no space available ATM, it turns on IRQ handling and sleeps waiting for it to
become available.

.. _`vmw_cmdbuf_space_pool`:

vmw_cmdbuf_space_pool
=====================

.. c:function:: int vmw_cmdbuf_space_pool(struct vmw_cmdbuf_man *man, struct vmw_cmdbuf_header *header, size_t size, bool interruptible)

    Set up a command buffer header with command buffer space from the main pool.

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

    :param header:
        Pointer to the header to set up.
    :type header: struct vmw_cmdbuf_header \*

    :param size:
        The requested size of the buffer space.
    :type size: size_t

    :param interruptible:
        Whether to sleep interruptible while waiting for space.
    :type interruptible: bool

.. _`vmw_cmdbuf_space_inline`:

vmw_cmdbuf_space_inline
=======================

.. c:function:: int vmw_cmdbuf_space_inline(struct vmw_cmdbuf_man *man, struct vmw_cmdbuf_header *header, int size)

    Set up a command buffer header with inline command buffer space.

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

    :param header:
        Pointer to the header to set up.
    :type header: struct vmw_cmdbuf_header \*

    :param size:
        The requested size of the buffer space.
    :type size: int

.. _`vmw_cmdbuf_alloc`:

vmw_cmdbuf_alloc
================

.. c:function:: void *vmw_cmdbuf_alloc(struct vmw_cmdbuf_man *man, size_t size, bool interruptible, struct vmw_cmdbuf_header **p_header)

    Allocate a command buffer header complete with command buffer space.

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

    :param size:
        The requested size of the buffer space.
    :type size: size_t

    :param interruptible:
        Whether to sleep interruptible while waiting for space.
    :type interruptible: bool

    :param p_header:
        points to a header pointer to populate on successful return.
    :type p_header: struct vmw_cmdbuf_header \*\*

.. _`vmw_cmdbuf_alloc.description`:

Description
-----------

Returns a pointer to command buffer space if successful. Otherwise
returns an error pointer. The header pointer returned in \ ``p_header``\  should
be used for upcoming calls to \ :c:func:`vmw_cmdbuf_reserve`\  and \ :c:func:`vmw_cmdbuf_commit`\ .

.. _`vmw_cmdbuf_reserve_cur`:

vmw_cmdbuf_reserve_cur
======================

.. c:function:: void *vmw_cmdbuf_reserve_cur(struct vmw_cmdbuf_man *man, size_t size, int ctx_id, bool interruptible)

    Reserve space for commands in the current command buffer.

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

    :param size:
        The requested size of the commands.
    :type size: size_t

    :param ctx_id:
        The context id if any. Otherwise set to SVGA3D_REG_INVALID.
    :type ctx_id: int

    :param interruptible:
        Whether to sleep interruptible while waiting for space.
    :type interruptible: bool

.. _`vmw_cmdbuf_reserve_cur.description`:

Description
-----------

Returns a pointer to command buffer space if successful. Otherwise
returns an error pointer.

.. _`vmw_cmdbuf_commit_cur`:

vmw_cmdbuf_commit_cur
=====================

.. c:function:: void vmw_cmdbuf_commit_cur(struct vmw_cmdbuf_man *man, size_t size, bool flush)

    Commit commands in the current command buffer.

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

    :param size:
        The size of the commands actually written.
    :type size: size_t

    :param flush:
        Whether to flush the command buffer immediately.
    :type flush: bool

.. _`vmw_cmdbuf_reserve`:

vmw_cmdbuf_reserve
==================

.. c:function:: void *vmw_cmdbuf_reserve(struct vmw_cmdbuf_man *man, size_t size, int ctx_id, bool interruptible, struct vmw_cmdbuf_header *header)

    Reserve space for commands in a command buffer.

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

    :param size:
        The requested size of the commands.
    :type size: size_t

    :param ctx_id:
        The context id if any. Otherwise set to SVGA3D_REG_INVALID.
    :type ctx_id: int

    :param interruptible:
        Whether to sleep interruptible while waiting for space.
    :type interruptible: bool

    :param header:
        Header of the command buffer. NULL if the current command buffer
        should be used.
    :type header: struct vmw_cmdbuf_header \*

.. _`vmw_cmdbuf_reserve.description`:

Description
-----------

Returns a pointer to command buffer space if successful. Otherwise
returns an error pointer.

.. _`vmw_cmdbuf_commit`:

vmw_cmdbuf_commit
=================

.. c:function:: void vmw_cmdbuf_commit(struct vmw_cmdbuf_man *man, size_t size, struct vmw_cmdbuf_header *header, bool flush)

    Commit commands in a command buffer.

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

    :param size:
        The size of the commands actually written.
    :type size: size_t

    :param header:
        Header of the command buffer. NULL if the current command buffer
        should be used.
    :type header: struct vmw_cmdbuf_header \*

    :param flush:
        Whether to flush the command buffer immediately.
    :type flush: bool

.. _`vmw_cmdbuf_send_device_command`:

vmw_cmdbuf_send_device_command
==============================

.. c:function:: int vmw_cmdbuf_send_device_command(struct vmw_cmdbuf_man *man, const void *command, size_t size)

    Send a command through the device context.

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

    :param command:
        Pointer to the command to send.
    :type command: const void \*

    :param size:
        Size of the command.
    :type size: size_t

.. _`vmw_cmdbuf_send_device_command.description`:

Description
-----------

Synchronously sends a device context command.

.. _`vmw_cmdbuf_preempt`:

vmw_cmdbuf_preempt
==================

.. c:function:: int vmw_cmdbuf_preempt(struct vmw_cmdbuf_man *man, u32 context)

    Send a preempt command through the device context.

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

    :param context:
        *undescribed*
    :type context: u32

.. _`vmw_cmdbuf_preempt.description`:

Description
-----------

Synchronously sends a preempt command.

.. _`vmw_cmdbuf_startstop`:

vmw_cmdbuf_startstop
====================

.. c:function:: int vmw_cmdbuf_startstop(struct vmw_cmdbuf_man *man, u32 context, bool enable)

    Send a start / stop command through the device context.

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

    :param context:
        *undescribed*
    :type context: u32

    :param enable:
        Whether to enable or disable the context.
    :type enable: bool

.. _`vmw_cmdbuf_startstop.description`:

Description
-----------

Synchronously sends a device start / stop context command.

.. _`vmw_cmdbuf_set_pool_size`:

vmw_cmdbuf_set_pool_size
========================

.. c:function:: int vmw_cmdbuf_set_pool_size(struct vmw_cmdbuf_man *man, size_t size, size_t default_size)

    Set command buffer manager sizes

    :param man:
        The command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

    :param size:
        The size of the main space pool.
    :type size: size_t

    :param default_size:
        The default size of the command buffer for small kernel
        submissions.
    :type default_size: size_t

.. _`vmw_cmdbuf_set_pool_size.description`:

Description
-----------

Set the size and allocate the main command buffer space pool,
as well as the default size of the command buffer for
small kernel submissions. If successful, this enables large command
submissions. Note that this function requires that rudimentary command
submission is already available and that the MOB memory manager is alive.
Returns 0 on success. Negative error code on failure.

.. _`vmw_cmdbuf_man_create`:

vmw_cmdbuf_man_create
=====================

.. c:function:: struct vmw_cmdbuf_man *vmw_cmdbuf_man_create(struct vmw_private *dev_priv)

    Create a command buffer manager and enable it for inline command buffer submissions only.

    :param dev_priv:
        Pointer to device private structure.
    :type dev_priv: struct vmw_private \*

.. _`vmw_cmdbuf_man_create.description`:

Description
-----------

Returns a pointer to a cummand buffer manager to success or error pointer
on failure. The command buffer manager will be enabled for submissions of
size VMW_CMDBUF_INLINE_SIZE only.

.. _`vmw_cmdbuf_remove_pool`:

vmw_cmdbuf_remove_pool
======================

.. c:function:: void vmw_cmdbuf_remove_pool(struct vmw_cmdbuf_man *man)

    Take down the main buffer space pool.

    :param man:
        Pointer to a command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

.. _`vmw_cmdbuf_remove_pool.description`:

Description
-----------

This function removes the main buffer space pool, and should be called
before MOB memory management is removed. When this function has been called,
only small command buffer submissions of size VMW_CMDBUF_INLINE_SIZE or
less are allowed, and the default size of the command buffer for small kernel
submissions is also set to this size.

.. _`vmw_cmdbuf_man_destroy`:

vmw_cmdbuf_man_destroy
======================

.. c:function:: void vmw_cmdbuf_man_destroy(struct vmw_cmdbuf_man *man)

    Take down a command buffer manager.

    :param man:
        Pointer to a command buffer manager.
    :type man: struct vmw_cmdbuf_man \*

.. _`vmw_cmdbuf_man_destroy.description`:

Description
-----------

This function idles and then destroys a command buffer manager.

.. This file was automatic generated / don't edit.

