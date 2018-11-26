.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/node.c

.. _`unregister_node`:

unregister_node
===============

.. c:function:: void unregister_node(struct node *node)

    unregister a node device

    :param node:
        node going away
    :type node: struct node \*

.. _`unregister_node.description`:

Description
-----------

Unregisters a node device \ ``node``\ .  All the devices on the node must be
unregistered before calling this function.

.. This file was automatic generated / don't edit.

