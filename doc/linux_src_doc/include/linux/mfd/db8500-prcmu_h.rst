.. -*- coding: utf-8; mode: rst -*-

==============
db8500-prcmu.h
==============


.. _`state`:

enum state
==========

.. c:type:: state

    ON/OFF state definition


.. _`state.definition`:

Definition
----------

.. code-block:: c

    enum state {
      OFF,
      ON
    };


.. _`state.constants`:

Constants
---------

:``OFF``:
    State is ON

:``ON``:
    State is OFF


.. _`ret_state`:

enum ret_state
==============

.. c:type:: ret_state

    general purpose On/Off/Retention states


.. _`ret_state.definition`:

Definition
----------

.. code-block:: c

    enum ret_state {
      OFFST,
      ONST,
      RETST
    };


.. _`ret_state.constants`:

Constants
---------

:``OFFST``:
-- undescribed --

:``ONST``:
-- undescribed --

:``RETST``:
-- undescribed --


.. _`clk_arm`:

enum clk_arm
============

.. c:type:: clk_arm

    ARM Cortex A9 clock schemes


.. _`clk_arm.definition`:

Definition
----------

.. code-block:: c

    enum clk_arm {
      A9_OFF,
      A9_BOOT,
      A9_OPPT1,
      A9_OPPT2,
      A9_EXTCLK
    };


.. _`clk_arm.constants`:

Constants
---------

:``A9_OFF``:
-- undescribed --

:``A9_BOOT``:
-- undescribed --

:``A9_OPPT1``:
-- undescribed --

:``A9_OPPT2``:
-- undescribed --

:``A9_EXTCLK``:
-- undescribed --


.. _`clk_gen`:

enum clk_gen
============

.. c:type:: clk_gen

    GEN#0/GEN#1 clock schemes


.. _`clk_gen.definition`:

Definition
----------

.. code-block:: c

    enum clk_gen {
      GEN_OFF,
      GEN_BOOT,
      GEN_OPPT1
    };


.. _`clk_gen.constants`:

Constants
---------

:``GEN_OFF``:
-- undescribed --

:``GEN_BOOT``:
-- undescribed --

:``GEN_OPPT1``:
-- undescribed --


.. _`romcode_write`:

enum romcode_write
==================

.. c:type:: romcode_write

    Romcode message written by A9 AND read by XP70


.. _`romcode_write.definition`:

Definition
----------

.. code-block:: c

    enum romcode_write {
      RDY_2_DS,
      RDY_2_XP70_RST
    };


.. _`romcode_write.constants`:

Constants
---------

:``RDY_2_DS``:
    Value set when ApDeepSleep state can be executed by XP70

:``RDY_2_XP70_RST``:
    Value set when 0x0F has been successfully polled by the
    romcode. The xp70 will go into self-reset


.. _`romcode_read`:

enum romcode_read
=================

.. c:type:: romcode_read

    Romcode message written by XP70 and read by A9


.. _`romcode_read.definition`:

Definition
----------

.. code-block:: c

    enum romcode_read {
      INIT,
      FS_2_DS,
      END_DS,
      DS_TO_FS,
      END_FS,
      SWR,
      END_SWR
    };


.. _`romcode_read.constants`:

Constants
---------

:``INIT``:
    Init value when romcode field is not used

:``FS_2_DS``:
    Value set when power state is going from ApExecute to
    ApDeepSleep

:``END_DS``:
    Value set when ApDeepSleep power state is reached coming from
    ApExecute state

:``DS_TO_FS``:
    Value set when power state is going from ApDeepSleep to
    ApExecute

:``END_FS``:
    Value set when ApExecute power state is reached coming from
    ApDeepSleep state

:``SWR``:
    Value set when power state is going to ApReset

:``END_SWR``:
    Value set when the xp70 finished executing ApReset actions and
    waits for romcode acknowledgment to go to self-reset


.. _`ap_pwrst`:

enum ap_pwrst
=============

.. c:type:: ap_pwrst

    current power states defined in PRCMU firmware


.. _`ap_pwrst.definition`:

Definition
----------

.. code-block:: c

    enum ap_pwrst {
      NO_PWRST,
      AP_BOOT,
      AP_EXECUTE,
      AP_DEEP_SLEEP,
      AP_SLEEP,
      AP_IDLE,
      AP_RESET
    };


