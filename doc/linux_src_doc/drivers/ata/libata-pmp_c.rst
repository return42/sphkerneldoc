.. -*- coding: utf-8; mode: rst -*-

============
libata-pmp.c
============


.. _`sata_pmp_read`:

sata_pmp_read
=============

.. c:function:: unsigned int sata_pmp_read (struct ata_link *link, int reg, u32 *r_val)

    read PMP register

    :param struct ata_link \*link:
        link to read PMP register for

    :param int reg:
        register to read

    :param u32 \*r_val:
        resulting value



.. _`sata_pmp_read.description`:

Description
-----------

Read PMP register.



.. _`sata_pmp_read.locking`:

LOCKING
-------

Kernel thread context (may sleep).



.. _`sata_pmp_read.returns`:

RETURNS
-------

0 on success, AC_ERR\_\* mask on failure.



.. _`sata_pmp_write`:

sata_pmp_write
==============

.. c:function:: unsigned int sata_pmp_write (struct ata_link *link, int reg, u32 val)

    write PMP register

    :param struct ata_link \*link:
        link to write PMP register for

    :param int reg:
        register to write

    :param u32 val:

        *undescribed*



.. _`sata_pmp_write.description`:

Description
-----------

Write PMP register.



.. _`sata_pmp_write.locking`:

LOCKING
-------

Kernel thread context (may sleep).



.. _`sata_pmp_write.returns`:

RETURNS
-------

0 on success, AC_ERR\_\* mask on failure.



.. _`sata_pmp_qc_defer_cmd_switch`:

sata_pmp_qc_defer_cmd_switch
============================

.. c:function:: int sata_pmp_qc_defer_cmd_switch (struct ata_queued_cmd *qc)

    qc_defer for command switching PMP

    :param struct ata_queued_cmd \*qc:
        ATA command in question



.. _`sata_pmp_qc_defer_cmd_switch.description`:

Description
-----------

A host which has command switching PMP support cannot issue
commands to multiple links simultaneously.



