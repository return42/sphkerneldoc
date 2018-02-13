.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/scsi/srp.h

.. _`srp_login_req_rdma`:

struct srp_login_req_rdma
=========================

.. c:type:: struct srp_login_req_rdma

    RDMA/CM login parameters.

.. _`srp_login_req_rdma.definition`:

Definition
----------

.. code-block:: c

    struct srp_login_req_rdma {
        u64 tag;
        __be16 req_buf_fmt;
        u8 req_flags;
        u8 opcode;
        __be32 req_it_iu_len;
        u8 initiator_port_id[16];
        u8 target_port_id[16];
    }

.. _`srp_login_req_rdma.members`:

Members
-------

tag
    *undescribed*

req_buf_fmt
    *undescribed*

req_flags
    *undescribed*

opcode
    *undescribed*

req_it_iu_len
    *undescribed*

initiator_port_id
    *undescribed*

target_port_id
    *undescribed*

.. _`srp_login_req_rdma.description`:

Description
-----------

RDMA/CM over InfiniBand can only carry 92 - 36 = 56 bytes of private
data. The \ ``srp_login_req_rdma``\  structure contains the same information as
\ ``srp_login_req``\  but with the reserved data removed.

.. This file was automatic generated / don't edit.