.. _`ap_pwrst.constants`:

Constants
---------

:``NO_PWRST``:
    Current power state init

:``AP_BOOT``:
    Current power state is apBoot

:``AP_EXECUTE``:
    Current power state is apExecute

:``AP_DEEP_SLEEP``:
    Current power state is apDeepSleep

:``AP_SLEEP``:
    Current power state is apSleep

:``AP_IDLE``:
    Current power state is apIdle

:``AP_RESET``:
    Current power state is apReset


.. _`ap_pwrst_trans`:

enum ap_pwrst_trans
===================

.. c:type:: ap_pwrst_trans

    Transition states defined in PRCMU firmware


.. _`ap_pwrst_trans.definition`:

Definition
----------

.. code-block:: c

    enum ap_pwrst_trans {
      PRCMU_AP_NO_CHANGE,
      APEXECUTE_TO_APSLEEP,
      APIDLE_TO_APSLEEP,
      PRCMU_AP_SLEEP,
      APBOOT_TO_APEXECUTE,
      APEXECUTE_TO_APDEEPSLEEP,
      PRCMU_AP_DEEP_SLEEP,
      APEXECUTE_TO_APIDLE,
      PRCMU_AP_IDLE,
      PRCMU_AP_DEEP_IDLE
    };


.. _`ap_pwrst_trans.constants`:

Constants
---------

:``PRCMU_AP_NO_CHANGE``:
-- undescribed --

:``APEXECUTE_TO_APSLEEP``:
    Power state transition from ApExecute to ApSleep

:``APIDLE_TO_APSLEEP``:
    Power state transition from ApIdle to ApSleep

:``PRCMU_AP_SLEEP``:
-- undescribed --

:``APBOOT_TO_APEXECUTE``:
    Power state transition from ApBoot to ApExecute

:``APEXECUTE_TO_APDEEPSLEEP``:
    Power state transition from ApExecute to
    ApDeepSleep

:``PRCMU_AP_DEEP_SLEEP``:
-- undescribed --

:``APEXECUTE_TO_APIDLE``:
    Power state transition from ApExecute to ApIdle

:``PRCMU_AP_IDLE``:
-- undescribed --

:``PRCMU_AP_DEEP_IDLE``:
-- undescribed --


.. _`hw_acc_state`:

enum hw_acc_state
=================

.. c:type:: hw_acc_state

    State definition for hardware accelerator


.. _`hw_acc_state.definition`:

Definition
----------

.. code-block:: c

    enum hw_acc_state {
      HW_NO_CHANGE,
      HW_OFF,
      HW_OFF_RAMRET,
      HW_ON
    };


.. _`hw_acc_state.constants`:

Constants
---------

:``HW_NO_CHANGE``:
    The hardware accelerator state must remain unchanged

:``HW_OFF``:
    The hardware accelerator must be switched off

:``HW_OFF_RAMRET``:
    The hardware accelerator must be switched off with its
    internal RAM in retention

:``HW_ON``:
    The hwa hardware accelerator hwa must be switched on


.. _`hw_acc_state.description`:

Description
-----------

NOTE! Deprecated, to be removed when all users switched over to use the
regulator API.



.. _`ap_pwrsttr_status`:

enum ap_pwrsttr_status
======================

.. c:type:: ap_pwrsttr_status

    Status messages definition for mbox_arm


.. _`ap_pwrsttr_status.definition`:

Definition
----------

