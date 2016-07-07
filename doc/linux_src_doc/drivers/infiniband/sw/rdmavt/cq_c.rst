.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/sw/rdmavt/cq.c

.. _`rvt_cq_enter`:

rvt_cq_enter
============

.. c:function:: void rvt_cq_enter(struct rvt_cq *cq, struct ib_wc *entry, bool solicited)

    add a new entry to the completion queue

    :param struct rvt_cq \*cq:
        completion queue

    :param struct ib_wc \*entry:
        work completion entry to add

    :param bool solicited:
        *undescribed*

.. _`rvt_cq_enter.description`:

Description
-----------

This may be called with qp->s_lock held.

.. _`rvt_create_cq`:

rvt_create_cq
=============

.. c:function:: struct ib_cq *rvt_create_cq(struct ib_device *ibdev, const struct ib_cq_init_attr *attr, struct ib_ucontext *context, struct ib_udata *udata)

    create a completion queue

    :param struct ib_device \*ibdev:
        the device this completion queue is attached to

    :param const struct ib_cq_init_attr \*attr:
        creation attributes

    :param struct ib_ucontext \*context:
        unused by the QLogic_IB driver

    :param struct ib_udata \*udata:
        user data for libibverbs.so

.. _`rvt_create_cq.description`:

Description
-----------

Called by \ :c:func:`ib_create_cq`\  in the generic verbs code.

.. _`rvt_create_cq.return`:

Return
------

pointer to the completion queue or negative errno values
for failure.

.. _`rvt_destroy_cq`:

rvt_destroy_cq
==============

.. c:function:: int rvt_destroy_cq(struct ib_cq *ibcq)

    destroy a completion queue

    :param struct ib_cq \*ibcq:
        the completion queue to destroy.

.. _`rvt_destroy_cq.description`:

Description
-----------

Called by \ :c:func:`ib_destroy_cq`\  in the generic verbs code.

.. _`rvt_destroy_cq.return`:

Return
------

always 0

.. _`rvt_req_notify_cq`:

rvt_req_notify_cq
=================

.. c:function:: int rvt_req_notify_cq(struct ib_cq *ibcq, enum ib_cq_notify_flags notify_flags)

    change the notification type for a completion queue

    :param struct ib_cq \*ibcq:
        the completion queue

    :param enum ib_cq_notify_flags notify_flags:
        the type of notification to request

.. _`rvt_req_notify_cq.description`:

Description
-----------

This may be called from interrupt context.  Also called by
\ :c:func:`ib_req_notify_cq`\  in the generic verbs code.

.. _`rvt_req_notify_cq.return`:

Return
------

0 for success.

.. _`rvt_resize_cq`:

rvt_resize_cq
=============

.. c:function:: int rvt_resize_cq(struct ib_cq *ibcq, int cqe, struct ib_udata *udata)

    change the size of the CQ

    :param struct ib_cq \*ibcq:
        the completion queue

    :param int cqe:
        *undescribed*

    :param struct ib_udata \*udata:
        *undescribed*

.. _`rvt_resize_cq.return`:

Return
------

0 for success.

.. _`rvt_poll_cq`:

rvt_poll_cq
===========

.. c:function:: int rvt_poll_cq(struct ib_cq *ibcq, int num_entries, struct ib_wc *entry)

    poll for work completion entries

    :param struct ib_cq \*ibcq:
        the completion queue to poll

    :param int num_entries:
        the maximum number of entries to return

    :param struct ib_wc \*entry:
        pointer to array where work completions are placed

.. _`rvt_poll_cq.description`:

Description
-----------

This may be called from interrupt context.  Also called by \ :c:func:`ib_poll_cq`\ 
in the generic verbs code.

.. _`rvt_poll_cq.return`:

Return
------

the number of completion entries polled.

.. _`rvt_driver_cq_init`:

rvt_driver_cq_init
==================

.. c:function:: int rvt_driver_cq_init(struct rvt_dev_info *rdi)

    Init cq resources on behalf of driver

    :param struct rvt_dev_info \*rdi:
        rvt dev structure

.. _`rvt_driver_cq_init.return`:

Return
------

0 on success

.. _`rvt_cq_exit`:

rvt_cq_exit
===========

.. c:function:: void rvt_cq_exit(struct rvt_dev_info *rdi)

    tear down cq reources

    :param struct rvt_dev_info \*rdi:
        rvt dev structure

.. This file was automatic generated / don't edit.

