.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-pipe-inode-info:

======================
struct pipe_inode_info
======================

*man struct pipe_inode_info(9)*

*4.6.0-rc5*

a linux kernel pipe


Synopsis
========

.. code-block:: c

    struct pipe_inode_info {
      struct mutex mutex;
      wait_queue_head_t wait;
      unsigned int nrbufs;
      unsigned int curbuf;
      unsigned int buffers;
      unsigned int readers;
      unsigned int writers;
      unsigned int files;
      unsigned int waiting_writers;
      unsigned int r_counter;
      unsigned int w_counter;
      struct page * tmp_page;
      struct fasync_struct * fasync_readers;
      struct fasync_struct * fasync_writers;
      struct pipe_buffer * bufs;
      struct user_struct * user;
    };


Members
=======

mutex
    mutex protecting the whole thing

wait
    reader/writer wait point in case of empty/full pipe

nrbufs
    the number of non-empty pipe buffers in this pipe

curbuf
    the current pipe buffer entry

buffers
    total number of buffers (should be a power of 2)

readers
    number of current readers of this pipe

writers
    number of current writers of this pipe

files
    number of struct file referring this pipe (protected by ->i_lock)

waiting_writers
    number of writers blocked waiting for room

r_counter
    reader counter

w_counter
    writer counter

tmp_page
    cached released page

fasync_readers
    reader side fasync

fasync_writers
    writer side fasync

bufs
    the circular array of pipe buffers

user
    the user who created this pipe


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
