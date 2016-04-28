.. -*- coding: utf-8; mode: rst -*-

.. _API-sys-kill:

========
sys_kill
========

*man sys_kill(9)*

*4.6.0-rc5*

send a signal to a process


Synopsis
========

.. c:function:: long sys_kill( pid_t pid, int sig )

Arguments
=========

``pid``
    the PID of the process

``sig``
    signal to be sent


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
