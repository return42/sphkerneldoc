.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/rfgain.h

.. _`ath5k_ini_rfgain`:

struct ath5k_ini_rfgain
=======================

.. c:type:: struct ath5k_ini_rfgain

    RF Gain table

.. _`ath5k_ini_rfgain.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_ini_rfgain {
        u16 rfg_register;
        u32 rfg_value[2];
    }

.. _`ath5k_ini_rfgain.members`:

Members
-------

rfg_register
    RF Gain register address

rfg_value
    Register value for 5 and 2GHz

.. _`ath5k_ini_rfgain.description`:

Description
-----------

Mode-specific RF Gain table (64bytes) for RF5111/5112
(RF5110 only comes with AR5210 and only supports a/turbo a mode so initial
RF Gain values are included in AR5K_AR5210_INI)

.. _`ath5k_gain_opt_step`:

struct ath5k_gain_opt_step
==========================

.. c:type:: struct ath5k_gain_opt_step

    An RF gain optimization step

.. _`ath5k_gain_opt_step.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_gain_opt_step {
        s8 gos_param[AR5K_GAIN_CRN_MAX_FIX_BITS];
        s8 gos_gain;
    }

.. _`ath5k_gain_opt_step.members`:

Members
-------

gos_param
    Set of parameters

gos_gain
    Gain

.. _`ath5k_gain_opt`:

struct ath5k_gain_opt
=====================

.. c:type:: struct ath5k_gain_opt

    RF Gain optimization ladder

.. _`ath5k_gain_opt.definition`:

Definition
----------

.. code-block:: c

    struct ath5k_gain_opt {
        u8 go_default;
        u8 go_steps_count;
        const struct ath5k_gain_opt_step go_step[AR5K_GAIN_STEP_COUNT];
    }

.. _`ath5k_gain_opt.members`:

Members
-------

go_default
    The default step

go_steps_count
    How many optimization steps

go_step
    Array of \ :c:type:`struct ath5k_gain_opt_step <ath5k_gain_opt_step>`\ 

.. This file was automatic generated / don't edit.

