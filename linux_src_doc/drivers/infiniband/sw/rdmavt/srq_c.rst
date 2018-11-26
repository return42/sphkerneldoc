.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/sw/rdmavt/srq.c

.. _`rvt_driver_srq_init`:

rvt_driver_srq_init
===================

.. c:function:: void rvt_driver_srq_init(struct rvt_dev_info *rdi)

    init srq resources on a per driver basis

    :param rdi:
        rvt dev structure
    :type rdi: struct rvt_dev_info \*

.. _`rvt_driver_srq_init.description`:

Description
-----------

Do any initialization needed when a driver registers with rdmavt.

.. _`rvt_create_srq`:

rvt_create_srq
==============

.. c:function:: struct ib_srq *rvt_create_srq(struct ib_pd *ibpd, struct ib_srq_init_attr *srq_init_attr, struct ib_udata *udata)

    create a shared receive queue

    :param ibpd:
        the protection domain of the SRQ to create
    :type ibpd: struct ib_pd \*

    :param srq_init_attr:
        the attributes of the SRQ
    :type srq_init_attr: struct ib_srq_init_attr \*

    :param udata:
        data from libibverbs when creating a user SRQ
    :type udata: struct ib_udata \*

.. _`rvt_create_srq.return`:

Return
------

Allocated srq object

.. _`rvt_modify_srq`:

rvt_modify_srq
==============

.. c:function:: int rvt_modify_srq(struct ib_srq *ibsrq, struct ib_srq_attr *attr, enum ib_srq_attr_mask attr_mask, struct ib_udata *udata)

    modify a shared receive queue

    :param ibsrq:
        the SRQ to modify
    :type ibsrq: struct ib_srq \*

    :param attr:
        the new attributes of the SRQ
    :type attr: struct ib_srq_attr \*

    :param attr_mask:
        indicates which attributes to modify
    :type attr_mask: enum ib_srq_attr_mask

    :param udata:
        user data for libibverbs.so
    :type udata: struct ib_udata \*

.. _`rvt_modify_srq.return`:

Return
------

0 on success

.. _`rvt_destroy_srq`:

rvt_destroy_srq
===============

.. c:function:: int rvt_destroy_srq(struct ib_srq *ibsrq)

    destory an srq

    :param ibsrq:
        srq object to destroy
    :type ibsrq: struct ib_srq \*

.. _`rvt_destroy_srq.description`:

Description
-----------

Return always 0

.. This file was automatic generated / don't edit.

