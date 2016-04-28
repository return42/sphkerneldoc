.. -*- coding: utf-8; mode: rst -*-

.. _API-seq-pad:

=======
seq_pad
=======

*man seq_pad(9)*

*4.6.0-rc5*

write padding spaces to buffer


Synopsis
========

.. c:function:: void seq_pad( struct seq_file * m, char c )

Arguments
=========

``m``
    seq_file identifying the buffer to which data should be written

``c``
    the byte to append after padding if non-zero


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
