.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qedi/qedi.h

.. _`iscsi_cid_queue`:

struct iscsi_cid_queue
======================

.. c:type:: struct iscsi_cid_queue

    Per adapter iscsi cid queue

.. _`iscsi_cid_queue.definition`:

Definition
----------

.. code-block:: c

    struct iscsi_cid_queue {
        void *cid_que_base;
        u32 *cid_que;
        u32 cid_q_prod_idx;
        u32 cid_q_cons_idx;
        u32 cid_q_max_idx;
        u32 cid_free_cnt;
        struct qedi_conn **conn_cid_tbl;
    }

.. _`iscsi_cid_queue.members`:

Members
-------

cid_que_base
    queue base memory

cid_que
    queue memory pointer

cid_q_prod_idx
    produce index

cid_q_cons_idx
    consumer index

cid_q_max_idx
    max index. used to detect wrap around condition

cid_free_cnt
    queue size

conn_cid_tbl
    iscsi cid to conn structure mapping table

.. _`iscsi_cid_queue.description`:

Description
-----------

Per adapter iSCSI CID Queue

.. This file was automatic generated / don't edit.