.. _`sata_pmp_qc_defer_cmd_switch.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)



.. _`sata_pmp_qc_defer_cmd_switch.returns`:

RETURNS
-------

ATA_DEFER\_\* if deferring is needed, 0 otherwise.



.. _`sata_pmp_scr_read`:

sata_pmp_scr_read
=================

.. c:function:: int sata_pmp_scr_read (struct ata_link *link, int reg, u32 *r_val)

    read PSCR

    :param struct ata_link \*link:
        ATA link to read PSCR for

    :param int reg:
        PSCR to read

    :param u32 \*r_val:
        resulting value



.. _`sata_pmp_scr_read.description`:

Description
-----------

Read PSCR ``reg`` into ``r_val`` for ``link``\ , to be called from
:c:func:`ata_scr_read`.



.. _`sata_pmp_scr_read.locking`:

LOCKING
-------

Kernel thread context (may sleep).



.. _`sata_pmp_scr_read.returns`:

RETURNS
-------

0 on success, -errno on failure.



.. _`sata_pmp_scr_write`:

sata_pmp_scr_write
==================

.. c:function:: int sata_pmp_scr_write (struct ata_link *link, int reg, u32 val)

    write PSCR

    :param struct ata_link \*link:
        ATA link to write PSCR for

    :param int reg:
        PSCR to write

    :param u32 val:
        value to be written



.. _`sata_pmp_scr_write.description`:

Description
-----------

Write ``val`` to PSCR ``reg`` for ``link``\ , to be called from
:c:func:`ata_scr_write` and :c:func:`ata_scr_write_flush`.



.. _`sata_pmp_scr_write.locking`:

LOCKING
-------

Kernel thread context (may sleep).



.. _`sata_pmp_scr_write.returns`:

RETURNS
-------

0 on success, -errno on failure.



.. _`sata_pmp_set_lpm`:

sata_pmp_set_lpm
================

.. c:function:: int sata_pmp_set_lpm (struct ata_link *link, enum ata_lpm_policy policy, unsigned hints)

    configure LPM for a PMP link

    :param struct ata_link \*link:
        PMP link to configure LPM for

    :param enum ata_lpm_policy policy:
        target LPM policy

    :param unsigned hints:
        LPM hints



.. _`sata_pmp_set_lpm.description`:

Description
-----------

Configure LPM for ``link``\ .  This function will contain any PMP
specific workarounds if necessary.



.. _`sata_pmp_set_lpm.locking`:

LOCKING
-------

EH context.



.. _`sata_pmp_set_lpm.returns`:

RETURNS
-------

0 on success, -errno on failure.



.. _`sata_pmp_read_gscr`:

sata_pmp_read_gscr
==================

.. c:function:: int sata_pmp_read_gscr (struct ata_device *dev, u32 *gscr)

    read GSCR block of SATA PMP

    :param struct ata_device \*dev:
        PMP device

    :param u32 \*gscr:
        buffer to read GSCR block into



.. _`sata_pmp_read_gscr.description`:

Description
-----------

Read selected PMP GSCRs from the PMP at ``dev``\ .  This will serve
as configuration and identification info for the PMP.



.. _`sata_pmp_read_gscr.locking`:

LOCKING
-------

Kernel thread context (may sleep).



.. _`sata_pmp_read_gscr.returns`:

RETURNS
-------

0 on success, -errno on failure.



.. _`sata_pmp_attach`:

sata_pmp_attach
===============

.. c:function:: int sata_pmp_attach (struct ata_device *dev)

    attach a SATA PMP device

    :param struct ata_device \*dev:
        SATA PMP device to attach



.. _`sata_pmp_attach.description`:

Description
-----------

Configure and attach SATA PMP device ``dev``\ .  This function is
also responsible for allocating and initializing PMP links.



.. _`sata_pmp_attach.locking`:

LOCKING
-------

Kernel thread context (may sleep).



.. _`sata_pmp_attach.returns`:

RETURNS
-------

0 on success, -errno on failure.



.. _`sata_pmp_detach`:

sata_pmp_detach
===============

.. c:function:: void sata_pmp_detach (struct ata_device *dev)

    detach a SATA PMP device

    :param struct ata_device \*dev:
        SATA PMP device to detach



.. _`sata_pmp_detach.description`:

Description
-----------

Detach SATA PMP device ``dev``\ .  This function is also
responsible for deconfiguring PMP links.



.. _`sata_pmp_detach.locking`:

LOCKING
-------

Kernel thread context (may sleep).



.. _`sata_pmp_same_pmp`:

sata_pmp_same_pmp
=================

.. c:function:: int sata_pmp_same_pmp (struct ata_device *dev, const u32 *new_gscr)

    does new GSCR matches the configured PMP?

    :param struct ata_device \*dev:
        PMP device to compare against

    :param const u32 \*new_gscr:
        GSCR block of the new device



.. _`sata_pmp_same_pmp.description`:

Description
-----------

Compare ``new_gscr`` against ``dev`` and determine whether ``dev`` is
the PMP described by ``new_gscr``\ .



.. _`sata_pmp_same_pmp.locking`:

LOCKING
-------

None.



.. _`sata_pmp_same_pmp.returns`:

RETURNS
-------

1 if ``dev`` matches ``new_gscr``\ , 0 otherwise.



.. _`sata_pmp_revalidate`:

sata_pmp_revalidate
===================

.. c:function:: int sata_pmp_revalidate (struct ata_device *dev, unsigned int new_class)

    revalidate SATA PMP

    :param struct ata_device \*dev:
        PMP device to revalidate

    :param unsigned int new_class:
        new class code



.. _`sata_pmp_revalidate.description`:

Description
-----------

Re-read GSCR block and make sure ``dev`` is still attached to the
port and properly configured.



.. _`sata_pmp_revalidate.locking`:

LOCKING
-------

Kernel thread context (may sleep).



.. _`sata_pmp_revalidate.returns`:

RETURNS
-------

0 on success, -errno otherwise.



.. _`sata_pmp_revalidate_quick`:

sata_pmp_revalidate_quick
=========================

.. c:function:: int sata_pmp_revalidate_quick (struct ata_device *dev)

    revalidate SATA PMP quickly

    :param struct ata_device \*dev:
        PMP device to revalidate



.. _`sata_pmp_revalidate_quick.description`:

Description
-----------

Make sure the attached PMP is accessible.



.. _`sata_pmp_revalidate_quick.locking`:

LOCKING
-------

Kernel thread context (may sleep).



.. _`sata_pmp_revalidate_quick.returns`:

RETURNS
-------

0 on success, -errno otherwise.



.. _`sata_pmp_eh_recover_pmp`:

sata_pmp_eh_recover_pmp
=======================

.. c:function:: int sata_pmp_eh_recover_pmp (struct ata_port *ap, ata_prereset_fn_t prereset, ata_reset_fn_t softreset, ata_reset_fn_t hardreset, ata_postreset_fn_t postreset)

    recover PMP

    :param struct ata_port \*ap:
        ATA port PMP is attached to

    :param ata_prereset_fn_t prereset:
        prereset method (can be NULL)

    :param ata_reset_fn_t softreset:
        softreset method

    :param ata_reset_fn_t hardreset:
        hardreset method

    :param ata_postreset_fn_t postreset:
        postreset method (can be NULL)



.. _`sata_pmp_eh_recover_pmp.description`:

Description
-----------

Recover PMP attached to ``ap``\ .  Recovery procedure is somewhat
similar to that of :c:func:`ata_eh_recover` except that reset should
always be performed in hard->soft sequence and recovery
failure results in PMP detachment.



.. _`sata_pmp_eh_recover_pmp.locking`:

LOCKING
-------

Kernel thread context (may sleep).



.. _`sata_pmp_eh_recover_pmp.returns`:

RETURNS
-------

0 on success, -errno on failure.



.. _`sata_pmp_eh_recover`:

sata_pmp_eh_recover
===================

.. c:function:: int sata_pmp_eh_recover (struct ata_port *ap)

    recover PMP-enabled port

    :param struct ata_port \*ap:
        ATA port to recover



.. _`sata_pmp_eh_recover.description`:

Description
-----------

Drive EH recovery operation for PMP enabled port ``ap``\ .  This
function recovers host and PMP ports with proper retrials and
fallbacks.  Actual recovery operations are performed using
:c:func:`ata_eh_recover` and :c:func:`sata_pmp_eh_recover_pmp`.



.. _`sata_pmp_eh_recover.locking`:

LOCKING
-------

Kernel thread context (may sleep).



.. _`sata_pmp_eh_recover.returns`:

RETURNS
-------

0 on success, -errno on failure.



.. _`sata_pmp_error_handler`:

sata_pmp_error_handler
======================

.. c:function:: void sata_pmp_error_handler (struct ata_port *ap)

    do standard error handling for PMP-enabled host

    :param struct ata_port \*ap:
        host port to handle error for



.. _`sata_pmp_error_handler.description`:

Description
-----------

Perform standard error handling sequence for PMP-enabled host
``ap``\ .



.. _`sata_pmp_error_handler.locking`:

LOCKING
-------

Kernel thread context (may sleep).

