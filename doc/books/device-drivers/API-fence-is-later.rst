.. -*- coding: utf-8; mode: rst -*-

.. _API-fence-is-later:

==============
fence_is_later
==============

*man fence_is_later(9)*

*4.6.0-rc5*

return if f1 is chronologically later than f2


Synopsis
========

.. c:function:: bool fence_is_later( struct fence * f1, struct fence * f2 )

Arguments
=========

``f1``
    [in] the first fence from the same context

``f2``
    [in] the second fence from the same context


Description
===========

Returns true if f1 is chronologically later than f2. Both fences must be
from the same context, since a seqno is not re-used across contexts.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
