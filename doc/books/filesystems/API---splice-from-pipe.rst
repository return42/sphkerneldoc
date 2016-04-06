
.. _API---splice-from-pipe:

==================
__splice_from_pipe
==================

*man __splice_from_pipe(9)*

*4.6.0-rc1*

splice data from a pipe to given actor


Synopsis
========

.. c:function:: ssize_t __splice_from_pipe( struct pipe_inode_info * pipe, struct splice_desc * sd, splice_actor * actor )

Arguments
=========

``pipe``
    pipe to splice from

``sd``
    information to ``actor``

``actor``
    handler that splices the data


Description
===========

This function does little more than loop over the pipe and call ``actor`` to do the actual moving of a single struct pipe_buffer to the desired destination. See pipe_to_file,
pipe_to_sendpage, or pipe_to_user.