.. code-block:: c

    enum ap_pwrsttr_status {
      BOOT_TO_EXECUTEOK,
      DEEPSLEEPOK,
      SLEEPOK,
      IDLEOK,
      SOFTRESETOK,
      SOFTRESETGO,
      BOOT_TO_EXECUTE,
      EXECUTE_TO_DEEPSLEEP,
      DEEPSLEEP_TO_EXECUTE,
      DEEPSLEEP_TO_EXECUTEOK,
      EXECUTE_TO_SLEEP,
      SLEEP_TO_EXECUTE,
      SLEEP_TO_EXECUTEOK,
      EXECUTE_TO_IDLE,
      IDLE_TO_EXECUTE,
      IDLE_TO_EXECUTEOK,
      RDYTODS_RETURNTOEXE,
      NORDYTODS_RETURNTOEXE,
      EXETOSLEEP_RETURNTOEXE,
      EXETOIDLE_RETURNTOEXE,
      INIT_STATUS,
      INITERROR,
      PLLARMLOCKP_ER,
      PLLDDRLOCKP_ER,
      PLLSOCLOCKP_ER,
      PLLSOCK1LOCKP_ER,
      ARMWFI_ER,
      SYSCLKOK_ER,
      I2C_NACK_DATA_ER,
      BOOT_ER,
      I2C_STATUS_ALWAYS_1,
      I2C_NACK_REG_ADDR_ER,
      I2C_NACK_DATA0123_ER,
      I2C_NACK_ADDR_ER,
      CURAPPWRSTISNOT_BOOT,
      CURAPPWRSTISNOT_EXECUTE,
      CURAPPWRSTISNOT_SLEEPMODE,
      CURAPPWRSTISNOT_CORRECTFORIT10,
      FIFO4500WUISNOT_WUPEVENT,
      PLL32KLOCKP_ER,
      DDRDEEPSLEEPOK_ER,
      ROMCODEREADY_ER,
      WUPBEFOREDS,
      DDRCONFIG_ER,
      WUPBEFORESLEEP,
      WUPBEFOREIDLE
    };


.. _`ap_pwrsttr_status.constants`:

Constants
---------

:``BOOT_TO_EXECUTEOK``:
    The apBoot to apExecute state transition has been
    completed

:``DEEPSLEEPOK``:
    The apExecute to apDeepSleep state transition has been
    completed

:``SLEEPOK``:
    The apExecute to apSleep state transition has been completed

:``IDLEOK``:
    The apExecute to apIdle state transition has been completed

:``SOFTRESETOK``:
    The A9 watchdog/ SoftReset state has been completed

:``SOFTRESETGO``:
    The A9 watchdog/SoftReset state is on going

:``BOOT_TO_EXECUTE``:
    The apBoot to apExecute state transition is on going

:``EXECUTE_TO_DEEPSLEEP``:
    The apExecute to apDeepSleep state transition is on
    going

:``DEEPSLEEP_TO_EXECUTE``:
    The apDeepSleep to apExecute state transition is on
    going

:``DEEPSLEEP_TO_EXECUTEOK``:
    The apDeepSleep to apExecute state transition has
    been completed

:``EXECUTE_TO_SLEEP``:
    The apExecute to apSleep state transition is on going

:``SLEEP_TO_EXECUTE``:
    The apSleep to apExecute state transition is on going

:``SLEEP_TO_EXECUTEOK``:
    The apSleep to apExecute state transition has been
    completed

:``EXECUTE_TO_IDLE``:
    The apExecute to apIdle state transition is on going

:``IDLE_TO_EXECUTE``:
    The apIdle to apExecute state transition is on going

:``IDLE_TO_EXECUTEOK``:
    The apIdle to apExecute state transition has been
    completed

:``RDYTODS_RETURNTOEXE``:
-- undescribed --

:``NORDYTODS_RETURNTOEXE``:
-- undescribed --

:``EXETOSLEEP_RETURNTOEXE``:
-- undescribed --

:``EXETOIDLE_RETURNTOEXE``:
-- undescribed --

:``INIT_STATUS``:
    Status init

:``INITERROR``:
-- undescribed --

:``PLLARMLOCKP_ER``:
-- undescribed --

:``PLLDDRLOCKP_ER``:
-- undescribed --

:``PLLSOCLOCKP_ER``:
-- undescribed --

:``PLLSOCK1LOCKP_ER``:
-- undescribed --

:``ARMWFI_ER``:
-- undescribed --

:``SYSCLKOK_ER``:
-- undescribed --

:``I2C_NACK_DATA_ER``:
-- undescribed --

:``BOOT_ER``:
-- undescribed --

:``I2C_STATUS_ALWAYS_1``:
-- undescribed --

:``I2C_NACK_REG_ADDR_ER``:
-- undescribed --

:``I2C_NACK_DATA0123_ER``:
-- undescribed --

:``I2C_NACK_ADDR_ER``:
-- undescribed --

:``CURAPPWRSTISNOT_BOOT``:
-- undescribed --

