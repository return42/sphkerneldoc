.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sparc/kernel/vio.c

.. _`vio_vdev_node`:

vio_vdev_node
=============

.. c:function:: u64 vio_vdev_node(struct mdesc_handle *hp, struct vio_dev *vdev)

    Find VDEV node in MD

    :param hp:
        Handle to the MD
    :type hp: struct mdesc_handle \*

    :param vdev:
        Pointer to VDEV
    :type vdev: struct vio_dev \*

.. _`vio_vdev_node.description`:

Description
-----------

Find the node in the current MD which matches the given vio_dev. This
must be done dynamically since the node value can change if the MD
is updated.

.. _`vio_vdev_node.note`:

NOTE
----

the MD must be locked, using \ :c:func:`mdesc_grab`\ , when calling this routine

.. _`vio_vdev_node.return`:

Return
------

The VDEV node in MDESC

.. This file was automatic generated / don't edit.

