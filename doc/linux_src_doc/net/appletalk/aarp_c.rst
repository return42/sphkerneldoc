.. -*- coding: utf-8; mode: rst -*-

======
aarp.c
======


.. _`aarp_entry`:

struct aarp_entry
=================

.. c:type:: aarp_entry

    AARP entry @last_sent - Last time we xmitted the aarp request @packet_queue - Queue of frames wait for resolution @status - Used for proxy AARP expires_at - Entry expiry time target_addr - DDP Address dev - Device to use hwaddr - Physical i/f address of target/router xmit_count - When this hits 10 we give up next - Next entry in chain


.. _`aarp_entry.definition`:

Definition
----------

.. code-block:: c

  struct aarp_entry {
  };


.. _`aarp_entry.members`:

Members
-------


