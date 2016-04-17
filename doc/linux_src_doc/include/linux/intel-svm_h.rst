.. -*- coding: utf-8; mode: rst -*-

===========
intel-svm.h
===========


.. _`intel_svm_bind_mm`:

intel_svm_bind_mm
=================

.. c:function:: int intel_svm_bind_mm (struct device *dev, int *pasid, int flags, struct svm_dev_ops *ops)

    Bind the current process to a PASID

    :param struct device \*dev:
        Device to be granted acccess

    :param int \*pasid:
        Address for allocated PASID

    :param int flags:
        Flags. Later for requesting supervisor mode, etc.

    :param struct svm_dev_ops \*ops:
        Callbacks to device driver



.. _`intel_svm_bind_mm.description`:

Description
-----------

This function attempts to enable PASID support for the given device.
If the ``pasid`` argument is non-\ ``NULL``\ , a PASID is allocated for access
to the MM of the current process.

By using a ``NULL`` value for the ``pasid`` argument, this function can
be used to simply validate that PASID support is available for the
given device — i.e. that it is behind an IOMMU which has the
requisite support, and is enabled.

Page faults are handled transparently by the IOMMU code, and there
should be no need for the device driver to be involved. If a page
fault cannot be handled (i.e. is an invalid address rather than
just needs paging in), then the page request will be completed by
the core IOMMU code with appropriate status, and the device itself
can then report the resulting fault to its driver via whatever
mechanism is appropriate.

Multiple calls from the same process may result in the same PASID
being re-used. A reference count is kept.



.. _`intel_svm_unbind_mm`:

intel_svm_unbind_mm
===================

.. c:function:: int intel_svm_unbind_mm (struct device *dev, int pasid)

    Unbind a specified PASID

    :param struct device \*dev:
        Device for which PASID was allocated

    :param int pasid:
        PASID value to be unbound



.. _`intel_svm_unbind_mm.description`:

Description
-----------

This function allows a PASID to be retired when the device no
longer requires access to the address space of a given process.

If the use count for the PASID in question reaches zero, the
PASID is revoked and may no longer be used by hardware.

Device drivers are required to ensure that no access (including
page requests) is currently outstanding for the PASID in question,
before calling this function.

