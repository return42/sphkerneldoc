.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/pcie/aer/aerdrv_core.c

.. _`add_error_device`:

add_error_device
================

.. c:function:: int add_error_device(struct aer_err_info *e_info, struct pci_dev *dev)

    list device to be handled

    :param struct aer_err_info \*e_info:
        pointer to error info

    :param struct pci_dev \*dev:
        pointer to pci_dev to be added

.. _`is_error_source`:

is_error_source
===============

.. c:function:: bool is_error_source(struct pci_dev *dev, struct aer_err_info *e_info)

    check whether the device is source of reported error

    :param struct pci_dev \*dev:
        pointer to pci_dev to be checked

    :param struct aer_err_info \*e_info:
        pointer to reported error info

.. _`find_source_device`:

find_source_device
==================

.. c:function:: bool find_source_device(struct pci_dev *parent, struct aer_err_info *e_info)

    search through device hierarchy for source device

    :param struct pci_dev \*parent:
        pointer to Root Port pci_dev data structure

    :param struct aer_err_info \*e_info:
        including detailed error information such like id

.. _`find_source_device.description`:

Description
-----------

Return true if found.

Invoked by DPC when error is detected at the Root Port.
Caller of this function must set id, severity, and multi_error_valid of
struct aer_err_info pointed by \ ``e_info``\  properly.  This function must fill
e_info->error_dev_num and e_info->dev[], based on the given information.

.. _`broadcast_error_message`:

broadcast_error_message
=======================

.. c:function:: pci_ers_result_t broadcast_error_message(struct pci_dev *dev, enum pci_channel_state state, char *error_mesg, int (*cb)(struct pci_dev *, void *))

    handle message broadcast to downstream drivers

    :param struct pci_dev \*dev:
        pointer to from where in a hierarchy message is broadcasted down

    :param enum pci_channel_state state:
        error state

    :param char \*error_mesg:
        message to print

    :param int (\*cb)(struct pci_dev \*, void \*):
        callback to be broadcasted

.. _`broadcast_error_message.description`:

Description
-----------

Invoked during error recovery process. Once being invoked, the content
of error severity will be broadcasted to all downstream drivers in a
hierarchy in question.

.. _`default_reset_link`:

default_reset_link
==================

.. c:function:: pci_ers_result_t default_reset_link(struct pci_dev *dev)

    default reset function

    :param struct pci_dev \*dev:
        pointer to pci_dev data structure

.. _`default_reset_link.description`:

Description
-----------

Invoked when performing link reset on a Downstream Port or a
Root Port with no aer driver.

.. _`do_recovery`:

do_recovery
===========

.. c:function:: void do_recovery(struct pci_dev *dev, int severity)

    handle nonfatal/fatal error recovery process

    :param struct pci_dev \*dev:
        pointer to a pci_dev data structure of agent detecting an error

    :param int severity:
        error severity type

.. _`do_recovery.description`:

Description
-----------

Invoked when an error is nonfatal/fatal. Once being invoked, broadcast
error detected message to all downstream drivers within a hierarchy in
question and return the returned code.

.. _`handle_error_source`:

handle_error_source
===================

.. c:function:: void handle_error_source(struct pcie_device *aerdev, struct pci_dev *dev, struct aer_err_info *info)

    handle logging error into an event log

    :param struct pcie_device \*aerdev:
        pointer to pcie_device data structure of the root port

    :param struct pci_dev \*dev:
        pointer to pci_dev data structure of error source device

    :param struct aer_err_info \*info:
        comprehensive error information

.. _`handle_error_source.description`:

Description
-----------

Invoked when an error being detected by Root Port.

.. _`get_device_error_info`:

get_device_error_info
=====================

.. c:function:: int get_device_error_info(struct pci_dev *dev, struct aer_err_info *info)

    read error status from dev and store it to info

    :param struct pci_dev \*dev:
        pointer to the device expected to have a error record

    :param struct aer_err_info \*info:
        pointer to structure to store the error record

.. _`get_device_error_info.description`:

Description
-----------

Return 1 on success, 0 on error.

Note that \ ``info``\  is reused among all error devices. Clear fields properly.

.. _`aer_isr_one_error`:

aer_isr_one_error
=================

.. c:function:: void aer_isr_one_error(struct pcie_device *p_device, struct aer_err_source *e_src)

    consume an error detected by root port

    :param struct pcie_device \*p_device:
        pointer to error root port service device

    :param struct aer_err_source \*e_src:
        pointer to an error source

.. _`get_e_source`:

get_e_source
============

.. c:function:: int get_e_source(struct aer_rpc *rpc, struct aer_err_source *e_src)

    retrieve an error source

    :param struct aer_rpc \*rpc:
        pointer to the root port which holds an error

    :param struct aer_err_source \*e_src:
        pointer to store retrieved error source

.. _`get_e_source.description`:

Description
-----------

Return 1 if an error source is retrieved, otherwise 0.

Invoked by DPC handler to consume an error.

.. _`aer_isr`:

aer_isr
=======

.. c:function:: void aer_isr(struct work_struct *work)

    consume errors detected by root port

    :param struct work_struct \*work:
        definition of this work item

.. _`aer_isr.description`:

Description
-----------

Invoked, as DPC, when root port records new detected error

.. _`aer_init`:

aer_init
========

.. c:function:: int aer_init(struct pcie_device *dev)

    provide AER initialization

    :param struct pcie_device \*dev:
        pointer to AER pcie device

.. _`aer_init.description`:

Description
-----------

Invoked when AER service driver is loaded.

.. This file was automatic generated / don't edit.