:``CURAPPWRSTISNOT_EXECUTE``:
-- undescribed --

:``CURAPPWRSTISNOT_SLEEPMODE``:
-- undescribed --

:``CURAPPWRSTISNOT_CORRECTFORIT10``:
-- undescribed --

:``FIFO4500WUISNOT_WUPEVENT``:
-- undescribed --

:``PLL32KLOCKP_ER``:
-- undescribed --

:``DDRDEEPSLEEPOK_ER``:
-- undescribed --

:``ROMCODEREADY_ER``:
-- undescribed --

:``WUPBEFOREDS``:
-- undescribed --

:``DDRCONFIG_ER``:
-- undescribed --

:``WUPBEFORESLEEP``:
-- undescribed --

:``WUPBEFOREIDLE``:
-- undescribed --


.. _`dvfs_stat`:

enum dvfs_stat
==============

.. c:type:: dvfs_stat

    DVFS status messages definition


.. _`dvfs_stat.definition`:

Definition
----------

.. code-block:: c

    enum dvfs_stat {
      DVFS_GO,
      DVFS_ARM100OPPOK,
      DVFS_ARM50OPPOK,
      DVFS_ARMEXTCLKOK,
      DVFS_NOCHGTCLKOK,
      DVFS_INITSTATUS
    };


.. _`dvfs_stat.constants`:

Constants
---------

:``DVFS_GO``:
    A state transition DVFS is on going

:``DVFS_ARM100OPPOK``:
    The state transition DVFS has been completed for 100OPP

:``DVFS_ARM50OPPOK``:
    The state transition DVFS has been completed for 50OPP

:``DVFS_ARMEXTCLKOK``:
    The state transition DVFS has been completed for EXTCLK

:``DVFS_NOCHGTCLKOK``:
    The state transition DVFS has been completed for
    NOCHGCLK

:``DVFS_INITSTATUS``:
    Value init


.. _`sva_mmdsp_stat`:

enum sva_mmdsp_stat
===================

.. c:type:: sva_mmdsp_stat

    SVA MMDSP status messages


.. _`sva_mmdsp_stat.definition`:

Definition
----------

.. code-block:: c

    enum sva_mmdsp_stat {
      SVA_MMDSP_GO,
      SVA_MMDSP_INIT
    };


.. _`sva_mmdsp_stat.constants`:

Constants
---------

:``SVA_MMDSP_GO``:
    SVAMMDSP interrupt has happened

:``SVA_MMDSP_INIT``:
    Status init


.. _`sia_mmdsp_stat`:

enum sia_mmdsp_stat
===================

.. c:type:: sia_mmdsp_stat

    SIA MMDSP status messages


.. _`sia_mmdsp_stat.definition`:

Definition
----------

.. code-block:: c

    enum sia_mmdsp_stat {
      SIA_MMDSP_GO,
      SIA_MMDSP_INIT
    };


.. _`sia_mmdsp_stat.constants`:

Constants
---------

:``SIA_MMDSP_GO``:
    SIAMMDSP interrupt has happened

:``SIA_MMDSP_INIT``:
    Status init


.. _`mbox_to_arm_err`:

enum mbox_to_arm_err
====================

.. c:type:: mbox_to_arm_err

    Error messages definition


.. _`mbox_to_arm_err.definition`:

Definition
----------

.. code-block:: c

    enum mbox_to_arm_err {
      INIT_ERR,
      PLLARMLOCKP_ERR,
      PLLDDRLOCKP_ERR,
      PLLSOC0LOCKP_ERR,
      PLLSOC1LOCKP_ERR,
      ARMWFI_ERR,
      SYSCLKOK_ERR,
      BOOT_ERR,
      ROMCODESAVECONTEXT,
      VARMHIGHSPEEDVALTO_ERR,
      VARMHIGHSPEEDACCESS_ERR,
      VARMLOWSPEEDVALTO_ERR,
      VARMLOWSPEEDACCESS_ERR,
      VARMRETENTIONVALTO_ERR,
      VARMRETENTIONACCESS_ERR,
      VAPEHIGHSPEEDVALTO_ERR,
      VSAFEHPVALTO_ERR,
      VMODSEL1VALTO_ERR,
      VMODSEL2VALTO_ERR,
      VARMOFFACCESS_ERR,
      VAPEOFFACCESS_ERR,
      VARMRETACCES_ERR,
      CURAPPWRSTISNOTBOOT,
      CURAPPWRSTISNOTEXECUTE,
      CURAPPWRSTISNOTSLEEPMODE,
      CURAPPWRSTISNOTCORRECTDBG,
      ARMREGU1VALTO_ERR,
      ARMREGU2VALTO_ERR,
      VAPEREGUVALTO_ERR,
      VSMPS3REGUVALTO_ERR,
      VMODREGUVALTO_ERR
    };


