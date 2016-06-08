.. -*- coding: utf-8; mode: rst -*-

.. _Network_Layer_Functions:

***********************
Network Layer Functions
***********************

The Z8530 layer provides functions to queue packets for transmission.
The driver internally buffers the frame currently being transmitted and
one further frame (in order to keep back to back transmission running).
Any further buffering is up to the caller.

The function ``z8530_queue_xmit`` takes a network buffer in sk_buff
format and queues it for transmission. The caller must provide the
entire packet with the exception of the bitstuffing and CRC. This is
normally done by the caller via the generic HDLC interface layer. It
returns 0 if the buffer has been queued and non zero values for queue
full. If the function accepts the buffer it becomes property of the
Z8530 layer and the caller should not free it.

The function ``z8530_get_stats`` returns a pointer to an internally
maintained per interface statistics block. This provides most of the
interface code needed to implement the network layer get_stats
callback.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
