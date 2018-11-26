.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/lpfc/lpfc_debugfs.h

.. _`lpfc_debug_dump_qe`:

lpfc_debug_dump_qe
==================

.. c:function:: void lpfc_debug_dump_qe(struct lpfc_queue *q, uint32_t idx)

    dump an specific entry from a queue

    :param q:
        Pointer to the queue descriptor.
    :type q: struct lpfc_queue \*

    :param idx:
        Index to the entry on the queue.
    :type idx: uint32_t

.. _`lpfc_debug_dump_qe.description`:

Description
-----------

This function dumps an entry indexed by \ ``idx``\  from a queue specified by the
queue descriptor \ ``q``\ .

.. _`lpfc_debug_dump_q`:

lpfc_debug_dump_q
=================

.. c:function:: void lpfc_debug_dump_q(struct lpfc_queue *q)

    dump all entries from an specific queue

    :param q:
        Pointer to the queue descriptor.
    :type q: struct lpfc_queue \*

.. _`lpfc_debug_dump_q.description`:

Description
-----------

This function dumps all entries from a queue specified by the queue
descriptor \ ``q``\ .

.. _`lpfc_debug_dump_wq`:

lpfc_debug_dump_wq
==================

.. c:function:: void lpfc_debug_dump_wq(struct lpfc_hba *phba, int qtype, int wqidx)

    dump all entries from the fcp or nvme work queue

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

    :param qtype:
        *undescribed*
    :type qtype: int

    :param wqidx:
        Index to a FCP or NVME work queue.
    :type wqidx: int

.. _`lpfc_debug_dump_wq.description`:

Description
-----------

This function dumps all entries from a FCP or NVME work queue specified
by the wqidx.

.. _`lpfc_debug_dump_cq`:

lpfc_debug_dump_cq
==================

.. c:function:: void lpfc_debug_dump_cq(struct lpfc_hba *phba, int qtype, int wqidx)

    dump all entries from a fcp or nvme work queue's cmpl queue

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

    :param qtype:
        *undescribed*
    :type qtype: int

    :param wqidx:
        Index to a FCP work queue.
    :type wqidx: int

.. _`lpfc_debug_dump_cq.description`:

Description
-----------

This function dumps all entries from a FCP or NVME completion queue
which is associated to the work queue specified by the \ ``wqidx``\ .

.. _`lpfc_debug_dump_hba_eq`:

lpfc_debug_dump_hba_eq
======================

.. c:function:: void lpfc_debug_dump_hba_eq(struct lpfc_hba *phba, int qidx)

    dump all entries from a fcp work queue's evt queue

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

    :param qidx:
        *undescribed*
    :type qidx: int

.. _`lpfc_debug_dump_hba_eq.description`:

Description
-----------

This function dumps all entries from a FCP event queue which is
associated to the FCP work queue specified by the \ ``fcp_wqidx``\ .

.. _`lpfc_debug_dump_dat_rq`:

lpfc_debug_dump_dat_rq
======================

.. c:function:: void lpfc_debug_dump_dat_rq(struct lpfc_hba *phba)

    dump all entries from the receive data queue

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

.. _`lpfc_debug_dump_dat_rq.description`:

Description
-----------

This function dumps all entries from the receive data queue.

.. _`lpfc_debug_dump_hdr_rq`:

lpfc_debug_dump_hdr_rq
======================

.. c:function:: void lpfc_debug_dump_hdr_rq(struct lpfc_hba *phba)

    dump all entries from the receive header queue

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

.. _`lpfc_debug_dump_hdr_rq.description`:

Description
-----------

This function dumps all entries from the receive header queue.

.. _`lpfc_debug_dump_wq_by_id`:

lpfc_debug_dump_wq_by_id
========================

.. c:function:: void lpfc_debug_dump_wq_by_id(struct lpfc_hba *phba, int qid)

    dump all entries from a work queue by queue id

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

    :param qid:
        Work queue identifier.
    :type qid: int

.. _`lpfc_debug_dump_wq_by_id.description`:

Description
-----------

This function dumps all entries from a work queue identified by the queue
identifier.

.. _`lpfc_debug_dump_mq_by_id`:

lpfc_debug_dump_mq_by_id
========================

.. c:function:: void lpfc_debug_dump_mq_by_id(struct lpfc_hba *phba, int qid)

    dump all entries from a mbox queue by queue id

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

    :param qid:
        Mbox work queue identifier.
    :type qid: int

.. _`lpfc_debug_dump_mq_by_id.description`:

Description
-----------

This function dumps all entries from a mbox work queue identified by the
queue identifier.

.. _`lpfc_debug_dump_rq_by_id`:

lpfc_debug_dump_rq_by_id
========================

.. c:function:: void lpfc_debug_dump_rq_by_id(struct lpfc_hba *phba, int qid)

    dump all entries from a receive queue by queue id

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

    :param qid:
        Receive queue identifier.
    :type qid: int

.. _`lpfc_debug_dump_rq_by_id.description`:

Description
-----------

This function dumps all entries from a receive queue identified by the
queue identifier.

.. _`lpfc_debug_dump_cq_by_id`:

lpfc_debug_dump_cq_by_id
========================

.. c:function:: void lpfc_debug_dump_cq_by_id(struct lpfc_hba *phba, int qid)

    dump all entries from a cmpl queue by queue id

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

    :param qid:
        Complete queue identifier.
    :type qid: int

.. _`lpfc_debug_dump_cq_by_id.description`:

Description
-----------

This function dumps all entries from a complete queue identified by the
queue identifier.

.. _`lpfc_debug_dump_eq_by_id`:

lpfc_debug_dump_eq_by_id
========================

.. c:function:: void lpfc_debug_dump_eq_by_id(struct lpfc_hba *phba, int qid)

    dump all entries from an event queue by queue id

    :param phba:
        Pointer to HBA context object.
    :type phba: struct lpfc_hba \*

    :param qid:
        Complete queue identifier.
    :type qid: int

.. _`lpfc_debug_dump_eq_by_id.description`:

Description
-----------

This function dumps all entries from an event queue identified by the
queue identifier.

.. This file was automatic generated / don't edit.

