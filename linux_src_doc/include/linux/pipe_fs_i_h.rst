.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/pipe_fs_i.h

.. _`pipe_buffer`:

struct pipe_buffer
==================

.. c:type:: struct pipe_buffer

    a linux kernel pipe buffer

.. _`pipe_buffer.definition`:

Definition
----------

.. code-block:: c

    struct pipe_buffer {
        struct page *page;
        unsigned int offset, len;
        const struct pipe_buf_operations *ops;
        unsigned int flags;
        unsigned long private;
    }

.. _`pipe_buffer.members`:

Members
-------

page
    the page containing the data for the pipe buffer

offset
    offset of data inside the \ ``page``\ 

len
    length of data inside the \ ``page``\ 

ops
    operations associated with this buffer. See \ ``pipe_buf_operations``\ .

flags
    pipe buffer flags. See above.

private
    private data owned by the ops.

.. _`pipe_inode_info`:

struct pipe_inode_info
======================

.. c:type:: struct pipe_inode_info

    a linux kernel pipe

.. _`pipe_inode_info.definition`:

Definition
----------

.. code-block:: c

    struct pipe_inode_info {
        struct mutex mutex;
        wait_queue_head_t wait;
        unsigned int nrbufs, curbuf, buffers;
        unsigned int readers;
        unsigned int writers;
        unsigned int files;
        unsigned int waiting_writers;
        unsigned int r_counter;
        unsigned int w_counter;
        struct page *tmp_page;
        struct fasync_struct *fasync_readers;
        struct fasync_struct *fasync_writers;
        struct pipe_buffer *bufs;
        struct user_struct *user;
    }

.. _`pipe_inode_info.members`:

Members
-------

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

.. _`pipe_buf_get`:

pipe_buf_get
============

.. c:function:: void pipe_buf_get(struct pipe_inode_info *pipe, struct pipe_buffer *buf)

    get a reference to a pipe_buffer

    :param struct pipe_inode_info \*pipe:
        the pipe that the buffer belongs to

    :param struct pipe_buffer \*buf:
        the buffer to get a reference to

.. _`pipe_buf_release`:

pipe_buf_release
================

.. c:function:: void pipe_buf_release(struct pipe_inode_info *pipe, struct pipe_buffer *buf)

    put a reference to a pipe_buffer

    :param struct pipe_inode_info \*pipe:
        the pipe that the buffer belongs to

    :param struct pipe_buffer \*buf:
        the buffer to put a reference to

.. _`pipe_buf_confirm`:

pipe_buf_confirm
================

.. c:function:: int pipe_buf_confirm(struct pipe_inode_info *pipe, struct pipe_buffer *buf)

    verify contents of the pipe buffer

    :param struct pipe_inode_info \*pipe:
        the pipe that the buffer belongs to

    :param struct pipe_buffer \*buf:
        the buffer to confirm

.. _`pipe_buf_steal`:

pipe_buf_steal
==============

.. c:function:: int pipe_buf_steal(struct pipe_inode_info *pipe, struct pipe_buffer *buf)

    attempt to take ownership of a pipe_buffer

    :param struct pipe_inode_info \*pipe:
        the pipe that the buffer belongs to

    :param struct pipe_buffer \*buf:
        the buffer to attempt to steal

.. This file was automatic generated / don't edit.

