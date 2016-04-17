.. -*- coding: utf-8; mode: rst -*-

============
rtc-ds1685.c
============


.. _`ds1685_read`:

ds1685_read
===========

.. c:function:: u8 ds1685_read (struct ds1685_priv *rtc, int reg)

    read a value from an rtc register.

    :param struct ds1685_priv \*rtc:
        pointer to the ds1685 rtc structure.

    :param int reg:
        the register address to read.



.. _`ds1685_write`:

ds1685_write
============

.. c:function:: void ds1685_write (struct ds1685_priv *rtc, int reg, u8 value)

    write a value to an rtc register.

    :param struct ds1685_priv \*rtc:
        pointer to the ds1685 rtc structure.

    :param int reg:
        the register address to write.

    :param u8 value:
        value to write to the register.



.. _`ds1685_rtc_bcd2bin`:

ds1685_rtc_bcd2bin
==================

.. c:function:: u8 ds1685_rtc_bcd2bin (struct ds1685_priv *rtc, u8 val, u8 bcd_mask, u8 bin_mask)

    bcd2bin wrapper in case platform doesn't support BCD.

    :param struct ds1685_priv \*rtc:
        pointer to the ds1685 rtc structure.

    :param u8 val:
        u8 time value to consider converting.

    :param u8 bcd_mask:
        u8 mask value if BCD mode is used.

    :param u8 bin_mask:
        u8 mask value if BIN mode is used.



.. _`ds1685_rtc_bcd2bin.description`:

Description
-----------

Returns the value, converted to BIN if originally in BCD and bcd_mode TRUE.



.. _`ds1685_rtc_bin2bcd`:

ds1685_rtc_bin2bcd
==================

.. c:function:: u8 ds1685_rtc_bin2bcd (struct ds1685_priv *rtc, u8 val, u8 bin_mask, u8 bcd_mask)

    bin2bcd wrapper in case platform doesn't support BCD.

    :param struct ds1685_priv \*rtc:
        pointer to the ds1685 rtc structure.

    :param u8 val:
        u8 time value to consider converting.

    :param u8 bin_mask:
        u8 mask value if BIN mode is used.

    :param u8 bcd_mask:
        u8 mask value if BCD mode is used.



.. _`ds1685_rtc_bin2bcd.description`:

Description
-----------

Returns the value, converted to BCD if originally in BIN and bcd_mode TRUE.



.. _`ds1685_rtc_switch_to_bank0`:

ds1685_rtc_switch_to_bank0
==========================

.. c:function:: void ds1685_rtc_switch_to_bank0 (struct ds1685_priv *rtc)

    switch the rtc to bank 0.

    :param struct ds1685_priv \*rtc:
        pointer to the ds1685 rtc structure.



.. _`ds1685_rtc_switch_to_bank1`:

ds1685_rtc_switch_to_bank1
==========================

.. c:function:: void ds1685_rtc_switch_to_bank1 (struct ds1685_priv *rtc)

    switch the rtc to bank 1.

    :param struct ds1685_priv \*rtc:
        pointer to the ds1685 rtc structure.



.. _`ds1685_rtc_begin_data_access`:

ds1685_rtc_begin_data_access
============================

.. c:function:: void ds1685_rtc_begin_data_access (struct ds1685_priv *rtc)

    prepare the rtc for data access.

    :param struct ds1685_priv \*rtc:
        pointer to the ds1685 rtc structure.



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

.. c:function:: void ds1685_rtc_end_data_access (struct ds1685_priv *rtc)

    end data access on the rtc.

    :param struct ds1685_priv \*rtc:
        pointer to the ds1685 rtc structure.



.. _`ds1685_rtc_end_data_access.this-ends-what-was-started-by-ds1685_rtc_begin_data_access`:

This ends what was started by ds1685_rtc_begin_data_access
----------------------------------------------------------

- Switches the rtc back to bank 0.
- Clears the SET bit in Control Register B.



.. _`ds1685_rtc_begin_ctrl_access`:

ds1685_rtc_begin_ctrl_access
============================

.. c:function:: void ds1685_rtc_begin_ctrl_access (struct ds1685_priv *rtc, unsigned long *flags)

    prepare the rtc for ctrl access.

    :param struct ds1685_priv \*rtc:
        pointer to the ds1685 rtc structure.

    :param unsigned long \*flags:
        irq flags variable for spin_lock_irqsave.



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

