.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/iosf_mbi.h

.. _`iosf_mbi_read`:

iosf_mbi_read
=============

.. c:function:: int iosf_mbi_read(u8 port, u8 opcode, u32 offset, u32 *mdr)

    MailBox Interface read command

    :param port:
        port indicating subunit being accessed
    :type port: u8

    :param opcode:
        port specific read or write opcode
    :type opcode: u8

    :param offset:
        register address offset
    :type offset: u32

    :param mdr:
        register data to be read
    :type mdr: u32 \*

.. _`iosf_mbi_read.description`:

Description
-----------

Locking is handled by spinlock - cannot sleep.

.. _`iosf_mbi_read.return`:

Return
------

Nonzero on error

.. _`iosf_mbi_write`:

iosf_mbi_write
==============

.. c:function:: int iosf_mbi_write(u8 port, u8 opcode, u32 offset, u32 mdr)

    MailBox unmasked write command

    :param port:
        port indicating subunit being accessed
    :type port: u8

    :param opcode:
        port specific read or write opcode
    :type opcode: u8

    :param offset:
        register address offset
    :type offset: u32

    :param mdr:
        register data to be written
    :type mdr: u32

.. _`iosf_mbi_write.description`:

Description
-----------

Locking is handled by spinlock - cannot sleep.

.. _`iosf_mbi_write.return`:

Return
------

Nonzero on error

.. _`iosf_mbi_modify`:

iosf_mbi_modify
===============

.. c:function:: int iosf_mbi_modify(u8 port, u8 opcode, u32 offset, u32 mdr, u32 mask)

    MailBox masked write command

    :param port:
        port indicating subunit being accessed
    :type port: u8

    :param opcode:
        port specific read or write opcode
    :type opcode: u8

    :param offset:
        register address offset
    :type offset: u32

    :param mdr:
        register data being modified
    :type mdr: u32

    :param mask:
        mask indicating bits in mdr to be modified
    :type mask: u32

.. _`iosf_mbi_modify.description`:

Description
-----------

Locking is handled by spinlock - cannot sleep.

.. _`iosf_mbi_modify.return`:

Return
------

Nonzero on error

.. _`iosf_mbi_punit_acquire`:

iosf_mbi_punit_acquire
======================

.. c:function:: void iosf_mbi_punit_acquire( void)

    Acquire access to the P-Unit

    :param void:
        no arguments
    :type void: 

.. _`iosf_mbi_punit_acquire.description`:

Description
-----------

One some systems the P-Unit accesses the PMIC to change various voltages
through the same bus as other kernel drivers use for e.g. battery monitoring.

If a driver sends requests to the P-Unit which require the P-Unit to access
the PMIC bus while another driver is also accessing the PMIC bus various bad
things happen.

Call this function before sending requests to the P-Unit which may make it
access the PMIC, be it through iosf_mbi\* functions or through other means.
This function will block all kernel access to the PMIC I2C bus, so that the
P-Unit can safely access the PMIC over the shared I2C bus.

Note on these systems the i2c-bus driver will request a sempahore from the
P-Unit for exclusive access to the PMIC bus when i2c drivers are accessing
it, but this does not appear to be sufficient, we still need to avoid making
certain P-Unit requests during the access window to avoid problems.

This function locks a mutex, as such it may sleep.

.. _`iosf_mbi_punit_release`:

iosf_mbi_punit_release
======================

.. c:function:: void iosf_mbi_punit_release( void)

    Release access to the P-Unit

    :param void:
        no arguments
    :type void: 

.. _`iosf_mbi_block_punit_i2c_access`:

iosf_mbi_block_punit_i2c_access
===============================

.. c:function:: int iosf_mbi_block_punit_i2c_access( void)

    Block P-Unit accesses to the PMIC bus

    :param void:
        no arguments
    :type void: 

.. _`iosf_mbi_block_punit_i2c_access.description`:

Description
-----------

Call this function to block P-Unit access to the PMIC I2C bus, so that the
kernel can safely access the PMIC over the shared I2C bus.

This function acquires the P-Unit bus semaphore and notifies
pmic_bus_access_notifier listeners that they may no longer access the
P-Unit in a way which may cause it to access the shared I2C bus.

Note this function may be called multiple times and the bus will not
be released until \ :c:func:`iosf_mbi_unblock_punit_i2c_access`\  has been called the
same amount of times.

.. _`iosf_mbi_block_punit_i2c_access.return`:

Return
------

Nonzero on error

.. _`iosf_mbi_register_pmic_bus_access_notifier`:

iosf_mbi_register_pmic_bus_access_notifier
==========================================

.. c:function:: int iosf_mbi_register_pmic_bus_access_notifier(struct notifier_block *nb)

    Register PMIC bus notifier

    :param nb:
        notifier_block to register
    :type nb: struct notifier_block \*

.. _`iosf_mbi_register_pmic_bus_access_notifier.description`:

Description
-----------

This function can be used by drivers which may need to acquire P-Unit
managed resources from interrupt context, where \ :c:func:`iosf_mbi_punit_acquire`\ 
can not be used.

This function allows a driver to register a notifier to get notified (in a
process context) before other drivers start accessing the PMIC bus.

This allows the driver to acquire any resources, which it may need during
the window the other driver is accessing the PMIC, before hand.

.. _`iosf_mbi_unregister_pmic_bus_access_notifier`:

iosf_mbi_unregister_pmic_bus_access_notifier
============================================

.. c:function:: int iosf_mbi_unregister_pmic_bus_access_notifier(struct notifier_block *nb)

    Unregister PMIC bus notifier

    :param nb:
        notifier_block to unregister
    :type nb: struct notifier_block \*

.. _`iosf_mbi_unregister_pmic_bus_access_notifier_unlocked`:

iosf_mbi_unregister_pmic_bus_access_notifier_unlocked
=====================================================

.. c:function:: int iosf_mbi_unregister_pmic_bus_access_notifier_unlocked(struct notifier_block *nb)

    Unregister PMIC bus notifier, unlocked

    :param nb:
        notifier_block to unregister
    :type nb: struct notifier_block \*

.. _`iosf_mbi_unregister_pmic_bus_access_notifier_unlocked.description`:

Description
-----------

Like \ :c:func:`iosf_mbi_unregister_pmic_bus_access_notifier`\ , but for use when the
caller has already called \ :c:func:`iosf_mbi_punit_acquire`\  itself.

.. _`iosf_mbi_assert_punit_acquired`:

iosf_mbi_assert_punit_acquired
==============================

.. c:function:: void iosf_mbi_assert_punit_acquired( void)

    Assert that the P-Unit has been acquired.

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

