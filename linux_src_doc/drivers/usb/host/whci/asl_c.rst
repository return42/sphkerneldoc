.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/whci/asl.c

.. _`process_qset`:

process_qset
============

.. c:function:: uint32_t process_qset(struct whc *whc, struct whc_qset *qset)

    process any recently inactivated or halted qTDs in a qset.

    :param whc:
        *undescribed*
    :type whc: struct whc \*

    :param qset:
        *undescribed*
    :type qset: struct whc_qset \*

.. _`process_qset.description`:

Description
-----------

After inactive qTDs are removed, new qTDs can be added if the
urb queue still contains URBs.

Returns any additional WUSBCMD bits for the ASL sync command (i.e.,
WUSBCMD_ASYNC_QSET_RM if a halted qset was removed).

.. _`asl_update`:

asl_update
==========

.. c:function:: void asl_update(struct whc *whc, uint32_t wusbcmd)

    request an ASL update and wait for the hardware to be synced

    :param whc:
        the WHCI HC
    :type whc: struct whc \*

    :param wusbcmd:
        WUSBCMD value to start the update.
    :type wusbcmd: uint32_t

.. _`asl_update.description`:

Description
-----------

If the WUSB HC is inactive (i.e., the ASL is stopped) then the
update must be skipped as the hardware may not respond to update
requests.

.. _`scan_async_work`:

scan_async_work
===============

.. c:function:: void scan_async_work(struct work_struct *work)

    scan the ASL for qsets to process.

    :param work:
        *undescribed*
    :type work: struct work_struct \*

.. _`scan_async_work.description`:

Description
-----------

Process each qset in the ASL in turn and then signal the WHC that
the ASL has been updated.

Then start, stop or update the asynchronous schedule as required.

.. _`asl_urb_enqueue`:

asl_urb_enqueue
===============

.. c:function:: int asl_urb_enqueue(struct whc *whc, struct urb *urb, gfp_t mem_flags)

    queue an URB onto the asynchronous list (ASL).

    :param whc:
        the WHCI host controller
    :type whc: struct whc \*

    :param urb:
        the URB to enqueue
    :type urb: struct urb \*

    :param mem_flags:
        flags for any memory allocations
    :type mem_flags: gfp_t

.. _`asl_urb_enqueue.description`:

Description
-----------

The qset for the endpoint is obtained and the urb queued on to it.

Work is scheduled to update the hardware's view of the ASL.

.. _`asl_urb_dequeue`:

asl_urb_dequeue
===============

.. c:function:: int asl_urb_dequeue(struct whc *whc, struct urb *urb, int status)

    remove an URB (qset) from the async list.

    :param whc:
        the WHCI host controller
    :type whc: struct whc \*

    :param urb:
        the URB to dequeue
    :type urb: struct urb \*

    :param status:
        the current status of the URB
    :type status: int

.. _`asl_urb_dequeue.description`:

Description
-----------

URBs that do yet have qTDs can simply be removed from the software
queue, otherwise the qset must be removed from the ASL so the qTDs
can be removed.

.. _`asl_qset_delete`:

asl_qset_delete
===============

.. c:function:: void asl_qset_delete(struct whc *whc, struct whc_qset *qset)

    delete a qset from the ASL

    :param whc:
        *undescribed*
    :type whc: struct whc \*

    :param qset:
        *undescribed*
    :type qset: struct whc_qset \*

.. _`asl_init`:

asl_init
========

.. c:function:: int asl_init(struct whc *whc)

    initialize the asynchronous schedule list

    :param whc:
        *undescribed*
    :type whc: struct whc \*

.. _`asl_init.description`:

Description
-----------

A dummy qset with no qTDs is added to the ASL to simplify removing
qsets (no need to stop the ASL when the last qset is removed).

.. _`asl_clean_up`:

asl_clean_up
============

.. c:function:: void asl_clean_up(struct whc *whc)

    free ASL resources

    :param whc:
        *undescribed*
    :type whc: struct whc \*

.. _`asl_clean_up.description`:

Description
-----------

The ASL is stopped and empty except for the dummy qset.

.. This file was automatic generated / don't edit.