.. c:function:: void ds1685_rtc_end_ctrl_access (struct ds1685_priv *rtc, unsigned long flags)

    end ctrl access on the rtc.

    :param struct ds1685_priv \*rtc:
        pointer to the ds1685 rtc structure.

    :param unsigned long flags:
        irq flags variable for spin_unlock_irqrestore.



.. _`ds1685_rtc_end_ctrl_access.this-ends-what-was-started-by-ds1685_rtc_begin_ctrl_access`:

This ends what was started by ds1685_rtc_begin_ctrl_access
----------------------------------------------------------

- Switches the rtc back to bank 0.
- Unsets the spinlock on the rtc IRQ.



.. _`ds1685_rtc_get_ssn`:

ds1685_rtc_get_ssn
==================

.. c:function:: void ds1685_rtc_get_ssn (struct ds1685_priv *rtc, u8 *ssn)

    retrieve the silicon serial number.

    :param struct ds1685_priv \*rtc:
        pointer to the ds1685 rtc structure.

    :param u8 \*ssn:
        u8 array to hold the bits of the silicon serial number.



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

.. c:function:: int ds1685_rtc_read_time (struct device *dev, struct rtc_time *tm)

    reads the time registers.

    :param struct device \*dev:
        pointer to device structure.

    :param struct rtc_time \*tm:
        pointer to rtc_time structure.



.. _`ds1685_rtc_set_time`:

ds1685_rtc_set_time
===================

.. c:function:: int ds1685_rtc_set_time (struct device *dev, struct rtc_time *tm)

    sets the time registers.

    :param struct device \*dev:
        pointer to device structure.

    :param struct rtc_time \*tm:
        pointer to rtc_time structure.



.. _`ds1685_rtc_read_alarm`:

ds1685_rtc_read_alarm
=====================

.. c:function:: int ds1685_rtc_read_alarm (struct device *dev, struct rtc_wkalrm *alrm)

    reads the alarm registers.

    :param struct device \*dev:
        pointer to device structure.

    :param struct rtc_wkalrm \*alrm:
        pointer to rtc_wkalrm structure.



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

.. c:function:: int ds1685_rtc_set_alarm (struct device *dev, struct rtc_wkalrm *alrm)

    sets the alarm in registers.

    :param struct device \*dev:
        pointer to device structure.

    :param struct rtc_wkalrm \*alrm:
        pointer to rtc_wkalrm structure.



.. _`ds1685_rtc_alarm_irq_enable`:

ds1685_rtc_alarm_irq_enable
===========================

.. c:function:: int ds1685_rtc_alarm_irq_enable (struct device *dev, unsigned int enabled)

    replaces ioctl() RTC_AIE on/off.

    :param struct device \*dev:
        pointer to device structure.

    :param unsigned int enabled:
        flag indicating whether to enable or disable.



.. _`ds1685_rtc_irq_handler`:

ds1685_rtc_irq_handler
======================

.. c:function:: irqreturn_t ds1685_rtc_irq_handler (int irq, void *dev_id)

    IRQ handler.

    :param int irq:
        IRQ number.

    :param void \*dev_id:
        platform device pointer.



.. _`ds1685_rtc_work_queue`:

ds1685_rtc_work_queue
=====================

.. c:function:: void ds1685_rtc_work_queue (struct work_struct *work)

    work queue handler.

    :param struct work_struct \*work:
        work_struct containing data to work on in task context.



.. _`ds1685_rtc_print_regs`:

ds1685_rtc_print_regs
=====================

.. c:function:: char*ds1685_rtc_print_regs (u8 hex, char *dest)

    helper function to print register values.

    :param u8 hex:
        hex byte to convert into binary bits.

    :param char \*dest:
        destination char array.



.. _`ds1685_rtc_print_regs.description`:

Description
-----------

This is basically a hex->binary function, just with extra spacing between
the digits.  It only works on 1-byte values (8 bits).



.. _`ds1685_rtc_proc`:

ds1685_rtc_proc
===============

.. c:function:: int ds1685_rtc_proc (struct device *dev, struct seq_file *seq)

    procfs access function.

    :param struct device \*dev:
        pointer to device structure.

    :param struct seq_file \*seq:
        pointer to seq_file structure.



.. _`ds1685_rtc_sysfs_nvram_read`:

ds1685_rtc_sysfs_nvram_read
===========================

