.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/vsp1/vsp1_dl.c

.. _`vsp1_dl_ext_header`:

struct vsp1_dl_ext_header
=========================

.. c:type:: struct vsp1_dl_ext_header

    Extended display list header

.. _`vsp1_dl_ext_header.definition`:

Definition
----------

.. code-block:: c

    struct vsp1_dl_ext_header {
        u32 padding;
        u16 pre_ext_dl_num_cmd;
        u16 flags;
        u32 pre_ext_dl_plist;
        u32 post_ext_dl_num_cmd;
        u32 post_ext_dl_plist;
    }

.. _`vsp1_dl_ext_header.members`:

Members
-------

padding
    padding zero bytes for alignment

pre_ext_dl_num_cmd
    number of pre-extended command bodies to parse

flags
    enables or disables execution of the pre and post command

pre_ext_dl_plist
    start address of pre-extended display list bodies

post_ext_dl_num_cmd
    number of post-extended command bodies to parse

post_ext_dl_plist
    start address of post-extended display list bodies

.. _`vsp1_pre_ext_dl_body`:

struct vsp1_pre_ext_dl_body
===========================

.. c:type:: struct vsp1_pre_ext_dl_body

    Pre Extended Display List Body

.. _`vsp1_pre_ext_dl_body.definition`:

Definition
----------

.. code-block:: c

    struct vsp1_pre_ext_dl_body {
        u32 opcode;
        u32 flags;
        u32 address_set;
        u32 reserved;
    }

.. _`vsp1_pre_ext_dl_body.members`:

Members
-------

opcode
    Extended display list command operation code

flags
    Pre-extended command flags. These are specific to each command

address_set
    Source address set pointer. Must have 16-byte alignment

reserved
    Zero bits for alignment.

.. _`vsp1_dl_body`:

struct vsp1_dl_body
===================

.. c:type:: struct vsp1_dl_body

    Display list body

.. _`vsp1_dl_body.definition`:

Definition
----------

.. code-block:: c

    struct vsp1_dl_body {
        struct list_head list;
        struct list_head free;
        refcount_t refcnt;
        struct vsp1_dl_body_pool *pool;
        struct vsp1_dl_entry *entries;
        dma_addr_t dma;
        size_t size;
        unsigned int num_entries;
        unsigned int max_entries;
    }

.. _`vsp1_dl_body.members`:

Members
-------

list
    entry in the display list list of bodies

free
    entry in the pool free body list

refcnt
    reference tracking for the body

pool
    pool to which this body belongs

entries
    array of entries

dma
    DMA address of the entries

size
    size of the DMA memory in bytes

num_entries
    number of stored entries

max_entries
    number of entries available

.. _`vsp1_dl_body_pool`:

struct vsp1_dl_body_pool
========================

.. c:type:: struct vsp1_dl_body_pool

    display list body pool

.. _`vsp1_dl_body_pool.definition`:

Definition
----------

.. code-block:: c

    struct vsp1_dl_body_pool {
        dma_addr_t dma;
        size_t size;
        void *mem;
        struct vsp1_dl_body *bodies;
        struct list_head free;
        spinlock_t lock;
        struct vsp1_device *vsp1;
    }

.. _`vsp1_dl_body_pool.members`:

Members
-------

dma
    DMA address of the entries

size
    size of the full DMA memory pool in bytes

mem
    CPU memory pointer for the pool

bodies
    Array of DLB structures for the pool

free
    List of free DLB entries

lock
    Protects the free list

vsp1
    the VSP1 device

.. _`vsp1_dl_cmd_pool`:

struct vsp1_dl_cmd_pool
=======================

.. c:type:: struct vsp1_dl_cmd_pool

    Display List commands pool

.. _`vsp1_dl_cmd_pool.definition`:

Definition
----------

.. code-block:: c

    struct vsp1_dl_cmd_pool {
        dma_addr_t dma;
        size_t size;
        void *mem;
        struct vsp1_dl_ext_cmd *cmds;
        struct list_head free;
        spinlock_t lock;
        struct vsp1_device *vsp1;
    }

.. _`vsp1_dl_cmd_pool.members`:

Members
-------

dma
    DMA address of the entries

size
    size of the full DMA memory pool in bytes

mem
    CPU memory pointer for the pool

cmds
    Array of command structures for the pool

free
    Free pool entries

lock
    Protects the free list

vsp1
    the VSP1 device

.. _`vsp1_dl_list`:

struct vsp1_dl_list
===================

.. c:type:: struct vsp1_dl_list

    Display list

.. _`vsp1_dl_list.definition`:

Definition
----------

.. code-block:: c

    struct vsp1_dl_list {
        struct list_head list;
        struct vsp1_dl_manager *dlm;
        struct vsp1_dl_header *header;
        struct vsp1_dl_ext_header *extension;
        dma_addr_t dma;
        struct vsp1_dl_body *body0;
        struct list_head bodies;
        struct vsp1_dl_ext_cmd *pre_cmd;
        struct vsp1_dl_ext_cmd *post_cmd;
        bool has_chain;
        struct list_head chain;
        bool internal;
    }

