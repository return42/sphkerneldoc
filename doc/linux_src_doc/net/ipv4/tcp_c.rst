.. -*- coding: utf-8; mode: rst -*-

=====
tcp.c
=====


.. _`tcp_splice_read`:

tcp_splice_read
===============

.. c:function:: ssize_t tcp_splice_read (struct socket *sock, loff_t *ppos, struct pipe_inode_info *pipe, size_t len, unsigned int flags)

    splice data from TCP socket to a pipe

    :param struct socket \*sock:
        socket to splice from

    :param loff_t \*ppos:
        position (not valid)

    :param struct pipe_inode_info \*pipe:
        pipe to splice to

    :param size_t len:
        number of bytes to splice

    :param unsigned int flags:
        splice modifier flags



.. _`tcp_splice_read.description`:

Description
-----------

Will read pages from given socket and fill them into a pipe.



.. _`tcp_get_md5sig_pool`:

tcp_get_md5sig_pool
===================

.. c:function:: struct tcp_md5sig_pool *tcp_get_md5sig_pool ( void)

    get md5sig_pool for this user

    :param void:
        no arguments



.. _`tcp_get_md5sig_pool.description`:

Description
-----------


We use percpu structure, so if we succeed, we exit with preemption
and BH disabled, to make sure another thread or softirq handling
wont try to get same context.

