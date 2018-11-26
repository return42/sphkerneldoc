.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/x86/dcdbas.c

.. _`smi_data_buf_free`:

smi_data_buf_free
=================

.. c:function:: void smi_data_buf_free( void)

    free SMI data buffer

    :param void:
        no arguments
    :type void: 

.. _`smi_data_buf_realloc`:

smi_data_buf_realloc
====================

.. c:function:: int smi_data_buf_realloc(unsigned long size)

    grow SMI data buffer if needed

    :param size:
        *undescribed*
    :type size: unsigned long

.. _`dcdbas_smi_request`:

dcdbas_smi_request
==================

.. c:function:: int dcdbas_smi_request(struct smi_cmd *smi_cmd)

    generate SMI request

    :param smi_cmd:
        *undescribed*
    :type smi_cmd: struct smi_cmd \*

.. _`dcdbas_smi_request.description`:

Description
-----------

Called with smi_data_lock.

.. _`smi_request_store`:

smi_request_store
=================

.. c:function:: ssize_t smi_request_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        *undescribed*
    :type buf: const char \*

    :param count:
        *undescribed*
    :type count: size_t

.. _`smi_request_store.the-valid-values-are`:

The valid values are
--------------------

0: zero SMI data buffer
1: generate calling interface SMI
2: generate raw SMI

User application writes smi_cmd to smi_data before telling driver
to generate SMI.

.. _`host_control_smi`:

host_control_smi
================

.. c:function:: int host_control_smi( void)

    generate host control SMI

    :param void:
        no arguments
    :type void: 

.. _`host_control_smi.description`:

Description
-----------

Caller must set up the host control command in smi_data_buf.

.. _`dcdbas_host_control`:

dcdbas_host_control
===================

.. c:function:: void dcdbas_host_control( void)

    initiate host control

    :param void:
        no arguments
    :type void: 

.. _`dcdbas_host_control.description`:

Description
-----------

This function is called by the driver after the system has
finished shutting down if the user application specified a
host control action to perform on shutdown.  It is safe to
use smi_data_buf at this point because the system has finished
shutting down and no userspace apps are running.

.. _`dcdbas_reboot_notify`:

dcdbas_reboot_notify
====================

.. c:function:: int dcdbas_reboot_notify(struct notifier_block *nb, unsigned long code, void *unused)

    handle reboot notification for host control

    :param nb:
        *undescribed*
    :type nb: struct notifier_block \*

    :param code:
        *undescribed*
    :type code: unsigned long

    :param unused:
        *undescribed*
    :type unused: void \*

.. _`dcdbas_init`:

dcdbas_init
===========

.. c:function:: int dcdbas_init( void)

    initialize driver

    :param void:
        no arguments
    :type void: 

.. _`dcdbas_exit`:

dcdbas_exit
===========

.. c:function:: void __exit dcdbas_exit( void)

    perform driver cleanup

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

