
.. _API-fault-in-user-writeable:

=======================
fault_in_user_writeable
=======================

*man fault_in_user_writeable(9)*

*4.6.0-rc1*

Fault in user address and verify RW access


Synopsis
========

.. c:function:: int fault_in_user_writeable( u32 __user * uaddr )

Arguments
=========

``uaddr``
    pointer to faulting user space address


Description
===========

Slow path to fixup the fault we just took in the atomic write access to ``uaddr``.

We have no generic implementation of a non-destructive write to the user address. We know that we faulted in the atomic pagefault disabled section so we can as well avoid the #PF
overhead by calling ``get_user_pages`` right away.
