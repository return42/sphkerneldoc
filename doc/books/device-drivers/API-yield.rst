
.. _API-yield:

=====
yield
=====

*man yield(9)*

*4.6.0-rc1*

yield the current processor to other threads.


Synopsis
========

.. c:function:: void __sched yield( void )

Arguments
=========

``void``
    no arguments


Description
===========

Do not ever use this function, there's a 99% chance you're doing it wrong.

The scheduler is at all times free to pick the calling task as the most eligible task to run, if removing the ``yield`` call from your code breaks it, its already broken.


Typical broken usage is
=======================

while (!event) ``yield``;

where one assumes that ``yield`` will let 'the other' process run that will make event true. If the current task is a SCHED_FIFO task that will never happen. Never use ``yield``
as a progress guarantee!!

If you want to use ``yield`` to wait for something, use ``wait_event``. If you want to use ``yield`` to be 'nice' for others, use ``cond_resched``. If you still want to use
``yield``, do not!
