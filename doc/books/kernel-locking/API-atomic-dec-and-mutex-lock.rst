.. -*- coding: utf-8; mode: rst -*-

.. _API-atomic-dec-and-mutex-lock:

=========================
atomic_dec_and_mutex_lock
=========================

*man atomic_dec_and_mutex_lock(9)*

*4.6.0-rc5*

return holding mutex if we dec to 0


Synopsis
========

.. c:function:: int atomic_dec_and_mutex_lock( atomic_t * cnt, struct mutex * lock )

Arguments
=========

``cnt``
    the atomic which we are to dec

``lock``
    the mutex to return holding if we dec to 0


Description
===========

return true and hold lock if we dec to 0, return false otherwise


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
