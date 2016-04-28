.. -*- coding: utf-8; mode: rst -*-

.. _API-lookup-one-len-unlocked:

=======================
lookup_one_len_unlocked
=======================

*man lookup_one_len_unlocked(9)*

*4.6.0-rc5*

filesystem helper to lookup single pathname component


Synopsis
========

.. c:function:: struct dentry * lookup_one_len_unlocked( const char * name, struct dentry * base, int len )

Arguments
=========

``name``
    pathname component to lookup

``base``
    base directory to lookup from

``len``
    maximum length ``len`` should be interpreted to


Description
===========

Note that this routine is purely a helper for filesystem usage and
should not be called by generic code.

Unlike lookup_one_len, it should be called without the parent i_mutex
held, and will take the i_mutex itself if necessary.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
