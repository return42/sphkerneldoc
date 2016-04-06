
.. _API-atomic-dec-and-mutex-lock:

=========================
atomic_dec_and_mutex_lock
=========================

*man atomic_dec_and_mutex_lock(9)*

*4.6.0-rc1*

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
