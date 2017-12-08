.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/x86_init.h

.. _`x86_init_mpparse`:

struct x86_init_mpparse
=======================

.. c:type:: struct x86_init_mpparse

    platform specific mpparse ops

.. _`x86_init_mpparse.definition`:

Definition
----------

.. code-block:: c

    struct x86_init_mpparse {
        void (*mpc_record)(unsigned int mode);
        void (*setup_ioapic_ids)(void);
        int (*mpc_apic_id)(struct mpc_cpu *m);
        void (*smp_read_mpc_oem)(struct mpc_table *mpc);
        void (*mpc_oem_pci_bus)(struct mpc_bus *m);
        void (*mpc_oem_bus_info)(struct mpc_bus *m, char *name);
        void (*find_smp_config)(void);
        void (*get_smp_config)(unsigned int early);
    }

.. _`x86_init_mpparse.members`:

Members
-------

mpc_record
    platform specific mpc record accounting

setup_ioapic_ids
    platform specific ioapic id override

mpc_apic_id
    platform specific mpc apic id assignment

smp_read_mpc_oem
    platform specific oem mpc table setup

mpc_oem_pci_bus
    platform specific pci bus setup (default NULL)

mpc_oem_bus_info
    platform specific mpc bus info

find_smp_config
    find the smp configuration

get_smp_config
    get the smp configuration

.. _`x86_init_resources`:

struct x86_init_resources
=========================

.. c:type:: struct x86_init_resources

    platform specific resource related ops

.. _`x86_init_resources.definition`:

Definition
----------

.. code-block:: c

    struct x86_init_resources {
        void (*probe_roms)(void);
        void (*reserve_resources)(void);
        char *(*memory_setup)(void);
    }

.. _`x86_init_resources.members`:

Members
-------

probe_roms
    probe BIOS roms

reserve_resources
    reserve the standard resources for the
    platform

memory_setup
    platform specific memory setup

.. _`x86_init_irqs`:

struct x86_init_irqs
====================

.. c:type:: struct x86_init_irqs

    platform specific interrupt setup

.. _`x86_init_irqs.definition`:

Definition
----------

.. code-block:: c

    struct x86_init_irqs {
        void (*pre_vector_init)(void);
        void (*intr_init)(void);
        void (*trap_init)(void);
        void (*intr_mode_init)(void);
    }

.. _`x86_init_irqs.members`:

Members
-------

pre_vector_init
    init code to run before interrupt vectors
    are set up.

intr_init
    interrupt init code

trap_init
    platform specific trap setup

intr_mode_init
    interrupt delivery mode setup

.. _`x86_init_oem`:

struct x86_init_oem
===================

.. c:type:: struct x86_init_oem

    oem platform specific customizing functions

.. _`x86_init_oem.definition`:

Definition
----------

.. code-block:: c

    struct x86_init_oem {
        void (*arch_setup)(void);
        void (*banner)(void);
    }

.. _`x86_init_oem.members`:

Members
-------

arch_setup
    platform specific architecture setup

banner
    print a platform specific banner

.. _`x86_init_paging`:

struct x86_init_paging
======================

.. c:type:: struct x86_init_paging

    platform specific paging functions

.. _`x86_init_paging.definition`:

Definition
----------

.. code-block:: c

    struct x86_init_paging {
        void (*pagetable_init)(void);
    }

.. _`x86_init_paging.members`:

Members
-------

pagetable_init
    platform specific paging initialization call to setup
    the kernel pagetables and prepare accessors functions.
    Callback must call \ :c:func:`paging_init`\ . Called once after the
    direct mapping for phys memory is available.

.. _`x86_init_timers`:

struct x86_init_timers
======================

.. c:type:: struct x86_init_timers

    platform specific timer setup

.. _`x86_init_timers.definition`:

Definition
----------

.. code-block:: c

    struct x86_init_timers {
        void (*setup_percpu_clockev)(void);
        void (*timer_init)(void);
        void (*wallclock_init)(void);
    }

.. _`x86_init_timers.members`:

Members
-------

setup_percpu_clockev
    *undescribed*

timer_init
    initialize the platform timer (default PIT/HPET)

wallclock_init
    init the wallclock device

.. _`x86_init_iommu`:

struct x86_init_iommu
=====================

.. c:type:: struct x86_init_iommu

    platform specific iommu setup

.. _`x86_init_iommu.definition`:

Definition
----------

.. code-block:: c

    struct x86_init_iommu {
        int (*iommu_init)(void);
    }

