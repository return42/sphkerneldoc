.. -*- coding: utf-8; mode: rst -*-

.. _pipes:

=========
pipes API
=========

Pipe interfaces are all for in-kernel (builtin image) use. They are not
exported for use by modules.


.. kernel-doc:: include/linux/pipe_fs_i.h
    :internal:

.. kernel-doc:: fs/pipe.c
    :functions: 



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
