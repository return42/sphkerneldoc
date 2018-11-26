.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/whci/qset.c

.. _`qset_fill_qh`:

qset_fill_qh
============

.. c:function:: void qset_fill_qh(struct whc *whc, struct whc_qset *qset, struct urb *urb)

    fill the static endpoint state in a qset's QHead

    :param whc:
        *undescribed*
    :type whc: struct whc \*

    :param qset:
        the qset whose QH needs initializing with static endpoint
        state
    :type qset: struct whc_qset \*

    :param urb:
        an urb for a transfer to this endpoint
    :type urb: struct urb \*

.. _`qset_clear`:

qset_clear
==========

.. c:function:: void qset_clear(struct whc *whc, struct whc_qset *qset)

    clear fields in a qset so it may be reinserted into a schedule.

    :param whc:
        *undescribed*
    :type whc: struct whc \*

    :param qset:
        *undescribed*
    :type qset: struct whc_qset \*

.. _`qset_clear.description`:

Description
-----------

The sequence number and current window are not cleared (see
\ :c:func:`qset_reset`\ ).

.. _`qset_reset`:

qset_reset
==========

.. c:function:: void qset_reset(struct whc *whc, struct whc_qset *qset)

    reset endpoint state in a qset.

    :param whc:
        *undescribed*
    :type whc: struct whc \*

    :param qset:
        *undescribed*
    :type qset: struct whc_qset \*

.. _`qset_reset.description`:

Description
-----------

Clears the sequence number and current window.  This qset must not
be in the ASL or PZL.

.. _`get_qset`:

get_qset
========

.. c:function:: struct whc_qset *get_qset(struct whc *whc, struct urb *urb, gfp_t mem_flags)

    get the qset for an async endpoint

    :param whc:
        *undescribed*
    :type whc: struct whc \*

    :param urb:
        *undescribed*
    :type urb: struct urb \*

    :param mem_flags:
        *undescribed*
    :type mem_flags: gfp_t

.. _`get_qset.description`:

Description
-----------

A new qset is created if one does not already exist.

.. _`qset_add_qtds`:

qset_add_qtds
=============

.. c:function:: enum whc_update qset_add_qtds(struct whc *whc, struct whc_qset *qset)

    add qTDs for an URB to a qset

    :param whc:
        *undescribed*
    :type whc: struct whc \*

    :param qset:
        *undescribed*
    :type qset: struct whc_qset \*

.. _`qset_add_qtds.description`:

Description
-----------

Returns true if the list (ASL/PZL) must be updated because (for a
WHCI 0.95 controller) an activated qTD was pointed to be iCur.

.. _`qset_remove_qtd`:

qset_remove_qtd
===============

.. c:function:: void qset_remove_qtd(struct whc *whc, struct whc_qset *qset)

    remove the first qTD from a qset.

    :param whc:
        *undescribed*
    :type whc: struct whc \*

    :param qset:
        *undescribed*
    :type qset: struct whc_qset \*

.. _`qset_remove_qtd.description`:

Description
-----------

The qTD might be still active (if it's part of a IN URB that
resulted in a short read) so ensure it's deactivated.

.. _`qset_free_std`:

qset_free_std
=============

.. c:function:: void qset_free_std(struct whc *whc, struct whc_std *std)

    remove an sTD and free it.

    :param whc:
        the WHCI host controller
    :type whc: struct whc \*

    :param std:
        the sTD to remove and free.
    :type std: struct whc_std \*

.. _`qset_remove_qtds`:

qset_remove_qtds
================

.. c:function:: void qset_remove_qtds(struct whc *whc, struct whc_qset *qset, struct urb *urb)

    remove an URB's qTDs (and sTDs).

    :param whc:
        *undescribed*
    :type whc: struct whc \*

    :param qset:
        *undescribed*
    :type qset: struct whc_qset \*

    :param urb:
        *undescribed*
    :type urb: struct urb \*

.. _`qset_free_stds`:

qset_free_stds
==============

.. c:function:: void qset_free_stds(struct whc_qset *qset, struct urb *urb)

    free any remaining sTDs for an URB.

    :param qset:
        *undescribed*
    :type qset: struct whc_qset \*

    :param urb:
        *undescribed*
    :type urb: struct urb \*

.. _`urb_dequeue_work`:

urb_dequeue_work
================

.. c:function:: void urb_dequeue_work(struct work_struct *work)

    executes asl/pzl update and gives back the urb to the system.

    :param work:
        *undescribed*
    :type work: struct work_struct \*

