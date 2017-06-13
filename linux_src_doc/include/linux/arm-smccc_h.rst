.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/arm-smccc.h

.. _`arm_smccc_res`:

struct arm_smccc_res
====================

.. c:type:: struct arm_smccc_res

    Result from SMC/HVC call \ ``a0``\ -a3 result values from registers 0 to 3

.. _`arm_smccc_res.definition`:

Definition
----------

.. code-block:: c

    struct arm_smccc_res {
        unsigned long a0;
        unsigned long a1;
        unsigned long a2;
        unsigned long a3;
    }

.. _`arm_smccc_res.members`:

Members
-------

a0
    *undescribed*

a1
    *undescribed*

a2
    *undescribed*

a3
    *undescribed*

.. _`arm_smccc_quirk`:

struct arm_smccc_quirk
======================

.. c:type:: struct arm_smccc_quirk

    Contains quirk information

.. _`arm_smccc_quirk.definition`:

Definition
----------

.. code-block:: c

    struct arm_smccc_quirk {
        int id;
        union state;
    }

.. _`arm_smccc_quirk.members`:

Members
-------

id
    quirk identification

state
    quirk specific information

.. _`__arm_smccc_smc`:

__arm_smccc_smc
===============

.. c:function:: void __arm_smccc_smc(unsigned long a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5, unsigned long a6, unsigned long a7, struct arm_smccc_res *res, struct arm_smccc_quirk *quirk)

    make SMC calls

    :param unsigned long a0:
        arguments passed in registers 0 to 7

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

    :param struct arm_smccc_quirk \*quirk:
        points to an arm_smccc_quirk, or NULL when no quirks are required.

.. _`__arm_smccc_smc.description`:

Description
-----------

This function is used to make SMC calls following SMC Calling Convention.
The content of the supplied param are copied to registers 0 to 7 prior
to the SMC instruction. The return values are updated with the content
from register 0 to 3 on return from the SMC instruction.  An optional
quirk structure provides vendor specific behavior.

.. _`__arm_smccc_hvc`:

__arm_smccc_hvc
===============

.. c:function:: void __arm_smccc_hvc(unsigned long a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5, unsigned long a6, unsigned long a7, struct arm_smccc_res *res, struct arm_smccc_quirk *quirk)

    make HVC calls

    :param unsigned long a0:
        arguments passed in registers 0 to 7

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

    :param struct arm_smccc_quirk \*quirk:
        points to an arm_smccc_quirk, or NULL when no quirks are required.

.. _`__arm_smccc_hvc.description`:

Description
-----------

This function is used to make HVC calls following SMC Calling
Convention.  The content of the supplied param are copied to registers 0
to 7 prior to the HVC instruction. The return values are updated with
the content from register 0 to 3 on return from the HVC instruction.  An
optional quirk structure provides vendor specific behavior.

.. This file was automatic generated / don't edit.