.. c:function:: ssize_t ds1685_rtc_sysfs_nvram_read (struct file *filp, struct kobject *kobj, struct bin_attribute *bin_attr, char *buf, loff_t pos, size_t size)

    reads rtc nvram via sysfs.

    :param struct file \*filp:

        *undescribed*

    :param struct kobject \*kobj:
        pointer to kobject structure.

    :param struct bin_attribute \*bin_attr:
        pointer to bin_attribute structure.

    :param char \*buf:
        pointer to char array to hold the output.

    :param loff_t pos:
        current file position pointer.

    :param size_t size:
        size of the data to read.



.. _`ds1685_rtc_sysfs_nvram_write`:

ds1685_rtc_sysfs_nvram_write
============================

.. c:function:: ssize_t ds1685_rtc_sysfs_nvram_write (struct file *filp, struct kobject *kobj, struct bin_attribute *bin_attr, char *buf, loff_t pos, size_t size)

    writes rtc nvram via sysfs.

    :param struct file \*filp:

        *undescribed*

    :param struct kobject \*kobj:
        pointer to kobject structure.

    :param struct bin_attribute \*bin_attr:
        pointer to bin_attribute structure.

    :param char \*buf:
        pointer to char array to hold the input.

    :param loff_t pos:
        current file position pointer.

    :param size_t size:
        size of the data to write.



.. _`ds1685_rtc_sysfs_battery_show`:

ds1685_rtc_sysfs_battery_show
=============================

.. c:function:: ssize_t ds1685_rtc_sysfs_battery_show (struct device *dev, struct device_attribute *attr, char *buf)

    sysfs file for main battery status.

    :param struct device \*dev:
        pointer to device structure.

    :param struct device_attribute \*attr:
        pointer to device_attribute structure.

    :param char \*buf:
        pointer to char array to hold the output.



.. _`ds1685_rtc_sysfs_auxbatt_show`:

ds1685_rtc_sysfs_auxbatt_show
=============================

.. c:function:: ssize_t ds1685_rtc_sysfs_auxbatt_show (struct device *dev, struct device_attribute *attr, char *buf)

    sysfs file for aux battery status.

    :param struct device \*dev:
        pointer to device structure.

    :param struct device_attribute \*attr:
        pointer to device_attribute structure.

    :param char \*buf:
        pointer to char array to hold the output.



.. _`ds1685_rtc_sysfs_serial_show`:

ds1685_rtc_sysfs_serial_show
============================

.. c:function:: ssize_t ds1685_rtc_sysfs_serial_show (struct device *dev, struct device_attribute *attr, char *buf)

    sysfs file for silicon serial number.

    :param struct device \*dev:
        pointer to device structure.

    :param struct device_attribute \*attr:
        pointer to device_attribute structure.

    :param char \*buf:
        pointer to char array to hold the output.



.. _`ds1685_rtc_ctrl_regs`:

struct ds1685_rtc_ctrl_regs
===========================

.. c:type:: ds1685_rtc_ctrl_regs

    


.. _`ds1685_rtc_ctrl_regs.definition`:

Definition
----------

.. code-block:: c

  struct ds1685_rtc_ctrl_regs {
    const char * name;
    const u8 reg;
    const u8 bit;
  };


.. _`ds1685_rtc_ctrl_regs.members`:

Members
-------

:``name``:
    char pointer for the bit name.

:``reg``:
    control register the bit is in.

:``bit``:
    the bit's offset in the register.




.. _`ds1685_rtc_sysfs_ctrl_regs_lookup`:

ds1685_rtc_sysfs_ctrl_regs_lookup
=================================

.. c:function:: const struct ds1685_rtc_ctrl_regs*ds1685_rtc_sysfs_ctrl_regs_lookup (const char *name)

    ctrl register bit lookup function.

    :param const char \*name:
        ctrl register bit to look up in ds1685_ctrl_regs_table.



.. _`ds1685_rtc_sysfs_ctrl_regs_show`:

ds1685_rtc_sysfs_ctrl_regs_show
===============================

.. c:function:: ssize_t ds1685_rtc_sysfs_ctrl_regs_show (struct device *dev, struct device_attribute *attr, char *buf)

    reads a ctrl register bit via sysfs.

    :param struct device \*dev:
        pointer to device structure.

    :param struct device_attribute \*attr:
        pointer to device_attribute structure.

    :param char \*buf:
        pointer to char array to hold the output.



.. _`ds1685_rtc_sysfs_ctrl_regs_store`:

ds1685_rtc_sysfs_ctrl_regs_store
================================

