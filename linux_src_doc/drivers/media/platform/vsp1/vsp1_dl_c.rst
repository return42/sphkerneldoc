.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/vsp1/vsp1_dl.c

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
        struct vsp1_device *vsp1;
        struct vsp1_dl_entry *entries;
        dma_addr_t dma;
        size_t size;
        unsigned int num_entries;
    }

.. _`vsp1_dl_body.members`:

Members
-------

list
    entry in the display list list of bodies

vsp1
    the VSP1 device

entries
    array of entries

dma
    DMA address of the entries

size
    size of the DMA memory in bytes

num_entries
    number of stored entries

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
        dma_addr_t dma;
        struct vsp1_dl_body body0;
        struct list_head fragments;
    }

.. _`vsp1_dl_list.members`:

Members
-------

list
    entry in the display list manager lists

dlm
    the display list manager

header
    display list header, NULL for headerless lists

dma
    DMA address for the header

body0
    first display list body

fragments
    list of extra display list bodies

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
        enum vsp1_dl_mode mode;
        struct vsp1_device *vsp1;
        spinlock_t lock;
        struct list_head free;
        struct vsp1_dl_list *active;
        struct vsp1_dl_list *queued;
        struct vsp1_dl_list *pending;
    }

.. _`vsp1_dl_manager.members`:

Members
-------

index
    index of the related WPF

mode
    display list operation mode (header or headerless)

vsp1
    the VSP1 device

lock
    protects the active, queued and pending lists

free
    array of all free display lists

active
    list currently being processed (loaded) by hardware

queued
    list queued to the hardware (written to the DL registers)

pending
    list waiting to be queued to the hardware

.. _`vsp1_dl_fragment_alloc`:

vsp1_dl_fragment_alloc
======================

.. c:function:: struct vsp1_dl_body *vsp1_dl_fragment_alloc(struct vsp1_device *vsp1, unsigned int num_entries)

    Allocate a display list fragment

    :param struct vsp1_device \*vsp1:
        The VSP1 device

    :param unsigned int num_entries:
        The maximum number of entries that the fragment can contain

.. _`vsp1_dl_fragment_alloc.description`:

Description
-----------

Allocate a display list fragment with enough memory to contain the requested
number of entries.

Return a pointer to a fragment on success or NULL if memory can't be
allocated.

.. _`vsp1_dl_fragment_free`:

vsp1_dl_fragment_free
=====================

.. c:function:: void vsp1_dl_fragment_free(struct vsp1_dl_body *dlb)

    Free a display list fragment

    :param struct vsp1_dl_body \*dlb:
        The fragment

.. _`vsp1_dl_fragment_free.description`:

Description
-----------

Free the given display list fragment and the associated DMA memory.

Fragments must only be freed explicitly if they are not added to a display
list, as the display list will take ownership of them and free them
otherwise. Manual free typically happens at cleanup time for fragments that
have been allocated but not used.

Passing a NULL pointer to this function is safe, in that case no operation
will be performed.

.. _`vsp1_dl_fragment_write`:

vsp1_dl_fragment_write
======================

.. c:function:: void vsp1_dl_fragment_write(struct vsp1_dl_body *dlb, u32 reg, u32 data)

    Write a register to a display list fragment

    :param struct vsp1_dl_body \*dlb:
        The fragment

    :param u32 reg:
        The register address

    :param u32 data:
        The register value

.. _`vsp1_dl_fragment_write.description`:

Description
-----------

Write the given register and value to the display list fragment. The maximum
number of entries that can be written in a fragment is specified when the
fragment is allocated by \ :c:func:`vsp1_dl_fragment_alloc`\ .

.. _`vsp1_dl_list_get`:

vsp1_dl_list_get
================

.. c:function:: struct vsp1_dl_list *vsp1_dl_list_get(struct vsp1_dl_manager *dlm)

    Get a free display list

    :param struct vsp1_dl_manager \*dlm:
        The display list manager

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

    :param struct vsp1_dl_list \*dl:
        The display list

.. _`vsp1_dl_list_put.description`:

Description
-----------

Release the display list and return it to the pool of free lists.

Passing a NULL pointer to this function is safe, in that case no operation
will be performed.

.. _`vsp1_dl_list_write`:

vsp1_dl_list_write
==================

.. c:function:: void vsp1_dl_list_write(struct vsp1_dl_list *dl, u32 reg, u32 data)

    Write a register to the display list

    :param struct vsp1_dl_list \*dl:
        The display list

    :param u32 reg:
        The register address

    :param u32 data:
        The register value

.. _`vsp1_dl_list_write.description`:

Description
-----------

Write the given register and value to the display list. Up to 256 registers
can be written per display list.

.. _`vsp1_dl_list_add_fragment`:

vsp1_dl_list_add_fragment
=========================

.. c:function:: int vsp1_dl_list_add_fragment(struct vsp1_dl_list *dl, struct vsp1_dl_body *dlb)

    Add a fragment to the display list

    :param struct vsp1_dl_list \*dl:
        The display list

    :param struct vsp1_dl_body \*dlb:
        The fragment

.. _`vsp1_dl_list_add_fragment.description`:

Description
-----------

Add a display list body as a fragment to a display list. Registers contained
in fragments are processed after registers contained in the main display
list, in the order in which fragments are added.

Adding a fragment to a display list passes ownership of the fragment to the
list. The caller must not touch the fragment after this call, and must not
free it explicitly with \ :c:func:`vsp1_dl_fragment_free`\ .

Fragments are only usable for display lists in header mode. Attempt to
add a fragment to a header-less display list will return an error.

.. This file was automatic generated / don't edit.
