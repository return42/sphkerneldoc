.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rtc/rtc-ds1685.c

.. _`ds1685_read`:

ds1685_read
===========

.. c:function:: u8 ds1685_read(struct ds1685_priv *rtc, int reg)

    read a value from an rtc register.

    :param rtc:
        pointer to the ds1685 rtc structure.
    :type rtc: struct ds1685_priv \*

    :param reg:
        the register address to read.
    :type reg: int

.. _`ds1685_write`:

ds1685_write
============

.. c:function:: void ds1685_write(struct ds1685_priv *rtc, int reg, u8 value)

    write a value to an rtc register.

    :param rtc:
        pointer to the ds1685 rtc structure.
    :type rtc: struct ds1685_priv \*

    :param reg:
        the register address to write.
    :type reg: int

    :param value:
        value to write to the register.
    :type value: u8

.. _`ds1685_rtc_bcd2bin`:

ds1685_rtc_bcd2bin
==================

.. c:function:: u8 ds1685_rtc_bcd2bin(struct ds1685_priv *rtc, u8 val, u8 bcd_mask, u8 bin_mask)

    bcd2bin wrapper in case platform doesn't support BCD.

    :param rtc:
        pointer to the ds1685 rtc structure.
    :type rtc: struct ds1685_priv \*

    :param val:
        u8 time value to consider converting.
    :type val: u8

    :param bcd_mask:
        u8 mask value if BCD mode is used.
    :type bcd_mask: u8

    :param bin_mask:
        u8 mask value if BIN mode is used.
    :type bin_mask: u8

.. _`ds1685_rtc_bcd2bin.description`:

Description
-----------

Returns the value, converted to BIN if originally in BCD and bcd_mode TRUE.

.. _`ds1685_rtc_bin2bcd`:

ds1685_rtc_bin2bcd
==================

.. c:function:: u8 ds1685_rtc_bin2bcd(struct ds1685_priv *rtc, u8 val, u8 bin_mask, u8 bcd_mask)

    bin2bcd wrapper in case platform doesn't support BCD.

    :param rtc:
        pointer to the ds1685 rtc structure.
    :type rtc: struct ds1685_priv \*

    :param val:
        u8 time value to consider converting.
    :type val: u8

    :param bin_mask:
        u8 mask value if BIN mode is used.
    :type bin_mask: u8

    :param bcd_mask:
        u8 mask value if BCD mode is used.
    :type bcd_mask: u8

.. _`ds1685_rtc_bin2bcd.description`:

Description
-----------

Returns the value, converted to BCD if originally in BIN and bcd_mode TRUE.

.. _`ds1685_rtc_check_mday`:

ds1685_rtc_check_mday
=====================

.. c:function:: int ds1685_rtc_check_mday(struct ds1685_priv *rtc, u8 mday)

    check validity of the day of month.

    :param rtc:
        pointer to the ds1685 rtc structure.
    :type rtc: struct ds1685_priv \*

    :param mday:
        day of month.
    :type mday: u8

.. _`ds1685_rtc_check_mday.description`:

Description
-----------

Returns -EDOM if the day of month is not within 1..31 range.

.. _`ds1685_rtc_switch_to_bank0`:

ds1685_rtc_switch_to_bank0
==========================

.. c:function:: void ds1685_rtc_switch_to_bank0(struct ds1685_priv *rtc)

    switch the rtc to bank 0.

    :param rtc:
        pointer to the ds1685 rtc structure.
    :type rtc: struct ds1685_priv \*

.. _`ds1685_rtc_switch_to_bank1`:

ds1685_rtc_switch_to_bank1
==========================

.. c:function:: void ds1685_rtc_switch_to_bank1(struct ds1685_priv *rtc)

    switch the rtc to bank 1.

    :param rtc:
        pointer to the ds1685 rtc structure.
    :type rtc: struct ds1685_priv \*

.. _`ds1685_rtc_begin_data_access`:

ds1685_rtc_begin_data_access
============================

.. c:function:: void ds1685_rtc_begin_data_access(struct ds1685_priv *rtc)

    prepare the rtc for data access.

    :param rtc:
        pointer to the ds1685 rtc structure.
    :type rtc: struct ds1685_priv \*

.. _`ds1685_rtc_begin_data_access.description`:

Description
-----------

This takes several steps to prepare the rtc for access to get/set time

.. _`ds1685_rtc_begin_data_access.and-alarm-values-from-the-rtc-registers`:

and alarm values from the rtc registers
---------------------------------------

- Sets the SET bit in Control Register B.
- Reads Ext Control Register 4A and checks the INCR bit.
- If INCR is active, a short delay is added before Ext Control Register 4A
is read again in a loop until INCR is inactive.
- Switches the rtc to bank 1.  This allows access to all relevant
data for normal rtc operation, as bank 0 contains only the nvram.

