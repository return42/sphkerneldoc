.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/vfio_ap_ops.c

.. _`vfio_ap_has_queue`:

vfio_ap_has_queue
=================

.. c:function:: int vfio_ap_has_queue(struct device *dev, void *data)

    :param dev:
        an AP queue device
    :type dev: struct device \*

    :param data:
        a struct vfio_ap_queue_reserved reference
    :type data: void \*

.. _`vfio_ap_has_queue.description`:

Description
-----------

Flags whether the AP queue device (@dev) has a queue ID containing the APQN,
apid or apqi specified in \ ``data``\ :

- If \ ``data``\  contains both an apid and apqi value, then \ ``data``\  will be flagged
as reserved if the APID and APQI fields for the AP queue device matches

- If \ ``data``\  contains only an apid value, \ ``data``\  will be flagged as
reserved if the APID field in the AP queue device matches

- If \ ``data``\  contains only an apqi value, \ ``data``\  will be flagged as
reserved if the APQI field in the AP queue device matches

Returns 0 to indicate the input to function succeeded. Returns -EINVAL if
\ ``data``\  does not contain either an apid or apqi.

.. _`vfio_ap_verify_queue_reserved`:

vfio_ap_verify_queue_reserved
=============================

.. c:function:: int vfio_ap_verify_queue_reserved(unsigned long *apid, unsigned long *apqi)

    :param apid:
        an AP adapter ID
    :type apid: unsigned long \*

    :param apqi:
        an AP queue index
    :type apqi: unsigned long \*

.. _`vfio_ap_verify_queue_reserved.description`:

Description
-----------

Verifies that the AP queue with \ ``apid``\ /@apqi is reserved by the VFIO AP device

.. _`vfio_ap_verify_queue_reserved.driver-according-to-the-following-rules`:

driver according to the following rules
---------------------------------------


- If both \ ``apid``\  and \ ``apqi``\  are not NULL, then there must be an AP queue
device bound to the vfio_ap driver with the APQN identified by \ ``apid``\  and
\ ``apqi``\ 

- If only \ ``apid``\  is not NULL, then there must be an AP queue device bound
to the vfio_ap driver with an APQN containing \ ``apid``\ 

- If only \ ``apqi``\  is not NULL, then there must be an AP queue device bound
to the vfio_ap driver with an APQN containing \ ``apqi``\ 

Returns 0 if the AP queue is reserved; otherwise, returns -EADDRNOTAVAIL.

.. _`vfio_ap_mdev_verify_no_sharing`:

vfio_ap_mdev_verify_no_sharing
==============================

.. c:function:: int vfio_ap_mdev_verify_no_sharing(struct ap_matrix_mdev *matrix_mdev)

    :param matrix_mdev:
        the mediated matrix device
    :type matrix_mdev: struct ap_matrix_mdev \*

.. _`vfio_ap_mdev_verify_no_sharing.description`:

Description
-----------

Verifies that the APQNs derived from the cross product of the AP adapter IDs
and AP queue indexes comprising the AP matrix are not configured for another
mediated device. AP queue sharing is not allowed.

Returns 0 if the APQNs are not shared, otherwise; returns -EADDRINUSE.

.. _`assign_adapter_store`:

assign_adapter_store
====================

.. c:function:: ssize_t assign_adapter_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    :param dev:
        the matrix device
    :type dev: struct device \*

    :param attr:
        the mediated matrix device's assign_adapter attribute
    :type attr: struct device_attribute \*

    :param buf:
        a buffer containing the AP adapter number (APID) to
        be assigned
    :type buf: const char \*

    :param count:
        the number of bytes in \ ``buf``\ 
    :type count: size_t

.. _`assign_adapter_store.description`:

Description
-----------

Parses the APID from \ ``buf``\  and sets the corresponding bit in the mediated
matrix device's APM.

Returns the number of bytes processed if the APID is valid; otherwise,

.. _`assign_adapter_store.returns-one-of-the-following-errors`:

returns one of the following errors
-----------------------------------


1. -EINVAL
The APID is not a valid number

2. -ENODEV
The APID exceeds the maximum value configured for the system

3. -EADDRNOTAVAIL
An APQN derived from the cross product of the APID being assigned
and the APQIs previously assigned is not bound to the vfio_ap device
driver; or, if no APQIs have yet been assigned, the APID is not
contained in an APQN bound to the vfio_ap device driver.

4. -EADDRINUSE
An APQN derived from the cross product of the APID being assigned
and the APQIs previously assigned is being used by another mediated
matrix device

.. _`unassign_adapter_store`:

unassign_adapter_store
======================

.. c:function:: ssize_t unassign_adapter_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    :param dev:
        the matrix device
    :type dev: struct device \*

    :param attr:
        the mediated matrix device's unassign_adapter attribute
    :type attr: struct device_attribute \*

    :param buf:
        a buffer containing the adapter number (APID) to be unassigned
    :type buf: const char \*

    :param count:
        the number of bytes in \ ``buf``\ 
    :type count: size_t

.. _`unassign_adapter_store.description`:

Description
-----------

Parses the APID from \ ``buf``\  and clears the corresponding bit in the mediated
matrix device's APM.

Returns the number of bytes processed if the APID is valid; otherwise,

