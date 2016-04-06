
.. _API-seq-pad:

=======
seq_pad
=======

*man seq_pad(9)*

*4.6.0-rc1*

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
