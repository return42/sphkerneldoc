
.. _API-do-sigtimedwait:

===============
do_sigtimedwait
===============

*man do_sigtimedwait(9)*

*4.6.0-rc1*

wait for queued signals specified in ``which``


Synopsis
========

.. c:function:: int do_sigtimedwait( const sigset_t * which, siginfo_t * info, const struct timespec * ts )

Arguments
=========

``which``
    queued signals to wait for

``info``
    if non-null, the signal's siginfo is returned here

``ts``
    upper bound on process time suspension
