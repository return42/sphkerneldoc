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
        struct mr_mfc _c;
        union {
            struct {
                __be32 mfc_mcastgrp;
                __be32 mfc_origin;
            } ;
            struct mfc_cache_cmp_arg cmparg;
        } ;
    }

.. _`mfc_cache.members`:

Members
-------

\_c
    Common multicast routing information; has to be first [for casting]

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

.. This file was automatic generated / don't edit.

