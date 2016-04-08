
.. _API-ata-exec-internal-sg:

====================
ata_exec_internal_sg
====================

*man ata_exec_internal_sg(9)*

*4.6.0-rc1*

execute libata internal command


Synopsis
========

.. c:function:: unsigned ata_exec_internal_sg( struct ata_device * dev, struct ata_taskfile * tf, const u8 * cdb, int dma_dir, struct scatterlist * sgl, unsigned int n_elem, unsigned long timeout )

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

``sgl``
    sg list for the data buffer of the command

``n_elem``
    Number of sg entries

``timeout``
    Timeout in msecs (0 for default)


Description
===========

Executes libata internal command with timeout. ``tf`` contains command on entry and result on return. Timeout and error conditions are reported via return value. No recovery action
is taken after a command times out. It's caller's duty to clean up after timeout.


LOCKING
=======

None. Should be called with kernel context, might sleep.


RETURNS
=======

Zero on success, AC_ERR_⋆ mask on failure
