.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/libata-pmp.c

.. _`sata_pmp_read`:

sata_pmp_read
=============

.. c:function:: unsigned int sata_pmp_read(struct ata_link *link, int reg, u32 *r_val)

    read PMP register

    :param link:
        link to read PMP register for
    :type link: struct ata_link \*

    :param reg:
        register to read
    :type reg: int

    :param r_val:
        resulting value
    :type r_val: u32 \*

.. _`sata_pmp_read.description`:

Description
-----------

Read PMP register.

.. _`sata_pmp_read.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. _`sata_pmp_read.return`:

Return
------

0 on success, AC_ERR\_\* mask on failure.

.. _`sata_pmp_write`:

sata_pmp_write
==============

.. c:function:: unsigned int sata_pmp_write(struct ata_link *link, int reg, u32 val)

    write PMP register

    :param link:
        link to write PMP register for
    :type link: struct ata_link \*

    :param reg:
        register to write
    :type reg: int

    :param val:
        *undescribed*
    :type val: u32

.. _`sata_pmp_write.description`:

Description
-----------

Write PMP register.

.. _`sata_pmp_write.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. _`sata_pmp_write.return`:

Return
------

0 on success, AC_ERR\_\* mask on failure.

.. _`sata_pmp_qc_defer_cmd_switch`:

sata_pmp_qc_defer_cmd_switch
============================

.. c:function:: int sata_pmp_qc_defer_cmd_switch(struct ata_queued_cmd *qc)

    qc_defer for command switching PMP

    :param qc:
        ATA command in question
    :type qc: struct ata_queued_cmd \*

.. _`sata_pmp_qc_defer_cmd_switch.description`:

Description
-----------

A host which has command switching PMP support cannot issue
commands to multiple links simultaneously.

.. _`sata_pmp_qc_defer_cmd_switch.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`sata_pmp_qc_defer_cmd_switch.return`:

Return
------

ATA_DEFER\_\* if deferring is needed, 0 otherwise.

.. _`sata_pmp_scr_read`:

sata_pmp_scr_read
=================

.. c:function:: int sata_pmp_scr_read(struct ata_link *link, int reg, u32 *r_val)

    read PSCR

    :param link:
        ATA link to read PSCR for
    :type link: struct ata_link \*

    :param reg:
        PSCR to read
    :type reg: int

    :param r_val:
        resulting value
    :type r_val: u32 \*

.. _`sata_pmp_scr_read.description`:

Description
-----------

Read PSCR \ ``reg``\  into \ ``r_val``\  for \ ``link``\ , to be called from
\ :c:func:`ata_scr_read`\ .

.. _`sata_pmp_scr_read.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. _`sata_pmp_scr_read.return`:

Return
------

0 on success, -errno on failure.

.. _`sata_pmp_scr_write`:

sata_pmp_scr_write
==================

.. c:function:: int sata_pmp_scr_write(struct ata_link *link, int reg, u32 val)

    write PSCR

    :param link:
        ATA link to write PSCR for
    :type link: struct ata_link \*

    :param reg:
        PSCR to write
    :type reg: int

    :param val:
        value to be written
    :type val: u32

.. _`sata_pmp_scr_write.description`:

Description
-----------

Write \ ``val``\  to PSCR \ ``reg``\  for \ ``link``\ , to be called from
\ :c:func:`ata_scr_write`\  and \ :c:func:`ata_scr_write_flush`\ .

.. _`sata_pmp_scr_write.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. _`sata_pmp_scr_write.return`:

Return
------

0 on success, -errno on failure.

.. _`sata_pmp_set_lpm`:

sata_pmp_set_lpm
================

.. c:function:: int sata_pmp_set_lpm(struct ata_link *link, enum ata_lpm_policy policy, unsigned hints)

    configure LPM for a PMP link

    :param link:
        PMP link to configure LPM for
    :type link: struct ata_link \*

    :param policy:
        target LPM policy
    :type policy: enum ata_lpm_policy

    :param hints:
        LPM hints
    :type hints: unsigned

.. _`sata_pmp_set_lpm.description`:

Description
-----------

Configure LPM for \ ``link``\ .  This function will contain any PMP
specific workarounds if necessary.

.. _`sata_pmp_set_lpm.locking`:

LOCKING
-------

EH context.

.. _`sata_pmp_set_lpm.return`:

Return
------

0 on success, -errno on failure.

.. _`sata_pmp_read_gscr`:

sata_pmp_read_gscr
==================

.. c:function:: int sata_pmp_read_gscr(struct ata_device *dev, u32 *gscr)

    read GSCR block of SATA PMP

    :param dev:
        PMP device
    :type dev: struct ata_device \*

    :param gscr:
        buffer to read GSCR block into
    :type gscr: u32 \*

.. _`sata_pmp_read_gscr.description`:

Description
-----------

Read selected PMP GSCRs from the PMP at \ ``dev``\ .  This will serve
as configuration and identification info for the PMP.

.. _`sata_pmp_read_gscr.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. _`sata_pmp_read_gscr.return`:

Return
------

0 on success, -errno on failure.

.. _`sata_pmp_attach`:

sata_pmp_attach
===============

.. c:function:: int sata_pmp_attach(struct ata_device *dev)

    attach a SATA PMP device

    :param dev:
        SATA PMP device to attach
    :type dev: struct ata_device \*

.. _`sata_pmp_attach.description`:

Description
-----------

