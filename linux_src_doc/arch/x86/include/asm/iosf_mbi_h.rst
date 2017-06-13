.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/iosf_mbi.h

.. _`iosf_mbi_read`:

iosf_mbi_read
=============

.. c:function:: int iosf_mbi_read(u8 port, u8 opcode, u32 offset, u32 *mdr)

    MailBox Interface read command

    :param u8 port:
        port indicating subunit being accessed

    :param u8 opcode:
        port specific read or write opcode

    :param u32 offset:
        register address offset

    :param u32 \*mdr:
        register data to be read

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

    :param u8 port:
        port indicating subunit being accessed

    :param u8 opcode:
        port specific read or write opcode

    :param u32 offset:
        register address offset

    :param u32 mdr:
        register data to be written

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

    :param u8 port:
        port indicating subunit being accessed

    :param u8 opcode:
        port specific read or write opcode

    :param u32 offset:
        register address offset

    :param u32 mdr:
        register data being modified

    :param u32 mask:
        mask indicating bits in mdr to be modified

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

    :param  void:
        no arguments

.. _`iosf_mbi_punit_acquire.description`:

Description
-----------

One some systems the P-Unit accesses the PMIC to change various voltages
through the same bus as other kernel drivers use for e.g. battery monitoring.

If a driver sends requests to the P-Unit which require the P-Unit to access
the PMIC bus while another driver is also accessing the PMIC bus various bad
things happen.

To avoid these problems this function must be called before accessing the
P-Unit or the PMIC, be it through iosf_mbi\* functions or through other means.

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

    :param  void:
        no arguments

.. _`iosf_mbi_register_pmic_bus_access_notifier`:

iosf_mbi_register_pmic_bus_access_notifier
==========================================

.. c:function:: int iosf_mbi_register_pmic_bus_access_notifier(struct notifier_block *nb)

    Register PMIC bus notifier

    :param struct notifier_block \*nb:
        notifier_block to register

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

    :param struct notifier_block \*nb:
        notifier_block to unregister

.. _`iosf_mbi_call_pmic_bus_access_notifier_chain`:

iosf_mbi_call_pmic_bus_access_notifier_chain
============================================

.. c:function:: int iosf_mbi_call_pmic_bus_access_notifier_chain(unsigned long val, void *v)

    Call PMIC bus notifier chain

    :param unsigned long val:
        action to pass into listener's notifier_call function

    :param void \*v:
        data pointer to pass into listener's notifier_call function

.. This file was automatic generated / don't edit.

