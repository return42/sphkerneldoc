.. -*- coding: utf-8; mode: rst -*-

.. _pipes:

*********
pipes API
*********

Pipe interfaces are all for in-kernel (builtin image) use. They are not
exported for use by modules.


.. kernel-doc:: include/linux/pipe_fs_i.h
    :man-sect: 9
    :internal:


.. kernel-doc:: fs/pipe.c
    :man-sect: 9
    :functions: 




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
