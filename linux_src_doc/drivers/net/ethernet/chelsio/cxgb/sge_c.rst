.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb/sge.c

.. _`recycle_fl_buf`:

recycle_fl_buf
==============

.. c:function:: void recycle_fl_buf(struct freelQ *fl, int idx)

    recycle a free list buffer

    :param struct freelQ \*fl:
        the free list

    :param int idx:
        index of buffer to recycle

.. _`recycle_fl_buf.description`:

Description
-----------

Recycles the specified buffer on the given free list by adding it at
the next available slot on the list.

.. _`get_packet`:

get_packet
==========

.. c:function:: struct sk_buff *get_packet(struct adapter *adapter, struct freelQ *fl, unsigned int len)

    return the next ingress packet buffer

    :param struct adapter \*adapter:
        the adapter that received the packet

    :param struct freelQ \*fl:
        the SGE free list holding the packet

    :param unsigned int len:
        the actual packet length, excluding any SGE padding

.. _`get_packet.description`:

Description
-----------

Get the next packet from a free list and complete setup of the
sk_buff.  If the packet is small we make a copy and recycle the
original buffer, otherwise we use the original buffer itself.  If a
positive drop threshold is supplied packets are dropped and their
buffers recycled if (a) the number of remaining buffers is under the
threshold and the packet is too big to copy, or (b) the packet should
be copied but there is no memory for the copy.

.. _`unexpected_offload`:

unexpected_offload
==================

.. c:function:: void unexpected_offload(struct adapter *adapter, struct freelQ *fl)

    handle an unexpected offload packet

    :param struct adapter \*adapter:
        the adapter

    :param struct freelQ \*fl:
        the free list that received the packet

.. _`unexpected_offload.description`:

Description
-----------

Called when we receive an unexpected offload packet (e.g., the TOE
function is disabled or the card is a NIC).  Prints a message and
recycles the buffer.

.. _`sge_rx`:

sge_rx
======

.. c:function:: void sge_rx(struct sge *sge, struct freelQ *fl, unsigned int len)

    process an ingress ethernet packet

    :param struct sge \*sge:
        the sge structure

    :param struct freelQ \*fl:
        the free list that contains the packet buffer

    :param unsigned int len:
        the packet length

.. _`sge_rx.description`:

Description
-----------

Process an ingress ethernet pakcet and deliver it to the stack.

.. This file was automatic generated / don't edit.

