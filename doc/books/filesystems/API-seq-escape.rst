.. -*- coding: utf-8; mode: rst -*-

.. _API-seq-escape:

==========
seq_escape
==========

*man seq_escape(9)*

*4.6.0-rc5*

print string into buffer, escaping some characters


Synopsis
========

.. c:function:: void seq_escape( struct seq_file * m, const char * s, const char * esc )

Arguments
=========

``m``
    target buffer

``s``
    string

``esc``
    set of characters that need escaping


Description
===========

Puts string into buffer, replacing each occurrence of character from
``esc`` with usual octal escape. Use ``seq_has_overflowed`` to check for
errors.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
