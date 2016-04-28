.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-target-reap-ref-release:

============================
scsi_target_reap_ref_release
============================

*man scsi_target_reap_ref_release(9)*

*4.6.0-rc5*

remove target from visibility


Synopsis
========

.. c:function:: void scsi_target_reap_ref_release( struct kref * kref )

Arguments
=========

``kref``
    the reap_ref in the target being released


Description
===========

Called on last put of reap_ref, which is the indication that no device
under this target is visible anymore, so render the target invisible in
sysfs. Note: we have to be in user context here because the target reaps
should be done in places where the scsi device visibility is being
removed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