.. _`ds1685_rtc_end_data_access`:

ds1685_rtc_end_data_access
==========================

.. c:function:: void ds1685_rtc_end_data_access(struct ds1685_priv *rtc)

    end data access on the rtc.

    :param rtc:
        pointer to the ds1685 rtc structure.
    :type rtc: struct ds1685_priv \*

.. _`ds1685_rtc_end_data_access.this-ends-what-was-started-by-ds1685_rtc_begin_data_access`:

This ends what was started by ds1685_rtc_begin_data_access
----------------------------------------------------------

- Switches the rtc back to bank 0.
- Clears the SET bit in Control Register B.

.. _`ds1685_rtc_begin_ctrl_access`:

ds1685_rtc_begin_ctrl_access
============================

.. c:function:: void ds1685_rtc_begin_ctrl_access(struct ds1685_priv *rtc, unsigned long *flags)

    prepare the rtc for ctrl access.

    :param rtc:
        pointer to the ds1685 rtc structure.
    :type rtc: struct ds1685_priv \*

    :param flags:
        irq flags variable for spin_lock_irqsave.
    :type flags: unsigned long \*

.. _`ds1685_rtc_begin_ctrl_access.description`:

Description
-----------

This takes several steps to prepare the rtc for access to read just the

.. _`ds1685_rtc_begin_ctrl_access.control-registers`:

control registers
-----------------

- Sets a spinlock on the rtc IRQ.
- Switches the rtc to bank 1.  This allows access to the two extended
control registers.

Only use this where you are certain another lock will not be held.

.. _`ds1685_rtc_end_ctrl_access`:

ds1685_rtc_end_ctrl_access
==========================

.. c:function:: void ds1685_rtc_end_ctrl_access(struct ds1685_priv *rtc, unsigned long flags)

    end ctrl access on the rtc.

    :param rtc:
        pointer to the ds1685 rtc structure.
    :type rtc: struct ds1685_priv \*

    :param flags:
        irq flags variable for spin_unlock_irqrestore.
    :type flags: unsigned long

.. _`ds1685_rtc_end_ctrl_access.this-ends-what-was-started-by-ds1685_rtc_begin_ctrl_access`:

This ends what was started by ds1685_rtc_begin_ctrl_access
----------------------------------------------------------

- Switches the rtc back to bank 0.
- Unsets the spinlock on the rtc IRQ.

.. _`ds1685_rtc_get_ssn`:

ds1685_rtc_get_ssn
==================

.. c:function:: void ds1685_rtc_get_ssn(struct ds1685_priv *rtc, u8 *ssn)

    retrieve the silicon serial number.

    :param rtc:
        pointer to the ds1685 rtc structure.
    :type rtc: struct ds1685_priv \*

    :param ssn:
        u8 array to hold the bits of the silicon serial number.
    :type ssn: u8 \*

.. _`ds1685_rtc_get_ssn.description`:

Description
-----------

This number starts at 0x40, and is 8-bytes long, ending at 0x47. The
first byte is the model number, the next six bytes are the serial number
digits, and the final byte is a CRC check byte.  Together, they form the
silicon serial number.

These values are stored in bank1, so ds1685_rtc_switch_to_bank1 must be
called first before calling this function, else data will be read out of
the bank0 NVRAM.  Be sure to call ds1685_rtc_switch_to_bank0 when done.

.. _`ds1685_rtc_read_time`:

ds1685_rtc_read_time
====================

.. c:function:: int ds1685_rtc_read_time(struct device *dev, struct rtc_time *tm)

    reads the time registers.

    :param dev:
        pointer to device structure.
    :type dev: struct device \*

    :param tm:
        pointer to rtc_time structure.
    :type tm: struct rtc_time \*

.. _`ds1685_rtc_set_time`:

ds1685_rtc_set_time
===================

.. c:function:: int ds1685_rtc_set_time(struct device *dev, struct rtc_time *tm)

    sets the time registers.

    :param dev:
        pointer to device structure.
    :type dev: struct device \*

    :param tm:
        pointer to rtc_time structure.
    :type tm: struct rtc_time \*

.. _`ds1685_rtc_read_alarm`:

ds1685_rtc_read_alarm
=====================

.. c:function:: int ds1685_rtc_read_alarm(struct device *dev, struct rtc_wkalrm *alrm)

    reads the alarm registers.

    :param dev:
        pointer to device structure.
    :type dev: struct device \*

    :param alrm:
        pointer to rtc_wkalrm structure.
    :type alrm: struct rtc_wkalrm \*

.. _`ds1685_rtc_read_alarm.there-are-three-primary-alarm-registers`:

There are three primary alarm registers
---------------------------------------

