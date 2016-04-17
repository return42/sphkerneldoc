.. -*- coding: utf-8; mode: rst -*-

=====
ata.h
=====


.. _`ata_id_major_version`:

ata_id_major_version
====================

.. c:function:: unsigned int ata_id_major_version (const u16 *id)

    get ATA level of drive

    :param const u16 \*id:
        Identify data



.. _`ata_id_major_version.caveats`:

Caveats
-------

ATA-1 considers identify optional
ATA-2 introduces mandatory identify
ATA-3 introduces word 80 and accurate reporting

The practical impact of this is that ata_id_major_version cannot
reliably report on drives below ATA3.

