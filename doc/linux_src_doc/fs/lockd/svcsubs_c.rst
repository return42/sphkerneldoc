.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/lockd/svcsubs.c

.. _`nlmsvc_invalidate_all`:

nlmsvc_invalidate_all
=====================

.. c:function:: void nlmsvc_invalidate_all( void)

    remove all locks held for clients

    :param  void:
        no arguments

.. _`nlmsvc_invalidate_all.description`:

Description
-----------

Release all locks held by NFS clients.

.. _`nlmsvc_unlock_all_by_sb`:

nlmsvc_unlock_all_by_sb
=======================

.. c:function:: int nlmsvc_unlock_all_by_sb(struct super_block *sb)

    release locks held on this file system

    :param struct super_block \*sb:
        super block

.. _`nlmsvc_unlock_all_by_sb.description`:

Description
-----------

Release all locks held by clients accessing this file system.

.. _`nlmsvc_unlock_all_by_ip`:

nlmsvc_unlock_all_by_ip
=======================

.. c:function:: int nlmsvc_unlock_all_by_ip(struct sockaddr *server_addr)

    release local locks by IP address

    :param struct sockaddr \*server_addr:
        server's IP address as seen by clients

.. _`nlmsvc_unlock_all_by_ip.description`:

Description
-----------

Release all locks held by clients accessing this host
via the passed in IP address.

.. This file was automatic generated / don't edit.

