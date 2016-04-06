
.. _API-kthread-freezable-should-stop:

=============================
kthread_freezable_should_stop
=============================

*man kthread_freezable_should_stop(9)*

*4.6.0-rc1*

should this freezable kthread return now?


Synopsis
========

.. c:function:: bool kthread_freezable_should_stop( bool * was_frozen )

Arguments
=========

``was_frozen``
    optional out parameter, indicates whether ``current`` was frozen


Description
===========

``kthread_should_stop`` for freezable kthreads, which will enter refrigerator if necessary. This function is safe from ``kthread_stop`` / freezer deadlock and freezable kthreads
should use this function instead of calling ``try_to_freeze`` directly.
