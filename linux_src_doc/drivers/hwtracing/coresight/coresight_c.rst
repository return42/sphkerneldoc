.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/coresight/coresight.c

.. _`coresight_node`:

struct coresight_node
=====================

.. c:type:: struct coresight_node

    elements of a path, from source to sink

.. _`coresight_node.definition`:

Definition
----------

.. code-block:: c

    struct coresight_node {
        struct coresight_device *csdev;
        struct list_head link;
    }

.. _`coresight_node.members`:

Members
-------

csdev
    Address of an element.

link
    hook to the list.

.. _`coresight_disable_source`:

coresight_disable_source
========================

.. c:function:: bool coresight_disable_source(struct coresight_device *csdev)

    Drop the reference count by 1 and disable the device if there are no users left.

    :param struct coresight_device \*csdev:
        *undescribed*

.. _`coresight_disable_source.description`:

Description
-----------

\ ``csdev``\  - The coresight device to disable

Returns true if the device has been disabled.

.. _`coresight_get_enabled_sink`:

coresight_get_enabled_sink
==========================

.. c:function:: struct coresight_device *coresight_get_enabled_sink(bool deactivate)

    returns the first enabled sink found on the bus

    :param bool deactivate:
        Whether the 'enable_sink' flag should be reset

.. _`coresight_get_enabled_sink.description`:

Description
-----------

When operated from perf the deactivate parameter should be set to 'true'.
That way the "enabled_sink" flag of the sink that was selected can be reset,
allowing for other concurrent perf sessions to choose a different sink.

When operated from sysFS users have full control and as such the deactivate
parameter should be set to 'false', hence mandating users to explicitly
clear the flag.

.. _`_coresight_build_path`:

\_coresight_build_path
======================

.. c:function:: int _coresight_build_path(struct coresight_device *csdev, struct coresight_device *sink, struct list_head *path)

    recursively build a path from a \ ``csdev``\  to a sink.

    :param struct coresight_device \*csdev:
        The device to start from.

    :param struct coresight_device \*sink:
        *undescribed*

    :param struct list_head \*path:
        The list to add devices to.

.. _`_coresight_build_path.description`:

Description
-----------

The tree of Coresight device is traversed until an activated sink is
found.  From there the sink is added to the list along with all the
devices that led to that point - the end result is a list from source
to sink. In that list the source is the first device and the sink the
last one.

.. _`coresight_release_path`:

coresight_release_path
======================

.. c:function:: void coresight_release_path(struct list_head *path)

    release a previously built path.

    :param struct list_head \*path:
        the path to release.

.. _`coresight_release_path.description`:

Description
-----------

Go through all the elements of a path and 1) removed it from the list and
2) free the memory allocated for each node.

.. _`coresight_timeout`:

coresight_timeout
=================

.. c:function:: int coresight_timeout(void __iomem *addr, u32 offset, int position, int value)

    loop until a bit has changed to a specific state.

    :param void __iomem \*addr:
        base address of the area of interest.

    :param u32 offset:
        address of a register, starting from \ ``addr``\ .

    :param int position:
        the position of the bit of interest.

    :param int value:
        the value the bit should have.

.. _`coresight_timeout.return`:

Return
------

0 as soon as the bit has taken the desired state or -EAGAIN if
TIMEOUT_US has elapsed, which ever happens first.

.. This file was automatic generated / don't edit.

