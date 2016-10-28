.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/pipe.c

.. _`generic_pipe_buf_steal`:

generic_pipe_buf_steal
======================

.. c:function:: int generic_pipe_buf_steal(struct pipe_inode_info *pipe, struct pipe_buffer *buf)

    attempt to take ownership of a \ :c:type:`struct pipe_buffer <pipe_buffer>`

    :param struct pipe_inode_info \*pipe:
        the pipe that the buffer belongs to

    :param struct pipe_buffer \*buf:
        the buffer to attempt to steal

.. _`generic_pipe_buf_steal.description`:

Description
-----------

This function attempts to steal the \ :c:type:`struct page <page>`\  attached to
\ ``buf``\ . If successful, this function returns 0 and returns with
the page locked. The caller may then reuse the page for whatever
he wishes; the typical use is insertion into a different file
page cache.

.. _`generic_pipe_buf_get`:

generic_pipe_buf_get
====================

.. c:function:: void generic_pipe_buf_get(struct pipe_inode_info *pipe, struct pipe_buffer *buf)

    get a reference to a \ :c:type:`struct pipe_buffer <pipe_buffer>`\ 

    :param struct pipe_inode_info \*pipe:
        the pipe that the buffer belongs to

    :param struct pipe_buffer \*buf:
        the buffer to get a reference to

.. _`generic_pipe_buf_get.description`:

Description
-----------

This function grabs an extra reference to \ ``buf``\ . It's used in
in the \ :c:func:`tee`\  system call, when we duplicate the buffers in one
pipe into another.

.. _`generic_pipe_buf_confirm`:

generic_pipe_buf_confirm
========================

.. c:function:: int generic_pipe_buf_confirm(struct pipe_inode_info *info, struct pipe_buffer *buf)

    verify contents of the pipe buffer

    :param struct pipe_inode_info \*info:
        the pipe that the buffer belongs to

    :param struct pipe_buffer \*buf:
        the buffer to confirm

.. _`generic_pipe_buf_confirm.description`:

Description
-----------

This function does nothing, because the generic pipe code uses
pages that are always good when inserted into the pipe.

.. _`generic_pipe_buf_release`:

generic_pipe_buf_release
========================

.. c:function:: void generic_pipe_buf_release(struct pipe_inode_info *pipe, struct pipe_buffer *buf)

    put a reference to a \ :c:type:`struct pipe_buffer <pipe_buffer>`\ 

    :param struct pipe_inode_info \*pipe:
        the pipe that the buffer belongs to

    :param struct pipe_buffer \*buf:
        the buffer to put a reference to

.. _`generic_pipe_buf_release.description`:

Description
-----------

This function releases a reference to \ ``buf``\ .

.. This file was automatic generated / don't edit.

