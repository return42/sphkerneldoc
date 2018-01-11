.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/overlay.c

.. _`fragment`:

struct fragment
===============

.. c:type:: struct fragment

    info about fragment nodes in overlay expanded device tree

.. _`fragment.definition`:

Definition
----------

.. code-block:: c

    struct fragment {
        struct device_node *target;
        struct device_node *overlay;
    }

.. _`fragment.members`:

Members
-------

target
    target of the overlay operation

overlay
    pointer to the \__overlay_\_ node

.. _`overlay_changeset`:

struct overlay_changeset
========================

.. c:type:: struct overlay_changeset


.. _`overlay_changeset.definition`:

Definition
----------

.. code-block:: c

    struct overlay_changeset {
        int id;
        struct list_head ovcs_list;
        struct device_node *overlay_tree;
        int count;
        struct fragment *fragments;
        bool symbols_fragment;
        struct of_changeset cset;
    }

.. _`overlay_changeset.members`:

Members
-------

id
    *undescribed*

ovcs_list
    list on which we are located

overlay_tree
    expanded device tree that contains the fragment nodes

count
    count of fragment structures

fragments
    fragment nodes in the overlay expanded device tree

symbols_fragment
    last element of \ ``fragments``\ [] is the  \__symbols_\_ node

cset
    changeset to apply fragments to live device tree

.. _`add_changeset_property`:

add_changeset_property
======================

.. c:function:: int add_changeset_property(struct overlay_changeset *ovcs, struct device_node *target_node, struct property *overlay_prop, bool is_symbols_prop)

    add \ ``overlay_prop``\  to overlay changeset

    :param struct overlay_changeset \*ovcs:
        overlay changeset

    :param struct device_node \*target_node:
        where to place \ ``overlay_prop``\  in live tree

    :param struct property \*overlay_prop:
        property to add or update, from overlay tree

    :param bool is_symbols_prop:
        1 if \ ``overlay_prop``\  is from node "/__symbols__"

.. _`add_changeset_property.description`:

Description
-----------

If \ ``overlay_prop``\  does not already exist in \ ``target_node``\ , add changeset entry
to add \ ``overlay_prop``\  in \ ``target_node``\ , else add changeset entry to update
value of \ ``overlay_prop``\ .

Some special properties are not updated (no error returned).

Update of property in symbols node is not allowed.

Returns 0 on success, -ENOMEM if memory allocation failure, or -EINVAL if
invalid \ ``overlay``\ .

.. _`add_changeset_node`:

add_changeset_node
==================

.. c:function:: int add_changeset_node(struct overlay_changeset *ovcs, struct device_node *target_node, struct device_node *node)

    add \ ``node``\  (and children) to overlay changeset

    :param struct overlay_changeset \*ovcs:
        overlay changeset

    :param struct device_node \*target_node:
        where to place \ ``node``\  in live tree

    :param struct device_node \*node:
        node from within overlay device tree fragment

.. _`add_changeset_node.description`:

Description
-----------

If \ ``node``\  does not already exist in \ ``target_node``\ , add changeset entry
to add \ ``node``\  in \ ``target_node``\ .

If \ ``node``\  already exists in \ ``target_node``\ , and the existing node has
a phandle, the overlay node is not allowed to have a phandle.

If \ ``node``\  has child nodes, add the children recursively via
\ :c:func:`build_changeset_next_level`\ .

.. _`add_changeset_node.note`:

NOTE
----

Multiple mods of created nodes not supported.
If more than one fragment contains a node that does not already exist
in the live tree, then for each fragment \ :c:func:`of_changeset_attach_node`\ 
will add a changeset entry to add the node.  When the changeset is
applied, \__of_attach_node() will attach the node twice (once for
each fragment).  At this point the device tree will be corrupted.

.. _`add_changeset_node.todo`:

TODO
----

add integrity check to ensure that multiple fragments do not
create the same node.

Returns 0 on success, -ENOMEM if memory allocation failure, or -EINVAL if
invalid \ ``overlay``\ .

.. _`build_changeset_next_level`:

build_changeset_next_level
==========================

.. c:function:: int build_changeset_next_level(struct overlay_changeset *ovcs, struct device_node *target_node, const struct device_node *overlay_node)

    add level of overlay changeset

    :param struct overlay_changeset \*ovcs:
        overlay changeset

    :param struct device_node \*target_node:
        where to place \ ``overlay_node``\  in live tree

    :param const struct device_node \*overlay_node:
        node from within an overlay device tree fragment

.. _`build_changeset_next_level.description`:

Description
-----------

Add the properties (if any) and nodes (if any) from \ ``overlay_node``\  to the
\ ``ovcs``\ ->cset changeset.  If an added node has child nodes, they will
be added recursively.

Do not allow symbols node to have any children.

Returns 0 on success, -ENOMEM if memory allocation failure, or -EINVAL if
invalid \ ``overlay_node``\ .