.. _`unassign_adapter_store.returns-one-of-the-following-errors`:

returns one of the following errors
-----------------------------------

-EINVAL if the APID is not a number
-ENODEV if the APID it exceeds the maximum value configured for the
system

.. _`assign_domain_store`:

assign_domain_store
===================

.. c:function:: ssize_t assign_domain_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    :param dev:
        the matrix device
    :type dev: struct device \*

    :param attr:
        the mediated matrix device's assign_domain attribute
    :type attr: struct device_attribute \*

    :param buf:
        a buffer containing the AP queue index (APQI) of the domain to
        be assigned
    :type buf: const char \*

    :param count:
        the number of bytes in \ ``buf``\ 
    :type count: size_t

.. _`assign_domain_store.description`:

Description
-----------

Parses the APQI from \ ``buf``\  and sets the corresponding bit in the mediated
matrix device's AQM.

Returns the number of bytes processed if the APQI is valid; otherwise returns

.. _`assign_domain_store.one-of-the-following-errors`:

one of the following errors
---------------------------


1. -EINVAL
The APQI is not a valid number

2. -ENODEV
The APQI exceeds the maximum value configured for the system

3. -EADDRNOTAVAIL
An APQN derived from the cross product of the APQI being assigned
and the APIDs previously assigned is not bound to the vfio_ap device
driver; or, if no APIDs have yet been assigned, the APQI is not
contained in an APQN bound to the vfio_ap device driver.

4. -EADDRINUSE
An APQN derived from the cross product of the APQI being assigned
and the APIDs previously assigned is being used by another mediated
matrix device

.. _`unassign_domain_store`:

unassign_domain_store
=====================

.. c:function:: ssize_t unassign_domain_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    :param dev:
        the matrix device
    :type dev: struct device \*

    :param attr:
        the mediated matrix device's unassign_domain attribute
    :type attr: struct device_attribute \*

    :param buf:
        a buffer containing the AP queue index (APQI) of the domain to
        be unassigned
    :type buf: const char \*

    :param count:
        the number of bytes in \ ``buf``\ 
    :type count: size_t

.. _`unassign_domain_store.description`:

Description
-----------

Parses the APQI from \ ``buf``\  and clears the corresponding bit in the
mediated matrix device's AQM.

Returns the number of bytes processed if the APQI is valid; otherwise,

.. _`unassign_domain_store.returns-one-of-the-following-errors`:

returns one of the following errors
-----------------------------------

-EINVAL if the APQI is not a number
-ENODEV if the APQI exceeds the maximum value configured for the system

.. _`assign_control_domain_store`:

assign_control_domain_store
===========================

.. c:function:: ssize_t assign_control_domain_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    :param dev:
        the matrix device
    :type dev: struct device \*

    :param attr:
        the mediated matrix device's assign_control_domain attribute
    :type attr: struct device_attribute \*

    :param buf:
        a buffer containing the domain ID to be assigned
    :type buf: const char \*

    :param count:
        the number of bytes in \ ``buf``\ 
    :type count: size_t

.. _`assign_control_domain_store.description`:

Description
-----------

Parses the domain ID from \ ``buf``\  and sets the corresponding bit in the mediated
matrix device's ADM.

Returns the number of bytes processed if the domain ID is valid; otherwise,

.. _`assign_control_domain_store.returns-one-of-the-following-errors`:

returns one of the following errors
-----------------------------------

-EINVAL if the ID is not a number
-ENODEV if the ID exceeds the maximum value configured for the system

.. _`unassign_control_domain_store`:

unassign_control_domain_store
=============================

.. c:function:: ssize_t unassign_control_domain_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    :param dev:
        the matrix device
    :type dev: struct device \*

    :param attr:
        the mediated matrix device's unassign_control_domain attribute
    :type attr: struct device_attribute \*

    :param buf:
        a buffer containing the domain ID to be unassigned
    :type buf: const char \*

    :param count:
        the number of bytes in \ ``buf``\ 
    :type count: size_t

.. _`unassign_control_domain_store.description`:

Description
-----------

Parses the domain ID from \ ``buf``\  and clears the corresponding bit in the
mediated matrix device's ADM.

Returns the number of bytes processed if the domain ID is valid; otherwise,

.. _`unassign_control_domain_store.returns-one-of-the-following-errors`:

returns one of the following errors
-----------------------------------

-EINVAL if the ID is not a number
-ENODEV if the ID exceeds the maximum value configured for the system

.. _`vfio_ap_mdev_set_kvm`:

vfio_ap_mdev_set_kvm
====================

.. c:function:: int vfio_ap_mdev_set_kvm(struct ap_matrix_mdev *matrix_mdev, struct kvm *kvm)

    :param matrix_mdev:
        a mediated matrix device
    :type matrix_mdev: struct ap_matrix_mdev \*

    :param kvm:
        reference to KVM instance
    :type kvm: struct kvm \*

.. _`vfio_ap_mdev_set_kvm.description`:

Description
-----------

Verifies no other mediated matrix device has \ ``kvm``\  and sets a reference to
it in \ ``matrix_mdev->kvm``\ .

Return 0 if no other mediated matrix device has a reference to \ ``kvm``\ ;
otherwise, returns an -EPERM.

.. This file was automatic generated / don't edit.

