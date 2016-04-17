.. -*- coding: utf-8; mode: rst -*-

==========
resolver.c
==========


.. _`__of_find_node_by_full_name`:

__of_find_node_by_full_name
===========================

.. c:function:: struct device_node *__of_find_node_by_full_name (struct device_node *node, const char *full_name)

    :param struct device_node \*node:

        *undescribed*

    :param const char \*full_name:

        *undescribed*



.. _`__of_find_node_by_full_name.description`:

Description
-----------

the child node links.



.. _`of_resolve_phandles`:

of_resolve_phandles
===================

.. c:function:: int of_resolve_phandles (struct device_node *resolve)

    Resolve the given node against the live tree.

    :param struct device_node \*resolve:
        Node to resolve



.. _`of_resolve_phandles.description`:

Description
-----------

Perform dynamic Device Tree resolution against the live tree
to the given node to resolve. This depends on the live tree
having a __symbols__ node, and the resolve node the __fixups__ &
__local_fixups__ nodes (if needed).
The result of the operation is a resolve node that it's contents
are fit to be inserted or operate upon the live tree.
Returns 0 on success or a negative error value on error.

