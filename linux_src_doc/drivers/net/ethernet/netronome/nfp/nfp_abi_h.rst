.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfp_abi.h

.. _`nfp_mbox_cmd`:

enum nfp_mbox_cmd
=================

.. c:type:: enum nfp_mbox_cmd

    PF mailbox commands

.. _`nfp_mbox_cmd.definition`:

Definition
----------

.. code-block:: c

    enum nfp_mbox_cmd {
        NFP_MBOX_NO_CMD,
        NFP_MBOX_POOL_GET,
        NFP_MBOX_POOL_SET,
        NFP_MBOX_PCIE_ABM_ENABLE,
        NFP_MBOX_PCIE_ABM_DISABLE
    };

.. _`nfp_mbox_cmd.constants`:

Constants
---------

NFP_MBOX_NO_CMD
    null command
    Used to indicate previous command has finished.

NFP_MBOX_POOL_GET
    get shared buffer pool info/config
    Input  - struct nfp_shared_buf_pool_id
    Output - struct nfp_shared_buf_pool_info_get

NFP_MBOX_POOL_SET
    set shared buffer pool info/config
    Input  - struct nfp_shared_buf_pool_info_set
    Output - None

NFP_MBOX_PCIE_ABM_ENABLE
    enable PCIe-side advanced buffer management
    Enable advanced buffer management of the PCIe block.  If ABM is disabled
    PCIe block maintains a very short queue of buffers and does tail drop.
    ABM allows more advanced buffering and priority control.
    Input  - None
    Output - None

NFP_MBOX_PCIE_ABM_DISABLE
    disable PCIe-side advanced buffer management
    Input  - None
    Output - None

.. _`nfp_shared_buf`:

struct nfp_shared_buf
=====================

.. c:type:: struct nfp_shared_buf

    NFP shared buffer description

.. _`nfp_shared_buf.definition`:

Definition
----------

.. code-block:: c

    struct nfp_shared_buf {
        __le32 id;
        __le32 size;
        __le16 ingress_pools_count;
        __le16 egress_pools_count;
        __le16 ingress_tc_count;
        __le16 egress_tc_count;
        __le32 pool_size_unit;
    }

.. _`nfp_shared_buf.members`:

Members
-------

id
    numerical user-visible id of the shared buffer

size
    size in bytes of the buffer

ingress_pools_count
    number of ingress pools

egress_pools_count
    number of egress pools

ingress_tc_count
    number of ingress trafic classes

egress_tc_count
    number of egress trafic classes

pool_size_unit
    pool size may be in credits, each credit is
    \ ``pool_size_unit``\  bytes

.. _`nfp_shared_buf_pool_id`:

struct nfp_shared_buf_pool_id
=============================

.. c:type:: struct nfp_shared_buf_pool_id

    shared buffer pool identification

.. _`nfp_shared_buf_pool_id.definition`:

Definition
----------

.. code-block:: c

    struct nfp_shared_buf_pool_id {
        __le32 shared_buf;
        __le32 pool;
    }

.. _`nfp_shared_buf_pool_id.members`:

Members
-------

shared_buf
    shared buffer id

pool
    pool index

.. _`nfp_shared_buf_pool_info_get`:

struct nfp_shared_buf_pool_info_get
===================================

.. c:type:: struct nfp_shared_buf_pool_info_get

    struct devlink_sb_pool_info mirror

.. _`nfp_shared_buf_pool_info_get.definition`:

Definition
----------

.. code-block:: c

    struct nfp_shared_buf_pool_info_get {
        __le32 pool_type;
        __le32 size;
        __le32 threshold_type;
    }

.. _`nfp_shared_buf_pool_info_get.members`:

Members
-------

pool_type
    one of enum devlink_sb_pool_type

size
    pool size in units of SB's \ ``pool_size_unit``\ 

threshold_type
    one of enum devlink_sb_threshold_type

.. _`nfp_shared_buf_pool_info_set`:

struct nfp_shared_buf_pool_info_set
===================================

.. c:type:: struct nfp_shared_buf_pool_info_set

    packed args of sb_pool_set

.. _`nfp_shared_buf_pool_info_set.definition`:

Definition
----------

.. code-block:: c

    struct nfp_shared_buf_pool_info_set {
        struct nfp_shared_buf_pool_id id;
        __le32 size;
        __le32 threshold_type;
    }

.. _`nfp_shared_buf_pool_info_set.members`:

Members
-------

id
    pool identification info

size
    pool size in units of SB's \ ``pool_size_unit``\ 

threshold_type
    one of enum devlink_sb_threshold_type

.. This file was automatic generated / don't edit.

