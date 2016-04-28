.. -*- coding: utf-8; mode: rst -*-

.. _API-sys-rt-sigpending:

=================
sys_rt_sigpending
=================

*man sys_rt_sigpending(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
