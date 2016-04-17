.. -*- coding: utf-8; mode: rst -*-

=========
recover.c
=========


.. _`ptlrpc_initiate_recovery`:

ptlrpc_initiate_recovery
========================

.. c:function:: void ptlrpc_initiate_recovery (struct obd_import *imp)

    :param struct obd_import \*imp:

        *undescribed*



.. _`ptlrpc_initiate_recovery.description`:

Description
-----------

This is done by just attempting a connect



.. _`ptlrpc_replay_next`:

ptlrpc_replay_next
==================

.. c:function:: int ptlrpc_replay_next (struct obd_import *imp, int *inflight)

    :param struct obd_import \*imp:

        *undescribed*

    :param int \*inflight:

        *undescribed*



.. _`ptlrpc_replay_next.description`:

Description
-----------

(based on what we have already replayed) and send it to server.



.. _`ptlrpc_resend`:

ptlrpc_resend
=============

.. c:function:: int ptlrpc_resend (struct obd_import *imp)

    :param struct obd_import \*imp:

        *undescribed*



.. _`ptlrpc_resend.description`:

Description
-----------

we completed replaying of requests and locks.



.. _`ptlrpc_wake_delayed`:

ptlrpc_wake_delayed
===================

.. c:function:: void ptlrpc_wake_delayed (struct obd_import *imp)

    :param struct obd_import \*imp:

        *undescribed*



.. _`ptlrpc_wake_delayed.description`:

Description
-----------

for resending



.. _`ptlrpc_set_import_active`:

ptlrpc_set_import_active
========================

.. c:function:: int ptlrpc_set_import_active (struct obd_import *imp, int active)

    :param struct obd_import \*imp:

        *undescribed*

    :param int active:

        *undescribed*



.. _`ptlrpc_set_import_active.description`:

Description
-----------

This should only be called by the ioctl interface, currently

 - the lctl deactivate and activate commands
 - echo 0/1 >> /sys/fs/lustre/osc/XXX/active
 - client umount -f (ll_umount_begin)

