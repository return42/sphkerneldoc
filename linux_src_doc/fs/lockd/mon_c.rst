.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/lockd/mon.c

.. _`nsm_monitor`:

nsm_monitor
===========

.. c:function:: int nsm_monitor(const struct nlm_host *host)

    Notify a peer in case we reboot

    :param host:
        pointer to nlm_host of peer to notify
    :type host: const struct nlm_host \*

.. _`nsm_monitor.description`:

Description
-----------

If this peer is not already monitored, this function sends an
upcall to the local rpc.statd to record the name/address of
the peer to notify in case we reboot.

Returns zero if the peer is monitored by the local rpc.statd;
otherwise a negative errno value is returned.

.. _`nsm_unmonitor`:

nsm_unmonitor
=============

.. c:function:: void nsm_unmonitor(const struct nlm_host *host)

    Unregister peer notification

    :param host:
        pointer to nlm_host of peer to stop monitoring
    :type host: const struct nlm_host \*

.. _`nsm_unmonitor.description`:

Description
-----------

If this peer is monitored, this function sends an upcall to
tell the local rpc.statd not to send this peer a notification
when we reboot.

.. _`nsm_get_handle`:

nsm_get_handle
==============

.. c:function:: struct nsm_handle *nsm_get_handle(const struct net *net, const struct sockaddr *sap, const size_t salen, const char *hostname, const size_t hostname_len)

    Find or create a cached nsm_handle

    :param net:
        network namespace
    :type net: const struct net \*

    :param sap:
        pointer to socket address of handle to find
    :type sap: const struct sockaddr \*

    :param salen:
        length of socket address
    :type salen: const size_t

    :param hostname:
        pointer to C string containing hostname to find
    :type hostname: const char \*

    :param hostname_len:
        length of C string
    :type hostname_len: const size_t

.. _`nsm_get_handle.description`:

Description
-----------

Behavior is modulated by the global nsm_use_hostnames variable.

Returns a cached nsm_handle after bumping its ref count, or
returns a fresh nsm_handle if a handle that matches \ ``sap``\  and/or
\ ``hostname``\  cannot be found in the handle cache.  Returns NULL if
an error occurs.

.. _`nsm_reboot_lookup`:

nsm_reboot_lookup
=================

.. c:function:: struct nsm_handle *nsm_reboot_lookup(const struct net *net, const struct nlm_reboot *info)

    match NLMPROC_SM_NOTIFY arguments to an nsm_handle

    :param net:
        network namespace
    :type net: const struct net \*

    :param info:
        pointer to NLMPROC_SM_NOTIFY arguments
    :type info: const struct nlm_reboot \*

.. _`nsm_reboot_lookup.description`:

Description
-----------

Returns a matching nsm_handle if found in the nsm cache. The returned
nsm_handle's reference count is bumped. Otherwise returns NULL if some
error occurred.

.. _`nsm_release`:

nsm_release
===========

.. c:function:: void nsm_release(struct nsm_handle *nsm)

    Release an NSM handle

    :param nsm:
        pointer to handle to be released
    :type nsm: struct nsm_handle \*

.. This file was automatic generated / don't edit.

