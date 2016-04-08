
.. _API-spans-boundary:

==============
spans_boundary
==============

*man spans_boundary(9)*

*4.6.0-rc1*

Check a packet can be ISA DMA'd


Synopsis
========

.. c:function:: int spans_boundary( struct sk_buff * skb )

Arguments
=========

``skb``
    The buffer to check


Description
===========

Returns true if the buffer cross a DMA boundary on a PC. The poor thing can only DMA within a 64K block not across the edges of it.
