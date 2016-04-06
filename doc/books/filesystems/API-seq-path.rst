
.. _API-seq-path:

========
seq_path
========

*man seq_path(9)*

*4.6.0-rc1*

seq_file interface to print a pathname


Synopsis
========

.. c:function:: int seq_path( struct seq_file * m, const struct path * path, const char * esc )

Arguments
=========

``m``
    the seq_file handle

``path``
    the struct path to print

``esc``
    set of characters to escape in the output


Description
===========

return the absolute path of 'path', as represented by the dentry / mnt pair in the path parameter.
