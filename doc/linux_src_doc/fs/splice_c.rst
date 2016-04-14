.. -*- coding: utf-8; mode: rst -*-

========
splice.c
========

.. _`splice_to_pipe`:

splice_to_pipe
==============

.. c:function:: ssize_t splice_to_pipe (struct pipe_inode_info *pipe, struct splice_pipe_desc *spd)

    fill passed data into a pipe

    :param struct pipe_inode_info \*pipe:
        pipe to fill

    :param struct splice_pipe_desc \*spd:
        data to fill


.. _`splice_to_pipe.description`:

Description
-----------

Description::

   ``spd`` contains a map of pages and len/offset tuples, along with
   the struct pipe_buf_operations associated with these pages. This
   function will link that data to the pipe.


.. _`generic_file_splice_read`:

generic_file_splice_read
========================

.. c:function:: ssize_t generic_file_splice_read (struct file *in, loff_t *ppos, struct pipe_inode_info *pipe, size_t len, unsigned int flags)

    splice data from file to a pipe

    :param struct file \*in:
        file to splice from

    :param loff_t \*ppos:
        position in ``in``

    :param struct pipe_inode_info \*pipe:
        pipe to splice to

    :param size_t len:
        number of bytes to splice

    :param unsigned int flags:
        splice modifier flags


.. _`generic_file_splice_read.description`:

Description
-----------

Description::

   Will read pages from given file and fill them into a pipe. Can be
   used as long as the address_space operations for the source implements
   a :c:func:`readpage` hook.


.. _`splice_from_pipe_feed`:

splice_from_pipe_feed
=====================

.. c:function:: int splice_from_pipe_feed (struct pipe_inode_info *pipe, struct splice_desc *sd, splice_actor *actor)

    feed available data from a pipe to a file

    :param struct pipe_inode_info \*pipe:
        pipe to splice from

    :param struct splice_desc \*sd:
        information to ``actor``

    :param splice_actor \*actor:
        handler that splices the data


.. _`splice_from_pipe_feed.description`:

Description
-----------

Description::

   This function loops over the pipe and calls ``actor`` to do the
   actual moving of a single struct pipe_buffer to the desired
   destination.  It returns when there's no more buffers left in
   the pipe or if the requested number of bytes (\ ``sd``\ ->total_len)
   have been copied.  It returns a positive number (one) if the
   pipe needs to be filled with more data, zero if the required
   number of bytes have been copied and -errno on error.

   This, together with splice_from_pipe_{begin,end,next}, may be
   used to implement the functionality of :c:func:`__splice_from_pipe` when
   locking is required around copying the pipe buffers to the
   destination.


.. _`splice_from_pipe_next`:

splice_from_pipe_next
=====================

.. c:function:: int splice_from_pipe_next (struct pipe_inode_info *pipe, struct splice_desc *sd)

    wait for some data to splice from

    :param struct pipe_inode_info \*pipe:
        pipe to splice from

    :param struct splice_desc \*sd:
        information about the splice operation


.. _`splice_from_pipe_next.description`:

Description
-----------

Description::

   This function will wait for some data and return a positive
   value (one) if pipe buffers are available.  It will return zero
   or -errno if no more data needs to be spliced.


.. _`splice_from_pipe_begin`:

splice_from_pipe_begin
======================

.. c:function:: void splice_from_pipe_begin (struct splice_desc *sd)

    start splicing from pipe

    :param struct splice_desc \*sd:
        information about the splice operation


.. _`splice_from_pipe_begin.description`:

Description
-----------

Description::

   This function should be called before a loop containing
   :c:func:`splice_from_pipe_next` and :c:func:`splice_from_pipe_feed` to
   initialize the necessary fields of ``sd``\ .


.. _`splice_from_pipe_end`:

splice_from_pipe_end
====================

.. c:function:: void splice_from_pipe_end (struct pipe_inode_info *pipe, struct splice_desc *sd)

    finish splicing from pipe

    :param struct pipe_inode_info \*pipe:
        pipe to splice from

    :param struct splice_desc \*sd:
        information about the splice operation


.. _`splice_from_pipe_end.description`:

Description
-----------

Description::

   This function will wake up pipe writers if necessary.  It should
   be called after a loop containing :c:func:`splice_from_pipe_next` and
   :c:func:`splice_from_pipe_feed`.


.. _`__splice_from_pipe`:

__splice_from_pipe
==================

