.. -*- coding: utf-8; mode: rst -*-

.. _API-sys-rt-sigaction:

================
sys_rt_sigaction
================

*man sys_rt_sigaction(9)*

*4.6.0-rc5*

alter an action taken by a process


Synopsis
========

.. c:function:: long sys_rt_sigaction( int sig, const struct sigaction __user * act, struct sigaction __user * oact, size_t sigsetsize )

Arguments
=========

``sig``
    signal to be sent

``act``
    new sigaction

``oact``
    used to save the previous sigaction

``sigsetsize``
    size of sigset_t type


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
