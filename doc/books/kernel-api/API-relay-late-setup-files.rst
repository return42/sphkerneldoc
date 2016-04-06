
.. _API-relay-late-setup-files:

======================
relay_late_setup_files
======================

*man relay_late_setup_files(9)*

*4.6.0-rc1*

triggers file creation


Synopsis
========

.. c:function:: int relay_late_setup_files( struct rchan * chan, const char * base_filename, struct dentry * parent )

Arguments
=========

``chan``
    channel to operate on

``base_filename``
    base name of files to create

``parent``
    dentry of parent directory, ``NULL`` for root directory


Description
===========

Returns 0 if successful, non-zero otherwise.

Use to setup files for a previously buffer-only channel. Useful to do early tracing in kernel, before VFS is up, for example.
