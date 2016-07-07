.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/common/mic_dev.h

.. _`mic_hw_family`:

enum mic_hw_family
==================

.. c:type:: enum mic_hw_family

    The hardware family to which a device belongs.

.. _`mic_hw_family.definition`:

Definition
----------

.. code-block:: c

    enum mic_hw_family {
        MIC_FAMILY_X100,
        MIC_FAMILY_X200,
        MIC_FAMILY_UNKNOWN,
        MIC_FAMILY_LAST
    };

.. _`mic_hw_family.constants`:

Constants
---------

MIC_FAMILY_X100
    *undescribed*

MIC_FAMILY_X200
    *undescribed*

MIC_FAMILY_UNKNOWN
    *undescribed*

MIC_FAMILY_LAST
    *undescribed*

.. _`mic_mw`:

struct mic_mw
=============

.. c:type:: struct mic_mw

    MIC memory window

.. _`mic_mw.definition`:

Definition
----------

.. code-block:: c

    struct mic_mw {
        phys_addr_t pa;
        void __iomem *va;
        resource_size_t len;
    }

.. _`mic_mw.members`:

Members
-------

pa
    Base physical address.

va
    Base ioremap'd virtual address.

len
    Size of the memory window.

.. This file was automatic generated / don't edit.