.. c:function:: ssize_t ds1685_rtc_sysfs_ctrl_regs_store (struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    writes a ctrl register bit via sysfs.

    :param struct device \*dev:
        pointer to device structure.

    :param struct device_attribute \*attr:
        pointer to device_attribute structure.

    :param const char \*buf:
        pointer to char array to hold the output.

    :param size_t count:
        number of bytes written.



.. _`ds1685_rtc_sysfs_ctrl_reg_ro`:

DS1685_RTC_SYSFS_CTRL_REG_RO
============================

.. c:function:: DS1685_RTC_SYSFS_CTRL_REG_RO ( bit)

    device_attribute for read-only register bit.

    :param bit:
        bit to read.



.. _`ds1685_rtc_sysfs_ctrl_reg_rw`:

DS1685_RTC_SYSFS_CTRL_REG_RW
============================

.. c:function:: DS1685_RTC_SYSFS_CTRL_REG_RW ( bit)

    device_attribute for read-write register bit.

    :param bit:
        bit to read or write.



.. _`ds1685_rtc_time_regs`:

struct ds1685_rtc_time_regs
===========================

.. c:type:: ds1685_rtc_time_regs

    


.. _`ds1685_rtc_time_regs.definition`:

Definition
----------

.. code-block:: c

  struct ds1685_rtc_time_regs {
    const char * name;
    const u8 reg;
  };


.. _`ds1685_rtc_time_regs.members`:

Members
-------

:``name``:
    char pointer for the bit name.

:``reg``:
    control register the bit is in.




.. _`ds1685_rtc_sysfs_time_regs_lookup`:

ds1685_rtc_sysfs_time_regs_lookup
=================================

.. c:function:: const struct ds1685_rtc_time_regs*ds1685_rtc_sysfs_time_regs_lookup (const char *name, bool bcd_mode)

    time/date reg bit lookup function.

    :param const char \*name:
        register bit to look up in ds1685_time_regs_bcd_table.

    :param bool bcd_mode:

        *undescribed*



.. _`ds1685_rtc_sysfs_time_regs_show`:

ds1685_rtc_sysfs_time_regs_show
===============================

.. c:function:: ssize_t ds1685_rtc_sysfs_time_regs_show (struct device *dev, struct device_attribute *attr, char *buf)

    reads a time/date register via sysfs.

    :param struct device \*dev:
        pointer to device structure.

    :param struct device_attribute \*attr:
        pointer to device_attribute structure.

    :param char \*buf:
        pointer to char array to hold the output.



.. _`ds1685_rtc_sysfs_time_regs_store`:

ds1685_rtc_sysfs_time_regs_store
================================

.. c:function:: ssize_t ds1685_rtc_sysfs_time_regs_store (struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    writes a time/date register via sysfs.

    :param struct device \*dev:
        pointer to device structure.

    :param struct device_attribute \*attr:
        pointer to device_attribute structure.

    :param const char \*buf:
        pointer to char array to hold the output.

    :param size_t count:
        number of bytes written.



.. _`ds1685_rtc_sysfs_time_reg_rw`:

DS1685_RTC_SYSFS_TIME_REG_RW
============================

.. c:function:: DS1685_RTC_SYSFS_TIME_REG_RW ( reg)

    device_attribute for a read-write time register.

    :param reg:
        time/date register to read or write.



.. _`ds1685_rtc_sysfs_register`:

ds1685_rtc_sysfs_register
=========================

.. c:function:: int ds1685_rtc_sysfs_register (struct device *dev)

    register sysfs files.

    :param struct device \*dev:
        pointer to device structure.



.. _`ds1685_rtc_sysfs_unregister`:

ds1685_rtc_sysfs_unregister
===========================

.. c:function:: int ds1685_rtc_sysfs_unregister (struct device *dev)

    unregister sysfs files.

    :param struct device \*dev:
        pointer to device structure.



.. _`ds1685_rtc_probe`:

ds1685_rtc_probe
================

.. c:function:: int ds1685_rtc_probe (struct platform_device *pdev)

    initializes rtc driver.

    :param struct platform_device \*pdev:
        pointer to platform_device structure.



.. _`ds1685_rtc_remove`:

ds1685_rtc_remove
=================

.. c:function:: int ds1685_rtc_remove (struct platform_device *pdev)

    removes rtc driver.

    :param struct platform_device \*pdev:
        pointer to platform_device structure.



.. _`ds1685_rtc_poweroff`:

ds1685_rtc_poweroff
===================

.. c:function:: void __noreturn ds1685_rtc_poweroff (struct platform_device *pdev)

    uses the RTC chip to power the system off.

    :param struct platform_device \*pdev:
        pointer to platform_device structure.

