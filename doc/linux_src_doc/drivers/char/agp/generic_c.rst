.. -*- coding: utf-8; mode: rst -*-

=========
generic.c
=========


.. _`agp_free_memory`:

agp_free_memory
===============

.. c:function:: void agp_free_memory (struct agp_memory *curr)

    free memory associated with an agp_memory pointer.

    :param struct agp_memory \*curr:
        agp_memory pointer to be freed.



.. _`agp_free_memory.description`:

Description
-----------

It is the only function that can be called when the backend is not owned
by the caller.  (So it can free memory on client death.)



.. _`agp_allocate_memory`:

agp_allocate_memory
===================

.. c:function:: struct agp_memory *agp_allocate_memory (struct agp_bridge_data *bridge, size_t page_count, u32 type)

    allocate a group of pages of a certain type.

    :param struct agp_bridge_data \*bridge:

        *undescribed*

    :param size_t page_count:
        size_t argument of the number of pages

    :param u32 type:
        u32 argument of the type of memory to be allocated.



.. _`agp_allocate_memory.description`:

Description
-----------

Every agp bridge device will allow you to allocate AGP_NORMAL_MEMORY which
maps to physical ram.  Any other type is device dependent.

It returns NULL whenever memory is unavailable.



.. _`agp_copy_info`:

agp_copy_info
=============

.. c:function:: int agp_copy_info (struct agp_bridge_data *bridge, struct agp_kern_info *info)

    copy bridge state information

    :param struct agp_bridge_data \*bridge:

        *undescribed*

    :param struct agp_kern_info \*info:
        agp_kern_info pointer.  The caller should insure that this pointer is valid.



.. _`agp_copy_info.description`:

Description
-----------

This function copies information about the agp bridge device and the state of
the agp backend into an agp_kern_info pointer.



.. _`agp_bind_memory`:

agp_bind_memory
===============

.. c:function:: int agp_bind_memory (struct agp_memory *curr, off_t pg_start)

    Bind an agp_memory structure into the GATT.

    :param struct agp_memory \*curr:
        agp_memory pointer

    :param off_t pg_start:
        an offset into the graphics aperture translation table



.. _`agp_bind_memory.description`:

Description
-----------

It returns -EINVAL if the pointer == NULL.
It returns -EBUSY if the area of the table requested is already in use.



.. _`agp_unbind_memory`:

agp_unbind_memory
=================

.. c:function:: int agp_unbind_memory (struct agp_memory *curr)

    Removes an agp_memory structure from the GATT

    :param struct agp_memory \*curr:
        agp_memory pointer to be removed from the GATT.



.. _`agp_unbind_memory.description`:

Description
-----------

It returns -EINVAL if this piece of agp_memory is not currently bound to
the graphics aperture translation table or if the agp_memory pointer == NULL



.. _`agp_collect_device_status`:

agp_collect_device_status
=========================

.. c:function:: u32 agp_collect_device_status (struct agp_bridge_data *bridge, u32 requested_mode, u32 bridge_agpstat)

    determine correct agp_cmd from various agp_stat's

    :param struct agp_bridge_data \*bridge:
        an agp_bridge_data struct allocated for the AGP host bridge.

    :param u32 requested_mode:
        requested agp_stat from userspace (Typically from X)

    :param u32 bridge_agpstat:
        current agp_stat from AGP bridge.



.. _`agp_collect_device_status.description`:

Description
-----------

This function will hunt for an AGP graphics card, and try to match
the requested mode to the capabilities of both the bridge and the card.



.. _`agp_enable`:

agp_enable
==========

.. c:function:: void agp_enable (struct agp_bridge_data *bridge, u32 mode)

    initialise the agp point-to-point connection.

    :param struct agp_bridge_data \*bridge:

        *undescribed*

    :param u32 mode:
        agp mode register value to configure with.

