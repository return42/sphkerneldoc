.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/sw/rdmavt/mcast.c

.. _`rvt_driver_mcast_init`:

rvt_driver_mcast_init
=====================

.. c:function:: void rvt_driver_mcast_init(struct rvt_dev_info *rdi)

    init resources for multicast

    :param struct rvt_dev_info \*rdi:
        rvt dev struct

.. _`rvt_driver_mcast_init.description`:

Description
-----------

This is per device that registers with rdmavt

.. _`rvt_mcast_qp_alloc`:

rvt_mcast_qp_alloc
==================

.. c:function:: struct rvt_mcast_qp *rvt_mcast_qp_alloc(struct rvt_qp *qp)

    alloc a struct to link a QP to mcast GID struct

    :param struct rvt_qp \*qp:
        the QP to link

.. _`rvt_mcast_alloc`:

rvt_mcast_alloc
===============

.. c:function:: struct rvt_mcast *rvt_mcast_alloc(union ib_gid *mgid, u16 lid)

    allocate the multicast GID structure

    :param union ib_gid \*mgid:
        the multicast GID

    :param u16 lid:
        the muilticast LID (host order)

.. _`rvt_mcast_alloc.description`:

Description
-----------

A list of QPs will be attached to this structure.

.. _`rvt_mcast_find`:

rvt_mcast_find
==============

.. c:function:: struct rvt_mcast *rvt_mcast_find(struct rvt_ibport *ibp, union ib_gid *mgid, u16 lid)

    search the global table for the given multicast GID/LID

    :param struct rvt_ibport \*ibp:
        the IB port structure

    :param union ib_gid \*mgid:
        the multicast GID to search for

    :param u16 lid:
        the multicast LID portion of the multicast address (host order)

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

    :param struct rvt_dev_info \*rdi:
        *undescribed*

    :param struct rvt_ibport \*ibp:
        *undescribed*

    :param struct rvt_mcast \*mcast:
        the mcast GID table

    :param struct rvt_mcast_qp \*mqp:
        the QP to attach

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

    :param struct ib_qp \*ibqp:
        Infiniband qp

    :param union ib_gid \*gid:
        multicast guid

    :param u16 lid:
        multicast lid

.. _`rvt_attach_mcast.return`:

Return
------

0 on success

.. _`rvt_detach_mcast`:

rvt_detach_mcast
================

.. c:function:: int rvt_detach_mcast(struct ib_qp *ibqp, union ib_gid *gid, u16 lid)

    remove a qp from a multicast group

    :param struct ib_qp \*ibqp:
        Infiniband qp

    :param union ib_gid \*gid:
        multicast guid

    :param u16 lid:
        multicast lid

.. _`rvt_detach_mcast.return`:

Return
------

0 on success

.. _`rvt_mcast_tree_empty`:

rvt_mcast_tree_empty
====================

.. c:function:: int rvt_mcast_tree_empty(struct rvt_dev_info *rdi)

    determine if any qps are attached to any mcast group \ ``rdi``\ : rvt dev struct

    :param struct rvt_dev_info \*rdi:
        *undescribed*

.. _`rvt_mcast_tree_empty.return`:

Return
------

in use count

.. This file was automatic generated / don't edit.

