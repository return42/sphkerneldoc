
.. _API-sys-sigpending:

==============
sys_sigpending
==============

*man sys_sigpending(9)*

*4.6.0-rc1*

examine pending signals


Synopsis
========

.. c:function:: long sys_sigpending( old_sigset_t __user * set )

Arguments
=========

``set``
    where mask of pending signal is returned
