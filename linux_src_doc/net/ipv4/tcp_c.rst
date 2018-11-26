.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv4/tcp.c

.. _`tcp_splice_read`:

tcp_splice_read
===============

.. c:function:: ssize_t tcp_splice_read(struct socket *sock, loff_t *ppos, struct pipe_inode_info *pipe, size_t len, unsigned int flags)

    splice data from TCP socket to a pipe

    :param sock:
        socket to splice from
    :type sock: struct socket \*

    :param ppos:
        position (not valid)
    :type ppos: loff_t \*

    :param pipe:
        pipe to splice to
    :type pipe: struct pipe_inode_info \*

    :param len:
        number of bytes to splice
    :type len: size_t

    :param flags:
        splice modifier flags
    :type flags: unsigned int

.. _`tcp_splice_read.description`:

Description
-----------

Will read pages from given socket and fill them into a pipe.

.. _`tcp_get_md5sig_pool`:

tcp_get_md5sig_pool
===================

.. c:function:: struct tcp_md5sig_pool *tcp_get_md5sig_pool( void)

    get md5sig_pool for this user

    :param void:
        no arguments
    :type void: 

.. _`tcp_get_md5sig_pool.description`:

Description
-----------

We use percpu structure, so if we succeed, we exit with preemption
and BH disabled, to make sure another thread or softirq handling
wont try to get same context.

.. This file was automatic generated / don't edit.

