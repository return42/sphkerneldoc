.. -*- coding: utf-8; mode: rst -*-

=========
lib-ptl.c
=========


.. _`lnetsetlazyportal`:

LNetSetLazyPortal
=================

.. c:function:: int LNetSetLazyPortal (int portal)

    :param int portal:

        *undescribed*



.. _`lnetsetlazyportal.description`:

Description
-----------


This portal attribute only affects incoming PUT requests to the portal,
and is off by default. By default, if there's no matching MD for an
incoming PUT request, it is simply dropped. With the lazy attribute on,
such requests are queued indefinitely until either a matching MD is
posted to the portal or the lazy attribute is turned off.

It would prevent dropped requests, however it should be regarded as the
last line of defense - i.e. users must keep a close watch on active
buffers on a lazy portal and once it becomes too low post more buffers as
soon as possible. This is because delayed requests usually have detrimental
effects on underlying network connections. A few delayed requests often
suffice to bring an underlying connection to a complete halt, due to flow
control mechanisms.

There's also a DOS attack risk. If users don't post match-all MDs on a
lazy portal, a malicious peer can easily stop a service by sending some
PUT requests with match bits that won't match any MD. A routed server is
especially vulnerable since the connections to its neighbor routers are
shared among all clients.

\param portal Index of the portal to enable the lazy attribute on.

\retval 0       On success.
\retval -EINVAL If \a portal is not a valid index.



.. _`lnetclearlazyportal`:

LNetClearLazyPortal
===================

.. c:function:: int LNetClearLazyPortal (int portal)

    :param int portal:

        *undescribed*



.. _`lnetclearlazyportal.description`:

Description
-----------

if any, will be all dropped when this function returns.

\param portal Index of the portal to disable the lazy attribute on.

\retval 0       On success.
\retval -EINVAL If \a portal is not a valid index.

