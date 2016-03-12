.. -*- coding: utf-8; mode: rst -*-

=========
v4l2-of.c
=========



.. _xref_v4l2_of_parse_endpoint:

v4l2_of_parse_endpoint
======================

.. c:function:: int v4l2_of_parse_endpoint (const struct device_node * node, struct v4l2_of_endpoint * endpoint)

    parse all endpoint node properties

    :param const struct device_node * node:
        pointer to endpoint device_node

    :param struct v4l2_of_endpoint * endpoint:
        pointer to the V4L2 OF endpoint data structure



Description
-----------

All properties are optional. If none are found, we don't set any flags.
This means the port has a static configuration and no properties have
to be specified explicitly.
If any properties that identify the bus as parallel are found and
slave-mode isn't set, we set V4L2_MBUS_MASTER. Similarly, if we recognise
the bus as serial CSI-2 and clock-noncontinuous isn't set, we set the
V4L2_MBUS_CSI2_CONTINUOUS_CLOCK flag.
The caller should hold a reference to **node**.



NOTE
----

This function does not parse properties the size of which is
variable without a low fixed limit. Please use
:c:func:`v4l2_of_alloc_parse_endpoint` in new drivers instead.



Return
------

0.




.. _xref_v4l2_of_alloc_parse_endpoint:

v4l2_of_alloc_parse_endpoint
============================

.. c:function:: struct v4l2_of_endpoint * v4l2_of_alloc_parse_endpoint (const struct device_node * node)

    parse all endpoint node properties

    :param const struct device_node * node:
        pointer to endpoint device_node



Description
-----------

All properties are optional. If none are found, we don't set any flags.
This means the port has a static configuration and no properties have
to be specified explicitly.
If any properties that identify the bus as parallel are found and
slave-mode isn't set, we set V4L2_MBUS_MASTER. Similarly, if we recognise
the bus as serial CSI-2 and clock-noncontinuous isn't set, we set the
V4L2_MBUS_CSI2_CONTINUOUS_CLOCK flag.
The caller should hold a reference to **node**.


:c:func:`v4l2_of_alloc_parse_endpoint` has two important differences to
:c:func:`v4l2_of_parse_endpoint`:


1. It also parses variable size data and


2. The memory it has allocated to store the variable size data must
   be freed using :c:func:`v4l2_of_free_endpoint` when no longer needed.



Return
------

Pointer to v4l2_of_endpoint if successful, on error a
negative error code.




.. _xref_v4l2_of_parse_link:

v4l2_of_parse_link
==================

.. c:function:: int v4l2_of_parse_link (const struct device_node * node, struct v4l2_of_link * link)

    parse a link between two endpoints

    :param const struct device_node * node:
        pointer to the endpoint at the local end of the link

    :param struct v4l2_of_link * link:
        pointer to the V4L2 OF link data structure



Description
-----------

Fill the link structure with the local and remote nodes and port numbers.
The local_node and remote_node fields are set to point to the local and
remote port's parent nodes respectively (the port parent node being the
parent node of the port node if that node isn't a 'ports' node, or the
grand-parent node of the port node otherwise).


A reference is taken to both the local and remote nodes, the caller must use
:c:func:`v4l2_of_put_link` to drop the references when done with the link.



Return
------

0 on success, or -ENOLINK if the remote endpoint can't be found.




.. _xref_v4l2_of_put_link:

v4l2_of_put_link
================

.. c:function:: void v4l2_of_put_link (struct v4l2_of_link * link)

    drop references to nodes in a link

    :param struct v4l2_of_link * link:
        pointer to the V4L2 OF link data structure



Description
-----------

Drop references to the local and remote nodes in the link. This function must
be called on every link parsed with :c:func:`v4l2_of_parse_link`.


