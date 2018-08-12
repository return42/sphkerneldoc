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

.. _`fwnode_reference_args`:

struct fwnode_reference_args
============================

.. c:type:: struct fwnode_reference_args

    Fwnode reference with additional arguments

.. _`fwnode_reference_args.definition`:

Definition
----------

.. code-block:: c

    struct fwnode_reference_args {
        struct fwnode_handle *fwnode;
        unsigned int nargs;
        unsigned int args[NR_FWNODE_REFERENCE_ARGS];
    }

.. _`fwnode_reference_args.members`:

Members
-------

fwnode
    - A reference to the base fwnode

nargs
    Number of elements in \ ``args``\  array

args
    Integer arguments on the fwnode

.. _`fwnode_operations`:

struct fwnode_operations
========================

.. c:type:: struct fwnode_operations

    Operations for fwnode interface

.. _`fwnode_operations.definition`:

Definition
----------

.. code-block:: c

    struct fwnode_operations {
        struct fwnode_handle *(*get)(struct fwnode_handle *fwnode);
        void (*put)(struct fwnode_handle *fwnode);
        bool (*device_is_available)(const struct fwnode_handle *fwnode);
        const void *(*device_get_match_data)(const struct fwnode_handle *fwnode, const struct device *dev);
        bool (*property_present)(const struct fwnode_handle *fwnode, const char *propname);
        int (*property_read_int_array)(const struct fwnode_handle *fwnode,const char *propname,unsigned int elem_size, void *val, size_t nval);
        int(*property_read_string_array)(const struct fwnode_handle *fwnode_handle,const char *propname, const char **val, size_t nval);
        struct fwnode_handle *(*get_parent)(const struct fwnode_handle *fwnode);
        struct fwnode_handle *(*get_next_child_node)(const struct fwnode_handle *fwnode, struct fwnode_handle *child);
        struct fwnode_handle *(*get_named_child_node)(const struct fwnode_handle *fwnode, const char *name);
        int (*get_reference_args)(const struct fwnode_handle *fwnode,const char *prop, const char *nargs_prop,unsigned int nargs, unsigned int index, struct fwnode_reference_args *args);
        struct fwnode_handle *(*graph_get_next_endpoint)(const struct fwnode_handle *fwnode, struct fwnode_handle *prev);
        struct fwnode_handle * (*graph_get_remote_endpoint)(const struct fwnode_handle *fwnode);
        struct fwnode_handle * (*graph_get_port_parent)(struct fwnode_handle *fwnode);
        int (*graph_parse_endpoint)(const struct fwnode_handle *fwnode, struct fwnode_endpoint *endpoint);
    }

.. _`fwnode_operations.members`:

Members
-------

get
    Get a reference to an fwnode.

put
    Put a reference to an fwnode.

device_is_available
    *undescribed*

device_get_match_data
    Return the device driver match data.

property_present
    Return true if a property is present.

property_read_int_array
    *undescribed*

property_read_string_array
    Read an array of string properties. Return zero
    on success, a negative error code otherwise.

get_parent
    Return the parent of an fwnode.

get_next_child_node
    Return the next child node in an iteration.

get_named_child_node
    Return a child node with a given name.

get_reference_args
    Return a reference pointed to by a property, with args

graph_get_next_endpoint
    Return an endpoint node in an iteration.

graph_get_remote_endpoint
    Return the remote endpoint node of a local
    endpoint node.

graph_get_port_parent
    Return the parent node of a port node.

graph_parse_endpoint
    Parse endpoint for port and endpoint id.

.. This file was automatic generated / don't edit.

