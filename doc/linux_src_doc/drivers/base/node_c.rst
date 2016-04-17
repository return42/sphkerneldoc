.. -*- coding: utf-8; mode: rst -*-

======
node.c
======


.. _`unregister_node`:

unregister_node
===============

.. c:function:: void unregister_node (struct node *node)

    unregister a node device

    :param struct node \*node:
        node going away



.. _`unregister_node.description`:

Description
-----------

Unregisters a node device ``node``\ .  All the devices on the node must be
unregistered before calling this function.

