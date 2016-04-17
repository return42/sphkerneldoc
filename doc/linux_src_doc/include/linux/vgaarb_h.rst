.. -*- coding: utf-8; mode: rst -*-

========
vgaarb.h
========


.. _`vga_set_legacy_decoding`:

vga_set_legacy_decoding
=======================

.. c:function:: void vga_set_legacy_decoding (struct pci_dev *pdev, unsigned int decodes)

    :param struct pci_dev \*pdev:
        pci device of the VGA card

    :param unsigned int decodes:
        bit mask of what legacy regions the card decodes



.. _`vga_set_legacy_decoding.description`:

Description
-----------

Indicates to the arbiter if the card decodes legacy VGA IOs,
legacy VGA Memory, both, or none. All cards default to both,
the card driver (fbdev for example) should tell the arbiter
if it has disabled legacy decoding, so the card can be left
out of the arbitration process (and can be safe to take
interrupts at any time.



.. _`vga_get`:

vga_get
=======

.. c:function:: int vga_get (struct pci_dev *pdev, unsigned int rsrc, int interruptible)

    acquire & locks VGA resources

    :param struct pci_dev \*pdev:
        pci device of the VGA card or NULL for the system default

    :param unsigned int rsrc:
        bit mask of resources to acquire and lock

    :param int interruptible:
        blocking should be interruptible by signals ?



.. _`vga_get.description`:

Description
-----------

This function acquires VGA resources for the given
card and mark those resources locked. If the resource requested
are "normal" (and not legacy) resources, the arbiter will first check
whether the card is doing legacy decoding for that type of resource. If
yes, the lock is "converted" into a legacy resource lock.
The arbiter will first look for all VGA cards that might conflict
and disable their IOs and/or Memory access, including VGA forwarding
on P2P bridges if necessary, so that the requested resources can
be used. Then, the card is marked as locking these resources and
the IO and/or Memory accesse are enabled on the card (including
VGA forwarding on parent P2P bridges if any).
This function will block if some conflicting card is already locking
one of the required resources (or any resource on a different bus
segment, since P2P bridges don't differenciate VGA memory and IO
afaik). You can indicate whether this blocking should be interruptible
by a signal (for userland interface) or not.
Must not be called at interrupt time or in atomic context.
If the card already owns the resources, the function succeeds.
Nested calls are supported (a per-resource counter is maintained)



.. _`vga_get_interruptible`:

vga_get_interruptible
=====================

.. c:function:: int vga_get_interruptible (struct pci_dev *pdev, unsigned int rsrc)

    :param struct pci_dev \*pdev:

        *undescribed*

    :param unsigned int rsrc:

        *undescribed*



.. _`vga_get_interruptible.description`:

Description
-----------


Shortcut to vga_get



.. _`vga_get_uninterruptible`:

vga_get_uninterruptible
=======================

.. c:function:: int vga_get_uninterruptible (struct pci_dev *pdev, unsigned int rsrc)

    :param struct pci_dev \*pdev:

        *undescribed*

    :param unsigned int rsrc:

        *undescribed*



.. _`vga_get_uninterruptible.description`:

Description
-----------


Shortcut to vga_get



.. _`vga_tryget`:

vga_tryget
==========

.. c:function:: int vga_tryget (struct pci_dev *pdev, unsigned int rsrc)

    try to acquire & lock legacy VGA resources

    :param struct pci_dev \*pdev:
        pci devivce of VGA card or NULL for system default

    :param unsigned int rsrc:
        bit mask of resources to acquire and lock



.. _`vga_tryget.description`:

Description
-----------

This function performs the same operation as :c:func:`vga_get`, but
will return an error (-EBUSY) instead of blocking if the resources
are already locked by another card. It can be called in any context



.. _`vga_put`:

vga_put
=======

.. c:function:: void vga_put (struct pci_dev *pdev, unsigned int rsrc)

    release lock on legacy VGA resources

    :param struct pci_dev \*pdev:
        pci device of VGA card or NULL for system default

    :param unsigned int rsrc:
        but mask of resource to release



.. _`vga_put.description`:

Description
-----------

This function releases resources previously locked by :c:func:`vga_get`
or :c:func:`vga_tryget`. The resources aren't disabled right away, so
that a subsequence :c:func:`vga_get` on the same card will succeed
immediately. Resources have a counter, so locks are only
released if the counter reaches 0.



.. _`vga_default_device`:

vga_default_device
==================

.. c:function:: struct pci_dev *vga_default_device ( void)

    :param void:
        no arguments



.. _`vga_default_device.description`:

Description
-----------


This can be defined by the platform. The default implementation
is rather dumb and will probably only work properly on single
vga card setups and/or x86 platforms.

If your VGA default device is not PCI, you'll have to return
NULL here. In this case, I assume it will not conflict with
any PCI card. If this is not true, I'll have to define two archs
hooks for enabling/disabling the VGA default device if that is
possible. This may be a problem with real _ISA_ VGA cards, in
addition to a PCI one. I don't know at this point how to deal
with that card. Can theirs IOs be disabled at all ? If not, then
I suppose it's a matter of having the proper arch hook telling
us about it, so we basically never allow anybody to succeed a
:c:func:`vga_get`...



.. _`vga_conflicts`:

vga_conflicts
=============

.. c:function:: int vga_conflicts (struct pci_dev *p1, struct pci_dev *p2)

    :param struct pci_dev \*p1:

        *undescribed*

    :param struct pci_dev \*p2:

        *undescribed*



.. _`vga_conflicts.description`:

Description
-----------


Architectures should define this if they have several
independent PCI domains that can afford concurrent VGA
decoding



.. _`vga_client_register`:

vga_client_register
===================

.. c:function:: int vga_client_register (struct pci_dev *pdev, void *cookie, void (*irq_set_state) (void *cookie, bool state, unsigned int (*set_vga_decode) (void *cookie, bool state)

    :param struct pci_dev \*pdev:
        pci device of the VGA client

    :param void \*cookie:
        client cookie to be used in callbacks

    :param void (\*irq_set_state) (void \*cookie, bool state):
        irq state change callback

    :param unsigned int (\*set_vga_decode) (void \*cookie, bool state):
        vga decode change callback



.. _`vga_client_register.return-value`:

return value
------------

0 on success, -1 on failure

        Register a client with the VGA arbitration logic

        Clients have two callback mechanisms they can use.
        irq enable/disable callback -
                If a client can't disable its GPUs VGA resources, then we
                need to be able to ask it to turn off its irqs when we
                turn off its mem and io decoding.
        set_vga_decode
                If a client can disable its GPU VGA resource, it will
                get a callback from this to set the encode/decode state



.. _`vga_client_register.rationale`:

Rationale
---------

we cannot disable VGA decode resources unconditionally
some single GPU laptops seem to require ACPI or BIOS access to the
VGA registers to control things like backlights etc.
Hopefully newer multi-GPU laptops do something saner, and desktops
won't have any special ACPI for this.
They driver will get a callback when VGA arbitration is first used
by userspace since we some older X servers have issues.

