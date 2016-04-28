.. -*- coding: utf-8; mode: rst -*-

.. _API-printk:

======
printk
======

*man printk(9)*

*4.6.0-rc5*

print a kernel message


Synopsis
========

.. c:function:: __visible int printk( const char * fmt, ... )

Arguments
=========

``fmt``
    format string

``...``
    variable arguments


Description
===========

This is ``printk``. It can be called from any context. We want it to
work.

We try to grab the console_lock. If we succeed, it's easy - we log the
output and call the console drivers. If we fail to get the semaphore, we
place the output into the log buffer and return. The current holder of
the console_sem will notice the new output in ``console_unlock``; and
will send it to the consoles before releasing the lock.

One effect of this deferred printing is that code which calls ``printk``
and then changes console_loglevel may break. This is because
console_loglevel is inspected when the actual printing occurs.


See also
========

printf(3)

See the ``vsnprintf`` documentation for format string extensions over
C99.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
