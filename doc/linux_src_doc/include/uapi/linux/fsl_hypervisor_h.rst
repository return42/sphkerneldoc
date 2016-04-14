.. -*- coding: utf-8; mode: rst -*-

================
fsl_hypervisor.h
================

.. _`fsl_hv_ioctl_restart`:

struct fsl_hv_ioctl_restart
===========================

.. c:type:: struct fsl_hv_ioctl_restart

    restart a partition



Definition
----------

.. code-block:: c

  struct fsl_hv_ioctl_restart {
    __u32 ret;
    __u32 partition;
  };



Members
-------

:``ret``:
    return error code from the hypervisor

:``partition``:
    the ID of the partition to restart, or -1 for the
    calling partition



Description
-----------

Used by FSL_HV_IOCTL_PARTITION_RESTART


.. _`fsl_hv_ioctl_status`:

struct fsl_hv_ioctl_status
==========================

.. c:type:: struct fsl_hv_ioctl_status

    get a partition's status



Definition
----------

.. code-block:: c

  struct fsl_hv_ioctl_status {
    __u32 ret;
    __u32 partition;
    __u32 status;
  };



Members
-------

:``ret``:
    return error code from the hypervisor

:``partition``:
    the ID of the partition to query, or -1 for the
    calling partition

:``status``:
    The returned status of the partition



Description
-----------

Used by FSL_HV_IOCTL_PARTITION_GET_STATUS

Values of 'status'::

   0 = Stopped
   1 = Running
   2 = Starting
   3 = Stopping


.. _`fsl_hv_ioctl_start`:

struct fsl_hv_ioctl_start
=========================

.. c:type:: struct fsl_hv_ioctl_start

    start a partition



Definition
----------

.. code-block:: c

  struct fsl_hv_ioctl_start {
    __u32 ret;
    __u32 partition;
    __u32 entry_point;
    __u32 load;
  };



Members
-------

:``ret``:
    return error code from the hypervisor

:``partition``:
    the ID of the partition to control

:``entry_point``:
    The offset within the guest IMA to start execution

:``load``:
    If non-zero, reload the partition's images before starting



Description
-----------

Used by FSL_HV_IOCTL_PARTITION_START


.. _`fsl_hv_ioctl_stop`:

struct fsl_hv_ioctl_stop
========================

.. c:type:: struct fsl_hv_ioctl_stop

    stop a partition



Definition
----------

.. code-block:: c

  struct fsl_hv_ioctl_stop {
    __u32 ret;
    __u32 partition;
  };



Members
-------

:``ret``:
    return error code from the hypervisor

:``partition``:
    the ID of the partition to stop, or -1 for the calling
    partition



Description
-----------

Used by FSL_HV_IOCTL_PARTITION_STOP


.. _`fsl_hv_ioctl_memcpy`:

struct fsl_hv_ioctl_memcpy
==========================

.. c:type:: struct fsl_hv_ioctl_memcpy

    copy memory between partitions



Definition
----------

.. code-block:: c

  struct fsl_hv_ioctl_memcpy {
    __u32 ret;
    __u32 source;
    __u32 target;
    __u32 reserved;
    __u64 count;
  };



Members
-------

:``ret``:
    return error code from the hypervisor

:``source``:
    the partition ID of the source partition, or -1 for this
    partition

:``target``:
    the partition ID of the target partition, or -1 for this
    partition

:``reserved``:
    reserved, must be set to 0

:``count``:
    the number of bytes to copy.  Both the local and remote
    buffers must be at least 'count' bytes long



Description
-----------

Used by FSL_HV_IOCTL_MEMCPY

The 'local' partition is the partition that calls this ioctl.  The
'remote' partition is a different partition.  The data is copied from
the 'source' paritition' to the 'target' partition.

The buffer in the remote partition must be guest physically
contiguous.

This ioctl does not support copying memory between two remote
partitions or within the same partition, so either 'source' or
'target' (but not both) must be -1.  In other words, either

source == local and target == remote

or
source == remote and target == local


.. _`fsl_hv_ioctl_doorbell`:

struct fsl_hv_ioctl_doorbell
============================

.. c:type:: struct fsl_hv_ioctl_doorbell

    ring a doorbell



Definition
----------

.. code-block:: c

  struct fsl_hv_ioctl_doorbell {
    __u32 ret;
    __u32 doorbell;
  };



Members
-------

:``ret``:
    return error code from the hypervisor

:``doorbell``:
    the handle of the doorbell to ring doorbell



Description
-----------

Used by FSL_HV_IOCTL_DOORBELL


.. _`fsl_hv_ioctl_prop`:

struct fsl_hv_ioctl_prop
========================

.. c:type:: struct fsl_hv_ioctl_prop

    get/set a device tree property



Definition
----------

.. code-block:: c

  struct fsl_hv_ioctl_prop {
    __u32 ret;
    __u32 handle;
    __u64 path;
    __u64 propname;
    __u64 propval;
    __u32 proplen;
    __u32 reserved;
  };



Members
-------

:``ret``:
    return error code from the hypervisor

:``handle``:
    handle of partition whose tree to access

:``path``:
    virtual address of path name of node to access

:``propname``:
    virtual address of name of property to access

:``propval``:
    virtual address of property data buffer

:``proplen``:
    Size of property data buffer

:``reserved``:
    reserved, must be set to 0



Description
-----------

Used by FSL_HV_IOCTL_DOORBELL

