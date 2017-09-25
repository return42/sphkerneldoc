.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/flower/main.h

.. _`nfp_flower_priv`:

struct nfp_flower_priv
======================

.. c:type:: struct nfp_flower_priv

    Flower APP per-vNIC priv data

.. _`nfp_flower_priv.definition`:

Definition
----------

.. code-block:: c

    struct nfp_flower_priv {
        struct nfp_app *app;
        struct nfp_net *nn;
        u32 mask_id_seed;
        u64 flower_version;
        struct nfp_fl_stats_id stats_ids;
        struct nfp_fl_mask_id mask_ids;
        DECLARE_HASHTABLE(mask_table, NFP_FLOWER_MASK_HASH_BITS);
        DECLARE_HASHTABLE(flow_table, NFP_FLOWER_HASH_BITS);
        struct work_struct cmsg_work;
        struct sk_buff_head cmsg_skbs;
    }

.. _`nfp_flower_priv.members`:

Members
-------

app
    Back pointer to app

nn
    Pointer to vNIC

mask_id_seed
    Seed used for mask hash table

flower_version
    HW version of flower

stats_ids
    List of free stats ids

mask_ids
    List of free mask ids

mask_table
    Hash table used to store masks

flow_table
    Hash table used to store flower rules

cmsg_work
    Workqueue for control messages processing

cmsg_skbs
    List of skbs for control message processing

.. This file was automatic generated / don't edit.