seconds, minutes, and hours.
A fourth alarm register for the month date is also available in bank1 for
kickstart/wakeup features.  The DS1685/DS1687 manual states that a
"don't care" value ranging from 0xc0 to 0xff may be written into one or
more of the three alarm bytes to act as a wildcard value.  The fourth
byte doesn't support a "don't care" value.

.. _`ds1685_rtc_set_alarm`:

ds1685_rtc_set_alarm
====================

.. c:function:: int ds1685_rtc_set_alarm(struct device *dev, struct rtc_wkalrm *alrm)

    sets the alarm in registers.

    :param dev:
        pointer to device structure.
    :type dev: struct device \*

    :param alrm:
        pointer to rtc_wkalrm structure.
    :type alrm: struct rtc_wkalrm \*

.. _`ds1685_rtc_alarm_irq_enable`:

ds1685_rtc_alarm_irq_enable
===========================

.. c:function:: int ds1685_rtc_alarm_irq_enable(struct device *dev, unsigned int enabled)

    replaces \ :c:func:`ioctl`\  RTC_AIE on/off.

    :param dev:
        pointer to device structure.
    :type dev: struct device \*

    :param enabled:
        flag indicating whether to enable or disable.
    :type enabled: unsigned int

.. _`ds1685_rtc_irq_handler`:

ds1685_rtc_irq_handler
======================

.. c:function:: irqreturn_t ds1685_rtc_irq_handler(int irq, void *dev_id)

    IRQ handler.

    :param irq:
        IRQ number.
    :type irq: int

    :param dev_id:
        platform device pointer.
    :type dev_id: void \*

.. _`ds1685_rtc_work_queue`:

ds1685_rtc_work_queue
=====================

.. c:function:: void ds1685_rtc_work_queue(struct work_struct *work)

    work queue handler.

    :param work:
        work_struct containing data to work on in task context.
    :type work: struct work_struct \*

.. _`ds1685_rtc_proc`:

ds1685_rtc_proc
===============

.. c:function:: int ds1685_rtc_proc(struct device *dev, struct seq_file *seq)

    procfs access function.

    :param dev:
        pointer to device structure.
    :type dev: struct device \*

    :param seq:
        pointer to seq_file structure.
    :type seq: struct seq_file \*

.. _`ds1685_rtc_sysfs_battery_show`:

ds1685_rtc_sysfs_battery_show
=============================

.. c:function:: ssize_t ds1685_rtc_sysfs_battery_show(struct device *dev, struct device_attribute *attr, char *buf)

    sysfs file for main battery status.

    :param dev:
        pointer to device structure.
    :type dev: struct device \*

    :param attr:
        pointer to device_attribute structure.
    :type attr: struct device_attribute \*

    :param buf:
        pointer to char array to hold the output.
    :type buf: char \*

.. _`ds1685_rtc_sysfs_auxbatt_show`:

ds1685_rtc_sysfs_auxbatt_show
=============================

.. c:function:: ssize_t ds1685_rtc_sysfs_auxbatt_show(struct device *dev, struct device_attribute *attr, char *buf)

    sysfs file for aux battery status.

    :param dev:
        pointer to device structure.
    :type dev: struct device \*

    :param attr:
        pointer to device_attribute structure.
    :type attr: struct device_attribute \*

    :param buf:
        pointer to char array to hold the output.
    :type buf: char \*

.. _`ds1685_rtc_sysfs_serial_show`:

ds1685_rtc_sysfs_serial_show
============================

.. c:function:: ssize_t ds1685_rtc_sysfs_serial_show(struct device *dev, struct device_attribute *attr, char *buf)

    sysfs file for silicon serial number.

    :param dev:
        pointer to device structure.
    :type dev: struct device \*

    :param attr:
        pointer to device_attribute structure.
    :type attr: struct device_attribute \*

    :param buf:
        pointer to char array to hold the output.
    :type buf: char \*

.. _`ds1685_rtc_probe`:

ds1685_rtc_probe
================

.. c:function:: int ds1685_rtc_probe(struct platform_device *pdev)

    initializes rtc driver.

    :param pdev:
        pointer to platform_device structure.
    :type pdev: struct platform_device \*

.. _`ds1685_rtc_remove`:

ds1685_rtc_remove
=================

.. c:function:: int ds1685_rtc_remove(struct platform_device *pdev)

    removes rtc driver.

    :param pdev:
        pointer to platform_device structure.
    :type pdev: struct platform_device \*

.. _`ds1685_rtc_poweroff`:

ds1685_rtc_poweroff
===================

.. c:function:: void __noreturn ds1685_rtc_poweroff(struct platform_device *pdev)

    uses the RTC chip to power the system off.

    :param pdev:
        pointer to platform_device structure.
    :type pdev: struct platform_device \*

.. This file was automatic generated / don't edit.

