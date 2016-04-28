.. -*- coding: utf-8; mode: rst -*-

.. _API-sys-sigpending:

==============
sys_sigpending
==============

*man sys_sigpending(9)*

*4.6.0-rc5*

examine pending signals


Synopsis
========

.. c:function:: long sys_sigpending( old_sigset_t __user * set )

Arguments
=========

``set``
    where mask of pending signal is returned


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
