.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/whci/pzl.c

.. _`pzl_process_qset`:

pzl_process_qset
================

.. c:function:: enum whc_update pzl_process_qset(struct whc *whc, struct whc_qset *qset)

    process any recently inactivated or halted qTDs in a qset.

    :param whc:
        *undescribed*
    :type whc: struct whc \*

    :param qset:
        *undescribed*
    :type qset: struct whc_qset \*

.. _`pzl_process_qset.description`:

Description
-----------

After inactive qTDs are removed, new qTDs can be added if the
urb queue still contains URBs.

Returns the schedule updates required.

.. _`pzl_start`:

pzl_start
=========

.. c:function:: void pzl_start(struct whc *whc)

    start the periodic schedule

    :param whc:
        the WHCI host controller
    :type whc: struct whc \*

.. _`pzl_start.description`:

Description
-----------

The PZL must be valid (e.g., all entries in the list should have
the T bit set).

.. _`pzl_stop`:

pzl_stop
========

.. c:function:: void pzl_stop(struct whc *whc)

    stop the periodic schedule

    :param whc:
        the WHCI host controller
    :type whc: struct whc \*

.. _`pzl_update`:

pzl_update
==========

.. c:function:: void pzl_update(struct whc *whc, uint32_t wusbcmd)

    request a PZL update and wait for the hardware to be synced

    :param whc:
        the WHCI HC
    :type whc: struct whc \*

    :param wusbcmd:
        WUSBCMD value to start the update.
    :type wusbcmd: uint32_t

.. _`pzl_update.description`:

Description
-----------

If the WUSB HC is inactive (i.e., the PZL is stopped) then the
update must be skipped as the hardware may not respond to update
requests.

.. _`scan_periodic_work`:

scan_periodic_work
==================

.. c:function:: void scan_periodic_work(struct work_struct *work)

    scan the PZL for qsets to process.

    :param work:
        *undescribed*
    :type work: struct work_struct \*

.. _`scan_periodic_work.description`:

Description
-----------

Process each qset in the PZL in turn and then signal the WHC that
the PZL has been updated.

Then start, stop or update the periodic schedule as required.

.. _`pzl_urb_enqueue`:

pzl_urb_enqueue
===============

.. c:function:: int pzl_urb_enqueue(struct whc *whc, struct urb *urb, gfp_t mem_flags)

    queue an URB onto the periodic list (PZL)

    :param whc:
        the WHCI host controller
    :type whc: struct whc \*

    :param urb:
        the URB to enqueue
    :type urb: struct urb \*

    :param mem_flags:
        flags for any memory allocations
    :type mem_flags: gfp_t

.. _`pzl_urb_enqueue.description`:

Description
-----------

The qset for the endpoint is obtained and the urb queued on to it.

Work is scheduled to update the hardware's view of the PZL.

.. _`pzl_urb_dequeue`:

pzl_urb_dequeue
===============

.. c:function:: int pzl_urb_dequeue(struct whc *whc, struct urb *urb, int status)

    remove an URB (qset) from the periodic list

    :param whc:
        the WHCI host controller
    :type whc: struct whc \*

    :param urb:
        the URB to dequeue
    :type urb: struct urb \*

    :param status:
        the current status of the URB
    :type status: int

.. _`pzl_urb_dequeue.description`:

Description
-----------

URBs that do yet have qTDs can simply be removed from the software
queue, otherwise the qset must be removed so the qTDs can be safely
removed.

.. _`pzl_qset_delete`:

pzl_qset_delete
===============

.. c:function:: void pzl_qset_delete(struct whc *whc, struct whc_qset *qset)

    delete a qset from the PZL

    :param whc:
        *undescribed*
    :type whc: struct whc \*

    :param qset:
        *undescribed*
    :type qset: struct whc_qset \*

.. _`pzl_init`:

pzl_init
========

.. c:function:: int pzl_init(struct whc *whc)

    initialize the periodic zone list

    :param whc:
        the WHCI host controller
    :type whc: struct whc \*

.. _`pzl_clean_up`:

pzl_clean_up
============

.. c:function:: void pzl_clean_up(struct whc *whc)

    free PZL resources

    :param whc:
        the WHCI host controller
    :type whc: struct whc \*

.. _`pzl_clean_up.description`:

Description
-----------

The PZL is stopped and empty.

.. This file was automatic generated / don't edit.

