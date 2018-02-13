.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soundwire/intel_init.c

.. _`sdw_intel_init`:

sdw_intel_init
==============

.. c:function:: void *sdw_intel_init(acpi_handle *parent_handle, struct sdw_intel_res *res)

    SoundWire Intel init routine

    :param acpi_handle \*parent_handle:
        ACPI parent handle

    :param struct sdw_intel_res \*res:
        resource data

.. _`sdw_intel_init.description`:

Description
-----------

This scans the namespace and creates SoundWire link controller devices
based on the info queried.

.. _`sdw_intel_exit`:

sdw_intel_exit
==============

.. c:function:: void sdw_intel_exit(void *arg)

    SoundWire Intel exit

    :param void \*arg:
        callback context

.. _`sdw_intel_exit.description`:

Description
-----------

Delete the controller instances created and cleanup

.. This file was automatic generated / don't edit.

