.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/qcom_scm.c

.. _`qcom_scm_set_cold_boot_addr`:

qcom_scm_set_cold_boot_addr
===========================

.. c:function:: int qcom_scm_set_cold_boot_addr(void *entry, const cpumask_t *cpus)

    Set the cold boot address for cpus

    :param void \*entry:
        Entry point function for the cpus

    :param const cpumask_t \*cpus:
        The cpumask of cpus that will use the entry point

.. _`qcom_scm_set_cold_boot_addr.description`:

Description
-----------

Set the cold boot address of the cpus. Any cpu outside the supported
range would be removed from the cpu present mask.

.. _`qcom_scm_set_warm_boot_addr`:

qcom_scm_set_warm_boot_addr
===========================

.. c:function:: int qcom_scm_set_warm_boot_addr(void *entry, const cpumask_t *cpus)

    Set the warm boot address for cpus

    :param void \*entry:
        Entry point function for the cpus

    :param const cpumask_t \*cpus:
        The cpumask of cpus that will use the entry point

.. _`qcom_scm_set_warm_boot_addr.description`:

Description
-----------

Set the Linux entry point for the SCM to transfer control to when coming
out of a power down. CPU power down may be executed on cpuidle or hotplug.

.. _`qcom_scm_cpu_power_down`:

qcom_scm_cpu_power_down
=======================

.. c:function:: void qcom_scm_cpu_power_down(u32 flags)

    Power down the cpu \ ``flags``\  - Flags to flush cache

    :param u32 flags:
        *undescribed*

.. _`qcom_scm_cpu_power_down.description`:

Description
-----------

This is an end point to power down cpu. If there was a pending interrupt,
the control would return from this function, otherwise, the cpu jumps to the
warm boot entry point set for this cpu upon reset.

.. _`qcom_scm_hdcp_available`:

qcom_scm_hdcp_available
=======================

.. c:function:: bool qcom_scm_hdcp_available( void)

    Check if secure environment supports HDCP.

    :param  void:
        no arguments

.. _`qcom_scm_hdcp_available.description`:

Description
-----------

Return true if HDCP is supported, false if not.

.. _`qcom_scm_hdcp_req`:

qcom_scm_hdcp_req
=================

.. c:function:: int qcom_scm_hdcp_req(struct qcom_scm_hdcp_req *req, u32 req_cnt, u32 *resp)

    Send HDCP request.

    :param struct qcom_scm_hdcp_req \*req:
        HDCP request array

    :param u32 req_cnt:
        HDCP request array count

    :param u32 \*resp:
        response buffer passed to SCM

.. _`qcom_scm_hdcp_req.description`:

Description
-----------

Write HDCP register(s) through SCM.

.. _`qcom_scm_pas_supported`:

qcom_scm_pas_supported
======================

.. c:function:: bool qcom_scm_pas_supported(u32 peripheral)

    Check if the peripheral authentication service is available for the given peripherial

    :param u32 peripheral:
        peripheral id

.. _`qcom_scm_pas_supported.description`:

Description
-----------

Returns true if PAS is supported for this peripheral, otherwise false.

.. _`qcom_scm_pas_init_image`:

qcom_scm_pas_init_image
=======================

.. c:function:: int qcom_scm_pas_init_image(u32 peripheral, const void *metadata, size_t size)

    Initialize peripheral authentication service state machine for a given peripheral, using the metadata

    :param u32 peripheral:
        peripheral id

    :param const void \*metadata:
        pointer to memory containing ELF header, program header table
        and optional blob of data used for authenticating the metadata
        and the rest of the firmware

    :param size_t size:
        size of the metadata

.. _`qcom_scm_pas_init_image.description`:

Description
-----------

Returns 0 on success.

.. _`qcom_scm_pas_mem_setup`:

qcom_scm_pas_mem_setup
======================

.. c:function:: int qcom_scm_pas_mem_setup(u32 peripheral, phys_addr_t addr, phys_addr_t size)

    Prepare the memory related to a given peripheral for firmware loading

    :param u32 peripheral:
        peripheral id

    :param phys_addr_t addr:
        start address of memory area to prepare

    :param phys_addr_t size:
        size of the memory area to prepare

.. _`qcom_scm_pas_mem_setup.description`:

Description
-----------

Returns 0 on success.

.. _`qcom_scm_pas_auth_and_reset`:

qcom_scm_pas_auth_and_reset
===========================

.. c:function:: int qcom_scm_pas_auth_and_reset(u32 peripheral)

    Authenticate the given peripheral firmware and reset the remote processor

    :param u32 peripheral:
        peripheral id

.. _`qcom_scm_pas_auth_and_reset.description`:

Description
-----------

Return 0 on success.

.. _`qcom_scm_pas_shutdown`:

qcom_scm_pas_shutdown
=====================

.. c:function:: int qcom_scm_pas_shutdown(u32 peripheral)

    Shut down the remote processor

    :param u32 peripheral:
        peripheral id

.. _`qcom_scm_pas_shutdown.description`:

Description
-----------

Returns 0 on success.

.. _`qcom_scm_is_available`:

qcom_scm_is_available
=====================

.. c:function:: bool qcom_scm_is_available( void)

    Checks if SCM is available

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

