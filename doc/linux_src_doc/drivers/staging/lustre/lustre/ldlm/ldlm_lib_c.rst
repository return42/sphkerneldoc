.. -*- coding: utf-8; mode: rst -*-

==========
ldlm_lib.c
==========


.. _`debug_subsystem`:

DEBUG_SUBSYSTEM
===============

.. c:function:: DEBUG_SUBSYSTEM ()



.. _`debug_subsystem.todo`:

TODO
----

This code more logically belongs in the ptlrpc module than in ldlm and
should be moved.



.. _`client_import_find_conn`:

client_import_find_conn
=======================

.. c:function:: int client_import_find_conn (struct obd_import *imp, lnet_nid_t peer, struct obd_uuid *uuid)

    :param struct obd_import \*imp:

        *undescribed*

    :param lnet_nid_t peer:

        *undescribed*

    :param struct obd_uuid \*uuid:

        *undescribed*



.. _`client_import_find_conn.description`:

Description
-----------

to find a conn uuid of \a imp which can reach \a peer.



.. _`target_pack_pool_reply`:

target_pack_pool_reply
======================

.. c:function:: int target_pack_pool_reply (struct ptlrpc_request *req)

    :param struct ptlrpc_request \*req:

        *undescribed*



.. _`ldlm_error2errno`:

ldlm_error2errno
================

.. c:function:: int ldlm_error2errno (enum ldlm_error error)

    :param enum ldlm_error error:

        *undescribed*



.. _`ldlm_error2errno.description`:

Description
-----------

not escape to the user level.

