.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/pseries/of_helpers.c

.. _`pseries_of_derive_parent`:

pseries_of_derive_parent
========================

.. c:function:: struct device_node *pseries_of_derive_parent(const char *path)

    basically like dirname(1)

    :param const char \*path:
        the full_name of a node to be added to the tree

.. _`pseries_of_derive_parent.description`:

Description
-----------

Returns the node which should be the parent of the node
described by path.  E.g., for path = "/foo/bar", returns
the node with full_name = "/foo".

.. This file was automatic generated / don't edit.

