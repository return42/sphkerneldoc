.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/resolver.c

.. _`of_resolve_phandles`:

of_resolve_phandles
===================

.. c:function:: int of_resolve_phandles(struct device_node *overlay)

    Relocate and resolve overlay against live tree

    :param struct device_node \*overlay:
        Pointer to devicetree overlay to relocate and resolve

.. _`of_resolve_phandles.description`:

Description
-----------

Modify (relocate) values of local phandles in \ ``overlay``\  to a range that
does not conflict with the live expanded devicetree.  Update references
to the local phandles in \ ``overlay``\ .  Update (resolve) phandle references
in \ ``overlay``\  that refer to the live expanded devicetree.

Phandle values in the live tree are in the range of
1 .. \ :c:func:`live_tree_max_phandle`\ .  The range of phandle values in the overlay
also begin with at 1.  Adjust the phandle values in the overlay to begin
at \ :c:func:`live_tree_max_phandle`\  + 1.  Update references to the phandles to
the adjusted phandle values.

The name of each property in the "__fixups__" node in the overlay matches
the name of a symbol (a label) in the live tree.  The values of each
property in the "__fixups__" node is a list of the property values in the
overlay that need to be updated to contain the phandle reference
corresponding to that symbol in the live tree.  Update the references in
the overlay with the phandle values in the live tree.

\ ``overlay``\  must be detached.

Resolving and applying \ ``overlay``\  to the live expanded devicetree must be
protected by a mechanism to ensure that multiple overlays are processed
in a single threaded manner so that multiple overlays will not relocate
phandles to overlapping ranges.  The mechanism to enforce this is not
yet implemented.

.. _`of_resolve_phandles.return`:

Return
------

%0 on success or a negative error value on error.

.. This file was automatic generated / don't edit.

