
.. _API-console-unlock:

==============
console_unlock
==============

*man console_unlock(9)*

*4.6.0-rc1*

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

Releases the console_lock which the caller holds on the console system and the console driver list.

While the console_lock was held, console output may have been buffered by ``printk``. If this is the case, ``console_unlock``; emits the output prior to releasing the lock.

If there is output waiting, we wake /dev/kmsg and ``syslog`` users.

``console_unlock``; may be called from any context.
