.. -*- coding: utf-8; mode: rst -*-

.. _API-to-seqno-fence:

==============
to_seqno_fence
==============

*man to_seqno_fence(9)*

*4.6.0-rc5*

cast a fence to a seqno_fence


Synopsis
========

.. c:function:: struct seqno_fence * to_seqno_fence( struct fence * fence )

Arguments
=========

``fence``
    fence to cast to a seqno_fence


Description
===========

Returns NULL if the fence is not a seqno_fence, or the seqno_fence
otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
