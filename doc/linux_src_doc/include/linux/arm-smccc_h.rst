.. -*- coding: utf-8; mode: rst -*-

===========
arm-smccc.h
===========


.. _`arm_smccc_res`:

struct arm_smccc_res
====================

.. c:type:: arm_smccc_res

    Result from SMC/HVC call @a0-a3 result values from registers 0 to 3


.. _`arm_smccc_res.definition`:

Definition
----------

.. code-block:: c

  struct arm_smccc_res {
  };


.. _`arm_smccc_res.members`:

Members
-------




.. _`arm_smccc_smc`:

arm_smccc_smc
=============

.. c:function:: void arm_smccc_smc (unsigned long a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5, unsigned long a6, unsigned long a7, struct arm_smccc_res *res)

    make SMC calls @a0-a7: arguments passed in registers 0 to 7

    :param unsigned long a0:

        *undescribed*

    :param unsigned long a1:

        *undescribed*

    :param unsigned long a2:

        *undescribed*

    :param unsigned long a3:

        *undescribed*

    :param unsigned long a4:

        *undescribed*

    :param unsigned long a5:

        *undescribed*

    :param unsigned long a6:

        *undescribed*

    :param unsigned long a7:

        *undescribed*

    :param struct arm_smccc_res \*res:
        result values from registers 0 to 3



.. _`arm_smccc_smc.description`:

Description
-----------

This function is used to make SMC calls following SMC Calling Convention.
The content of the supplied param are copied to registers 0 to 7 prior
to the SMC instruction. The return values are updated with the content
from register 0 to 3 on return from the SMC instruction.



.. _`arm_smccc_hvc`:

arm_smccc_hvc
=============

.. c:function:: void arm_smccc_hvc (unsigned long a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5, unsigned long a6, unsigned long a7, struct arm_smccc_res *res)

    make HVC calls @a0-a7: arguments passed in registers 0 to 7

    :param unsigned long a0:

        *undescribed*

    :param unsigned long a1:

        *undescribed*

    :param unsigned long a2:

        *undescribed*

    :param unsigned long a3:

        *undescribed*

    :param unsigned long a4:

        *undescribed*

    :param unsigned long a5:

        *undescribed*

    :param unsigned long a6:

        *undescribed*

    :param unsigned long a7:

        *undescribed*

    :param struct arm_smccc_res \*res:
        result values from registers 0 to 3



.. _`arm_smccc_hvc.description`:

Description
-----------

This function is used to make HVC calls following SMC Calling
Convention.  The content of the supplied param are copied to registers 0
to 7 prior to the HVC instruction. The return values are updated with
the content from register 0 to 3 on return from the HVC instruction.

