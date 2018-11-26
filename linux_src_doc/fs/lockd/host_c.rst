.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/lockd/host.c

.. _`nlmclnt_lookup_host`:

nlmclnt_lookup_host
===================

.. c:function:: struct nlm_host *nlmclnt_lookup_host(const struct sockaddr *sap, const size_t salen, const unsigned short protocol, const u32 version, const char *hostname, int noresvport, struct net *net)

    Find an NLM host handle matching a remote server

    :param sap:
        network address of server
    :type sap: const struct sockaddr \*

    :param salen:
        length of server address
    :type salen: const size_t

    :param protocol:
        transport protocol to use
    :type protocol: const unsigned short

    :param version:
        NLM protocol version
    :type version: const u32

    :param hostname:
        '\0'-terminated hostname of server
    :type hostname: const char \*

    :param noresvport:
        1 if non-privileged port should be used
    :type noresvport: int

    :param net:
        *undescribed*
    :type net: struct net \*

.. _`nlmclnt_lookup_host.description`:

Description
-----------

Returns an nlm_host structure that matches the passed-in
[server address, transport protocol, NLM version, server hostname].
If one doesn't already exist in the host cache, a new handle is
created and returned.

.. _`nlmclnt_release_host`:

nlmclnt_release_host
====================

.. c:function:: void nlmclnt_release_host(struct nlm_host *host)

    release client nlm_host

    :param host:
        nlm_host to release
    :type host: struct nlm_host \*

.. _`nlmsvc_lookup_host`:

nlmsvc_lookup_host
==================

.. c:function:: struct nlm_host *nlmsvc_lookup_host(const struct svc_rqst *rqstp, const char *hostname, const size_t hostname_len)

    Find an NLM host handle matching a remote client

    :param rqstp:
        incoming NLM request
    :type rqstp: const struct svc_rqst \*

    :param hostname:
        name of client host
    :type hostname: const char \*

    :param hostname_len:
        length of client hostname
    :type hostname_len: const size_t

.. _`nlmsvc_lookup_host.description`:

Description
-----------

Returns an nlm_host structure that matches the [client address,
transport protocol, NLM version, client hostname] of the passed-in
NLM request.  If one doesn't already exist in the host cache, a
new handle is created and returned.

Before possibly creating a new nlm_host, construct a sockaddr
for a specific source address in case the local system has
multiple network addresses.  The family of the address in
rq_daddr is guaranteed to be the same as the family of the
address in rq_addr, so it's safe to use the same family for
the source address.

.. _`nlmsvc_release_host`:

nlmsvc_release_host
===================

.. c:function:: void nlmsvc_release_host(struct nlm_host *host)

    release server nlm_host

    :param host:
        nlm_host to release
    :type host: struct nlm_host \*

.. _`nlmsvc_release_host.description`:

Description
-----------

Host is destroyed later in \ :c:func:`nlm_gc_host`\ .

.. _`nlm_host_rebooted`:

nlm_host_rebooted
=================

.. c:function:: void nlm_host_rebooted(const struct net *net, const struct nlm_reboot *info)

    Release all resources held by rebooted host

    :param net:
        network namespace
    :type net: const struct net \*

    :param info:
        pointer to decoded results of NLM_SM_NOTIFY call
    :type info: const struct nlm_reboot \*

.. _`nlm_host_rebooted.description`:

Description
-----------

We were notified that the specified host has rebooted.  Release
all resources held by that peer.

.. This file was automatic generated / don't edit.

