.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/auth_gss/gss_mech_switch.c

.. _`gss_mech_register`:

gss_mech_register
=================

.. c:function:: int gss_mech_register(struct gss_api_mech *gm)

    register a GSS mechanism

    :param struct gss_api_mech \*gm:
        GSS mechanism handle

.. _`gss_mech_register.description`:

Description
-----------

Returns zero if successful, or a negative errno.

.. _`gss_mech_unregister`:

gss_mech_unregister
===================

.. c:function:: void gss_mech_unregister(struct gss_api_mech *gm)

    release a GSS mechanism

    :param struct gss_api_mech \*gm:
        GSS mechanism handle

.. _`gss_mech_list_pseudoflavors`:

gss_mech_list_pseudoflavors
===========================

.. c:function:: int gss_mech_list_pseudoflavors(rpc_authflavor_t *array_ptr, int size)

    Discover registered GSS pseudoflavors

    :param rpc_authflavor_t \*array_ptr:
        *undescribed*

    :param int size:
        size of "array"

.. _`gss_mech_list_pseudoflavors.description`:

Description
-----------

Returns the number of array items filled in, or a negative errno.

The returned array is not sorted by any policy.  Callers should not
rely on the order of the items in the returned array.

.. _`gss_svc_to_pseudoflavor`:

gss_svc_to_pseudoflavor
=======================

.. c:function:: rpc_authflavor_t gss_svc_to_pseudoflavor(struct gss_api_mech *gm, u32 qop, u32 service)

    map a GSS service number to a pseudoflavor

    :param struct gss_api_mech \*gm:
        GSS mechanism handle

    :param u32 qop:
        GSS quality-of-protection value

    :param u32 service:
        GSS service value

.. _`gss_svc_to_pseudoflavor.description`:

Description
-----------

Returns a matching security flavor, or RPC_AUTH_MAXFLAVOR if none is found.

.. _`gss_mech_info2flavor`:

gss_mech_info2flavor
====================

.. c:function:: rpc_authflavor_t gss_mech_info2flavor(struct rpcsec_gss_info *info)

    look up a pseudoflavor given a GSS tuple

    :param struct rpcsec_gss_info \*info:
        a GSS mech OID, quality of protection, and service value

.. _`gss_mech_info2flavor.description`:

Description
-----------

Returns a matching pseudoflavor, or RPC_AUTH_MAXFLAVOR if the tuple is
not supported.

.. _`gss_mech_flavor2info`:

gss_mech_flavor2info
====================

.. c:function:: int gss_mech_flavor2info(rpc_authflavor_t pseudoflavor, struct rpcsec_gss_info *info)

    look up a GSS tuple for a given pseudoflavor

    :param rpc_authflavor_t pseudoflavor:
        GSS pseudoflavor to match

    :param struct rpcsec_gss_info \*info:
        rpcsec_gss_info structure to fill in

.. _`gss_mech_flavor2info.description`:

Description
-----------

Returns zero and fills in "info" if pseudoflavor matches a
supported mechanism.  Otherwise a negative errno is returned.

.. This file was automatic generated / don't edit.

