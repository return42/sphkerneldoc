
.. _API-scsi-test-unit-ready:

====================
scsi_test_unit_ready
====================

*man scsi_test_unit_ready(9)*

*4.6.0-rc1*

test if unit is ready


Synopsis
========

.. c:function:: int scsi_test_unit_ready( struct scsi_device * sdev, int timeout, int retries, struct scsi_sense_hdr * sshdr_external )

Arguments
=========

``sdev``
    scsi device to change the state of.

``timeout``
    command timeout

``retries``
    number of retries before failing

``sshdr_external``
    Optional pointer to struct scsi_sense_hdr for returning sense. Make sure that this is cleared before passing in.


Description
===========

Returns zero if unsuccessful or an error if TUR failed. For removable media, UNIT_ATTENTION sets ->changed flag.
