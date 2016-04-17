.. -*- coding: utf-8; mode: rst -*-

=========
overlay.c
=========


.. _`of_overlay_info`:

struct of_overlay_info
======================

.. c:type:: of_overlay_info

    Holds a single overlay info


.. _`of_overlay_info.definition`:

Definition
----------

.. code-block:: c

  struct of_overlay_info {
    struct device_node * target;
    struct device_node * overlay;
  };


.. _`of_overlay_info.members`:

Members
-------

:``target``:
    target of the overlay operation

:``overlay``:
    pointer to the overlay contents node




.. _`of_overlay_info.description`:

Description
-----------

Holds a single overlay state, including all the overlay logs &
records.



.. _`of_overlay`:

struct of_overlay
=================

.. c:type:: of_overlay

    Holds a complete overlay transaction


.. _`of_overlay.definition`:

Definition
----------

.. code-block:: c

  struct of_overlay {
    struct list_head node;
    int count;
    struct of_overlay_info * ovinfo_tab;
    struct of_changeset cset;
  };


.. _`of_overlay.members`:

Members
-------

:``node``:
    List on which we are located

:``count``:
    Count of ovinfo structures

:``ovinfo_tab``:
    Overlay info table (count sized)

:``cset``:
    Changeset to be used




.. _`of_overlay.description`:

Description
-----------

Holds a complete overlay transaction



.. _`of_overlay_apply`:

of_overlay_apply
================

.. c:function:: int of_overlay_apply (struct of_overlay *ov)

    Apply @count overlays pointed at by @ovinfo_tab

    :param struct of_overlay \*ov:
        Overlay to apply



.. _`of_overlay_apply.description`:

Description
-----------

Applies the overlays given, while handling all error conditions
appropriately. Either the operation succeeds, or if it fails the
live tree is reverted to the state before the attempt.
Returns 0, or an error if the overlay attempt failed.



.. _`of_fill_overlay_info`:

of_fill_overlay_info
====================

.. c:function:: int of_fill_overlay_info (struct of_overlay *ov, struct device_node *info_node, struct of_overlay_info *ovinfo)

    Fill an overlay info structure @ov Overlay to fill

    :param struct of_overlay \*ov:

        *undescribed*

    :param struct device_node \*info_node:
        Device node containing the overlay

    :param struct of_overlay_info \*ovinfo:
        Pointer to the overlay info structure to fill



.. _`of_fill_overlay_info.description`:

Description
-----------

Fills an overlay info structure with the overlay information
from a device node. This device node must have a target property
which contains a phandle of the overlay target node, and an
__overlay__ child node which has the overlay contents.
Both ovinfo->target & ovinfo->overlay have their references taken.

Returns 0 on success, or a negative error value.



.. _`of_build_overlay_info`:

of_build_overlay_info
=====================

.. c:function:: int of_build_overlay_info (struct of_overlay *ov, struct device_node *tree)

    Build an overlay info array @ov Overlay to build

    :param struct of_overlay \*ov:

        *undescribed*

    :param struct device_node \*tree:
        Device node containing all the overlays



.. _`of_build_overlay_info.description`:

Description
-----------

Helper function that given a tree containing overlay information,
allocates and builds an overlay info array containing it, ready
for use using of_overlay_apply.

Returns 0 on success with the ``cntp`` ``ovinfop`` pointers valid,
while on error a negative error value is returned.



.. _`of_free_overlay_info`:

of_free_overlay_info
====================

.. c:function:: int of_free_overlay_info (struct of_overlay *ov)

    Free an overlay info array @ov Overlay to free the overlay info from

    :param struct of_overlay \*ov:

        *undescribed*



.. _`of_free_overlay_info.description`:

Description
-----------

Releases the memory of a previously allocated ovinfo array
by of_build_overlay_info.
Returns 0, or an error if the arguments are bogus.



.. _`of_overlay_create`:

of_overlay_create
=================

.. c:function:: int of_overlay_create (struct device_node *tree)

    Create and apply an overlay

    :param struct device_node \*tree:
        Device node containing all the overlays



.. _`of_overlay_create.description`:

Description
-----------

Creates and applies an overlay while also keeping track
of the overlay in a list. This list can be used to prevent
illegal overlay removals.

Returns the id of the created overlay, or a negative error number



.. _`of_overlay_destroy`:

of_overlay_destroy
==================

.. c:function:: int of_overlay_destroy (int id)

    Removes an overlay

    :param int id:
        Overlay id number returned by a previous call to of_overlay_create



.. _`of_overlay_destroy.description`:

Description
-----------

Removes an overlay if it is permissible.

Returns 0 on success, or a negative error number



.. _`of_overlay_destroy_all`:

of_overlay_destroy_all
======================

.. c:function:: int of_overlay_destroy_all ( void)

    Removes all overlays from the system

    :param void:
        no arguments



.. _`of_overlay_destroy_all.description`:

Description
-----------


Removes all overlays from the system in the correct order.

Returns 0 on success, or a negative error number

