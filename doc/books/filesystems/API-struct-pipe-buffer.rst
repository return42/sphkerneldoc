.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-pipe-buffer:

==================
struct pipe_buffer
==================

*man struct pipe_buffer(9)*

*4.6.0-rc5*

a linux kernel pipe buffer


Synopsis
========

.. code-block:: c

    struct pipe_buffer {
      struct page * page;
      unsigned int offset;
      unsigned int len;
      const struct pipe_buf_operations * ops;
      unsigned int flags;
      unsigned long private;
    };


Members
=======

page
    the page containing the data for the pipe buffer

offset
    offset of data inside the ``page``

len
    length of data inside the ``page``

ops
    operations associated with this buffer. See ``pipe_buf_operations``.

flags
    pipe buffer flags. See above.

private
    private data owned by the ops.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
