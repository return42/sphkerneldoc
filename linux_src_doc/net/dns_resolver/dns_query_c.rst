.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dns_resolver/dns_query.c

.. _`dns_query`:

dns_query
=========

.. c:function:: int dns_query(const char *type, const char *name, size_t namelen, const char *options, char **_result, time64_t *_expiry)

    Query the DNS

    :param type:
        Query type (or NULL for straight host->IP lookup)
    :type type: const char \*

    :param name:
        Name to look up
    :type name: const char \*

    :param namelen:
        Length of name
    :type namelen: size_t

    :param options:
        Request options (or NULL if no options)
    :type options: const char \*

    :param _result:
        Where to place the returned data (or NULL)
    :type _result: char \*\*

    :param _expiry:
        Where to store the result expiry time (or NULL)
    :type _expiry: time64_t \*

.. _`dns_query.description`:

Description
-----------

The data will be returned in the pointer at \*result, if provided, and the
caller is responsible for freeing it.

The description should be of the form "[<query_type>:]<domain_name>", and
the options need to be appropriate for the query type requested.  If no
query_type is given, then the query is a straight hostname to IP address
lookup.

The DNS resolution lookup is performed by upcalling to userspace by way of
requesting a key of type dns_resolver.

Returns the size of the result on success, -ve error code otherwise.

.. This file was automatic generated / don't edit.

