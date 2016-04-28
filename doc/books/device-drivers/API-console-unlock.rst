.. -*- coding: utf-8; mode: rst -*-

.. _API-console-unlock:

==============
console_unlock
==============

*man console_unlock(9)*

*4.6.0-rc5*

unlock the console system


Synopsis
========

.. c:function:: void console_unlock( void )

Arguments
=========

``void``
    no arguments


Description
===========

Releases the console_lock which the caller holds on the console system
and the console driver list.

While the console_lock was held, console output may have been buffered
by ``printk``. If this is the case, ``console_unlock``; emits the output
prior to releasing the lock.

If there is output waiting, we wake /dev/kmsg and ``syslog`` users.

``console_unlock``; may be called from any context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
