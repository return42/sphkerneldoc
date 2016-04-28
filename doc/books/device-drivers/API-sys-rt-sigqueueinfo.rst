.. -*- coding: utf-8; mode: rst -*-

.. _API-sys-rt-sigqueueinfo:

===================
sys_rt_sigqueueinfo
===================

*man sys_rt_sigqueueinfo(9)*

*4.6.0-rc5*

send signal information to a signal


Synopsis
========

.. c:function:: long sys_rt_sigqueueinfo( pid_t pid, int sig, siginfo_t __user * uinfo )

Arguments
=========

``pid``
    the PID of the thread

``sig``
    signal to be sent

``uinfo``
    signal info to be sent


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
