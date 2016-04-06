
.. _API-seq-file-path:

=============
seq_file_path
=============

*man seq_file_path(9)*

*4.6.0-rc1*

seq_file interface to print a pathname of a file


Synopsis
========

.. c:function:: int seq_file_path( struct seq_file * m, struct file * file, const char * esc )

Arguments
=========

``m``
    the seq_file handle

``file``
    the struct file to print

``esc``
    set of characters to escape in the output


Description
===========

return the absolute path to the file.
