.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/appletalk/aarp.c

.. _`aarp_entry`:

struct aarp_entry
=================

.. c:type:: struct aarp_entry

    AARP entry \ ``last_sent``\  - Last time we xmitted the aarp request \ ``packet_queue``\  - Queue of frames wait for resolution \ ``status``\  - Used for proxy AARP expires_at - Entry expiry time target_addr - DDP Address dev - Device to use hwaddr - Physical i/f address of target/router xmit_count - When this hits 10 we give up next - Next entry in chain

.. _`aarp_entry.definition`:

Definition
----------

.. code-block:: c

    struct aarp_entry {
        unsigned long last_sent;
        struct sk_buff_head packet_queue;
        int status;
        unsigned long expires_at;
        struct atalk_addr target_addr;
        struct net_device *dev;
        char hwaddr[ETH_ALEN];
        unsigned short xmit_count;
        struct aarp_entry *next;
    }

.. _`aarp_entry.members`:

Members
-------

last_sent
    *undescribed*

packet_queue
    *undescribed*

status
    *undescribed*

expires_at
    *undescribed*

target_addr
    *undescribed*

dev
    *undescribed*

xmit_count
    *undescribed*

next
    *undescribed*

.. This file was automatic generated / don't edit.

