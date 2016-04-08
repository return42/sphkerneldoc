
.. _API-ata-exec-internal:

=================
ata_exec_internal
=================

*man ata_exec_internal(9)*

*4.6.0-rc1*

execute libata internal command


Synopsis
========

.. c:function:: unsigned ata_exec_internal( struct ata_device * dev, struct ata_taskfile * tf, const u8 * cdb, int dma_dir, void * buf, unsigned int buflen, unsigned long timeout )

Arguments
=========

``dev``
    Device to which the command is sent

``tf``
    Taskfile registers for the command and the result

``cdb``
    CDB for packet command

``dma_dir``
    Data transfer direction of the command

``buf``
    Data buffer of the command

``buflen``
    Length of data buffer

``timeout``
    Timeout in msecs (0 for default)


Description
===========

Wrapper around ``ata_exec_internal_sg`` which takes simple buffer instead of sg list.


LOCKING
=======

None. Should be called with kernel context, might sleep.


RETURNS
=======

Zero on success, AC_ERR_⋆ mask on failure