Configure and attach SATA PMP device \ ``dev``\ .  This function is
also responsible for allocating and initializing PMP links.

.. _`sata_pmp_attach.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. _`sata_pmp_attach.return`:

Return
------

0 on success, -errno on failure.

.. _`sata_pmp_detach`:

sata_pmp_detach
===============

.. c:function:: void sata_pmp_detach(struct ata_device *dev)

    detach a SATA PMP device

    :param dev:
        SATA PMP device to detach
    :type dev: struct ata_device \*

.. _`sata_pmp_detach.description`:

Description
-----------

Detach SATA PMP device \ ``dev``\ .  This function is also
responsible for deconfiguring PMP links.

.. _`sata_pmp_detach.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. _`sata_pmp_same_pmp`:

sata_pmp_same_pmp
=================

.. c:function:: int sata_pmp_same_pmp(struct ata_device *dev, const u32 *new_gscr)

    does new GSCR matches the configured PMP?

    :param dev:
        PMP device to compare against
    :type dev: struct ata_device \*

    :param new_gscr:
        GSCR block of the new device
    :type new_gscr: const u32 \*

.. _`sata_pmp_same_pmp.description`:

Description
-----------

Compare \ ``new_gscr``\  against \ ``dev``\  and determine whether \ ``dev``\  is
the PMP described by \ ``new_gscr``\ .

.. _`sata_pmp_same_pmp.locking`:

LOCKING
-------

None.

.. _`sata_pmp_same_pmp.return`:

Return
------

1 if \ ``dev``\  matches \ ``new_gscr``\ , 0 otherwise.

.. _`sata_pmp_revalidate`:

sata_pmp_revalidate
===================

.. c:function:: int sata_pmp_revalidate(struct ata_device *dev, unsigned int new_class)

    revalidate SATA PMP

    :param dev:
        PMP device to revalidate
    :type dev: struct ata_device \*

    :param new_class:
        new class code
    :type new_class: unsigned int

.. _`sata_pmp_revalidate.description`:

Description
-----------

Re-read GSCR block and make sure \ ``dev``\  is still attached to the
port and properly configured.

.. _`sata_pmp_revalidate.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. _`sata_pmp_revalidate.return`:

Return
------

0 on success, -errno otherwise.

.. _`sata_pmp_revalidate_quick`:

sata_pmp_revalidate_quick
=========================

.. c:function:: int sata_pmp_revalidate_quick(struct ata_device *dev)

    revalidate SATA PMP quickly

    :param dev:
        PMP device to revalidate
    :type dev: struct ata_device \*

.. _`sata_pmp_revalidate_quick.description`:

Description
-----------

Make sure the attached PMP is accessible.

.. _`sata_pmp_revalidate_quick.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. _`sata_pmp_revalidate_quick.return`:

Return
------

0 on success, -errno otherwise.

.. _`sata_pmp_eh_recover_pmp`:

sata_pmp_eh_recover_pmp
=======================

.. c:function:: int sata_pmp_eh_recover_pmp(struct ata_port *ap, ata_prereset_fn_t prereset, ata_reset_fn_t softreset, ata_reset_fn_t hardreset, ata_postreset_fn_t postreset)

    recover PMP

    :param ap:
        ATA port PMP is attached to
    :type ap: struct ata_port \*

    :param prereset:
        prereset method (can be NULL)
    :type prereset: ata_prereset_fn_t

    :param softreset:
        softreset method
    :type softreset: ata_reset_fn_t

    :param hardreset:
        hardreset method
    :type hardreset: ata_reset_fn_t

    :param postreset:
        postreset method (can be NULL)
    :type postreset: ata_postreset_fn_t

.. _`sata_pmp_eh_recover_pmp.description`:

Description
-----------

Recover PMP attached to \ ``ap``\ .  Recovery procedure is somewhat
similar to that of \ :c:func:`ata_eh_recover`\  except that reset should
always be performed in hard->soft sequence and recovery
failure results in PMP detachment.

.. _`sata_pmp_eh_recover_pmp.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. _`sata_pmp_eh_recover_pmp.return`:

Return
------

0 on success, -errno on failure.

.. _`sata_pmp_eh_recover`:

sata_pmp_eh_recover
===================

.. c:function:: int sata_pmp_eh_recover(struct ata_port *ap)

    recover PMP-enabled port

    :param ap:
        ATA port to recover
    :type ap: struct ata_port \*

.. _`sata_pmp_eh_recover.description`:

Description
-----------

Drive EH recovery operation for PMP enabled port \ ``ap``\ .  This
function recovers host and PMP ports with proper retrials and
fallbacks.  Actual recovery operations are performed using
\ :c:func:`ata_eh_recover`\  and \ :c:func:`sata_pmp_eh_recover_pmp`\ .

.. _`sata_pmp_eh_recover.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. _`sata_pmp_eh_recover.return`:

Return
------

0 on success, -errno on failure.

.. _`sata_pmp_error_handler`:

sata_pmp_error_handler
======================

.. c:function:: void sata_pmp_error_handler(struct ata_port *ap)

    do standard error handling for PMP-enabled host

    :param ap:
        host port to handle error for
    :type ap: struct ata_port \*

.. _`sata_pmp_error_handler.description`:

Description
-----------

Perform standard error handling sequence for PMP-enabled host
\ ``ap``\ .

.. _`sata_pmp_error_handler.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. This file was automatic generated / don't edit.

