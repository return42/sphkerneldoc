.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ptlrpc/import.c

.. _`__import_set_state`:

__import_set_state
==================

.. c:function:: void __import_set_state(struct obd_import *imp, enum lustre_imp_state state)

    Helper function. Must be called under imp_lock.

    :param struct obd_import \*imp:
        *undescribed*

    :param enum lustre_imp_state state:
        *undescribed*

.. _`ptlrpc_set_import_discon`:

ptlrpc_set_import_discon
========================

.. c:function:: int ptlrpc_set_import_discon(struct obd_import *imp, __u32 conn_cnt)

    connected. \ ``imp``\  - import to be disconnected \ ``conn_cnt``\  - connection count (epoch) of the request that timed out and caused the disconnection.  In some cases, multiple inflight requests can fail to a single target (e.g. OST bulk requests) and if one has already caused a reconnection (increasing the import->conn_cnt) the older failure should not also cause a reconnection.  If zero it forces a reconnect.

    :param struct obd_import \*imp:
        *undescribed*

    :param __u32 conn_cnt:
        *undescribed*

.. _`ptlrpc_invalidate_import`:

ptlrpc_invalidate_import
========================

.. c:function:: void ptlrpc_invalidate_import(struct obd_import *imp)

    for all the RPC completions, and finally notify the obd to invalidate its state (ie cancel locks, clear pending requests, etc).

    :param struct obd_import \*imp:
        *undescribed*

.. _`import_select_connection`:

import_select_connection
========================

.. c:function:: int import_select_connection(struct obd_import *imp)

    present). We typically chose connection that we have not tried to connect to the longest

    :param struct obd_import \*imp:
        *undescribed*

.. _`ptlrpc_connect_import`:

ptlrpc_connect_import
=====================

.. c:function:: int ptlrpc_connect_import(struct obd_import *imp)

    initializing CONNECT RPC request and passing it to ptlrpcd for actual sending. Returns 0 on success or error code.

    :param struct obd_import \*imp:
        *undescribed*

.. _`ptlrpc_connect_interpret`:

ptlrpc_connect_interpret
========================

.. c:function:: int ptlrpc_connect_interpret(const struct lu_env *env, struct ptlrpc_request *request, void *data, int rc)

    Looks into returned status of connect operation and decides what to do with the import - i.e enter recovery, promote it to full state for normal operations of disconnect it due to an error.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct ptlrpc_request \*request:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param int rc:
        *undescribed*

.. _`completed_replay_interpret`:

completed_replay_interpret
==========================

.. c:function:: int completed_replay_interpret(const struct lu_env *env, struct ptlrpc_request *req, void *data, int rc)

    \see signal_completed_replay

    :param const struct lu_env \*env:
        *undescribed*

    :param struct ptlrpc_request \*req:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param int rc:
        *undescribed*

.. _`signal_completed_replay`:

signal_completed_replay
=======================

.. c:function:: int signal_completed_replay(struct obd_import *imp)

    Achieved by just sending a PING request

    :param struct obd_import \*imp:
        *undescribed*

.. _`ptlrpc_invalidate_import_thread`:

ptlrpc_invalidate_import_thread
===============================

.. c:function:: int ptlrpc_invalidate_import_thread(void *data)

    separate thread, so that whatever application happened to encounter a problem could still be killed or otherwise continue

    :param void \*data:
        *undescribed*

.. _`ptlrpc_import_recovery_state_machine`:

ptlrpc_import_recovery_state_machine
====================================

.. c:function:: int ptlrpc_import_recovery_state_machine(struct obd_import *imp)

    side recovery on import.

    :param struct obd_import \*imp:
        *undescribed*

.. _`ptlrpc_import_recovery_state_machine.description`:

Description
-----------

Typically we have two possibly paths. If we came to server and it is not
in recovery, we just enter IMP_EVICTED state, invalidate our import
state and reconnect from scratch.
If we came to server that is in recovery, we enter IMP_REPLAY import state.
We go through our list of requests to replay and send them to server one by
one.
After sending all request from the list we change import state to
IMP_REPLAY_LOCKS and re-request all the locks we believe we have from server
and also all the locks we don't yet have and wait for server to grant us.
After that we send a special "replay completed" request and change import
state to IMP_REPLAY_WAIT.
Upon receiving reply to that "replay completed" RPC we enter IMP_RECOVER
state and resend all requests from sending list.
After that we promote import to FULL state and send all delayed requests
and import is fully operational after that.

.. This file was automatic generated / don't edit.

