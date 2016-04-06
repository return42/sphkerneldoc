
.. _API-ipc-parse-version:

=================
ipc_parse_version
=================

*man ipc_parse_version(9)*

*4.6.0-rc1*

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

Return IPC_64 for new style IPC and IPC_OLD for old style IPC. The ``cmd`` value is turned from an encoding command and version into just the command code.
