.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ptlrpc/recover.c

.. _`ptlrpc_initiate_recovery`:

ptlrpc_initiate_recovery
========================

.. c:function:: void ptlrpc_initiate_recovery(struct obd_import *imp)

    This is done by just attempting a connect

    :param struct obd_import \*imp:
        *undescribed*

.. _`ptlrpc_replay_next`:

ptlrpc_replay_next
==================

.. c:function:: int ptlrpc_replay_next(struct obd_import *imp, int *inflight)

    (based on what we have already replayed) and send it to server.

    :param struct obd_import \*imp:
        *undescribed*

    :param int \*inflight:
        *undescribed*

.. _`ptlrpc_resend`:

ptlrpc_resend
=============

.. c:function:: int ptlrpc_resend(struct obd_import *imp)

    we completed replaying of requests and locks.

    :param struct obd_import \*imp:
        *undescribed*

.. _`ptlrpc_wake_delayed`:

ptlrpc_wake_delayed
===================

.. c:function:: void ptlrpc_wake_delayed(struct obd_import *imp)

    for resending

    :param struct obd_import \*imp:
        *undescribed*

.. _`ptlrpc_set_import_active`:

ptlrpc_set_import_active
========================

.. c:function:: int ptlrpc_set_import_active(struct obd_import *imp, int active)

    This should only be called by the ioctl interface, currently - the lctl deactivate and activate commands - echo 0/1 >> /sys/fs/lustre/osc/XXX/active - client umount -f (ll_umount_begin)

    :param struct obd_import \*imp:
        *undescribed*

    :param int active:
        *undescribed*

.. This file was automatic generated / don't edit.

