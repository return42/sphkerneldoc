.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-media-file-operations:

============================
struct media_file_operations
============================

*man struct media_file_operations(9)*

*4.6.0-rc5*

Media device file operations


Synopsis
========

.. code-block:: c

    struct media_file_operations {
      struct module * owner;
      ssize_t (* read) (struct file *, char __user *, size_t, loff_t *);
      ssize_t (* write) (struct file *, const char __user *, size_t, loff_t *);
      unsigned int (* poll) (struct file *, struct poll_table_struct *);
      long (* ioctl) (struct file *, unsigned int, unsigned long);
      long (* compat_ioctl) (struct file *, unsigned int, unsigned long);
      int (* open) (struct file *);
      int (* release) (struct file *);
    };


Members
=======

owner
    should be filled with ``THIS_MODULE``

read
    pointer to the function that implements ``read`` syscall

write
    pointer to the function that implements ``write`` syscall

poll
    pointer to the function that implements ``poll`` syscall

ioctl
    pointer to the function that implements ``ioctl`` syscall

compat_ioctl
    pointer to the function that will handle 32 bits userspace calls to
    the the ``ioctl`` syscall on a Kernel compiled with 64 bits.

open
    pointer to the function that implements ``open`` syscall

release
    pointer to the function that will release the resources allocated by
    the ``open`` function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
