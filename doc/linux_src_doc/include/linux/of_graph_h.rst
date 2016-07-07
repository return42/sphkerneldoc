.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/of_graph.h

.. _`of_endpoint`:

struct of_endpoint
==================

.. c:type:: struct of_endpoint

    the OF graph endpoint data structure

.. _`of_endpoint.definition`:

Definition
----------

.. code-block:: c

    struct of_endpoint {
        unsigned int port;
        unsigned int id;
        const struct device_node *local_node;
    }

.. _`of_endpoint.members`:

Members
-------

port
    identifier (value of reg property) of a port this endpoint belongs to

id
    identifier (value of reg property) of this endpoint

local_node
    pointer to device_node of this endpoint

.. _`for_each_endpoint_of_node`:

for_each_endpoint_of_node
=========================

.. c:function::  for_each_endpoint_of_node( parent,  child)

    iterate over every endpoint in a device node

    :param  parent:
        parent device node containing ports and endpoints

    :param  child:
        loop variable pointing to the current endpoint node

.. _`for_each_endpoint_of_node.description`:

Description
-----------

When breaking out of the loop, of_node_put(child) has to be called manually.

.. This file was automatic generated / don't edit.

