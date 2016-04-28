.. -*- coding: utf-8; mode: rst -*-

.. _API-w1-reset-resume-command:

=======================
w1_reset_resume_command
=======================

*man w1_reset_resume_command(9)*

*4.6.0-rc5*

resume instead of another match ROM


Synopsis
========

.. c:function:: int w1_reset_resume_command( struct w1_master * dev )

Arguments
=========

``dev``
    the master device


Description
===========

When the workflow with a slave amongst many requires several successive
commands a reset between each, this function is similar to doing a reset
then a match ROM for the last matched ROM. The advantage being that the
matched ROM step is skipped in favor of the resume command. The slave
must support the command of course.

If the bus has only one slave, traditionnaly the match ROM is skipped
and a “SKIP ROM” is done for efficiency. On multi-slave busses, this
doesn't work of course, but the resume command is the next best thing.

The w1 master lock must be held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
