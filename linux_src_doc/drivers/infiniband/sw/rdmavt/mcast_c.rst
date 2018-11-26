.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/sw/rdmavt/mcast.c

.. _`rvt_driver_mcast_init`:

rvt_driver_mcast_init
=====================

.. c:function:: void rvt_driver_mcast_init(struct rvt_dev_info *rdi)

    init resources for multicast

    :param rdi:
        rvt dev struct
    :type rdi: struct rvt_dev_info \*

.. _`rvt_driver_mcast_init.description`:

Description
-----------

This is per device that registers with rdmavt

.. _`rvt_mcast_qp_alloc`:

rvt_mcast_qp_alloc
==================

.. c:function:: struct rvt_mcast_qp *rvt_mcast_qp_alloc(struct rvt_qp *qp)

    alloc a struct to link a QP to mcast GID struct

    :param qp:
        the QP to link
    :type qp: struct rvt_qp \*

.. _`rvt_mcast_alloc`:

rvt_mcast_alloc
===============

.. c:function:: struct rvt_mcast *rvt_mcast_alloc(union ib_gid *mgid, u16 lid)

    allocate the multicast GID structure

    :param mgid:
        the multicast GID
    :type mgid: union ib_gid \*

    :param lid:
        the muilticast LID (host order)
    :type lid: u16

.. _`rvt_mcast_alloc.description`:

Description
-----------

A list of QPs will be attached to this structure.

.. _`rvt_mcast_find`:

rvt_mcast_find
==============

.. c:function:: struct rvt_mcast *rvt_mcast_find(struct rvt_ibport *ibp, union ib_gid *mgid, u16 lid)

    search the global table for the given multicast GID/LID

    :param ibp:
        the IB port structure
    :type ibp: struct rvt_ibport \*

    :param mgid:
        the multicast GID to search for
    :type mgid: union ib_gid \*

    :param lid:
        the multicast LID portion of the multicast address (host order)
    :type lid: u16

.. _`rvt_mcast_find.note`:

NOTE
----

It is valid to have 1 MLID with multiple MGIDs.  It is not valid
to have 1 MGID with multiple MLIDs.

.. _`rvt_mcast_find.description`:

Description
-----------

The caller is responsible for decrementing the reference count if found.

.. _`rvt_mcast_find.return`:

Return
------

NULL if not found.

.. _`rvt_mcast_add`:

rvt_mcast_add
=============

.. c:function:: int rvt_mcast_add(struct rvt_dev_info *rdi, struct rvt_ibport *ibp, struct rvt_mcast *mcast, struct rvt_mcast_qp *mqp)

    insert mcast GID into table and attach QP struct

    :param rdi:
        *undescribed*
    :type rdi: struct rvt_dev_info \*

    :param ibp:
        *undescribed*
    :type ibp: struct rvt_ibport \*

    :param mcast:
        the mcast GID table
    :type mcast: struct rvt_mcast \*

    :param mqp:
        the QP to attach
    :type mqp: struct rvt_mcast_qp \*

.. _`rvt_mcast_add.return`:

Return
------

zero if both were added.  Return EEXIST if the GID was already in
the table but the QP was added.  Return ESRCH if the QP was already
attached and neither structure was added. Return EINVAL if the MGID was
found, but the MLID did NOT match.

.. _`rvt_attach_mcast`:

rvt_attach_mcast
================

.. c:function:: int rvt_attach_mcast(struct ib_qp *ibqp, union ib_gid *gid, u16 lid)

    attach a qp to a multicast group

    :param ibqp:
        Infiniband qp
    :type ibqp: struct ib_qp \*

    :param gid:
        multicast guid
    :type gid: union ib_gid \*

    :param lid:
        multicast lid
    :type lid: u16

.. _`rvt_attach_mcast.return`:

Return
------

0 on success

.. _`rvt_detach_mcast`:

rvt_detach_mcast
================

.. c:function:: int rvt_detach_mcast(struct ib_qp *ibqp, union ib_gid *gid, u16 lid)

    remove a qp from a multicast group

    :param ibqp:
        Infiniband qp
    :type ibqp: struct ib_qp \*

    :param gid:
        multicast guid
    :type gid: union ib_gid \*

    :param lid:
        multicast lid
    :type lid: u16

.. _`rvt_detach_mcast.return`:

Return
------

0 on success

.. _`rvt_mcast_tree_empty`:

rvt_mcast_tree_empty
====================

.. c:function:: int rvt_mcast_tree_empty(struct rvt_dev_info *rdi)

    determine if any qps are attached to any mcast group \ ``rdi``\ : rvt dev struct

    :param rdi:
        *undescribed*
    :type rdi: struct rvt_dev_info \*

.. _`rvt_mcast_tree_empty.return`:

Return
------

in use count

.. This file was automatic generated / don't edit.

