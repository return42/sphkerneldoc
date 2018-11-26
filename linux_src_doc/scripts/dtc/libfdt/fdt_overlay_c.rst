.. -*- coding: utf-8; mode: rst -*-
.. src-file: scripts/dtc/libfdt/fdt_overlay.c

.. _`overlay_get_target_phandle`:

overlay_get_target_phandle
==========================

.. c:function:: uint32_t overlay_get_target_phandle(const void *fdto, int fragment)

    retrieves the target phandle of a fragment

    :param fdto:
        pointer to the device tree overlay blob
    :type fdto: const void \*

    :param fragment:
        node offset of the fragment in the overlay
    :type fragment: int

.. _`overlay_get_target_phandle.description`:

Description
-----------

\ :c:func:`overlay_get_target_phandle`\  retrieves the target phandle of an
overlay fragment when that fragment uses a phandle (target
property) instead of a path (target-path property).

.. _`overlay_get_target_phandle.return`:

Return
------

the phandle pointed by the target property
0, if the phandle was not found
-1, if the phandle was malformed

.. _`overlay_get_target`:

overlay_get_target
==================

.. c:function:: int overlay_get_target(const void *fdt, const void *fdto, int fragment, char const **pathp)

    retrieves the offset of a fragment's target

    :param fdt:
        Base device tree blob
    :type fdt: const void \*

    :param fdto:
        Device tree overlay blob
    :type fdto: const void \*

    :param fragment:
        node offset of the fragment in the overlay
    :type fragment: int

    :param pathp:
        pointer which receives the path of the target (or NULL)
    :type pathp: char const \*\*

.. _`overlay_get_target.description`:

Description
-----------

\ :c:func:`overlay_get_target`\  retrieves the target offset in the base
device tree of a fragment, no matter how the actual targetting is
done (through a phandle or a path)

.. _`overlay_get_target.return`:

Return
------

the targetted node offset in the base device tree
Negative error code on error

.. _`overlay_phandle_add_offset`:

overlay_phandle_add_offset
==========================

.. c:function:: int overlay_phandle_add_offset(void *fdt, int node, const char *name, uint32_t delta)

    Increases a phandle by an offset

    :param fdt:
        Base device tree blob
    :type fdt: void \*

    :param node:
        Device tree overlay blob
    :type node: int

    :param name:
        Name of the property to modify (phandle or linux,phandle)
    :type name: const char \*

    :param delta:
        offset to apply
    :type delta: uint32_t

.. _`overlay_phandle_add_offset.description`:

Description
-----------

\ :c:func:`overlay_phandle_add_offset`\  increments a node phandle by a given
offset.

.. _`overlay_phandle_add_offset.return`:

Return
------

0 on success.
Negative error code on error

.. _`overlay_adjust_node_phandles`:

overlay_adjust_node_phandles
============================

.. c:function:: int overlay_adjust_node_phandles(void *fdto, int node, uint32_t delta)

    Offsets the phandles of a node

    :param fdto:
        Device tree overlay blob
    :type fdto: void \*

    :param node:
        Offset of the node we want to adjust
    :type node: int

    :param delta:
        Offset to shift the phandles of
    :type delta: uint32_t

.. _`overlay_adjust_node_phandles.description`:

Description
-----------

\ :c:func:`overlay_adjust_node_phandles`\  adds a constant to all the phandles
of a given node. This is mainly use as part of the overlay
application process, when we want to update all the overlay
phandles to not conflict with the overlays of the base device tree.

.. _`overlay_adjust_node_phandles.return`:

Return
------

0 on success
Negative error code on failure

.. _`overlay_adjust_local_phandles`:

overlay_adjust_local_phandles
=============================

.. c:function:: int overlay_adjust_local_phandles(void *fdto, uint32_t delta)

    Adjust the phandles of a whole overlay

    :param fdto:
        Device tree overlay blob
    :type fdto: void \*

    :param delta:
        Offset to shift the phandles of
    :type delta: uint32_t