.. _`vsp1_dl_list.members`:

Members
-------

list
    entry in the display list manager lists

dlm
    the display list manager

header
    display list header

extension
    extended display list header. NULL for normal lists

dma
    DMA address for the header

body0
    first display list body

bodies
    list of extra display list bodies

pre_cmd
    pre command to be issued through extended dl header

post_cmd
    post command to be issued through extended dl header

has_chain
    if true, indicates that there's a partition chain

chain
    entry in the display list partition chain

internal
    whether the display list is used for internal purpose

.. _`vsp1_dl_manager`:

struct vsp1_dl_manager
======================

.. c:type:: struct vsp1_dl_manager

    Display List manager

.. _`vsp1_dl_manager.definition`:

Definition
----------

.. code-block:: c

    struct vsp1_dl_manager {
        unsigned int index;
        bool singleshot;
        struct vsp1_device *vsp1;
        spinlock_t lock;
        struct list_head free;
        struct vsp1_dl_list *active;
        struct vsp1_dl_list *queued;
        struct vsp1_dl_list *pending;
        struct vsp1_dl_body_pool *pool;
        struct vsp1_dl_cmd_pool *cmdpool;
    }

.. _`vsp1_dl_manager.members`:

Members
-------

index
    index of the related WPF

singleshot
    execute the display list in single-shot mode

vsp1
    the VSP1 device

lock
    protects the free, active, queued, and pending lists

free
    array of all free display lists

active
    list currently being processed (loaded) by hardware

queued
    list queued to the hardware (written to the DL registers)

pending
    list waiting to be queued to the hardware

pool
    body pool for the display list bodies

cmdpool
    commands pool for extended display list

.. _`vsp1_dl_body_pool_create`:

vsp1_dl_body_pool_create
========================

.. c:function:: struct vsp1_dl_body_pool *vsp1_dl_body_pool_create(struct vsp1_device *vsp1, unsigned int num_bodies, unsigned int num_entries, size_t extra_size)

    Create a pool of bodies from a single allocation

    :param vsp1:
        The VSP1 device
    :type vsp1: struct vsp1_device \*

    :param num_bodies:
        The number of bodies to allocate
    :type num_bodies: unsigned int

    :param num_entries:
        The maximum number of entries that a body can contain
    :type num_entries: unsigned int

    :param extra_size:
        Extra allocation provided for the bodies
    :type extra_size: size_t

.. _`vsp1_dl_body_pool_create.description`:

Description
-----------

Allocate a pool of display list bodies each with enough memory to contain the
requested number of entries plus the \ ``extra_size``\ .

Return a pointer to a pool on success or NULL if memory can't be allocated.

.. _`vsp1_dl_body_pool_destroy`:

vsp1_dl_body_pool_destroy
=========================

.. c:function:: void vsp1_dl_body_pool_destroy(struct vsp1_dl_body_pool *pool)

    Release a body pool

    :param pool:
        The body pool
    :type pool: struct vsp1_dl_body_pool \*

.. _`vsp1_dl_body_pool_destroy.description`:

Description
-----------

Release all components of a pool allocation.

.. _`vsp1_dl_body_get`:

vsp1_dl_body_get
================

.. c:function:: struct vsp1_dl_body *vsp1_dl_body_get(struct vsp1_dl_body_pool *pool)

    Obtain a body from a pool

    :param pool:
        The body pool
    :type pool: struct vsp1_dl_body_pool \*

.. _`vsp1_dl_body_get.description`:

Description
-----------

Obtain a body from the pool without blocking.

Returns a display list body or NULL if there are none available.

.. _`vsp1_dl_body_put`:

vsp1_dl_body_put
================

.. c:function:: void vsp1_dl_body_put(struct vsp1_dl_body *dlb)

    Return a body back to its pool

    :param dlb:
        The display list body
    :type dlb: struct vsp1_dl_body \*

.. _`vsp1_dl_body_put.description`:

Description
-----------

Return a body back to the pool, and reset the num_entries to clear the list.

.. _`vsp1_dl_body_write`:

vsp1_dl_body_write
==================

.. c:function:: void vsp1_dl_body_write(struct vsp1_dl_body *dlb, u32 reg, u32 data)

    Write a register to a display list body

    :param dlb:
        The body
    :type dlb: struct vsp1_dl_body \*

    :param reg:
        The register address
    :type reg: u32

    :param data:
        The register value
    :type data: u32

.. _`vsp1_dl_body_write.description`:

Description
-----------

Write the given register and value to the display list body. The maximum
number of entries that can be written in a body is specified when the body is
allocated by \ :c:func:`vsp1_dl_body_alloc`\ .

.. _`vsp1_dl_cmd_pool_create`:

vsp1_dl_cmd_pool_create
=======================

