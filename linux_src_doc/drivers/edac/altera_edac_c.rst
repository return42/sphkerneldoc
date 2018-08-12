.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/edac/altera_edac.c

.. _`s10_protected_reg_write`:

s10_protected_reg_write
=======================

.. c:function:: int s10_protected_reg_write(void *context, unsigned int reg, unsigned int val)

    Write to a protected SMC register.

    :param void \*context:
        Not used.

    :param unsigned int reg:
        Address of register

    :param unsigned int val:
        *undescribed*

.. _`s10_protected_reg_write.return`:

Return
------

INTEL_SIP_SMC_STATUS_OK (0) on success
INTEL_SIP_SMC_REG_ERROR on error
INTEL_SIP_SMC_RETURN_UNKNOWN_FUNCTION if not supported

.. _`s10_protected_reg_read`:

s10_protected_reg_read
======================

.. c:function:: int s10_protected_reg_read(void *context, unsigned int reg, unsigned int *val)

    Read the status of a protected SMC register

    :param void \*context:
        Not used.

    :param unsigned int reg:
        Address of register

    :param unsigned int \*val:
        *undescribed*

.. _`s10_protected_reg_read.return`:

Return
------

INTEL_SIP_SMC_STATUS_OK (0) on success
INTEL_SIP_SMC_REG_ERROR on error
INTEL_SIP_SMC_RETURN_UNKNOWN_FUNCTION if not supported

.. This file was automatic generated / don't edit.

