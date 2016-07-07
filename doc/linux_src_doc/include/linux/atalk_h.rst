.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/atalk.h

.. _`atalk_iface`:

struct atalk_iface
==================

.. c:type:: struct atalk_iface

    AppleTalk Interface \ ``dev``\  - Network device associated with this interface \ ``address``\  - Our address \ ``status``\  - What are we doing? \ ``nets``\  - Associated direct netrange \ ``next``\  - next element in the list of interfaces

.. _`atalk_iface.definition`:

Definition
----------

.. code-block:: c

    struct atalk_iface {
        struct net_device *dev;
        struct atalk_addr address;
        int status;
        #define ATIF_PROBE 1
        #define ATIF_PROBE_FAIL 2
        struct atalk_netrange nets;
        struct atalk_iface *next;
    }

.. _`atalk_iface.members`:

Members
-------

dev
    *undescribed*

address
    *undescribed*

status
    *undescribed*

nets
    *undescribed*

next
    *undescribed*

.. This file was automatic generated / don't edit.

