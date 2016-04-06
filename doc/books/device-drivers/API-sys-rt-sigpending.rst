
.. _API-sys-rt-sigpending:

=================
sys_rt_sigpending
=================

*man sys_rt_sigpending(9)*

*4.6.0-rc1*

examine a pending signal that has been raised while blocked


Synopsis
========

.. c:function:: long sys_rt_sigpending( sigset_t __user * uset, size_t sigsetsize )

Arguments
=========

``uset``
    stores pending signals

``sigsetsize``
    size of sigset_t type or larger
