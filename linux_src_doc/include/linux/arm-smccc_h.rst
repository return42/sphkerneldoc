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
        union {
            unsigned long a6;
        } state;
    }

.. _`arm_smccc_quirk.members`:

Members
-------

id
    quirk identification

state
    quirk specific information

.. _`__arm_smccc_smc`:

\__arm_smccc_smc
================

.. c:function:: void __arm_smccc_smc(unsigned long a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5, unsigned long a6, unsigned long a7, struct arm_smccc_res *res, struct arm_smccc_quirk *quirk)

    make SMC calls

    :param a0:
        arguments passed in registers 0 to 7
    :type a0: unsigned long

    :param a1:
        *undescribed*
    :type a1: unsigned long

    :param a2:
        *undescribed*
    :type a2: unsigned long

    :param a3:
        *undescribed*
    :type a3: unsigned long

    :param a4:
        *undescribed*
    :type a4: unsigned long

    :param a5:
        *undescribed*
    :type a5: unsigned long

    :param a6:
        *undescribed*
    :type a6: unsigned long

    :param a7:
        *undescribed*
    :type a7: unsigned long

    :param res:
        result values from registers 0 to 3
    :type res: struct arm_smccc_res \*

    :param quirk:
        points to an arm_smccc_quirk, or NULL when no quirks are required.
    :type quirk: struct arm_smccc_quirk \*

.. _`__arm_smccc_smc.description`:

Description
-----------

This function is used to make SMC calls following SMC Calling Convention.
The content of the supplied param are copied to registers 0 to 7 prior
to the SMC instruction. The return values are updated with the content
from register 0 to 3 on return from the SMC instruction.  An optional
quirk structure provides vendor specific behavior.

.. _`__arm_smccc_hvc`:

\__arm_smccc_hvc
================

.. c:function:: void __arm_smccc_hvc(unsigned long a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5, unsigned long a6, unsigned long a7, struct arm_smccc_res *res, struct arm_smccc_quirk *quirk)

    make HVC calls

    :param a0:
        arguments passed in registers 0 to 7
    :type a0: unsigned long

    :param a1:
        *undescribed*
    :type a1: unsigned long

    :param a2:
        *undescribed*
    :type a2: unsigned long

    :param a3:
        *undescribed*
    :type a3: unsigned long

    :param a4:
        *undescribed*
    :type a4: unsigned long

    :param a5:
        *undescribed*
    :type a5: unsigned long

    :param a6:
        *undescribed*
    :type a6: unsigned long

    :param a7:
        *undescribed*
    :type a7: unsigned long

    :param res:
        result values from registers 0 to 3
    :type res: struct arm_smccc_res \*

    :param quirk:
        points to an arm_smccc_quirk, or NULL when no quirks are required.
    :type quirk: struct arm_smccc_quirk \*

.. _`__arm_smccc_hvc.description`:

Description
-----------

This function is used to make HVC calls following SMC Calling
Convention.  The content of the supplied param are copied to registers 0
to 7 prior to the HVC instruction. The return values are updated with
the content from register 0 to 3 on return from the HVC instruction.  An
optional quirk structure provides vendor specific behavior.

.. This file was automatic generated / don't edit.