.. _`overlay_adjust_local_phandles.description`:

Description
-----------

\ :c:func:`overlay_adjust_local_phandles`\  adds a constant to all the
phandles of an overlay. This is mainly use as part of the overlay
application process, when we want to update all the overlay
phandles to not conflict with the overlays of the base device tree.

.. _`overlay_adjust_local_phandles.return`:

Return
------

0 on success
Negative error code on failure

.. _`overlay_update_local_node_references`:

overlay_update_local_node_references
====================================

.. c:function:: int overlay_update_local_node_references(void *fdto, int tree_node, int fixup_node, uint32_t delta)

    Adjust the overlay references

    :param fdto:
        Device tree overlay blob
    :type fdto: void \*

    :param tree_node:
        Node offset of the node to operate on
    :type tree_node: int

    :param fixup_node:
        Node offset of the matching local fixups node
    :type fixup_node: int

    :param delta:
        Offset to shift the phandles of
    :type delta: uint32_t

.. _`overlay_update_local_node_references.description`:

Description
-----------

\ :c:func:`overlay_update_local_nodes_references`\  update the phandles
pointing to a node within the device tree overlay by adding a
constant delta.

This is mainly used as part of a device tree application process,
where you want the device tree overlays phandles to not conflict
with the ones from the base device tree before merging them.

.. _`overlay_update_local_node_references.return`:

Return
------

0 on success
Negative error code on failure

.. _`overlay_update_local_references`:

overlay_update_local_references
===============================

.. c:function:: int overlay_update_local_references(void *fdto, uint32_t delta)

    Adjust the overlay references

    :param fdto:
        Device tree overlay blob
    :type fdto: void \*

    :param delta:
        Offset to shift the phandles of
    :type delta: uint32_t

.. _`overlay_update_local_references.description`:

Description
-----------

\ :c:func:`overlay_update_local_references`\  update all the phandles pointing
to a node within the device tree overlay by adding a constant
delta to not conflict with the base overlay.

This is mainly used as part of a device tree application process,
where you want the device tree overlays phandles to not conflict
with the ones from the base device tree before merging them.

.. _`overlay_update_local_references.return`:

Return
------

0 on success
Negative error code on failure

.. _`overlay_fixup_one_phandle`:

overlay_fixup_one_phandle
=========================

.. c:function:: int overlay_fixup_one_phandle(void *fdt, void *fdto, int symbols_off, const char *path, uint32_t path_len, const char *name, uint32_t name_len, int poffset, const char *label)

    Set an overlay phandle to the base one

    :param fdt:
        Base Device Tree blob
    :type fdt: void \*

    :param fdto:
        Device tree overlay blob
    :type fdto: void \*

    :param symbols_off:
        Node offset of the symbols node in the base device tree
    :type symbols_off: int

    :param path:
        Path to a node holding a phandle in the overlay
    :type path: const char \*

    :param path_len:
        number of path characters to consider
    :type path_len: uint32_t

    :param name:
        Name of the property holding the phandle reference in the overlay
    :type name: const char \*

    :param name_len:
        number of name characters to consider
    :type name_len: uint32_t

    :param poffset:
        Offset within the overlay property where the phandle is stored
    :type poffset: int

    :param label:
        Label of the node referenced by the phandle
    :type label: const char \*

.. _`overlay_fixup_one_phandle.description`:

Description
-----------

\ :c:func:`overlay_fixup_one_phandle`\  resolves an overlay phandle pointing to
a node in the base device tree.

This is part of the device tree overlay application process, when
you want all the phandles in the overlay to point to the actual
base dt nodes.

.. _`overlay_fixup_one_phandle.return`:

Return
------

0 on success
Negative error code on failure

.. _`overlay_fixup_phandle`:

overlay_fixup_phandle
=====================