.. c:function:: struct vsp1_dl_cmd_pool *vsp1_dl_cmd_pool_create(struct vsp1_device *vsp1, enum vsp1_extcmd_type type, unsigned int num_cmds)

    Create a pool of commands from a single allocation

    :param vsp1:
        The VSP1 device
    :type vsp1: struct vsp1_device \*

    :param type:
        The command pool type
    :type type: enum vsp1_extcmd_type

    :param num_cmds:
        The number of commands to allocate
    :type num_cmds: unsigned int

.. _`vsp1_dl_cmd_pool_create.description`:

Description
-----------

Allocate a pool of commands each with enough memory to contain the private
data of each command. The allocation sizes are dependent upon the command
type.

Return a pointer to the pool on success or NULL if memory can't be allocated.

.. _`vsp1_dl_list_get`:

vsp1_dl_list_get
================

.. c:function:: struct vsp1_dl_list *vsp1_dl_list_get(struct vsp1_dl_manager *dlm)

    Get a free display list

    :param dlm:
        The display list manager
    :type dlm: struct vsp1_dl_manager \*

.. _`vsp1_dl_list_get.description`:

Description
-----------

Get a display list from the pool of free lists and return it.

This function must be called without the display list manager lock held.

.. _`vsp1_dl_list_put`:

vsp1_dl_list_put
================

.. c:function:: void vsp1_dl_list_put(struct vsp1_dl_list *dl)

    Release a display list

    :param dl:
        The display list
    :type dl: struct vsp1_dl_list \*

.. _`vsp1_dl_list_put.description`:

Description
-----------

Release the display list and return it to the pool of free lists.

Passing a NULL pointer to this function is safe, in that case no operation
will be performed.

.. _`vsp1_dl_list_get_body0`:

vsp1_dl_list_get_body0
======================

.. c:function:: struct vsp1_dl_body *vsp1_dl_list_get_body0(struct vsp1_dl_list *dl)

    Obtain the default body for the display list

    :param dl:
        The display list
    :type dl: struct vsp1_dl_list \*

.. _`vsp1_dl_list_get_body0.description`:

Description
-----------

Obtain a pointer to the internal display list body allowing this to be passed
directly to configure operations.

.. _`vsp1_dl_list_add_body`:

vsp1_dl_list_add_body
=====================

.. c:function:: int vsp1_dl_list_add_body(struct vsp1_dl_list *dl, struct vsp1_dl_body *dlb)

    Add a body to the display list

    :param dl:
        The display list
    :type dl: struct vsp1_dl_list \*

    :param dlb:
        The body
    :type dlb: struct vsp1_dl_body \*

.. _`vsp1_dl_list_add_body.description`:

Description
-----------

Add a display list body to a display list. Registers contained in bodies are
processed after registers contained in the main display list, in the order in
which bodies are added.

Adding a body to a display list passes ownership of the body to the list. The
caller retains its reference to the fragment when adding it to the display
list, but is not allowed to add new entries to the body.

The reference must be explicitly released by a call to \ :c:func:`vsp1_dl_body_put`\ 
when the body isn't needed anymore.

.. _`vsp1_dl_list_add_chain`:

vsp1_dl_list_add_chain
======================

.. c:function:: int vsp1_dl_list_add_chain(struct vsp1_dl_list *head, struct vsp1_dl_list *dl)

    Add a display list to a chain

    :param head:
        The head display list
    :type head: struct vsp1_dl_list \*

    :param dl:
        The new display list
    :type dl: struct vsp1_dl_list \*

.. _`vsp1_dl_list_add_chain.description`:

Description
-----------

Add a display list to an existing display list chain. The chained lists
will be automatically processed by the hardware without intervention from
the CPU. A display list end interrupt will only complete after the last
display list in the chain has completed processing.

Adding a display list to a chain passes ownership of the display list to
the head display list item. The chain is released when the head dl item is
put back with \__vsp1_dl_list_put().

.. _`vsp1_dlm_irq_frame_end`:

vsp1_dlm_irq_frame_end
======================

.. c:function:: unsigned int vsp1_dlm_irq_frame_end(struct vsp1_dl_manager *dlm)

    Display list handler for the frame end interrupt

    :param dlm:
        the display list manager
    :type dlm: struct vsp1_dl_manager \*

.. _`vsp1_dlm_irq_frame_end.description`:

Description
-----------

Return a set of flags that indicates display list completion status.

The VSP1_DL_FRAME_END_COMPLETED flag indicates that the previous display list
has completed at frame end. If the flag is not returned display list
completion has been delayed by one frame because the display list commit
raced with the frame end interrupt. The function always returns with the flag
set in single-shot mode as display list processing is then not continuous and
races never occur.

The VSP1_DL_FRAME_END_INTERNAL flag indicates that the previous display list
has completed and had been queued with the internal notification flag.
Internal notification is only supported for continuous mode.

.. This file was automatic generated / don't edit.

