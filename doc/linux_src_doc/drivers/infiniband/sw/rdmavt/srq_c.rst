.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/sw/rdmavt/srq.c

.. _`rvt_driver_srq_init`:

rvt_driver_srq_init
===================

.. c:function:: void rvt_driver_srq_init(struct rvt_dev_info *rdi)

    init srq resources on a per driver basis

    :param struct rvt_dev_info \*rdi:
        rvt dev structure

.. _`rvt_driver_srq_init.description`:

Description
-----------

Do any initialization needed when a driver registers with rdmavt.

.. _`rvt_create_srq`:

rvt_create_srq
==============

.. c:function:: struct ib_srq *rvt_create_srq(struct ib_pd *ibpd, struct ib_srq_init_attr *srq_init_attr, struct ib_udata *udata)

    create a shared receive queue

    :param struct ib_pd \*ibpd:
        the protection domain of the SRQ to create

    :param struct ib_srq_init_attr \*srq_init_attr:
        the attributes of the SRQ

    :param struct ib_udata \*udata:
        data from libibverbs when creating a user SRQ

.. _`rvt_create_srq.return`:

Return
------

Allocated srq object

.. _`rvt_modify_srq`:

rvt_modify_srq
==============

.. c:function:: int rvt_modify_srq(struct ib_srq *ibsrq, struct ib_srq_attr *attr, enum ib_srq_attr_mask attr_mask, struct ib_udata *udata)

    modify a shared receive queue

    :param struct ib_srq \*ibsrq:
        the SRQ to modify

    :param struct ib_srq_attr \*attr:
        the new attributes of the SRQ

    :param enum ib_srq_attr_mask attr_mask:
        indicates which attributes to modify

    :param struct ib_udata \*udata:
        user data for libibverbs.so

.. _`rvt_modify_srq.return`:

Return
------

0 on success

.. _`rvt_destroy_srq`:

rvt_destroy_srq
===============

.. c:function:: int rvt_destroy_srq(struct ib_srq *ibsrq)

    destory an srq

    :param struct ib_srq \*ibsrq:
        srq object to destroy

.. _`rvt_destroy_srq.description`:

Description
-----------

Return always 0

.. This file was automatic generated / don't edit.

