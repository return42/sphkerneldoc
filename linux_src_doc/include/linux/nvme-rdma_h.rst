.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/nvme-rdma.h

.. _`nvme_rdma_cm_req`:

struct nvme_rdma_cm_req
=======================

.. c:type:: struct nvme_rdma_cm_req

    rdma connect request

.. _`nvme_rdma_cm_req.definition`:

Definition
----------

.. code-block:: c

    struct nvme_rdma_cm_req {
        __le16 recfmt;
        __le16 qid;
        __le16 hrqsize;
        __le16 hsqsize;
        u8 rsvd;
    }

.. _`nvme_rdma_cm_req.members`:

Members
-------

recfmt
    format of the RDMA Private Data

qid
    queue Identifier for the Admin or I/O Queue

hrqsize
    host receive queue size to be created

hsqsize
    host send queue size to be created

rsvd
    *undescribed*

.. _`nvme_rdma_cm_rep`:

struct nvme_rdma_cm_rep
=======================

.. c:type:: struct nvme_rdma_cm_rep

    rdma connect reply

.. _`nvme_rdma_cm_rep.definition`:

Definition
----------

.. code-block:: c

    struct nvme_rdma_cm_rep {
        __le16 recfmt;
        __le16 crqsize;
        u8 rsvd;
    }

.. _`nvme_rdma_cm_rep.members`:

Members
-------

recfmt
    format of the RDMA Private Data

crqsize
    controller receive queue size

rsvd
    *undescribed*

.. _`nvme_rdma_cm_rej`:

struct nvme_rdma_cm_rej
=======================

.. c:type:: struct nvme_rdma_cm_rej

    rdma connect reject

.. _`nvme_rdma_cm_rej.definition`:

Definition
----------

.. code-block:: c

    struct nvme_rdma_cm_rej {
        __le16 recfmt;
        __le16 sts;
    }

.. _`nvme_rdma_cm_rej.members`:

Members
-------

recfmt
    format of the RDMA Private Data

sts
    *undescribed*

.. This file was automatic generated / don't edit.

