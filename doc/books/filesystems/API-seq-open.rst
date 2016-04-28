.. -*- coding: utf-8; mode: rst -*-

.. _API-seq-open:

========
seq_open
========

*man seq_open(9)*

*4.6.0-rc5*

initialize sequential file


Synopsis
========

.. c:function:: int seq_open( struct file * file, const struct seq_operations * op )

Arguments
=========

``file``
    file we initialize

``op``
    method table describing the sequence


Description
===========

``seq_open`` sets ``file``, associating it with a sequence described by
``op``. ``op``->``start`` sets the iterator up and returns the first
element of sequence. ``op``->``stop`` shuts it down. ``op``->``next``
returns the next element of sequence. ``op``->``show`` prints element
into the buffer. In case of error ->``start`` and ->``next`` return
ERR_PTR(error). In the end of sequence they return ``NULL``. ->``show``
returns 0 in case of success and negative number in case of error.
Returning SEQ_SKIP means “discard this element and move on”.


Note
====

``seq_open`` will allocate a struct seq_file and store its pointer in
``file``->private_data. This pointer should not be modified.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