.. c:function:: ssize_t __splice_from_pipe (struct pipe_inode_info *pipe, struct splice_desc *sd, splice_actor *actor)

    splice data from a pipe to given actor

    :param struct pipe_inode_info \*pipe:
        pipe to splice from

    :param struct splice_desc \*sd:
        information to ``actor``

    :param splice_actor \*actor:
        handler that splices the data


.. _`__splice_from_pipe.description`:

Description
-----------

Description::

   This function does little more than loop over the pipe and call
   ``actor`` to do the actual moving of a single struct pipe_buffer to
   the desired destination. See pipe_to_file, pipe_to_sendpage, or
   pipe_to_user.


.. _`splice_from_pipe`:

splice_from_pipe
================

.. c:function:: ssize_t splice_from_pipe (struct pipe_inode_info *pipe, struct file *out, loff_t *ppos, size_t len, unsigned int flags, splice_actor *actor)

    splice data from a pipe to a file

    :param struct pipe_inode_info \*pipe:
        pipe to splice from

    :param struct file \*out:
        file to splice to

    :param loff_t \*ppos:
        position in ``out``

    :param size_t len:
        how many bytes to splice

    :param unsigned int flags:
        splice modifier flags

    :param splice_actor \*actor:
        handler that splices the data


.. _`splice_from_pipe.description`:

Description
-----------

Description::

   See __splice_from_pipe. This function locks the pipe inode,
   otherwise it's identical to :c:func:`__splice_from_pipe`.


.. _`iter_file_splice_write`:

iter_file_splice_write
======================

.. c:function:: ssize_t iter_file_splice_write (struct pipe_inode_info *pipe, struct file *out, loff_t *ppos, size_t len, unsigned int flags)

    splice data from a pipe to a file

    :param struct pipe_inode_info \*pipe:
        pipe info

    :param struct file \*out:
        file to write to

    :param loff_t \*ppos:
        position in ``out``

    :param size_t len:
        number of bytes to splice

    :param unsigned int flags:
        splice modifier flags


.. _`iter_file_splice_write.description`:

Description
-----------

Description::

   Will either move or copy pages (determined by ``flags`` options) from
   the given pipe inode to the given file.
   This one is ->write_iter-based.


.. _`generic_splice_sendpage`:

generic_splice_sendpage
=======================

.. c:function:: ssize_t generic_splice_sendpage (struct pipe_inode_info *pipe, struct file *out, loff_t *ppos, size_t len, unsigned int flags)

    splice data from a pipe to a socket

    :param struct pipe_inode_info \*pipe:
        pipe to splice from

    :param struct file \*out:
        socket to write to

    :param loff_t \*ppos:
        position in ``out``

    :param size_t len:
        number of bytes to splice

    :param unsigned int flags:
        splice modifier flags


.. _`generic_splice_sendpage.description`:

Description
-----------

Description::

   Will send ``len`` bytes from the pipe to a network socket. No data copying
   is involved.


.. _`splice_direct_to_actor`:

splice_direct_to_actor
======================

.. c:function:: ssize_t splice_direct_to_actor (struct file *in, struct splice_desc *sd, splice_direct_actor *actor)

    splices data directly between two non-pipes

    :param struct file \*in:
        file to splice from

    :param struct splice_desc \*sd:
        actor information on where to splice to

    :param splice_direct_actor \*actor:
        handles the data splicing


.. _`splice_direct_to_actor.description`:

Description
-----------

Description::

   This is a special case helper to splice directly between two
   points, without requiring an explicit pipe. Internally an allocated
   pipe is cached in the process, and reused during the lifetime of
   that process.


.. _`do_splice_direct`:

do_splice_direct
================

.. c:function:: long do_splice_direct (struct file *in, loff_t *ppos, struct file *out, loff_t *opos, size_t len, unsigned int flags)

    splices data directly between two files

    :param struct file \*in:
        file to splice from

    :param loff_t \*ppos:
        input file offset

    :param struct file \*out:
        file to splice to

    :param loff_t \*opos:
        output file offset

    :param size_t len:
        number of bytes to splice

    :param unsigned int flags:
        splice modifier flags


.. _`do_splice_direct.description`:

Description
-----------

Description::

   For use by :c:func:`do_sendfile`. splice can easily emulate sendfile, but
   doing it in the application would incur an extra system call
   (splice in + splice out, as compared to just :c:func:`sendfile`). So this helper
   can splice directly through a process-private pipe.