.. c:function:: int overlay_fixup_phandle(void *fdt, void *fdto, int symbols_off, int property)

    Set an overlay phandle to the base one

    :param fdt:
        Base Device Tree blob
    :type fdt: void \*

    :param fdto:
        Device tree overlay blob
    :type fdto: void \*

    :param symbols_off:
        Node offset of the symbols node in the base device tree
    :type symbols_off: int

    :param property:
        Property offset in the overlay holding the list of fixups
    :type property: int

.. _`overlay_fixup_phandle.description`:

Description
-----------

\ :c:func:`overlay_fixup_phandle`\  resolves all the overlay phandles pointed
to in a \__fixups_\_ property, and updates them to match the phandles
in use in the base device tree.

This is part of the device tree overlay application process, when
you want all the phandles in the overlay to point to the actual
base dt nodes.

.. _`overlay_fixup_phandle.return`:

Return
------

0 on success
Negative error code on failure

.. _`overlay_fixup_phandles`:

overlay_fixup_phandles
======================

.. c:function:: int overlay_fixup_phandles(void *fdt, void *fdto)

    Resolve the overlay phandles to the base device tree

    :param fdt:
        Base Device Tree blob
    :type fdt: void \*

    :param fdto:
        Device tree overlay blob
    :type fdto: void \*

.. _`overlay_fixup_phandles.description`:

Description
-----------

\ :c:func:`overlay_fixup_phandles`\  resolves all the overlay phandles pointing
to nodes in the base device tree.

This is one of the steps of the device tree overlay application
process, when you want all the phandles in the overlay to point to
the actual base dt nodes.

.. _`overlay_fixup_phandles.return`:

Return
------

0 on success
Negative error code on failure

.. _`overlay_apply_node`:

overlay_apply_node
==================

.. c:function:: int overlay_apply_node(void *fdt, int target, void *fdto, int node)

    Merges a node into the base device tree

    :param fdt:
        Base Device Tree blob
    :type fdt: void \*

    :param target:
        Node offset in the base device tree to apply the fragment to
    :type target: int

    :param fdto:
        Device tree overlay blob
    :type fdto: void \*

    :param node:
        Node offset in the overlay holding the changes to merge
    :type node: int

.. _`overlay_apply_node.description`:

Description
-----------

\ :c:func:`overlay_apply_node`\  merges a node into a target base device tree
node pointed.

This is part of the final step in the device tree overlay
application process, when all the phandles have been adjusted and
resolved and you just have to merge overlay into the base device
tree.

.. _`overlay_apply_node.return`:

Return
------

0 on success
Negative error code on failure

.. _`overlay_merge`:

overlay_merge
=============

.. c:function:: int overlay_merge(void *fdt, void *fdto)

    Merge an overlay into its base device tree

    :param fdt:
        Base Device Tree blob
    :type fdt: void \*

    :param fdto:
        Device tree overlay blob
    :type fdto: void \*

.. _`overlay_merge.description`:

Description
-----------

\ :c:func:`overlay_merge`\  merges an overlay into its base device tree.

This is the next to last step in the device tree overlay application
process, when all the phandles have been adjusted and resolved and
you just have to merge overlay into the base device tree.

.. _`overlay_merge.return`:

Return
------

0 on success
Negative error code on failure

.. _`overlay_symbol_update`:

overlay_symbol_update
=====================

.. c:function:: int overlay_symbol_update(void *fdt, void *fdto)

    Update the symbols of base tree after a merge

    :param fdt:
        Base Device Tree blob
    :type fdt: void \*

    :param fdto:
        Device tree overlay blob
    :type fdto: void \*

.. _`overlay_symbol_update.description`:

Description
-----------

\ :c:func:`overlay_symbol_update`\  updates the symbols of the base tree with the
symbols of the applied overlay

This is the last step in the device tree overlay application
process, allowing the reference of overlay symbols by subsequent
overlay operations.

.. _`overlay_symbol_update.return`:

Return
------

0 on success
Negative error code on failure

.. This file was automatic generated / don't edit.