.. _`x86_init_iommu.members`:

Members
-------

iommu_init
    platform specific iommu setup

.. _`x86_init_pci`:

struct x86_init_pci
===================

.. c:type:: struct x86_init_pci

    platform specific pci init functions

.. _`x86_init_pci.definition`:

Definition
----------

.. code-block:: c

    struct x86_init_pci {
        int (*arch_init)(void);
        int (*init)(void);
        void (*init_irq)(void);
        void (*fixup_irqs)(void);
    }

.. _`x86_init_pci.members`:

Members
-------

arch_init
    platform specific pci arch init call

init
    platform specific pci subsystem init

init_irq
    platform specific pci irq init

fixup_irqs
    platform specific pci irq fixup

.. _`x86_hyper_init`:

struct x86_hyper_init
=====================

.. c:type:: struct x86_hyper_init

    x86 hypervisor init functions

.. _`x86_hyper_init.definition`:

Definition
----------

.. code-block:: c

    struct x86_hyper_init {
        void (*init_platform)(void);
        void (*guest_late_init)(void);
        bool (*x2apic_available)(void);
        void (*init_mem_mapping)(void);
    }

.. _`x86_hyper_init.members`:

Members
-------

init_platform
    platform setup

guest_late_init
    guest late init

x2apic_available
    X2APIC detection

init_mem_mapping
    setup early mappings during \ :c:func:`init_mem_mapping`\ 

.. _`x86_init_ops`:

struct x86_init_ops
===================

.. c:type:: struct x86_init_ops

    functions for platform specific setup

.. _`x86_init_ops.definition`:

Definition
----------

.. code-block:: c

    struct x86_init_ops {
        struct x86_init_resources resources;
        struct x86_init_mpparse mpparse;
        struct x86_init_irqs irqs;
        struct x86_init_oem oem;
        struct x86_init_paging paging;
        struct x86_init_timers timers;
        struct x86_init_iommu iommu;
        struct x86_init_pci pci;
        struct x86_hyper_init hyper;
    }

.. _`x86_init_ops.members`:

Members
-------

resources
    *undescribed*

mpparse
    *undescribed*

irqs
    *undescribed*

oem
    *undescribed*

paging
    *undescribed*

timers
    *undescribed*

iommu
    *undescribed*

pci
    *undescribed*

hyper
    *undescribed*

.. _`x86_cpuinit_ops`:

struct x86_cpuinit_ops
======================

.. c:type:: struct x86_cpuinit_ops

    platform specific cpu hotplug setups

.. _`x86_cpuinit_ops.definition`:

Definition
----------

.. code-block:: c

    struct x86_cpuinit_ops {
        void (*setup_percpu_clockev)(void);
        void (*early_percpu_clock_init)(void);
        void (*fixup_cpu_id)(struct cpuinfo_x86 *c, int node);
    }

.. _`x86_cpuinit_ops.members`:

Members
-------

setup_percpu_clockev
    set up the per cpu clock event device

early_percpu_clock_init
    early init of the per cpu clock event device

fixup_cpu_id
    *undescribed*

.. _`x86_legacy_devices`:

struct x86_legacy_devices
=========================

.. c:type:: struct x86_legacy_devices

    legacy x86 devices

.. _`x86_legacy_devices.definition`:

Definition
----------

.. code-block:: c

    struct x86_legacy_devices {
        int pnpbios;
    }

.. _`x86_legacy_devices.members`:

Members
-------

pnpbios
    this platform can have a PNPBIOS. If this is disabled the platform
    is known to never have a PNPBIOS.

.. _`x86_legacy_devices.description`:

Description
-----------

These are devices known to require LPC or ISA bus. The definition of legacy
devices adheres to the ACPI 5.2.9.3 IA-PC Boot Architecture flag
ACPI_FADT_LEGACY_DEVICES. These devices consist of user visible devices on
the LPC or ISA bus. User visible devices are devices that have end-user
accessible connectors (for example, LPT parallel port). Legacy devices on
the LPC bus consist for example of serial and parallel ports, PS/2 keyboard
/ mouse, and the floppy disk controller. A system that lacks all known
legacy devices can assume all devices can be detected exclusively via
standard device enumeration mechanisms including the ACPI namespace.

A system which has does not have ACPI_FADT_LEGACY_DEVICES enabled must not
have any of the legacy devices enumerated below present.

.. _`x86_legacy_i8042_state`:

enum x86_legacy_i8042_state
===========================

.. c:type:: enum x86_legacy_i8042_state

    i8042 keyboard controller state

.. _`x86_legacy_i8042_state.definition`:

Definition
----------

.. code-block:: c

    enum x86_legacy_i8042_state {
        X86_LEGACY_I8042_PLATFORM_ABSENT,
        X86_LEGACY_I8042_FIRMWARE_ABSENT,
        X86_LEGACY_I8042_EXPECTED_PRESENT
    };

.. _`x86_legacy_i8042_state.constants`:

Constants
---------

X86_LEGACY_I8042_PLATFORM_ABSENT
    the controller is always absent on
    given platform/subarch.

X86_LEGACY_I8042_FIRMWARE_ABSENT
    firmware reports that the controller
    is absent.

X86_LEGACY_I8042_EXPECTED_PRESENT
    *undescribed*

.. _`x86_legacy_features`:

struct x86_legacy_features
==========================

.. c:type:: struct x86_legacy_features

    legacy x86 features

.. _`x86_legacy_features.definition`:

Definition
----------

.. code-block:: c

    struct x86_legacy_features {
        enum x86_legacy_i8042_state i8042;
        int rtc;
        int no_vga;
        int reserve_bios_regions;
        struct x86_legacy_devices devices;
    }

.. _`x86_legacy_features.members`:

Members
-------

i8042
    indicated if we expect the device to have i8042 controller
    present.

rtc
    this device has a CMOS real-time clock present

no_vga
    *undescribed*

reserve_bios_regions
    boot code will search for the EBDA address and the
    start of the 640k - 1M BIOS region.  If false, the platform must
    ensure that its memory map correctly reserves sub-1MB regions as needed.

devices
    legacy x86 devices, refer to struct x86_legacy_devices
    documentation for further details.

.. _`x86_hyper_runtime`:

struct x86_hyper_runtime
========================

.. c:type:: struct x86_hyper_runtime

    x86 hypervisor specific runtime callbacks

.. _`x86_hyper_runtime.definition`:

Definition
----------

.. code-block:: c

    struct x86_hyper_runtime {
        void (*pin_vcpu)(int cpu);
    }

.. _`x86_hyper_runtime.members`:

Members
-------

pin_vcpu
    pin current vcpu to specified physical cpu (run rarely)

.. _`x86_platform_ops`:

struct x86_platform_ops
=======================

.. c:type:: struct x86_platform_ops

    platform specific runtime functions

.. _`x86_platform_ops.definition`:

Definition
----------

.. code-block:: c

    struct x86_platform_ops {
        unsigned long (*calibrate_cpu)(void);
        unsigned long (*calibrate_tsc)(void);
        void (*get_wallclock)(struct timespec *ts);
        int (*set_wallclock)(const struct timespec *ts);
        void (*iommu_shutdown)(void);
        bool (*is_untracked_pat_range)(u64 start, u64 end);
        void (*nmi_init)(void);
        unsigned char (*get_nmi_reason)(void);
        void (*save_sched_clock_state)(void);
        void (*restore_sched_clock_state)(void);
        void (*apic_post_init)(void);
        struct x86_legacy_features legacy;
        void (*set_legacy_features)(void);
        struct x86_hyper_runtime hyper;
    }

.. _`x86_platform_ops.members`:

Members
-------

calibrate_cpu
    calibrate CPU

calibrate_tsc
    calibrate TSC, if different from CPU

get_wallclock
    get time from HW clock like RTC etc.

set_wallclock
    set time back to HW clock
    \ ``is_untracked_pat_range``\       exclude from PAT logic
    \ ``nmi_init``\                     enable NMI on cpus

iommu_shutdown
    *undescribed*

is_untracked_pat_range
    *undescribed*

nmi_init
    *undescribed*

get_nmi_reason
    *undescribed*

save_sched_clock_state
    save state for \ :c:func:`sched_clock`\  on suspend

restore_sched_clock_state
    restore state for \ :c:func:`sched_clock`\  on resume

apic_post_init
    adjust apic if needed

legacy
    legacy features

set_legacy_features
    override legacy features. Use of this callback
    is highly discouraged. You should only need
    this if your hardware platform requires further
    custom fine tuning far beyond what may be
    possible in \ :c:func:`x86_early_init_platform_quirks`\  by
    only using the current x86_hardware_subarch
    semantics.

hyper
    x86 hypervisor specific runtime callbacks

.. This file was automatic generated / don't edit.

