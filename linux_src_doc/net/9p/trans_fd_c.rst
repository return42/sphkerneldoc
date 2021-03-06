.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/9p/trans_fd.c

.. _`p9_fd_opts`:

struct p9_fd_opts
=================

.. c:type:: struct p9_fd_opts

    per-transport options

.. _`p9_fd_opts.definition`:

Definition
----------

.. code-block:: c

    struct p9_fd_opts {
        int rfd;
        int wfd;
        u16 port;
        bool privport;
    }

.. _`p9_fd_opts.members`:

Members
-------

rfd
    file descriptor for reading (trans=fd)

wfd
    file descriptor for writing (trans=fd)

port
    port to connect to (trans=tcp)

privport
    *undescribed*

.. _`p9_conn`:

struct p9_conn
==============

.. c:type:: struct p9_conn

    fd mux connection state information

.. _`p9_conn.definition`:

Definition
----------

.. code-block:: c

    struct p9_conn {
        struct list_head mux_list;
        struct p9_client *client;
        int err;
        struct list_head req_list;
        struct list_head unsent_req_list;
        struct p9_req_t *rreq;
        struct p9_req_t *wreq;
        char tmp_buf[7];
        struct p9_fcall rc;
        int wpos;
        int wsize;
        char *wbuf;
        struct list_head poll_pending_link;
        struct p9_poll_wait poll_wait[MAXPOLLWADDR];
        poll_table pt;
        struct work_struct rq;
        struct work_struct wq;
        unsigned long wsched;
    }

.. _`p9_conn.members`:

Members
-------

mux_list
    list link for mux to manage multiple connections (?)

client
    reference to client instance for this connection

err
    error state

req_list
    accounting for requests which have been sent

unsent_req_list
    accounting for requests that haven't been sent

rreq
    *undescribed*

wreq
    *undescribed*

tmp_buf
    temporary buffer to read in header

rc
    temporary fcall for reading current frame

wpos
    write position for current frame

wsize
    amount of data to write for current frame

wbuf
    current write buffer

poll_pending_link
    pending links to be polled per conn

poll_wait
    array of wait_q's for various worker threads

pt
    poll state

rq
    current read work

wq
    current write work

wsched
    ????

.. _`p9_trans_fd`:

struct p9_trans_fd
==================

.. c:type:: struct p9_trans_fd

    transport state

.. _`p9_trans_fd.definition`:

Definition
----------

.. code-block:: c

    struct p9_trans_fd {
        struct file *rd;
        struct file *wr;
        struct p9_conn conn;
    }

.. _`p9_trans_fd.members`:

Members
-------

rd
    reference to file to read from

wr
    reference of file to write to

conn
    connection state reference

.. _`p9_conn_cancel`:

p9_conn_cancel
==============

.. c:function:: void p9_conn_cancel(struct p9_conn *m, int err)

    cancel all pending requests with error

    :param m:
        mux data
    :type m: struct p9_conn \*

    :param err:
        error code
    :type err: int

.. _`p9_fd_read`:

p9_fd_read
==========

.. c:function:: int p9_fd_read(struct p9_client *client, void *v, int len)

    read from a fd

    :param client:
        client instance
    :type client: struct p9_client \*

    :param v:
        buffer to receive data into
    :type v: void \*

    :param len:
        size of receive buffer
    :type len: int

.. _`p9_read_work`:

p9_read_work
============

.. c:function:: void p9_read_work(struct work_struct *work)

    called when there is some data to be read from a transport

    :param work:
        container of work to be done
    :type work: struct work_struct \*

.. _`p9_fd_write`:

p9_fd_write
===========

.. c:function:: int p9_fd_write(struct p9_client *client, void *v, int len)

    write to a socket

    :param client:
        client instance
    :type client: struct p9_client \*

    :param v:
        buffer to send data from
    :type v: void \*

    :param len:
        size of send buffer
    :type len: int

.. _`p9_write_work`:

p9_write_work
=============

.. c:function:: void p9_write_work(struct work_struct *work)

    called when a transport can send some data

    :param work:
        container for work to be done
    :type work: struct work_struct \*

.. _`p9_pollwait`:

p9_pollwait
===========

.. c:function:: void p9_pollwait(struct file *filp, wait_queue_head_t *wait_address, poll_table *p)

    add poll task to the wait queue

    :param filp:
        file pointer being polled
    :type filp: struct file \*

    :param wait_address:
        wait_q to block on
    :type wait_address: wait_queue_head_t \*

    :param p:
        poll state
    :type p: poll_table \*

.. _`p9_pollwait.description`:

Description
-----------

called by files poll operation to add v9fs-poll task to files wait queue

.. _`p9_conn_create`:

p9_conn_create
==============

.. c:function:: void p9_conn_create(struct p9_client *client)

    initialize the per-session mux data

    :param client:
        client instance
    :type client: struct p9_client \*

.. _`p9_conn_create.note`:

Note
----

Creates the polling task if this is the first session.

.. _`p9_poll_mux`:

p9_poll_mux
===========

.. c:function:: void p9_poll_mux(struct p9_conn *m)

    polls a mux and schedules read or write works if necessary

    :param m:
        connection to poll
    :type m: struct p9_conn \*

.. _`p9_fd_request`:

p9_fd_request
=============

.. c:function:: int p9_fd_request(struct p9_client *client, struct p9_req_t *req)

    send 9P request The function can sleep until the request is scheduled for sending. The function can be interrupted. Return from the function is not a guarantee that the request is sent successfully.

    :param client:
        client instance
    :type client: struct p9_client \*

    :param req:
        request to be sent
    :type req: struct p9_req_t \*

.. _`parse_opts`:

parse_opts
==========

.. c:function:: int parse_opts(char *params, struct p9_fd_opts *opts)

    parse mount options into p9_fd_opts structure

    :param params:
        options string passed from mount
    :type params: char \*

    :param opts:
        fd transport-specific structure to parse options into
    :type opts: struct p9_fd_opts \*

.. _`parse_opts.description`:

Description
-----------

Returns 0 upon success, -ERRNO upon failure

.. _`p9_conn_destroy`:

p9_conn_destroy
===============

.. c:function:: void p9_conn_destroy(struct p9_conn *m)

    cancels all pending requests of mux

    :param m:
        mux to destroy
    :type m: struct p9_conn \*

.. _`p9_fd_close`:

p9_fd_close
===========

.. c:function:: void p9_fd_close(struct p9_client *client)

    shutdown file descriptor transport

    :param client:
        client instance
    :type client: struct p9_client \*

.. _`p9_poll_workfn`:

p9_poll_workfn
==============

.. c:function:: void p9_poll_workfn(struct work_struct *work)

    poll worker thread

    :param work:
        work queue
    :type work: struct work_struct \*

.. _`p9_poll_workfn.description`:

Description
-----------

polls all v9fs transports for new events and queues the appropriate
work to the work queue

.. This file was automatic generated / don't edit.

