.. -*- coding: utf-8; mode: rst -*-

========
dcdbas.c
========


.. _`smi_data_buf_free`:

smi_data_buf_free
=================

.. c:function:: void smi_data_buf_free ( void)

    :param void:
        no arguments



.. _`smi_data_buf_realloc`:

smi_data_buf_realloc
====================

.. c:function:: int smi_data_buf_realloc (unsigned long size)

    :param unsigned long size:

        *undescribed*



.. _`dcdbas_smi_request`:

dcdbas_smi_request
==================

.. c:function:: int dcdbas_smi_request (struct smi_cmd *smi_cmd)

    :param struct smi_cmd \*smi_cmd:

        *undescribed*



.. _`dcdbas_smi_request.description`:

Description
-----------


Called with smi_data_lock.



.. _`smi_request_store`:

smi_request_store
=================

.. c:function:: ssize_t smi_request_store (struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    :param struct device \*dev:

        *undescribed*

    :param struct device_attribute \*attr:

        *undescribed*

    :param const char \*buf:

        *undescribed*

    :param size_t count:

        *undescribed*



.. _`smi_request_store.0`:

0
-

zero SMI data buffer



.. _`smi_request_store.1`:

1
-

generate calling interface SMI



.. _`smi_request_store.2`:

2
-

generate raw SMI

User application writes smi_cmd to smi_data before telling driver
to generate SMI.



.. _`host_control_smi`:

host_control_smi
================

.. c:function:: int host_control_smi ( void)

    :param void:
        no arguments



.. _`host_control_smi.description`:

Description
-----------


Caller must set up the host control command in smi_data_buf.



.. _`dcdbas_host_control`:

dcdbas_host_control
===================

.. c:function:: void dcdbas_host_control ( void)

    :param void:
        no arguments



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

.. c:function:: int dcdbas_reboot_notify (struct notifier_block *nb, unsigned long code, void *unused)

    :param struct notifier_block \*nb:

        *undescribed*

    :param unsigned long code:

        *undescribed*

    :param void \*unused:

        *undescribed*



.. _`dcdbas_init`:

dcdbas_init
===========

.. c:function:: int dcdbas_init ( void)

    :param void:
        no arguments



.. _`dcdbas_exit`:

dcdbas_exit
===========

.. c:function:: void __exit dcdbas_exit ( void)

    :param void:
        no arguments

