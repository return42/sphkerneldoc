.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/fwnode.h

.. _`fwnode_endpoint`:

struct fwnode_endpoint
======================

.. c:type:: struct fwnode_endpoint

    Fwnode graph endpoint

.. _`fwnode_endpoint.definition`:

Definition
----------

.. code-block:: c

    struct fwnode_endpoint {
        unsigned int port;
        unsigned int id;
        const struct fwnode_handle *local_fwnode;
    }

.. _`fwnode_endpoint.members`:

Members
-------

port
    Port number

id
    Endpoint id

local_fwnode
    reference to the related fwnode

.. This file was automatic generated / don't edit.

