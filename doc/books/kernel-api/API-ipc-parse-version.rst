.. -*- coding: utf-8; mode: rst -*-

.. _API-ipc-parse-version:

=================
ipc_parse_version
=================

*man ipc_parse_version(9)*

*4.6.0-rc5*

ipc call version


Synopsis
========

.. c:function:: int ipc_parse_version( int * cmd )

Arguments
=========

``cmd``
    pointer to command


Description
===========

Return IPC_64 for new style IPC and IPC_OLD for old style IPC. The
``cmd`` value is turned from an encoding command and version into just
the command code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
