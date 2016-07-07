.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dns_resolver/dns_query.c

.. _`dns_query`:

dns_query
=========

.. c:function:: int dns_query(const char *type, const char *name, size_t namelen, const char *options, char **_result, time64_t *_expiry)

    Query the DNS

    :param const char \*type:
        Query type (or NULL for straight host->IP lookup)

    :param const char \*name:
        Name to look up

    :param size_t namelen:
        Length of name

    :param const char \*options:
        Request options (or NULL if no options)

    :param char \*\*_result:
        Where to place the returned data.

    :param time64_t \*_expiry:
        Where to store the result expiry time (or NULL)

.. _`dns_query.description`:

Description
-----------

The data will be returned in the pointer at \*result, and the caller is
responsible for freeing it.

The description should be of the form "[<query_type>:]<domain_name>", and
the options need to be appropriate for the query type requested.  If no
query_type is given, then the query is a straight hostname to IP address
lookup.

The DNS resolution lookup is performed by upcalling to userspace by way of
requesting a key of type dns_resolver.

Returns the size of the result on success, -ve error code otherwise.

.. This file was automatic generated / don't edit.