.. _`mbox_to_arm_err.constants`:

Constants
---------

:``INIT_ERR``:
    Init value

:``PLLARMLOCKP_ERR``:
    PLLARM has not been correctly locked in given time

:``PLLDDRLOCKP_ERR``:
    PLLDDR has not been correctly locked in the given time

:``PLLSOC0LOCKP_ERR``:
    PLLSOC0 has not been correctly locked in the given time

:``PLLSOC1LOCKP_ERR``:
    PLLSOC1 has not been correctly locked in the given time

:``ARMWFI_ERR``:
    The ARM WFI has not been correctly executed in the given time

:``SYSCLKOK_ERR``:
    The SYSCLK is not available in the given time

:``BOOT_ERR``:
    Romcode has not validated the XP70 self reset in the given time

:``ROMCODESAVECONTEXT``:
    The Romcode didn.t correctly save it secure context

:``VARMHIGHSPEEDVALTO_ERR``:
    The ARM high speed supply value transfered
    through I2C has not been correctly executed in the given time

:``VARMHIGHSPEEDACCESS_ERR``:
    The command value of VarmHighSpeedVal transfered
    through I2C has not been correctly executed in the given time

:``VARMLOWSPEEDVALTO_ERR``:
    The ARM low speed supply value transfered through
    I2C has not been correctly executed in the given time

:``VARMLOWSPEEDACCESS_ERR``:
    The command value of VarmLowSpeedVal transfered
    through I2C has not been correctly executed in the given time

:``VARMRETENTIONVALTO_ERR``:
    The ARM retention supply value transfered through
    I2C has not been correctly executed in the given time

:``VARMRETENTIONACCESS_ERR``:
    The command value of VarmRetentionVal transfered
    through I2C has not been correctly executed in the given time

:``VAPEHIGHSPEEDVALTO_ERR``:
    The APE highspeed supply value transfered through
    I2C has not been correctly executed in the given time

:``VSAFEHPVALTO_ERR``:
    The SAFE high power supply value transfered through I2C
    has not been correctly executed in the given time

:``VMODSEL1VALTO_ERR``:
    The MODEM sel1 supply value transfered through I2C has
    not been correctly executed in the given time

:``VMODSEL2VALTO_ERR``:
    The MODEM sel2 supply value transfered through I2C has
    not been correctly executed in the given time

:``VARMOFFACCESS_ERR``:
    The command value of Varm ON/OFF transfered through
    I2C has not been correctly executed in the given time

:``VAPEOFFACCESS_ERR``:
    The command value of Vape ON/OFF transfered through
    I2C has not been correctly executed in the given time

:``VARMRETACCES_ERR``:
    The command value of Varm retention ON/OFF transfered
    through I2C has not been correctly executed in the given time

:``CURAPPWRSTISNOTBOOT``:
    Generated when Arm want to do power state transition
    ApBoot to ApExecute but the power current state is not Apboot

:``CURAPPWRSTISNOTEXECUTE``:
    Generated when Arm want to do power state
    transition from ApExecute to others power state but the
    power current state is not ApExecute

:``CURAPPWRSTISNOTSLEEPMODE``:
    Generated when wake up events are transmitted
    but the power current state is not ApDeepSleep/ApSleep/ApIdle

:``CURAPPWRSTISNOTCORRECTDBG``:
    Generated when wake up events are transmitted
    but the power current state is not correct

:``ARMREGU1VALTO_ERR``:
    The ArmRegu1 value transferred through I2C has not
    been correctly executed in the given time

:``ARMREGU2VALTO_ERR``:
    The ArmRegu2 value transferred through I2C has not
    been correctly executed in the given time

