.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/iwcm.c

.. _`iw_cm_check_wildcard`:

iw_cm_check_wildcard
====================

.. c:function:: void iw_cm_check_wildcard(struct sockaddr_storage *pm_addr, struct sockaddr_storage *cm_addr, struct sockaddr_storage *cm_outaddr)

    If IP address is 0 then use original

    :param pm_addr:
        sockaddr containing the ip to check for wildcard
    :type pm_addr: struct sockaddr_storage \*

    :param cm_addr:
        sockaddr containing the actual IP address
    :type cm_addr: struct sockaddr_storage \*

    :param cm_outaddr:
        sockaddr to set IP addr which leaving port
    :type cm_outaddr: struct sockaddr_storage \*

.. _`iw_cm_check_wildcard.description`:

Description
-----------

Checks the pm_addr for wildcard and then sets cm_outaddr's
IP to the actual (cm_addr).

.. _`iw_cm_map`:

iw_cm_map
=========

.. c:function:: int iw_cm_map(struct iw_cm_id *cm_id, bool active)

    Use portmapper to map the ports

    :param cm_id:
        connection manager pointer
    :type cm_id: struct iw_cm_id \*

    :param active:
        Indicates the active side when true
        returns nonzero for error only if \ :c:func:`iwpm_create_mapinfo`\  fails
    :type active: bool

.. _`iw_cm_map.description`:

Description
-----------

Tries to add a mapping for a port using the Portmapper. If
successful in mapping the IP/Port it will check the remote
mapped IP address for a wildcard IP address and replace the
zero IP address with the remote_addr.

.. This file was automatic generated / don't edit.

