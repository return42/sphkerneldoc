.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/dbx500-prcmu.h

.. _`prcmu_wdog_id`:

enum prcmu_wdog_id
==================

.. c:type:: enum prcmu_wdog_id

    PRCMU watchdog IDs

.. _`prcmu_wdog_id.definition`:

Definition
----------

.. code-block:: c

    enum prcmu_wdog_id {
        PRCMU_WDOG_ALL,
        PRCMU_WDOG_CPU1,
        PRCMU_WDOG_CPU2
    };

.. _`prcmu_wdog_id.constants`:

Constants
---------

PRCMU_WDOG_ALL
    use all timers

PRCMU_WDOG_CPU1
    use first CPU timer only

PRCMU_WDOG_CPU2
    use second CPU timer conly

.. _`ape_opp`:

enum ape_opp
============

.. c:type:: enum ape_opp

    APE OPP states definition

.. _`ape_opp.definition`:

Definition
----------

.. code-block:: c

    enum ape_opp {
        APE_OPP_INIT,
        APE_NO_CHANGE,
        APE_100_OPP,
        APE_50_OPP,
        APE_50_PARTLY_25_OPP
    };

.. _`ape_opp.constants`:

Constants
---------

APE_OPP_INIT
    *undescribed*

APE_NO_CHANGE
    The APE operating point is unchanged

APE_100_OPP
    The new APE operating point is ape100opp

APE_50_OPP
    50%

APE_50_PARTLY_25_OPP
    50%, except some clocks at 25%.

.. _`arm_opp`:

enum arm_opp
============

.. c:type:: enum arm_opp

    ARM OPP states definition

.. _`arm_opp.definition`:

Definition
----------

.. code-block:: c

    enum arm_opp {
        ARM_OPP_INIT,
        ARM_NO_CHANGE,
        ARM_100_OPP,
        ARM_50_OPP,
        ARM_MAX_OPP,
        ARM_MAX_FREQ100OPP,
        ARM_EXTCLK
    };

.. _`arm_opp.constants`:

Constants
---------

ARM_OPP_INIT
    *undescribed*

ARM_NO_CHANGE
    The ARM operating point is unchanged

ARM_100_OPP
    The new ARM operating point is arm100opp

ARM_50_OPP
    The new ARM operating point is arm50opp

ARM_MAX_OPP
    Operating point is "max" (more than 100)

ARM_MAX_FREQ100OPP
    Set max opp if available, else 100

ARM_EXTCLK
    The new ARM operating point is armExtClk

.. _`ddr_opp`:

enum ddr_opp
============

.. c:type:: enum ddr_opp

    DDR OPP states definition

.. _`ddr_opp.definition`:

Definition
----------

.. code-block:: c

    enum ddr_opp {
        DDR_100_OPP,
        DDR_50_OPP,
        DDR_25_OPP
    };

.. _`ddr_opp.constants`:

Constants
---------

DDR_100_OPP
    The new DDR operating point is ddr100opp

DDR_50_OPP
    The new DDR operating point is ddr50opp

DDR_25_OPP
    The new DDR operating point is ddr25opp

.. _`ddr_pwrst`:

enum ddr_pwrst
==============

.. c:type:: enum ddr_pwrst

    DDR power states definition

.. _`ddr_pwrst.definition`:

Definition
----------

.. code-block:: c

    enum ddr_pwrst {
        DDR_PWR_STATE_UNCHANGED,
        DDR_PWR_STATE_ON,
        DDR_PWR_STATE_OFFLOWLAT,
        DDR_PWR_STATE_OFFHIGHLAT
    };

.. _`ddr_pwrst.constants`:

Constants
---------

DDR_PWR_STATE_UNCHANGED
    SDRAM and DDR controller state is unchanged

DDR_PWR_STATE_ON
    *undescribed*

DDR_PWR_STATE_OFFLOWLAT
    *undescribed*

DDR_PWR_STATE_OFFHIGHLAT
    *undescribed*

.. This file was automatic generated / don't edit.

