.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/9p/client.c

.. _`parse_opts`:

parse_opts
==========

.. c:function:: int parse_opts(char *opts, struct p9_client *clnt)

    parse mount options into client structure

    :param opts:
        options string passed from mount
    :type opts: char \*

    :param clnt:
        existing v9fs client information
    :type clnt: struct p9_client \*

.. _`parse_opts.description`:

Description
-----------

Return 0 upon success, -ERRNO upon failure

.. _`p9_tag_alloc`:

p9_tag_alloc
============

.. c:function:: struct p9_req_t *p9_tag_alloc(struct p9_client *c, int8_t type, unsigned int max_size)

    Allocate a new request.

    :param c:
        Client session.
    :type c: struct p9_client \*

    :param type:
        Transaction type.
    :type type: int8_t

    :param max_size:
        Maximum packet size for this request.
    :type max_size: unsigned int

.. _`p9_tag_alloc.context`:

Context
-------

Process context.

.. _`p9_tag_alloc.return`:

Return
------

Pointer to new request.

.. _`p9_tag_lookup`:

p9_tag_lookup
=============

.. c:function:: struct p9_req_t *p9_tag_lookup(struct p9_client *c, u16 tag)

    Look up a request by tag.

    :param c:
        Client session.
    :type c: struct p9_client \*

    :param tag:
        Transaction ID.
    :type tag: u16

.. _`p9_tag_lookup.context`:

Context
-------

Any context.

.. _`p9_tag_lookup.return`:

Return
------

A request, or \ ``NULL``\  if there is no request with that tag.

.. _`p9_tag_remove`:

p9_tag_remove
=============

.. c:function:: int p9_tag_remove(struct p9_client *c, struct p9_req_t *r)

    Remove a tag.

    :param c:
        Client session.
    :type c: struct p9_client \*

    :param r:
        Request of reference.
    :type r: struct p9_req_t \*

.. _`p9_tag_remove.context`:

Context
-------

Any context.

.. _`p9_tag_cleanup`:

p9_tag_cleanup
==============

.. c:function:: void p9_tag_cleanup(struct p9_client *c)

    cleans up tags structure and reclaims resources

    :param c:
        v9fs client struct
    :type c: struct p9_client \*

.. _`p9_tag_cleanup.description`:

Description
-----------

This frees resources associated with the tags structure

.. _`p9_client_cb`:

p9_client_cb
============

.. c:function:: void p9_client_cb(struct p9_client *c, struct p9_req_t *req, int status)

    call back from transport to client c: client state

    :param c:
        *undescribed*
    :type c: struct p9_client \*

    :param req:
        *undescribed*
    :type req: struct p9_req_t \*

    :param status:
        *undescribed*
    :type status: int

.. _`p9_client_cb.req`:

req
---

request received

.. _`p9_parse_header`:

p9_parse_header
===============

.. c:function:: int p9_parse_header(struct p9_fcall *pdu, int32_t *size, int8_t *type, int16_t *tag, int rewind)

    parse header arguments out of a packet

    :param pdu:
        packet to parse
    :type pdu: struct p9_fcall \*

    :param size:
        size of packet
    :type size: int32_t \*

    :param type:
        type of request
    :type type: int8_t \*

    :param tag:
        tag of packet
    :type tag: int16_t \*

    :param rewind:
        set if we need to rewind offset afterwards
    :type rewind: int

.. _`p9_check_errors`:

p9_check_errors
===============

.. c:function:: int p9_check_errors(struct p9_client *c, struct p9_req_t *req)

    check 9p packet for error return and process it

    :param c:
        current client instance
    :type c: struct p9_client \*

    :param req:
        request to parse and check for error conditions
    :type req: struct p9_req_t \*

.. _`p9_check_errors.description`:

Description
-----------

returns error code if one is discovered, otherwise returns 0

this will have to be more complicated if we have multiple
error packet types

.. _`p9_check_zc_errors`:

p9_check_zc_errors
==================

.. c:function:: int p9_check_zc_errors(struct p9_client *c, struct p9_req_t *req, struct iov_iter *uidata, int in_hdrlen)

    check 9p packet for error return and process it

    :param c:
        current client instance
    :type c: struct p9_client \*

    :param req:
        request to parse and check for error conditions
    :type req: struct p9_req_t \*

    :param uidata:
        *undescribed*
    :type uidata: struct iov_iter \*

    :param in_hdrlen:
        Size of response protocol buffer.
    :type in_hdrlen: int

.. _`p9_check_zc_errors.description`:

Description
-----------

returns error code if one is discovered, otherwise returns 0

this will have to be more complicated if we have multiple
error packet types

.. _`p9_client_flush`:

p9_client_flush
===============

.. c:function:: int p9_client_flush(struct p9_client *c, struct p9_req_t *oldreq)

    flush (cancel) a request

    :param c:
        client state
    :type c: struct p9_client \*

    :param oldreq:
        request to cancel
    :type oldreq: struct p9_req_t \*

.. _`p9_client_flush.description`:

Description
-----------

This sents a flush for a particular request and links
the flush request to the original request.  The current
code only supports a single flush request although the protocol
allows for multiple flush requests to be sent for a single request.

.. _`p9_client_rpc`:

p9_client_rpc
=============

.. c:function:: struct p9_req_t *p9_client_rpc(struct p9_client *c, int8_t type, const char *fmt,  ...)

    issue a request and wait for a response

    :param c:
        client session
    :type c: struct p9_client \*

    :param type:
        type of request
    :type type: int8_t

    :param fmt:
        protocol format string (see protocol.c)
    :type fmt: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`p9_client_rpc.description`:

Description
-----------

Returns request structure (which client must free using p9_tag_remove)

.. _`p9_client_zc_rpc`:

p9_client_zc_rpc
================

.. c:function:: struct p9_req_t *p9_client_zc_rpc(struct p9_client *c, int8_t type, struct iov_iter *uidata, struct iov_iter *uodata, int inlen, int olen, int in_hdrlen, const char *fmt,  ...)

    issue a request and wait for a response

    :param c:
        client session
    :type c: struct p9_client \*

    :param type:
        type of request
    :type type: int8_t

    :param uidata:
        destination for zero copy read
    :type uidata: struct iov_iter \*

    :param uodata:
        source for zero copy write
    :type uodata: struct iov_iter \*

    :param inlen:
        read buffer size
    :type inlen: int

    :param olen:
        write buffer size
    :type olen: int

    :param in_hdrlen:
        *undescribed*
    :type in_hdrlen: int

    :param fmt:
        protocol format string (see protocol.c)
    :type fmt: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`p9_client_zc_rpc.description`:

Description
-----------

Returns request structure (which client must free using p9_tag_remove)

.. This file was automatic generated / don't edit.

