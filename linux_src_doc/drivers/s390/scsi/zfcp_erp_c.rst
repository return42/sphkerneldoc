.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/scsi/zfcp_erp.c

.. _`zfcp_erp_adapter_reopen`:

zfcp_erp_adapter_reopen
=======================

.. c:function:: void zfcp_erp_adapter_reopen(struct zfcp_adapter *adapter, int clear, char *id)

    Reopen adapter.

    :param struct zfcp_adapter \*adapter:
        Adapter to reopen.

    :param int clear:
        Status flags to clear.

    :param char \*id:
        Id for debug trace event.

.. _`zfcp_erp_adapter_shutdown`:

zfcp_erp_adapter_shutdown
=========================

.. c:function:: void zfcp_erp_adapter_shutdown(struct zfcp_adapter *adapter, int clear, char *id)

    Shutdown adapter.

    :param struct zfcp_adapter \*adapter:
        Adapter to shut down.

    :param int clear:
        Status flags to clear.

    :param char \*id:
        Id for debug trace event.

.. _`zfcp_erp_port_shutdown`:

zfcp_erp_port_shutdown
======================

.. c:function:: void zfcp_erp_port_shutdown(struct zfcp_port *port, int clear, char *id)

    Shutdown port

    :param struct zfcp_port \*port:
        Port to shut down.

    :param int clear:
        Status flags to clear.

    :param char \*id:
        Id for debug trace event.

.. _`zfcp_erp_port_forced_reopen`:

zfcp_erp_port_forced_reopen
===========================

.. c:function:: void zfcp_erp_port_forced_reopen(struct zfcp_port *port, int clear, char *id)

    Forced close of port and open again

    :param struct zfcp_port \*port:
        Port to force close and to reopen.

    :param int clear:
        Status flags to clear.

    :param char \*id:
        Id for debug trace event.

.. _`zfcp_erp_port_reopen`:

zfcp_erp_port_reopen
====================

.. c:function:: int zfcp_erp_port_reopen(struct zfcp_port *port, int clear, char *id)

    trigger remote port recovery

    :param struct zfcp_port \*port:
        port to recover

    :param int clear:
        *undescribed*

    :param char \*id:
        Id for debug trace event.

.. _`zfcp_erp_port_reopen.description`:

Description
-----------

Returns 0 if recovery has been triggered, < 0 if not.

.. _`zfcp_erp_lun_reopen`:

zfcp_erp_lun_reopen
===================

.. c:function:: void zfcp_erp_lun_reopen(struct scsi_device *sdev, int clear, char *id)

    initiate reopen of a LUN

    :param struct scsi_device \*sdev:
        SCSI device / LUN to be reopened

    :param int clear:
        *undescribed*

    :param char \*id:
        Id for debug trace event.

.. _`zfcp_erp_lun_reopen.return`:

Return
------

0 on success, < 0 on error

.. _`zfcp_erp_lun_shutdown`:

zfcp_erp_lun_shutdown
=====================

.. c:function:: void zfcp_erp_lun_shutdown(struct scsi_device *sdev, int clear, char *id)

    Shutdown LUN

    :param struct scsi_device \*sdev:
        SCSI device / LUN to shut down.

    :param int clear:
        Status flags to clear.

    :param char \*id:
        Id for debug trace event.

.. _`zfcp_erp_lun_shutdown_wait`:

zfcp_erp_lun_shutdown_wait
==========================

.. c:function:: void zfcp_erp_lun_shutdown_wait(struct scsi_device *sdev, char *id)

    Shutdown LUN and wait for erp completion

    :param struct scsi_device \*sdev:
        SCSI device / LUN to shut down.

    :param char \*id:
        Id for debug trace event.

.. _`zfcp_erp_lun_shutdown_wait.description`:

Description
-----------

Do not acquire a reference for the LUN when creating the ERP
action. It is safe, because this function waits for the ERP to
complete first. This allows to shutdown the LUN, even when the SCSI
device is in the state SDEV_DEL when scsi_device_get will fail.

.. _`zfcp_erp_notify`:

zfcp_erp_notify
===============

.. c:function:: void zfcp_erp_notify(struct zfcp_erp_action *erp_action, unsigned long set_mask)

    Trigger ERP action.

    :param struct zfcp_erp_action \*erp_action:
        ERP action to continue.

    :param unsigned long set_mask:
        ERP action status flags to set.

