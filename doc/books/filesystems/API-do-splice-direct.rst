.. -*- coding: utf-8; mode: rst -*-

.. _API-do-splice-direct:

================
do_splice_direct
================

*man do_splice_direct(9)*

*4.6.0-rc5*

splices data directly between two files


Synopsis
========

.. c:function:: long do_splice_direct( struct file * in, loff_t * ppos, struct file * out, loff_t * opos, size_t len, unsigned int flags )

Arguments
=========

``in``
    file to splice from

``ppos``
    input file offset

``out``
    file to splice to

``opos``
    output file offset

``len``
    number of bytes to splice

``flags``
    splice modifier flags


Description
===========

For use by ``do_sendfile``. splice can easily emulate sendfile, but
doing it in the application would incur an extra system call (splice in
+ splice out, as compared to just ``sendfile``). So this helper can
splice directly through a process-private pipe.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
