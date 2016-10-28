.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/lpfc/lpfc_debugfs.h

.. _`lpfc_debug_dump_qe`:

lpfc_debug_dump_qe
==================

.. c:function:: void lpfc_debug_dump_qe(struct lpfc_queue *q, uint32_t idx)

    dump an specific entry from a queue

    :param struct lpfc_queue \*q:
        Pointer to the queue descriptor.

    :param uint32_t idx:
        Index to the entry on the queue.

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

    :param struct lpfc_queue \*q:
        Pointer to the queue descriptor.

.. _`lpfc_debug_dump_q.description`:

Description
-----------

This function dumps all entries from a queue specified by the queue
descriptor \ ``q``\ .

.. _`lpfc_debug_dump_fcp_wq`:

lpfc_debug_dump_fcp_wq
======================

.. c:function:: void lpfc_debug_dump_fcp_wq(struct lpfc_hba *phba, int fcp_wqidx)

    dump all entries from a fcp work queue

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param int fcp_wqidx:
        Index to a FCP work queue.

.. _`lpfc_debug_dump_fcp_wq.description`:

Description
-----------

This function dumps all entries from a FCP work queue specified by the
\ ``fcp_wqidx``\ .

.. _`lpfc_debug_dump_fcp_cq`:

lpfc_debug_dump_fcp_cq
======================

.. c:function:: void lpfc_debug_dump_fcp_cq(struct lpfc_hba *phba, int fcp_wqidx)

    dump all entries from a fcp work queue's cmpl queue

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param int fcp_wqidx:
        Index to a FCP work queue.

.. _`lpfc_debug_dump_fcp_cq.description`:

Description
-----------

This function dumps all entries from a FCP complete queue which is
associated to the FCP work queue specified by the \ ``fcp_wqidx``\ .

.. _`lpfc_debug_dump_hba_eq`:

lpfc_debug_dump_hba_eq
======================

.. c:function:: void lpfc_debug_dump_hba_eq(struct lpfc_hba *phba, int fcp_wqidx)

    dump all entries from a fcp work queue's evt queue

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param int fcp_wqidx:
        Index to a FCP work queue.

.. _`lpfc_debug_dump_hba_eq.description`:

Description
-----------

This function dumps all entries from a FCP event queue which is
associated to the FCP work queue specified by the \ ``fcp_wqidx``\ .

.. _`lpfc_debug_dump_els_wq`:

lpfc_debug_dump_els_wq
======================

.. c:function:: void lpfc_debug_dump_els_wq(struct lpfc_hba *phba)

    dump all entries from the els work queue

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_debug_dump_els_wq.description`:

Description
-----------

This function dumps all entries from the ELS work queue.

.. _`lpfc_debug_dump_mbx_wq`:

lpfc_debug_dump_mbx_wq
======================

.. c:function:: void lpfc_debug_dump_mbx_wq(struct lpfc_hba *phba)

    dump all entries from the mbox work queue

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_debug_dump_mbx_wq.description`:

Description
-----------

This function dumps all entries from the MBOX work queue.

.. _`lpfc_debug_dump_dat_rq`:

lpfc_debug_dump_dat_rq
======================

.. c:function:: void lpfc_debug_dump_dat_rq(struct lpfc_hba *phba)

    dump all entries from the receive data queue

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_debug_dump_dat_rq.description`:

Description
-----------

This function dumps all entries from the receive data queue.

.. _`lpfc_debug_dump_hdr_rq`:

lpfc_debug_dump_hdr_rq
======================

.. c:function:: void lpfc_debug_dump_hdr_rq(struct lpfc_hba *phba)

    dump all entries from the receive header queue

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_debug_dump_hdr_rq.description`:

Description
-----------

This function dumps all entries from the receive header queue.

.. _`lpfc_debug_dump_els_cq`:

lpfc_debug_dump_els_cq
======================

.. c:function:: void lpfc_debug_dump_els_cq(struct lpfc_hba *phba)

    dump all entries from the els complete queue

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_debug_dump_els_cq.description`:

Description
-----------

This function dumps all entries from the els complete queue.

.. _`lpfc_debug_dump_mbx_cq`:

lpfc_debug_dump_mbx_cq
======================

.. c:function:: void lpfc_debug_dump_mbx_cq(struct lpfc_hba *phba)

    dump all entries from the mbox complete queue

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

.. _`lpfc_debug_dump_mbx_cq.description`:

Description
-----------

This function dumps all entries from the mbox complete queue.

.. _`lpfc_debug_dump_wq_by_id`:

lpfc_debug_dump_wq_by_id
========================

.. c:function:: void lpfc_debug_dump_wq_by_id(struct lpfc_hba *phba, int qid)

    dump all entries from a work queue by queue id

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param int qid:
        Work queue identifier.

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

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param int qid:
        Mbox work queue identifier.

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

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param int qid:
        Receive queue identifier.

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

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param int qid:
        Complete queue identifier.

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

    :param struct lpfc_hba \*phba:
        Pointer to HBA context object.

    :param int qid:
        Complete queue identifier.

.. _`lpfc_debug_dump_eq_by_id.description`:

Description
-----------

This function dumps all entries from an event queue identified by the
queue identifier.

.. This file was automatic generated / don't edit.