.. _`build_changeset`:

build_changeset
===============

.. c:function:: int build_changeset(struct overlay_changeset *ovcs)

    populate overlay changeset in \ ``ovcs``\  from \ ``ovcs``\ ->fragments

    :param struct overlay_changeset \*ovcs:
        Overlay changeset

.. _`build_changeset.description`:

Description
-----------

Create changeset \ ``ovcs``\ ->cset to contain the nodes and properties of the
overlay device tree fragments in \ ``ovcs``\ ->fragments[].  If an error occurs,
any portions of the changeset that were successfully created will remain
in \ ``ovcs``\ ->cset.

Returns 0 on success, -ENOMEM if memory allocation failure, or -EINVAL if
invalid overlay in \ ``ovcs``\ ->fragments[].

.. _`init_overlay_changeset`:

init_overlay_changeset
======================

.. c:function:: int init_overlay_changeset(struct overlay_changeset *ovcs, struct device_node *tree)

    initialize overlay changeset from overlay tree \ ``ovcs``\         Overlay changeset to build

    :param struct overlay_changeset \*ovcs:
        *undescribed*

    :param struct device_node \*tree:
        Contains all the overlay fragments and overlay fixup nodes

.. _`init_overlay_changeset.description`:

Description
-----------

Initialize \ ``ovcs``\ .  Populate \ ``ovcs``\ ->fragments with node information from
the top level of \ ``tree``\ .  The relevant top level nodes are the fragment
nodes and the \__symbols_\_ node.  Any other top level node will be ignored.

Returns 0 on success, -ENOMEM if memory allocation failure, -EINVAL if error
detected in \ ``tree``\ , or -ENOSPC if \ :c:func:`idr_alloc`\  error.

.. _`of_overlay_apply`:

of_overlay_apply
================

.. c:function:: int of_overlay_apply(struct device_node *tree, int *ovcs_id)

    Create and apply an overlay changeset

    :param struct device_node \*tree:
        Expanded overlay device tree

    :param int \*ovcs_id:
        Pointer to overlay changeset id

.. _`of_overlay_apply.description`:

Description
-----------

Creates and applies an overlay changeset.

If an error occurs in a pre-apply notifier, then no changes are made
to the device tree.

A non-zero return value will not have created the changeset if error is from:
- parameter checks
- building the changeset
- overlay changeset pre-apply notifier

If an error is returned by an overlay changeset pre-apply notifier
then no further overlay changeset pre-apply notifier will be called.

A non-zero return value will have created the changeset if error is from:
- overlay changeset entry notifier
- overlay changeset post-apply notifier

If an error is returned by an overlay changeset post-apply notifier
then no further overlay changeset post-apply notifier will be called.

If more than one notifier returns an error, then the last notifier
error to occur is returned.

If an error occurred while applying the overlay changeset, then an
attempt is made to revert any changes that were made to the
device tree.  If there were any errors during the revert attempt
then the state of the device tree can not be determined, and any
following attempt to apply or remove an overlay changeset will be
refused.

Returns 0 on success, or a negative error number.  Overlay changeset
id is returned to \*ovcs_id.

.. _`of_overlay_remove`:

of_overlay_remove
=================

.. c:function:: int of_overlay_remove(int *ovcs_id)

    Revert and free an overlay changeset

    :param int \*ovcs_id:
        Pointer to overlay changeset id

.. _`of_overlay_remove.description`:

Description
-----------

Removes an overlay if it is permissible.  \ ``ovcs_id``\  was previously returned
by \ :c:func:`of_overlay_apply`\ .

If an error occurred while attempting to revert the overlay changeset,
then an attempt is made to re-apply any changeset entry that was
reverted.  If an error occurs on re-apply then the state of the device
tree can not be determined, and any following attempt to apply or remove
an overlay changeset will be refused.

A non-zero return value will not revert the changeset if error is from:
- parameter checks
- overlay changeset pre-remove notifier
- overlay changeset entry revert

If an error is returned by an overlay changeset pre-remove notifier
then no further overlay changeset pre-remove notifier will be called.

If more than one notifier returns an error, then the last notifier
error to occur is returned.

A non-zero return value will revert the changeset if error is from:
- overlay changeset entry notifier
- overlay changeset post-remove notifier

If an error is returned by an overlay changeset post-remove notifier
then no further overlay changeset post-remove notifier will be called.

Returns 0 on success, or a negative error number.  \*ovcs_id is set to
zero after reverting the changeset, even if a subsequent error occurs.

.. _`of_overlay_remove_all`:

of_overlay_remove_all
=====================

.. c:function:: int of_overlay_remove_all( void)

    Reverts and frees all overlay changesets

    :param  void:
        no arguments

.. _`of_overlay_remove_all.description`:

Description
-----------

Removes all overlays from the system in the correct order.

Returns 0 on success, or a negative error number

.. This file was automatic generated / don't edit.

