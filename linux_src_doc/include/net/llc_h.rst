.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/llc.h

.. _`llc_sap`:

struct llc_sap
==============

.. c:type:: struct llc_sap

    Defines the SAP component

.. _`llc_sap.definition`:

Definition
----------

.. code-block:: c

    struct llc_sap {
        unsigned char state;
        unsigned char p_bit;
        unsigned char f_bit;
        refcount_t refcnt;
        int (*rcv_func)(struct sk_buff *skb,struct net_device *dev,struct packet_type *pt, struct net_device *orig_dev);
        struct llc_addr laddr;
        struct list_head node;
        spinlock_t sk_lock;
        int sk_count;
        struct hlist_nulls_head sk_laddr_hash[LLC_SK_LADDR_HASH_ENTRIES];
        struct hlist_head sk_dev_hash[LLC_SK_DEV_HASH_ENTRIES];
    }

.. _`llc_sap.members`:

Members
-------

state
    *undescribed*

p_bit
    *undescribed*

f_bit
    *undescribed*

refcnt
    *undescribed*

rcv_func
    *undescribed*

laddr
    *undescribed*

node
    *undescribed*

sk_lock
    *undescribed*

sk_count
    *undescribed*

sk_laddr_hash
    *undescribed*

sk_dev_hash
    *undescribed*

.. _`llc_sap.description`:

Description
-----------

@station - station this sap belongs to
\ ``state``\  - sap state
\ ``p_bit``\  - only lowest-order bit used
\ ``f_bit``\  - only lowest-order bit used
\ ``laddr``\  - SAP value in this 'lsap'
\ ``node``\  - entry in station sap_list
\ ``sk_list``\  - LLC sockets this one manages

.. This file was automatic generated / don't edit.

