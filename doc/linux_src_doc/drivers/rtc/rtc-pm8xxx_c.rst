.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rtc/rtc-pm8xxx.c

.. _`pm8xxx_rtc_regs`:

struct pm8xxx_rtc_regs
======================

.. c:type:: struct pm8xxx_rtc_regs

    describe RTC registers per PMIC versions

.. _`pm8xxx_rtc_regs.definition`:

Definition
----------

.. code-block:: c

    struct pm8xxx_rtc_regs {
        unsigned int ctrl;
        unsigned int write;
        unsigned int read;
        unsigned int alarm_ctrl;
        unsigned int alarm_ctrl2;
        unsigned int alarm_rw;
        unsigned int alarm_en;
    }

.. _`pm8xxx_rtc_regs.members`:

Members
-------

ctrl
    base address of control register

write
    base address of write register

read
    base address of read register

alarm_ctrl
    base address of alarm control register

alarm_ctrl2
    base address of alarm control2 register

alarm_rw
    base address of alarm read-write register

alarm_en
    alarm enable mask

.. _`pm8xxx_rtc`:

struct pm8xxx_rtc
=================

.. c:type:: struct pm8xxx_rtc

    rtc driver internal structure

.. _`pm8xxx_rtc.definition`:

Definition
----------

.. code-block:: c

    struct pm8xxx_rtc {
        struct rtc_device *rtc;
        struct regmap *regmap;
        bool allow_set_time;
        int rtc_alarm_irq;
        const struct pm8xxx_rtc_regs *regs;
        struct device *rtc_dev;
        spinlock_t ctrl_reg_lock;
    }

.. _`pm8xxx_rtc.members`:

Members
-------

rtc
    rtc device for this driver.

regmap
    regmap used to access RTC registers

allow_set_time
    indicates whether writing to the RTC is allowed

rtc_alarm_irq
    rtc alarm irq number.

regs
    *undescribed*

rtc_dev
    device structure.

ctrl_reg_lock
    spinlock protecting access to ctrl_reg.

.. This file was automatic generated / don't edit.