.. _`zfcp_erp_timeout_handler`:

zfcp_erp_timeout_handler
========================

.. c:function:: void zfcp_erp_timeout_handler(unsigned long data)

    Trigger ERP action from timed out ERP request

    :param unsigned long data:
        ERP action (from timer data)

.. _`zfcp_erp_thread_setup`:

zfcp_erp_thread_setup
=====================

.. c:function:: int zfcp_erp_thread_setup(struct zfcp_adapter *adapter)

    Start ERP thread for adapter

    :param struct zfcp_adapter \*adapter:
        Adapter to start the ERP thread for

.. _`zfcp_erp_thread_setup.description`:

Description
-----------

Returns 0 on success or error code from \ :c:func:`kernel_thread`\ 

.. _`zfcp_erp_thread_kill`:

zfcp_erp_thread_kill
====================

.. c:function:: void zfcp_erp_thread_kill(struct zfcp_adapter *adapter)

    Stop ERP thread.

    :param struct zfcp_adapter \*adapter:
        Adapter where the ERP thread should be stopped.

.. _`zfcp_erp_thread_kill.description`:

Description
-----------

The caller of this routine ensures that the specified adapter has
been shut down and that this operation has been completed. Thus,
there are no pending erp_actions which would need to be handled
here.

.. _`zfcp_erp_wait`:

zfcp_erp_wait
=============

.. c:function:: void zfcp_erp_wait(struct zfcp_adapter *adapter)

    wait for completion of error recovery on an adapter

    :param struct zfcp_adapter \*adapter:
        adapter for which to wait for completion of its error recovery

.. _`zfcp_erp_set_adapter_status`:

zfcp_erp_set_adapter_status
===========================

.. c:function:: void zfcp_erp_set_adapter_status(struct zfcp_adapter *adapter, u32 mask)

    set adapter status bits

    :param struct zfcp_adapter \*adapter:
        adapter to change the status

    :param u32 mask:
        status bits to change

.. _`zfcp_erp_set_adapter_status.description`:

Description
-----------

Changes in common status bits are propagated to attached ports and LUNs.

.. _`zfcp_erp_clear_adapter_status`:

zfcp_erp_clear_adapter_status
=============================

.. c:function:: void zfcp_erp_clear_adapter_status(struct zfcp_adapter *adapter, u32 mask)

    clear adapter status bits

    :param struct zfcp_adapter \*adapter:
        adapter to change the status

    :param u32 mask:
        status bits to change

.. _`zfcp_erp_clear_adapter_status.description`:

Description
-----------

Changes in common status bits are propagated to attached ports and LUNs.

.. _`zfcp_erp_set_port_status`:

zfcp_erp_set_port_status
========================

.. c:function:: void zfcp_erp_set_port_status(struct zfcp_port *port, u32 mask)

    set port status bits

    :param struct zfcp_port \*port:
        port to change the status

    :param u32 mask:
        status bits to change

.. _`zfcp_erp_set_port_status.description`:

Description
-----------

Changes in common status bits are propagated to attached LUNs.

.. _`zfcp_erp_clear_port_status`:

zfcp_erp_clear_port_status
==========================

.. c:function:: void zfcp_erp_clear_port_status(struct zfcp_port *port, u32 mask)

    clear port status bits

    :param struct zfcp_port \*port:
        adapter to change the status

    :param u32 mask:
        status bits to change

.. _`zfcp_erp_clear_port_status.description`:

Description
-----------

Changes in common status bits are propagated to attached LUNs.

.. _`zfcp_erp_set_lun_status`:

zfcp_erp_set_lun_status
=======================

.. c:function:: void zfcp_erp_set_lun_status(struct scsi_device *sdev, u32 mask)

    set lun status bits

    :param struct scsi_device \*sdev:
        SCSI device / lun to set the status bits

    :param u32 mask:
        status bits to change

.. _`zfcp_erp_clear_lun_status`:

zfcp_erp_clear_lun_status
=========================

.. c:function:: void zfcp_erp_clear_lun_status(struct scsi_device *sdev, u32 mask)

    clear lun status bits

    :param struct scsi_device \*sdev:
        SCSi device / lun to clear the status bits

    :param u32 mask:
        status bits to change

.. This file was automatic generated / don't edit.
