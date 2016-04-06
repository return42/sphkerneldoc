
.. _API-splice-from-pipe-begin:

======================
splice_from_pipe_begin
======================

*man splice_from_pipe_begin(9)*

*4.6.0-rc1*

start splicing from pipe


Synopsis
========

.. c:function:: void splice_from_pipe_begin( struct splice_desc * sd )

Arguments
=========

``sd``
    information about the splice operation


Description
===========

This function should be called before a loop containing ``splice_from_pipe_next`` and ``splice_from_pipe_feed`` to initialize the necessary fields of ``sd``.