:``VAPEREGUVALTO_ERR``:
    The VApeRegu value transfered through I2C has not
    been correctly executed in the given time

:``VSMPS3REGUVALTO_ERR``:
    The VSmps3Regu value transfered through I2C has not
    been correctly executed in the given time

:``VMODREGUVALTO_ERR``:
    The VModemRegu value transfered through I2C has not
    been correctly executed in the given time


.. _`sia_sva_pwr_policy`:

enum sia_sva_pwr_policy
=======================

.. c:type:: sia_sva_pwr_policy

    Power policy


.. _`sia_sva_pwr_policy.definition`:

Definition
----------

.. code-block:: c

    enum sia_sva_pwr_policy {
      NO_CHGT,
      DSPOFF_HWPOFF,
      DSPOFFRAMRET_HWPOFF,
      DSPCLKOFF_HWPOFF,
      DSPCLKOFF_HWPCLKOFF
    };


.. _`sia_sva_pwr_policy.constants`:

Constants
---------

:``NO_CHGT``:
    No change

:``DSPOFF_HWPOFF``:
-- undescribed --

:``DSPOFFRAMRET_HWPOFF``:
-- undescribed --

:``DSPCLKOFF_HWPOFF``:
-- undescribed --

:``DSPCLKOFF_HWPCLKOFF``:
-- undescribed --


.. _`auto_enable`:

enum auto_enable
================

.. c:type:: auto_enable

    Auto Power enable


.. _`auto_enable.definition`:

Definition
----------

.. code-block:: c

    enum auto_enable {
      AUTO_OFF,
      AUTO_ON
    };


.. _`auto_enable.constants`:

Constants
---------

:``AUTO_OFF``:
-- undescribed --

:``AUTO_ON``:
-- undescribed --


.. _`prcmu_power_status`:

enum prcmu_power_status
=======================

.. c:type:: prcmu_power_status

    results from set_power_state


.. _`prcmu_power_status.definition`:

Definition
----------

.. code-block:: c

    enum prcmu_power_status {
      PRCMU_SLEEP_OK,
      PRCMU_DEEP_SLEEP_OK,
      PRCMU_IDLE_OK,
      PRCMU_DEEPIDLE_OK,
      PRCMU_PRCMU2ARMPENDINGIT_ER,
      PRCMU_ARMPENDINGIT_ER
    };


.. _`prcmu_power_status.constants`:

Constants
---------

:``PRCMU_SLEEP_OK``:
    Sleep went ok

:``PRCMU_DEEP_SLEEP_OK``:
    DeepSleep went ok

:``PRCMU_IDLE_OK``:
    Idle went ok

:``PRCMU_DEEPIDLE_OK``:
    DeepIdle went ok

:``PRCMU_PRCMU2ARMPENDINGIT_ER``:
    Pending interrupt detected

:``PRCMU_ARMPENDINGIT_ER``:
    Pending interrupt detected


.. _`prcmu_auto_pm_config`:

struct prcmu_auto_pm_config
===========================

.. c:type:: prcmu_auto_pm_config

    Autonomous power management configuration.


.. _`prcmu_auto_pm_config.definition`:

Definition
----------

.. code-block:: c

  struct prcmu_auto_pm_config {
    u8 sia_auto_pm_enable;
    u8 sia_power_on;
    u8 sia_policy;
    u8 sva_auto_pm_enable;
    u8 sva_power_on;
    u8 sva_policy;
  };


.. _`prcmu_auto_pm_config.members`:

Members
-------

:``sia_auto_pm_enable``:
    SIA autonomous pm enable. (PRCMU_AUTO_PM_{OFF,ON})

:``sia_power_on``:
    SIA power ON enable. (PRCMU_AUTO_PM_POWER_ON\_\* bitmask)

:``sia_policy``:
    SIA power policy. (enum prcmu_auto_pm_policy)

:``sva_auto_pm_enable``:
    SVA autonomous pm enable. (PRCMU_AUTO_PM_{OFF,ON})

:``sva_power_on``:
    SVA power ON enable. (PRCMU_AUTO_PM_POWER_ON\_\* bitmask)

:``sva_policy``:
    SVA power policy. (enum prcmu_auto_pm_policy)


