.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/unittest.c

.. _`update_node_properties`:

update_node_properties
======================

.. c:function:: void update_node_properties(struct device_node *np, struct device_node *dup)

    adds the properties of np into dup node (present in live tree) and updates parent of children of np to dup.

    :param np:
        node already present in live tree
    :type np: struct device_node \*

    :param dup:
        node present in live tree to be updated
    :type dup: struct device_node \*

.. _`attach_node_and_children`:

attach_node_and_children
========================

.. c:function:: int attach_node_and_children(struct device_node *np)

    attaches nodes and its children to live tree

    :param np:
        Node to attach to live tree
    :type np: struct device_node \*

.. _`unittest_data_add`:

unittest_data_add
=================

.. c:function:: int unittest_data_add( void)

    Reads, copies data from linked tree and attaches it to the live tree

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

