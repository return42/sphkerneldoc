.. -*- coding: utf-8; mode: rst -*-

.. _API-relay-open:

==========
relay_open
==========

*man relay_open(9)*

*4.6.0-rc5*

create a new relay channel


Synopsis
========

.. c:function:: struct rchan * relay_open( const char * base_filename, struct dentry * parent, size_t subbuf_size, size_t n_subbufs, struct rchan_callbacks * cb, void * private_data )

Arguments
=========

``base_filename``
    base name of files to create, ``NULL`` for buffering only

``parent``
    dentry of parent directory, ``NULL`` for root directory or buffer

``subbuf_size``
    size of sub-buffers

``n_subbufs``
    number of sub-buffers

``cb``
    client callback functions

``private_data``
    user-defined data


Description
===========

Returns channel pointer if successful, ``NULL`` otherwise.

Creates a channel buffer for each cpu using the sizes and attributes
specified. The created channel buffer files will be named
base_filename0...base_filenameN-1. File permissions will be
``S_IRUSR``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
