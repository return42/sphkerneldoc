.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/bnx2i/bnx2i_init.c

.. _`bnx2i_identify_device`:

bnx2i_identify_device
=====================

.. c:function:: void bnx2i_identify_device(struct bnx2i_hba *hba, struct cnic_dev *dev)

    identifies NetXtreme II device type

    :param struct bnx2i_hba \*hba:
        Adapter structure pointer

    :param struct cnic_dev \*dev:
        *undescribed*

.. _`bnx2i_identify_device.description`:

Description
-----------

This function identifies the NX2 device type and sets appropriate
queue mailbox register access method, 5709 requires driver to
access MBOX regs using \*bin\* mode

.. _`get_adapter_list_head`:

get_adapter_list_head
=====================

.. c:function:: struct bnx2i_hba *get_adapter_list_head( void)

    returns head of adapter list

    :param  void:
        no arguments

.. _`bnx2i_find_hba_for_cnic`:

bnx2i_find_hba_for_cnic
=======================

.. c:function:: struct bnx2i_hba *bnx2i_find_hba_for_cnic(struct cnic_dev *cnic)

    maps cnic device instance to bnx2i adapter instance

    :param struct cnic_dev \*cnic:
        pointer to cnic device instance

.. _`bnx2i_start`:

bnx2i_start
===========

.. c:function:: void bnx2i_start(void *handle)

    cnic callback to initialize & start adapter instance

    :param void \*handle:
        transparent handle pointing to adapter structure

.. _`bnx2i_start.description`:

Description
-----------

This function maps adapter structure to pcidev structure and initiates
firmware handshake to enable/initialize on chip iscsi components
This bnx2i - cnic interface api callback is issued after following
2 conditions are met -
a) underlying network interface is up (marked by event 'NETDEV_UP'
from netdev
b) bnx2i adapter instance is registered

.. _`bnx2i_chip_cleanup`:

bnx2i_chip_cleanup
==================

.. c:function:: void bnx2i_chip_cleanup(struct bnx2i_hba *hba)

    local routine to handle chip cleanup

    :param struct bnx2i_hba \*hba:
        Adapter instance to register

.. _`bnx2i_chip_cleanup.description`:

Description
-----------

Driver checks if adapter still has any active connections before
executing the cleanup process

.. _`bnx2i_stop`:

bnx2i_stop
==========

.. c:function:: void bnx2i_stop(void *handle)

    cnic callback to shutdown adapter instance

    :param void \*handle:
        transparent handle pointing to adapter structure

.. _`bnx2i_stop.description`:

Description
-----------

driver checks if adapter is already in shutdown mode, if not start
the shutdown process

.. _`bnx2i_init_one`:

bnx2i_init_one
==============

.. c:function:: int bnx2i_init_one(struct bnx2i_hba *hba, struct cnic_dev *cnic)

    initialize an adapter instance and allocate memory resources

    :param struct bnx2i_hba \*hba:
        bnx2i adapter instance

    :param struct cnic_dev \*cnic:
        cnic device handle

.. _`bnx2i_init_one.description`:

Description
-----------

Global resource lock is held during critical sections below. This routine is
called from either \ :c:func:`cnic_register_driver`\  or device hot plug context and
and does majority of device specific initialization

.. _`bnx2i_ulp_init`:

bnx2i_ulp_init
==============

.. c:function:: void bnx2i_ulp_init(struct cnic_dev *dev)

    initialize an adapter instance

    :param struct cnic_dev \*dev:
        cnic device handle

.. _`bnx2i_ulp_init.description`:

Description
-----------

Called from \ :c:func:`cnic_register_driver`\  context to initialize all enumerated
cnic devices. This routine allocate adapter structure and other
device specific resources.

.. _`bnx2i_ulp_exit`:

bnx2i_ulp_exit
==============

.. c:function:: void bnx2i_ulp_exit(struct cnic_dev *dev)

    shuts down adapter instance and frees all resources

    :param struct cnic_dev \*dev:
        cnic device handle

.. _`bnx2i_get_stats`:

bnx2i_get_stats
===============

.. c:function:: int bnx2i_get_stats(void *handle)

    Retrieve various statistic from iSCSI offload

    :param void \*handle:
        bnx2i_hba

.. _`bnx2i_get_stats.description`:

Description
-----------

function callback exported via bnx2i - cnic driver interface to
retrieve various iSCSI offload related statistics.

.. _`bnx2i_percpu_thread_create`:

bnx2i_percpu_thread_create
==========================

.. c:function:: void bnx2i_percpu_thread_create(unsigned int cpu)

    Create a receive thread for an online CPU

    :param unsigned int cpu:
        cpu index for the online cpu

.. _`bnx2i_cpu_callback`:

bnx2i_cpu_callback
==================

.. c:function:: int bnx2i_cpu_callback(struct notifier_block *nfb, unsigned long action, void *hcpu)

    Handler for CPU hotplug events

    :param struct notifier_block \*nfb:
        The callback data block

    :param unsigned long action:
        The event triggering the callback

    :param void \*hcpu:
        The index of the CPU that the event is for

.. _`bnx2i_cpu_callback.description`:

Description
-----------

This creates or destroys per-CPU data for iSCSI

Returns NOTIFY_OK always.

.. _`bnx2i_mod_init`:

bnx2i_mod_init
==============

.. c:function:: int bnx2i_mod_init( void)

    module init entry point

    :param  void:
        no arguments

.. _`bnx2i_mod_init.description`:

Description
-----------

initialize any driver wide global data structures such as endpoint pool,
tcp port manager/queue, sysfs. finally driver will register itself
with the cnic module

.. _`bnx2i_mod_exit`:

bnx2i_mod_exit
==============

.. c:function:: void __exit bnx2i_mod_exit( void)

    module cleanup/exit entry point

    :param  void:
        no arguments

.. _`bnx2i_mod_exit.description`:

Description
-----------

Global resource lock and host adapter lock is held during critical sections
in this function. Driver will browse through the adapter list, cleans-up
each instance, unregisters iscsi transport name and finally driver will
unregister itself with the cnic module

.. This file was automatic generated / don't edit.

