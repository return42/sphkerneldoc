.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/auth.c

.. _`rpcauth_get_pseudoflavor`:

rpcauth_get_pseudoflavor
========================

.. c:function:: rpc_authflavor_t rpcauth_get_pseudoflavor(rpc_authflavor_t flavor, struct rpcsec_gss_info *info)

    check if security flavor is supported

    :param flavor:
        a security flavor
    :type flavor: rpc_authflavor_t

    :param info:
        a GSS mech OID, quality of protection, and service value
    :type info: struct rpcsec_gss_info \*

.. _`rpcauth_get_pseudoflavor.description`:

Description
-----------

Verifies that an appropriate kernel module is available or already loaded.
Returns an equivalent pseudoflavor, or RPC_AUTH_MAXFLAVOR if "flavor" is
not supported locally.

.. _`rpcauth_get_gssinfo`:

rpcauth_get_gssinfo
===================

.. c:function:: int rpcauth_get_gssinfo(rpc_authflavor_t pseudoflavor, struct rpcsec_gss_info *info)

    find GSS tuple matching a GSS pseudoflavor

    :param pseudoflavor:
        GSS pseudoflavor to match
    :type pseudoflavor: rpc_authflavor_t

    :param info:
        rpcsec_gss_info structure to fill in
    :type info: struct rpcsec_gss_info \*

.. _`rpcauth_get_gssinfo.description`:

Description
-----------

Returns zero and fills in "info" if pseudoflavor matches a
supported mechanism.

.. _`rpcauth_list_flavors`:

rpcauth_list_flavors
====================

.. c:function:: int rpcauth_list_flavors(rpc_authflavor_t *array, int size)

    discover registered flavors and pseudoflavors

    :param array:
        array to fill in
    :type array: rpc_authflavor_t \*

    :param size:
        size of "array"
    :type size: int

.. _`rpcauth_list_flavors.description`:

Description
-----------

Returns the number of array items filled in, or a negative errno.

The returned array is not sorted by any policy.  Callers should not
rely on the order of the items in the returned array.

.. This file was automatic generated / don't edit.

