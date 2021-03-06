.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/fcoe/fcoe_sysfs.c

.. _`fcoe_ctlr_device_release`:

fcoe_ctlr_device_release
========================

.. c:function:: void fcoe_ctlr_device_release(struct device *dev)

    Release the FIP ctlr memory

    :param dev:
        Pointer to the FIP ctlr's embedded device
    :type dev: struct device \*

.. _`fcoe_ctlr_device_release.description`:

Description
-----------

Called when the last FIP ctlr reference is released.

.. _`fcoe_fcf_device_release`:

fcoe_fcf_device_release
=======================

.. c:function:: void fcoe_fcf_device_release(struct device *dev)

    Release the FIP fcf memory

    :param dev:
        Pointer to the fcf's embedded device
    :type dev: struct device \*

.. _`fcoe_fcf_device_release.description`:

Description
-----------

Called when the last FIP fcf reference is released.

.. _`fcoe_ctlr_device_flush_work`:

fcoe_ctlr_device_flush_work
===========================

.. c:function:: void fcoe_ctlr_device_flush_work(struct fcoe_ctlr_device *ctlr)

    Flush a FIP ctlr's workqueue

    :param ctlr:
        Pointer to the FIP ctlr whose workqueue is to be flushed
    :type ctlr: struct fcoe_ctlr_device \*

.. _`fcoe_ctlr_device_queue_work`:

fcoe_ctlr_device_queue_work
===========================

.. c:function:: int fcoe_ctlr_device_queue_work(struct fcoe_ctlr_device *ctlr, struct work_struct *work)

    Schedule work for a FIP ctlr's workqueue

    :param ctlr:
        Pointer to the FIP ctlr who owns the devloss workqueue
    :type ctlr: struct fcoe_ctlr_device \*

    :param work:
        Work to queue for execution
    :type work: struct work_struct \*

.. _`fcoe_ctlr_device_queue_work.return-value`:

Return value
------------

1 on success / 0 already queued / < 0 for error

.. _`fcoe_ctlr_device_flush_devloss`:

fcoe_ctlr_device_flush_devloss
==============================

.. c:function:: void fcoe_ctlr_device_flush_devloss(struct fcoe_ctlr_device *ctlr)

    Flush a FIP ctlr's devloss workqueue

    :param ctlr:
        Pointer to FIP ctlr whose workqueue is to be flushed
    :type ctlr: struct fcoe_ctlr_device \*

.. _`fcoe_ctlr_device_queue_devloss_work`:

fcoe_ctlr_device_queue_devloss_work
===================================

.. c:function:: int fcoe_ctlr_device_queue_devloss_work(struct fcoe_ctlr_device *ctlr, struct delayed_work *work, unsigned long delay)

    Schedule work for a FIP ctlr's devloss workqueue

    :param ctlr:
        Pointer to the FIP ctlr who owns the devloss workqueue
    :type ctlr: struct fcoe_ctlr_device \*

    :param work:
        Work to queue for execution
    :type work: struct delayed_work \*

    :param delay:
        jiffies to delay the work queuing
    :type delay: unsigned long

.. _`fcoe_ctlr_device_queue_devloss_work.return-value`:

Return value
------------

1 on success / 0 already queued / < 0 for error

.. _`fcoe_ctlr_device_add`:

fcoe_ctlr_device_add
====================

.. c:function:: struct fcoe_ctlr_device *fcoe_ctlr_device_add(struct device *parent, struct fcoe_sysfs_function_template *f, int priv_size)

    Add a FIP ctlr to sysfs

    :param parent:
        The parent device to which the fcoe_ctlr instance
        should be attached
    :type parent: struct device \*

    :param f:
        The LLD's FCoE sysfs function template pointer
    :type f: struct fcoe_sysfs_function_template \*

    :param priv_size:
        Size to be allocated with the fcoe_ctlr_device for the LLD
    :type priv_size: int

.. _`fcoe_ctlr_device_add.description`:

Description
-----------

This routine allocates a FIP ctlr object with some additional memory
for the LLD. The FIP ctlr is initialized, added to sysfs and then
attributes are added to it.

.. _`fcoe_ctlr_device_delete`:

fcoe_ctlr_device_delete
=======================

.. c:function:: void fcoe_ctlr_device_delete(struct fcoe_ctlr_device *ctlr)

    Delete a FIP ctlr and its subtree from sysfs

    :param ctlr:
        A pointer to the ctlr to be deleted
    :type ctlr: struct fcoe_ctlr_device \*

.. _`fcoe_ctlr_device_delete.description`:

Description
-----------

Deletes a FIP ctlr and any fcfs attached
to it. Deleting fcfs will cause their childen
to be deleted as well.

The ctlr is detached from sysfs and it's resources
are freed (work q), but the memory is not freed
until its last reference is released.

This routine expects no locks to be held before
calling.

.. _`fcoe_ctlr_device_delete.todo`:

TODO
----

Currently there are no callbacks to clean up LLD data
for a fcoe_fcf_device. LLDs must keep this in mind as they need
to clean up each of their LLD data for all fcoe_fcf_device before
calling fcoe_ctlr_device_delete.

.. _`fcoe_fcf_device_final_delete`:

fcoe_fcf_device_final_delete
============================

.. c:function:: void fcoe_fcf_device_final_delete(struct work_struct *work)

    Final delete routine

    :param work:
        The FIP fcf's embedded work struct
    :type work: struct work_struct \*

.. _`fcoe_fcf_device_final_delete.description`:

Description
-----------

It is expected that the fcf has been removed from
the FIP ctlr's list before calling this routine.

.. _`fip_timeout_deleted_fcf`:

fip_timeout_deleted_fcf
=======================

.. c:function:: void fip_timeout_deleted_fcf(struct work_struct *work)

    Delete a fcf when the devloss timer fires

    :param work:
        The FIP fcf's embedded work struct
    :type work: struct work_struct \*

.. _`fip_timeout_deleted_fcf.description`:

Description
-----------

Removes the fcf from the FIP ctlr's list of fcfs and
queues the final deletion.

.. _`fcoe_fcf_device_delete`:

fcoe_fcf_device_delete
======================

.. c:function:: void fcoe_fcf_device_delete(struct fcoe_fcf_device *fcf)

    Delete a FIP fcf

    :param fcf:
        Pointer to the fcf which is to be deleted
    :type fcf: struct fcoe_fcf_device \*

.. _`fcoe_fcf_device_delete.description`:

Description
-----------

Queues the FIP fcf on the devloss workqueue

Expects the ctlr_attrs mutex to be held for fcf
state change.

.. _`fcoe_fcf_device_add`:

fcoe_fcf_device_add
===================

.. c:function:: struct fcoe_fcf_device *fcoe_fcf_device_add(struct fcoe_ctlr_device *ctlr, struct fcoe_fcf_device *new_fcf)

    Add a FCoE sysfs fcoe_fcf_device to the system

    :param ctlr:
        The fcoe_ctlr_device that will be the fcoe_fcf_device parent
    :type ctlr: struct fcoe_ctlr_device \*

    :param new_fcf:
        A temporary FCF used for lookups on the current list of fcfs
    :type new_fcf: struct fcoe_fcf_device \*

.. _`fcoe_fcf_device_add.description`:

Description
-----------

Expects to be called with the ctlr->lock held

.. This file was automatic generated / don't edit.