.. _`qset_add_urb_sg_linearize`:

qset_add_urb_sg_linearize
=========================

.. c:function:: int qset_add_urb_sg_linearize(struct whc *whc, struct whc_qset *qset, struct urb *urb, gfp_t mem_flags)

    add an urb with sg list, copying the data

    :param whc:
        *undescribed*
    :type whc: struct whc \*

    :param qset:
        *undescribed*
    :type qset: struct whc_qset \*

    :param urb:
        *undescribed*
    :type urb: struct urb \*

    :param mem_flags:
        *undescribed*
    :type mem_flags: gfp_t

.. _`qset_add_urb_sg_linearize.description`:

Description
-----------

If the URB contains an sg list whose elements cannot be directly
mapped to qTDs then the data must be transferred via bounce
buffers.

.. _`qset_add_urb`:

qset_add_urb
============

.. c:function:: int qset_add_urb(struct whc *whc, struct whc_qset *qset, struct urb *urb, gfp_t mem_flags)

    add an urb to the qset's queue.

    :param whc:
        *undescribed*
    :type whc: struct whc \*

    :param qset:
        *undescribed*
    :type qset: struct whc_qset \*

    :param urb:
        *undescribed*
    :type urb: struct urb \*

    :param mem_flags:
        *undescribed*
    :type mem_flags: gfp_t

.. _`qset_add_urb.description`:

Description
-----------

The URB is chopped into sTDs, one for each qTD that will required.
At least one qTD (and sTD) is required even if the transfer has no
data (e.g., for some control transfers).

.. _`qset_remove_urb`:

qset_remove_urb
===============

.. c:function:: void qset_remove_urb(struct whc *whc, struct whc_qset *qset, struct urb *urb, int status)

    remove an URB from the urb queue.

    :param whc:
        *undescribed*
    :type whc: struct whc \*

    :param qset:
        *undescribed*
    :type qset: struct whc_qset \*

    :param urb:
        *undescribed*
    :type urb: struct urb \*

    :param status:
        *undescribed*
    :type status: int

.. _`qset_remove_urb.description`:

Description
-----------

The URB is returned to the USB subsystem.

.. _`get_urb_status_from_qtd`:

get_urb_status_from_qtd
=======================

.. c:function:: int get_urb_status_from_qtd(struct urb *urb, u32 status)

    get the completed urb status from qTD status

    :param urb:
        completed urb
    :type urb: struct urb \*

    :param status:
        qTD status
    :type status: u32

.. _`process_inactive_qtd`:

process_inactive_qtd
====================

.. c:function:: void process_inactive_qtd(struct whc *whc, struct whc_qset *qset, struct whc_qtd *qtd)

    process an inactive (but not halted) qTD.

    :param whc:
        *undescribed*
    :type whc: struct whc \*

    :param qset:
        *undescribed*
    :type qset: struct whc_qset \*

    :param qtd:
        *undescribed*
    :type qtd: struct whc_qtd \*

.. _`process_inactive_qtd.description`:

Description
-----------

Update the urb with the transfer bytes from the qTD, if the urb is
completely transferred or (in the case of an IN only) the LPF is
set, then the transfer is complete and the urb should be returned
to the system.

.. _`process_halted_qtd`:

process_halted_qtd
==================

.. c:function:: void process_halted_qtd(struct whc *whc, struct whc_qset *qset, struct whc_qtd *qtd)

    process a qset with a halted qtd

    :param whc:
        *undescribed*
    :type whc: struct whc \*

    :param qset:
        *undescribed*
    :type qset: struct whc_qset \*

    :param qtd:
        *undescribed*
    :type qtd: struct whc_qtd \*

.. _`process_halted_qtd.description`:

Description
-----------

Remove all the qTDs for the failed URB and return the failed URB to
the USB subsystem.  Then remove all other qTDs so the qset can be
removed.

.. _`process_halted_qtd.fixme`:

FIXME
-----

this is the point where rate adaptation can be done.  If a
transfer failed because it exceeded the maximum number of retries
then it could be reactivated with a slower rate without having to
remove the qset.

.. _`qset_delete`:

qset_delete
===========

.. c:function:: void qset_delete(struct whc *whc, struct whc_qset *qset)

    wait for a qset to be unused, then free it.

    :param whc:
        *undescribed*
    :type whc: struct whc \*

    :param qset:
        *undescribed*
    :type qset: struct whc_qset \*

.. This file was automatic generated / don't edit.

