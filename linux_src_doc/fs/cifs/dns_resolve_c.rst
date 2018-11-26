.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/cifs/dns_resolve.c

.. _`dns_resolve_server_name_to_ip`:

dns_resolve_server_name_to_ip
=============================

.. c:function:: int dns_resolve_server_name_to_ip(const char *unc, char **ip_addr)

    Resolve UNC server name to ip address.

    :param unc:
        UNC path specifying the server (with '/' as delimiter)
    :type unc: const char \*

    :param ip_addr:
        Where to return the IP address.
    :type ip_addr: char \*\*

.. _`dns_resolve_server_name_to_ip.description`:

Description
-----------

The IP address will be returned in string form, and the caller is
responsible for freeing it.

Returns length of result on success, -ve on error.

.. This file was automatic generated / don't edit.

