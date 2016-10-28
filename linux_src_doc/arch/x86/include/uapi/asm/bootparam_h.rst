.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/uapi/asm/bootparam.h

.. _`x86_hardware_subarch`:

enum x86_hardware_subarch
=========================

.. c:type:: enum x86_hardware_subarch

    x86 hardware subarchitecture

.. _`x86_hardware_subarch.definition`:

Definition
----------

.. code-block:: c

    enum x86_hardware_subarch {
        X86_SUBARCH_PC,
        X86_SUBARCH_LGUEST,
        X86_SUBARCH_XEN,
        X86_SUBARCH_INTEL_MID,
        X86_SUBARCH_CE4100,
        X86_NR_SUBARCHS
    };

.. _`x86_hardware_subarch.constants`:

Constants
---------

X86_SUBARCH_PC
    Should be used if the hardware is enumerable using standard
    PC mechanisms (PCI, ACPI) and doesn't need a special boot flow.

X86_SUBARCH_LGUEST
    Used for x86 hypervisor demo, lguest

X86_SUBARCH_XEN
    Used for Xen guest types which follow the PV boot path,
    which start at asm \ :c:func:`startup_xen`\  entry point and later jump to the C
    \ :c:func:`xen_start_kernel`\  entry point. Both domU and dom0 type of guests are
    currently supportd through this PV boot path.

X86_SUBARCH_INTEL_MID
    Used for Intel MID (Mobile Internet Device) platform
    systems which do not have the PCI legacy interfaces.

X86_SUBARCH_CE4100
    Used for Intel CE media processor (CE4100) SoC for
    for settop boxes and media devices, the use of a subarch for CE4100
    is more of a hack...

X86_NR_SUBARCHS
    *undescribed*

.. _`x86_hardware_subarch.description`:

Description
-----------

The x86 hardware_subarch and hardware_subarch_data were added as of the x86
boot protocol 2.07 to help distinguish and support custom x86 boot
sequences. This enum represents accepted values for the x86
hardware_subarch.  Custom x86 boot sequences (not X86_SUBARCH_PC) do not
have or simply \*cannot\* make use of natural stubs like BIOS or EFI, the
hardware_subarch can be used on the Linux entry path to revector to a
subarchitecture stub when needed. This subarchitecture stub can be used to
set up Linux boot parameters or for special care to account for nonstandard
handling of page tables.

These enums should only ever be used by x86 code, and the code that uses
it should be well contained and compartamentalized.

KVM and Xen HVM do not have a subarch as these are expected to follow
standard x86 boot entries. If there is a genuine need for "hypervisor" type
that should be considered separately in the future. Future guest types
should seriously consider working with standard x86 boot stubs such as
the BIOS or EFI boot stubs.

.. _`x86_hardware_subarch.warning`:

WARNING
-------

this enum is only used for legacy hacks, for platform features that
are not easily enumerated or discoverable. You should not ever use
this for new features.

.. This file was automatic generated / don't edit.

