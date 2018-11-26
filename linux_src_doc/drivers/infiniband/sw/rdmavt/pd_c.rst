.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/sw/rdmavt/pd.c

.. _`rvt_alloc_pd`:

rvt_alloc_pd
============

.. c:function:: struct ib_pd *rvt_alloc_pd(struct ib_device *ibdev, struct ib_ucontext *context, struct ib_udata *udata)

    allocate a protection domain

    :param ibdev:
        ib device
    :type ibdev: struct ib_device \*

    :param context:
        optional user context
    :type context: struct ib_ucontext \*

    :param udata:
        optional user data
    :type udata: struct ib_udata \*

.. _`rvt_alloc_pd.description`:

Description
-----------

Allocate and keep track of a PD.

.. _`rvt_alloc_pd.return`:

Return
------

0 on success

.. _`rvt_dealloc_pd`:

rvt_dealloc_pd
==============

.. c:function:: int rvt_dealloc_pd(struct ib_pd *ibpd)

    Free PD

    :param ibpd:
        Free up PD
    :type ibpd: struct ib_pd \*

.. _`rvt_dealloc_pd.return`:

Return
------

always 0

.. This file was automatic generated / don't edit.

