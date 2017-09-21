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
        union {unnamed_union};
        struct mfc_cache_cmp_arg cmparg;
         };
        vifi_t mfc_parent;
        int mfc_flags;
        union unres;
        struct res;
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


cmparg
    used for rhashtable comparisons

}
    *undescribed*

mfc_parent
    source interface (iif)

mfc_flags
    entry flags

unres
    *undescribed*

res
    *undescribed*

mfc_un
    *undescribed*

list
    global entry list

rcu
    used for entry destruction

.. This file was automatic generated / don't edit.

