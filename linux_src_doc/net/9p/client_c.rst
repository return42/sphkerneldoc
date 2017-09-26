.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/9p/client.c

.. _`parse_opts`:

parse_opts
==========

.. c:function:: int parse_opts(char *opts, struct p9_client *clnt)

    parse mount options into client structure

    :param char \*opts:
        options string passed from mount

    :param struct p9_client \*clnt:
        existing v9fs client information

.. _`parse_opts.description`:

Description
-----------

Return 0 upon success, -ERRNO upon failure

.. _`p9_tag_alloc`:

p9_tag_alloc
============

.. c:function:: struct p9_req_t *p9_tag_alloc(struct p9_client *c, u16 tag, unsigned int max_size)

    lookup/allocate a request by tag

    :param struct p9_client \*c:
        client session to lookup tag within

    :param u16 tag:
        numeric id for transaction

    :param unsigned int max_size:
        *undescribed*

.. _`p9_tag_alloc.description`:

Description
-----------

this is a simple array lookup, but will grow the
request_slots as necessary to accommodate transaction
ids which did not previously have a slot.

this code relies on the client spinlock to manage locks, its
possible we should switch to something else, but I'd rather
stick with something low-overhead for the common case.

.. _`p9_tag_lookup`:

p9_tag_lookup
=============

.. c:function:: struct p9_req_t *p9_tag_lookup(struct p9_client *c, u16 tag)

    lookup a request by tag

    :param struct p9_client \*c:
        client session to lookup tag within

    :param u16 tag:
        numeric id for transaction

.. _`p9_tag_init`:

p9_tag_init
===========

.. c:function:: int p9_tag_init(struct p9_client *c)

    setup tags structure and contents

    :param struct p9_client \*c:
        v9fs client struct

.. _`p9_tag_init.description`:

Description
-----------

This initializes the tags structure for each client instance.

.. _`p9_tag_cleanup`:

p9_tag_cleanup
==============

.. c:function:: void p9_tag_cleanup(struct p9_client *c)

    cleans up tags structure and reclaims resources

    :param struct p9_client \*c:
        v9fs client struct

.. _`p9_tag_cleanup.description`:

Description
-----------

This frees resources associated with the tags structure

.. _`p9_free_req`:

p9_free_req
===========

.. c:function:: void p9_free_req(struct p9_client *c, struct p9_req_t *r)

    free a request and clean-up as necessary c: client state r: request to release

    :param struct p9_client \*c:
        *undescribed*

    :param struct p9_req_t \*r:
        *undescribed*

.. _`p9_client_cb`:

p9_client_cb
============

.. c:function:: void p9_client_cb(struct p9_client *c, struct p9_req_t *req, int status)

    call back from transport to client c: client state

    :param struct p9_client \*c:
        *undescribed*

    :param struct p9_req_t \*req:
        *undescribed*

    :param int status:
        *undescribed*

.. _`p9_client_cb.req`:

req
---

request received

.. _`p9_parse_header`:

p9_parse_header
===============

.. c:function:: int p9_parse_header(struct p9_fcall *pdu, int32_t *size, int8_t *type, int16_t *tag, int rewind)

    parse header arguments out of a packet

    :param struct p9_fcall \*pdu:
        packet to parse

    :param int32_t \*size:
        size of packet

    :param int8_t \*type:
        type of request

    :param int16_t \*tag:
        tag of packet

    :param int rewind:
        set if we need to rewind offset afterwards

.. _`p9_check_errors`:

p9_check_errors
===============

.. c:function:: int p9_check_errors(struct p9_client *c, struct p9_req_t *req)

    check 9p packet for error return and process it

    :param struct p9_client \*c:
        current client instance

    :param struct p9_req_t \*req:
        request to parse and check for error conditions

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

    :param struct p9_client \*c:
        current client instance

    :param struct p9_req_t \*req:
        request to parse and check for error conditions

    :param struct iov_iter \*uidata:
        *undescribed*

    :param int in_hdrlen:
        Size of response protocol buffer.

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

    :param struct p9_client \*c:
        client state

    :param struct p9_req_t \*oldreq:
        request to cancel

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

    :param struct p9_client \*c:
        client session

    :param int8_t type:
        type of request

    :param const char \*fmt:
        protocol format string (see protocol.c)

    :param ellipsis ellipsis:
        variable arguments

.. _`p9_client_rpc.description`:

Description
-----------

Returns request structure (which client must free using p9_free_req)

.. _`p9_client_zc_rpc`:

p9_client_zc_rpc
================

.. c:function:: struct p9_req_t *p9_client_zc_rpc(struct p9_client *c, int8_t type, struct iov_iter *uidata, struct iov_iter *uodata, int inlen, int olen, int in_hdrlen, const char *fmt,  ...)

    issue a request and wait for a response

    :param struct p9_client \*c:
        client session

    :param int8_t type:
        type of request

    :param struct iov_iter \*uidata:
        destination for zero copy read

    :param struct iov_iter \*uodata:
        source for zero copy write

    :param int inlen:
        read buffer size

    :param int olen:
        write buffer size

    :param int in_hdrlen:
        *undescribed*

    :param const char \*fmt:
        protocol format string (see protocol.c)

    :param ellipsis ellipsis:
        variable arguments

.. _`p9_client_zc_rpc.description`:

Description
-----------

Returns request structure (which client must free using p9_free_req)

.. This file was automatic generated / don't edit.

