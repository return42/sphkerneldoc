.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/v4l2-core/v4l2-fwnode.c

.. _`v4l2_fwnode_endpoint_parse`:

v4l2_fwnode_endpoint_parse
==========================

.. c:function:: int v4l2_fwnode_endpoint_parse(struct fwnode_handle *fwnode, struct v4l2_fwnode_endpoint *vep)

    parse all fwnode node properties

    :param struct fwnode_handle \*fwnode:
        pointer to the endpoint's fwnode handle

    :param struct v4l2_fwnode_endpoint \*vep:
        pointer to the V4L2 fwnode data structure

.. _`v4l2_fwnode_endpoint_parse.description`:

Description
-----------

All properties are optional. If none are found, we don't set any flags. This
means the port has a static configuration and no properties have to be
specified explicitly. If any properties that identify the bus as parallel
are found and slave-mode isn't set, we set V4L2_MBUS_MASTER. Similarly, if
we recognise the bus as serial CSI-2 and clock-noncontinuous isn't set, we
set the V4L2_MBUS_CSI2_CONTINUOUS_CLOCK flag. The caller should hold a
reference to \ ``fwnode``\ .

.. _`v4l2_fwnode_endpoint_parse.note`:

NOTE
----

This function does not parse properties the size of which is variable
without a low fixed limit. Please use \ :c:func:`v4l2_fwnode_endpoint_alloc_parse`\  in
new drivers instead.

.. _`v4l2_fwnode_endpoint_parse.return`:

Return
------

0 on success or a negative error code on failure.

.. _`v4l2_fwnode_endpoint_alloc_parse`:

v4l2_fwnode_endpoint_alloc_parse
================================

.. c:function:: struct v4l2_fwnode_endpoint *v4l2_fwnode_endpoint_alloc_parse(struct fwnode_handle *fwnode)

    parse all fwnode node properties

    :param struct fwnode_handle \*fwnode:
        pointer to the endpoint's fwnode handle

.. _`v4l2_fwnode_endpoint_alloc_parse.description`:

Description
-----------

All properties are optional. If none are found, we don't set any flags. This
means the port has a static configuration and no properties have to be
specified explicitly. If any properties that identify the bus as parallel
are found and slave-mode isn't set, we set V4L2_MBUS_MASTER. Similarly, if
we recognise the bus as serial CSI-2 and clock-noncontinuous isn't set, we
set the V4L2_MBUS_CSI2_CONTINUOUS_CLOCK flag. The caller should hold a
reference to \ ``fwnode``\ .

\ :c:func:`v4l2_fwnode_endpoint_alloc_parse`\  has two important differences to
\ :c:func:`v4l2_fwnode_endpoint_parse`\ :

1. It also parses variable size data.

2. The memory it has allocated to store the variable size data must be freed
using \ :c:func:`v4l2_fwnode_endpoint_free`\  when no longer needed.

.. _`v4l2_fwnode_endpoint_alloc_parse.return`:

Return
------

Pointer to v4l2_fwnode_endpoint if successful, on an error pointer
on error.

.. _`v4l2_fwnode_parse_link`:

v4l2_fwnode_parse_link
======================

.. c:function:: int v4l2_fwnode_parse_link(struct fwnode_handle *__fwnode, struct v4l2_fwnode_link *link)

    parse a link between two endpoints

    :param struct fwnode_handle \*__fwnode:
        pointer to the endpoint's fwnode at the local end of the link

    :param struct v4l2_fwnode_link \*link:
        pointer to the V4L2 fwnode link data structure

.. _`v4l2_fwnode_parse_link.description`:

Description
-----------

Fill the link structure with the local and remote nodes and port numbers.
The local_node and remote_node fields are set to point to the local and
remote port's parent nodes respectively (the port parent node being the
parent node of the port node if that node isn't a 'ports' node, or the
grand-parent node of the port node otherwise).

A reference is taken to both the local and remote nodes, the caller must use
\ :c:func:`v4l2_fwnode_endpoint_put_link`\  to drop the references when done with the
link.

.. _`v4l2_fwnode_parse_link.return`:

Return
------

0 on success, or -ENOLINK if the remote endpoint fwnode can't be
found.

.. _`v4l2_fwnode_put_link`:

v4l2_fwnode_put_link
====================

.. c:function:: void v4l2_fwnode_put_link(struct v4l2_fwnode_link *link)

    drop references to nodes in a link

    :param struct v4l2_fwnode_link \*link:
        pointer to the V4L2 fwnode link data structure

.. _`v4l2_fwnode_put_link.description`:

Description
-----------

Drop references to the local and remote nodes in the link. This function
must be called on every link parsed with \ :c:func:`v4l2_fwnode_parse_link`\ .

.. This file was automatic generated / don't edit.

