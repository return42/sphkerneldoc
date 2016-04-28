.. -*- coding: utf-8; mode: rst -*-

.. _API-seq-path:

========
seq_path
========

*man seq_path(9)*

*4.6.0-rc5*

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

return the absolute path of 'path', as represented by the dentry / mnt
pair in the path parameter.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
