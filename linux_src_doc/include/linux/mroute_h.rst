.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mroute.h

.. _`mfc_cache`:

struct mfc_cache
================

.. c:type:: struct mfc_cache

    multicast routing entries

.. _`mfc_cache.definition`:

Definition
----------

.. code-block:: c

    struct mfc_cache {
        struct rhlist_head mnode;
        union {
            struct {
                __be32 mfc_mcastgrp;
                __be32 mfc_origin;
            } ;
            struct mfc_cache_cmp_arg cmparg;
        } ;
        vifi_t mfc_parent;
        int mfc_flags;
        union {
            struct {
                unsigned long expires;
                struct sk_buff_head unresolved;
            } unres;
            struct {
                unsigned long last_assert;
                int minvif;
                int maxvif;
                unsigned long bytes;
                unsigned long pkt;
                unsigned long wrong_if;
                unsigned long lastuse;
                unsigned char ttls[MAXVIFS];
            } res;
        } mfc_un;
        struct list_head list;
        struct rcu_head rcu;
    }

.. _`mfc_cache.members`:

Members
-------

mnode
    rhashtable list

{unnamed_union}
    anonymous

{unnamed_struct}
    anonymous

mfc_mcastgrp
    destination multicast group address

mfc_origin
    source address

cmparg
    used for rhashtable comparisons

mfc_parent
    source interface (iif)

mfc_flags
    entry flags

mfc_un
    *undescribed*

unres
    *undescribed*

expires
    unresolved entry expire time

unresolved
    unresolved cached skbs

res
    *undescribed*

last_assert
    time of last assert

minvif
    minimum VIF id

maxvif
    maximum VIF id

bytes
    bytes that have passed for this entry

pkt
    packets that have passed for this entry

wrong_if
    number of wrong source interface hits

lastuse
    time of last use of the group (traffic or update)

ttls
    OIF TTL threshold array

list
    global entry list

rcu
    used for entry destruction

.. This file was automatic generated / don't edit.

